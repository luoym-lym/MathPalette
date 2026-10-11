"""Local-only SOLIDGEO ORIGINAL question review. Never a Special approval API."""
from __future__ import annotations

import argparse
import hmac
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
from urllib.parse import unquote, urlsplit
import webbrowser

try:
    from .importer import ROOT, ReviewError, parse_json
    from .store import ReviewStore
except ImportError:
    from importer import ROOT, ReviewError, parse_json
    from store import ReviewStore

STATIC = Path(__file__).resolve().parent / 'static'


def make_handler(store):
    class Handler(BaseHTTPRequestHandler):
        server_version = 'SOLIDGEO-OriginalReview/1.0'

        def log_message(self, format, *args):
            if self.path != '/api/state':
                super().log_message(format, *args)

        def _send(self, data, status=200, content_type='application/json; charset=utf-8'):
            if not isinstance(data, bytes):
                data = json.dumps(data, ensure_ascii=False, allow_nan=False).encode('utf-8')
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('X-Frame-Options', 'DENY')
            self.send_header('Referrer-Policy', 'no-referrer')
            self.send_header('Cross-Origin-Resource-Policy', 'same-origin')
            self.send_header('Content-Security-Policy', "default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'")
            self.end_headers()
            self.wfile.write(data)

        def _error(self, error):
            if isinstance(error, ReviewError):
                status, code, message = error.status, error.code, str(error)
            elif isinstance(error, (ValueError, KeyError, TypeError, UnicodeError)):
                status, code, message = 400, 'invalid_request', str(error)
            elif isinstance(error, TimeoutError):
                status, code, message = 409, 'busy', '其他审核窗口正在写入，请稍后重试。'
            else:
                status, code, message = 500, 'internal_error', str(error)
            self._send({'ok': False, 'error': message, 'message': message, 'code': code}, status)

        def _guard(self, *, mutation=False):
            if self.client_address[0] not in ('127.0.0.1', '::1'):
                raise ReviewError('仅允许本机访问。', 403, 'not_loopback')
            hosts = self.headers.get_all('Host', [])
            expected = {f'127.0.0.1:{self.server.server_port}', f'localhost:{self.server.server_port}'}
            if len(hosts) != 1 or hosts[0] not in expected:
                raise ReviewError('仅允许本机工作台地址。', 403, 'invalid_host')
            origins = self.headers.get_all('Origin', [])
            if len(origins) > 1 or origins and origins[0] != 'http://' + hosts[0]:
                raise ReviewError('拒绝其他网页来源。', 403, 'invalid_origin')
            if self.headers.get('Sec-Fetch-Site') not in (None, 'same-origin', 'none'):
                raise ReviewError('拒绝跨站请求。', 403, 'cross_site_request')
            if mutation:
                tokens = self.headers.get_all('X-Review-Token', [])
                if len(tokens) != 1 or not hmac.compare_digest(tokens[0], store.review_token):
                    raise ReviewError('审核页面会话已过期，请刷新。', 403, 'invalid_session')

        def do_GET(self):
            try:
                self._guard()
                path = unquote(urlsplit(self.path).path)
                if path == '/api/state':
                    return self._send(store.snapshot())
                if path == '/api/health':
                    return self._send({'ready': True, 'session_id': store.session_id, 'mode': 'original_review'})
                if path.startswith('/api/image/'):
                    parts = path.removeprefix('/api/image/').split('/')
                    if len(parts) != 2:
                        raise ReviewError('图片路径无效。', 404, 'not_found')
                    data, mime = store.image(*parts)
                    return self._send(data, content_type=mime)
                static = {'/': ('index.html', 'text/html; charset=utf-8'),
                          '/index.html': ('index.html', 'text/html; charset=utf-8'),
                          '/app.js': ('app.js', 'text/javascript; charset=utf-8'),
                          '/style.css': ('style.css', 'text/css; charset=utf-8'),
                          '/vendor/katex.min.js': ('vendor/katex.min.js', 'application/javascript; charset=utf-8'),
                          '/vendor/auto-render.min.js': ('vendor/auto-render.min.js', 'application/javascript; charset=utf-8')}
                if path in static:
                    name, mime = static[path]
                    return self._send((STATIC / name).read_bytes(), content_type=mime)
                raise ReviewError('路径不存在。', 404, 'not_found')
            except (BrokenPipeError, ConnectionResetError):
                return
            except Exception as error:
                self._error(error)

        def do_POST(self):
            try:
                self._guard(mutation=True)
                if self.headers.get('Transfer-Encoding') is not None:
                    raise ReviewError('不接受分块请求。', 400, 'invalid_request')
                lengths = self.headers.get_all('Content-Length', [])
                if len(lengths) != 1:
                    raise ReviewError('请求长度无效。', 411, 'invalid_length')
                length = int(lengths[0])
                if not 0 < length <= 64 * 1024:
                    raise ReviewError('请求大小无效。', 413, 'invalid_length')
                if self.headers.get('Content-Type', '').split(';')[0].strip().lower() != 'application/json':
                    raise ReviewError('请求须为 application/json。', 415, 'invalid_content_type')
                self.connection.settimeout(15)
                raw = self.rfile.read(length)
                if len(raw) != length:
                    raise ReviewError('请求正文不完整。', 400, 'invalid_length')
                body = parse_json(raw.decode('utf-8'))
                if not isinstance(body, dict):
                    raise ReviewError('请求正文必须为对象。')
                path = urlsplit(self.path).path
                if path == '/api/navigate':
                    return self._send(store.navigate(body['candidate_id']))
                if path in ('/api/pass', '/api/delete'):
                    method = store.pass_candidate if path == '/api/pass' else store.delete_candidate
                    return self._send(method(body['candidate_id'], body['content_sha256'], body['request_id']))
                if path == '/api/shutdown':
                    self._send({'ok': True, 'stopping': True})
                    threading.Thread(target=self.server.shutdown, daemon=True).start()
                    return
                raise ReviewError('路径不存在。', 404, 'not_found')
            except (BrokenPipeError, ConnectionResetError):
                return
            except Exception as error:
                self._error(error)

        def do_OPTIONS(self):
            self._send({'ok': False, 'error': '不支持跨域请求。', 'code': 'cors_disabled'}, 403)

    return Handler


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='Repository root (isolated copies supported).')
    parser.add_argument('--port', type=int, default=8770)
    parser.add_argument('--open-browser', action='store_true')
    args = parser.parse_args(argv)
    if not 0 <= args.port <= 65535:
        parser.error('Port must be in 0..65535')
    store = ReviewStore(args.root)
    server = ThreadingHTTPServer(('127.0.0.1', args.port), make_handler(store))
    server.daemon_threads = True
    url = f'http://127.0.0.1:{server.server_port}/'
    print(f'SOLIDGEO 原题审核（本机）: {url}', flush=True)
    if args.open_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
