"""Loopback-only multi-source original-question review server (no third-party API)."""
from __future__ import annotations
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
import os
from pathlib import Path
import re
import sys
import threading
from urllib.parse import parse_qs, urlsplit
import webbrowser

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from review_workbench.service import MultiSourceReviewService, ReviewError
from review_workbench.transactions import RecoveryRequired, safe_path


class ReviewHTTPServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, address, service):
        if address[0] != '127.0.0.1':
            raise ValueError('This workbench must bind to 127.0.0.1')
        self.service = service
        super().__init__(address, ReviewHandler)


class ReviewHandler(BaseHTTPRequestHandler):
    server_version = 'MathPaletteReview/1'
    protocol_version = 'HTTP/1.1'

    def _headers(self, status, mime, length, *, cache='no-store'):
        self.send_response(status)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(length))
        self.send_header('Cache-Control', cache)
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'no-referrer')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'")
        self.end_headers()

    def _json(self, payload, status=200):
        data = json.dumps(payload, ensure_ascii=False, allow_nan=False).encode('utf-8')
        self._headers(status, 'application/json; charset=utf-8', len(data))
        self.wfile.write(data)

    def _guard_host(self):
        port = self.server.server_address[1]
        allowed = {f'127.0.0.1:{port}', f'localhost:{port}'}
        if self.headers.get('Host') not in allowed:
            raise ReviewError('Only this local workbench host is allowed', status=403, code='invalid_host')

    def _guard_write(self):
        self._guard_host()
        origin = self.headers.get('Origin')
        if origin is not None and origin != 'http://' + self.headers['Host']:
            raise ReviewError('Cross-site writes are not allowed', status=403, code='cross_site')
        if self.headers.get('Sec-Fetch-Site') not in (None, 'same-origin', 'none'):
            raise ReviewError('Cross-site writes are not allowed', status=403, code='cross_site')
        if self.headers.get('X-Review-Workbench') != '1':
            raise ReviewError('A workbench review request header is required', status=403, code='missing_review_header')
        if self.headers.get_content_type() != 'application/json':
            raise ReviewError('Send application/json', status=415, code='content_type')
        if self.headers.get('Transfer-Encoding'):
            raise ReviewError('Chunked requests are not supported')

    def _error(self, error):
        if isinstance(error, ReviewError):
            self._json({'error': {'code': error.code, 'message': str(error)}}, error.status)
        elif isinstance(error, RecoveryRequired):
            self._json({'error': {'code': 'recovery_required', 'message': str(error) + '. Review writes are blocked until this conflict is repaired.'}}, 503)
        elif isinstance(error, TimeoutError):
            self._json({'error': {'code': 'busy', 'message': str(error)}}, 503)
        else:
            self.log_error('%s: %s', type(error).__name__, error)
            self._json({'error': {'code': 'validation_failed', 'message': str(error)}}, 422)

    def do_GET(self):
        try:
            self._guard_host()
            path = urlsplit(self.path)
            if path.path == '/api/candidates':
                self._json(self.server.service.list_candidates())
                return
            match = re.fullmatch(r'/api/candidates/(MVI?[0-9]{4,8})', path.path)
            if match:
                self._json(self.server.service.detail(match[1]))
                return
            match = re.fullmatch(r'/api/candidates/(MVI?[0-9]{4,8})/image/(source|redraw)', path.path)
            if match:
                query = parse_qs(path.query)
                data, suffix = self.server.service.image(match[1], match[2], query.get('sha256', [''])[0])
                mime = {'.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg'}.get(suffix, 'application/octet-stream')
                self._headers(200, mime, len(data), cache='private, max-age=31536000, immutable')
                self.wfile.write(data)
                return
            if path.path.startswith('/api/'):
                raise ReviewError('API endpoint not found', status=404, code='not_found')
            name = 'index.html' if path.path == '/' else path.path.removeprefix('/static/').lstrip('/')
            if '%' in name or '\\' in name or name.startswith('.') or '..' in Path(name).parts:
                raise ReviewError('Invalid static path', status=404, code='not_found')
            static = safe_path(self.server.service.root / 'review_workbench/static', name)
            if not static.is_file():
                raise ReviewError('Static file not found', status=404, code='not_found')
            data = static.read_bytes()
            mime = mimetypes.guess_type(static.name)[0] or 'application/octet-stream'
            if mime.startswith('text/') or mime in ('application/javascript', 'application/json'):
                mime += '; charset=utf-8'
            self._headers(200, mime, len(data))
            self.wfile.write(data)
        except (BrokenPipeError, ConnectionResetError):
            return
        except Exception as error:
            self._error(error)

    def do_POST(self):
        try:
            self._guard_write()
            length = int(self.headers.get('Content-Length', '0'))
            if length < 1 or length > 4096:
                raise ReviewError('Invalid request body size', status=413, code='body_size')
            body = json.loads(self.rfile.read(length))
            if not isinstance(body, dict) or set(body) != {'fingerprint', 'request_id'}:
                raise ReviewError('Request must contain fingerprint and request_id only')
            match = re.fullmatch(r'/api/candidates/(MVI?[0-9]{4,8})/(pass|delete)', urlsplit(self.path).path)
            if not match:
                raise ReviewError('API endpoint not found', status=404, code='not_found')
            self._json(self.server.service.decide(match[1], match[2], body['fingerprint'], body['request_id']))
        except (BrokenPipeError, ConnectionResetError):
            return
        except Exception as error:
            self.close_connection = True
            self._error(error)

    def do_OPTIONS(self):
        self._json({'error': {'code': 'cross_site', 'message': 'Cross-origin requests are not enabled'}}, 403)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8770)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--no-browser', action='store_true')
    args = parser.parse_args()
    os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    service = MultiSourceReviewService(args.root)
    server = ReviewHTTPServer(('127.0.0.1', args.port), service)
    url = f'http://127.0.0.1:{server.server_address[1]}/'
    print(f'MathPalette original review: {url}\nOnly clicking Pass approves an original. Ctrl+C stops this server.', flush=True)
    if not args.no_browser:
        threading.Timer(0.3, webbrowser.open, args=[url]).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
