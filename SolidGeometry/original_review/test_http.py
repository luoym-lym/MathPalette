"""Real loopback HTTP contract/security tests, always against isolated fixtures."""
from __future__ import annotations

import http.client
import json
import threading
from http.server import ThreadingHTTPServer
import unittest
import uuid

from server import make_handler
from store import ReviewStore
from test_support import IsolatedRepository, file_hashes


class HTTPReviewTests(unittest.TestCase):
    def setUp(self):
        self.fixture = IsolatedRepository(2)
        self.store = ReviewStore(self.fixture.root)
        self.server = None
        try:
            self.server = ThreadingHTTPServer(('127.0.0.1', 0), make_handler(self.store))
        except PermissionError as error:
            self.fixture.close()
            self.skipTest('The execution environment denies loopback sockets: ' + str(error))
        self.server.daemon_threads = True
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.host = f'127.0.0.1:{self.server.server_port}'
        self.origin = 'http://' + self.host

    def tearDown(self):
        if self.server is not None:
            self.server.shutdown()
            self.server.server_close()
            self.thread.join(5)
        self.fixture.close()

    def request(self, method, path, body=None, headers=None, *, raw=None):
        payload = json.dumps(body).encode() if body is not None else raw
        default = {'Host': self.host}
        if method == 'POST':
            default.update({'Content-Type': 'application/json', 'X-Review-Token': self.store.review_token,
                            'Origin': self.origin})
        default.update(headers or {})
        default = {key: value for key, value in default.items() if value is not None}
        connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port, timeout=20)
        try:
            connection.request(method, path, body=payload, headers=default)
            response = connection.getresponse()
            content = response.read()
            if response.headers.get_content_type() == 'application/json':
                content = json.loads(content)
            return response.status, dict(response.headers), content
        finally:
            connection.close()

    def mutation_body(self, index=0):
        status, _, state = self.request('GET', '/api/state')
        self.assertEqual(status, 200)
        row = state['candidates'][index]
        return {'candidate_id': row['id'], 'content_sha256': row['content_sha256'], 'request_id': uuid.uuid4().hex}

    def test_state_health_images_static_and_security_headers(self):
        status, headers, state = self.request('GET', '/api/state')
        self.assertEqual(status, 200)
        self.assertEqual(state['review_token'], self.store.review_token)
        self.assertEqual(headers['Cache-Control'], 'no-store')
        self.assertEqual(headers['X-Content-Type-Options'], 'nosniff')
        self.assertEqual(headers['Cross-Origin-Resource-Policy'], 'same-origin')
        self.assertIn("frame-ancestors 'none'", headers['Content-Security-Policy'])
        for row in state['candidates']:
            for field in ('source_image_url', 'redraw_image_url'):
                status, headers, image = self.request('GET', row[field])
                self.assertEqual(status, 200)
                self.assertTrue(headers['Content-Type'].startswith('image/'))
                self.assertTrue(image.startswith(b'\x89PNG'))
        for path in ('/', '/index.html', '/style.css', '/app.js', '/vendor/katex.min.js',
                     '/vendor/auto-render.min.js', '/api/health'):
            with self.subTest(path=path):
                self.assertEqual(self.request('GET', path)[0], 200)

    def test_origin_host_fetch_site_and_token_guards_reject_mutations(self):
        body = self.mutation_body()
        before = file_hashes(self.fixture.root)
        cases = [({'Host': 'evil.example'}, 'invalid_host'),
                 ({'Origin': 'https://evil.example'}, 'invalid_origin'),
                 ({'Origin': 'null'}, 'invalid_origin'),
                 ({'Sec-Fetch-Site': 'cross-site'}, 'cross_site_request'),
                 ({'Sec-Fetch-Site': 'same-site'}, 'cross_site_request'),
                 ({'X-Review-Token': None}, 'invalid_session'),
                 ({'X-Review-Token': 'old-token'}, 'invalid_session')]
        for headers, code in cases:
            with self.subTest(headers=headers):
                status, _, data = self.request('POST', '/api/pass', body, headers)
                self.assertEqual(status, 403)
                self.assertEqual(data['code'], code)
                self.assertEqual(file_hashes(self.fixture.root), before)
        for headers in ({'Host': 'evil.example'}, {'Origin': 'https://evil.example'}, {'Sec-Fetch-Site': 'cross-site'}):
            self.assertEqual(self.request('GET', '/api/state', headers=headers)[0], 403)

    def test_duplicate_host_origin_and_token_are_rejected(self):
        body = json.dumps(self.mutation_body()).encode()
        for duplicated in ('Host', 'Origin', 'X-Review-Token'):
            connection = http.client.HTTPConnection('127.0.0.1', self.server.server_port, timeout=10)
            try:
                connection.putrequest('POST', '/api/pass', skip_host=True)
                pairs = [('Host', self.host), ('Origin', self.origin),
                         ('X-Review-Token', self.store.review_token), ('Content-Type', 'application/json'),
                         ('Content-Length', str(len(body)))]
                for key, value in pairs:
                    connection.putheader(key, value)
                    if key == duplicated:
                        connection.putheader(key, value)
                connection.endheaders(body)
                response = connection.getresponse()
                self.assertEqual(response.status, 403)
                response.read()
            finally:
                connection.close()

    def test_navigation_and_idempotent_pass_use_exact_candidate(self):
        first = self.mutation_body(0)
        second = self.fixture.candidates[1]['id']
        status, _, state = self.request('POST', '/api/navigate', {'candidate_id': second})
        self.assertEqual(status, 200)
        self.assertEqual(state['current_candidate_id'], second)
        # An older tab's click still targets its explicit candidate, never the
        # server-wide current selection of another tab.
        status, _, result = self.request('POST', '/api/pass', first)
        self.assertEqual(status, 200)
        self.assertEqual(result['result']['candidate_id'], first['candidate_id'])
        self.assertEqual(result['result']['formal_id'], 'Solid17')
        again = self.request('POST', '/api/pass', first)
        self.assertEqual(again[0], 200)
        self.assertEqual(again[2]['result'], result['result'])
        bad = {**first, 'request_id': uuid.uuid4().hex}
        status, _, data = self.request('POST', '/api/delete', bad)
        self.assertEqual(status, 409)
        self.assertEqual(data['code'], 'already_reviewed')

    def test_delete_replay_returns_durable_result_and_image_becomes_404(self):
        body = self.mutation_body()
        first = self.request('POST', '/api/delete', body)
        self.assertEqual(first[0], 200)
        self.assertTrue(first[2]['result']['deleted_files'])
        self.assertEqual(self.request('POST', '/api/delete', body)[2]['result'], first[2]['result'])
        self.assertEqual(self.request('GET', f"/api/image/{body['candidate_id']}/source")[0], 404)

    def test_stale_hash_malformed_json_and_invalid_content_types_fail_closed(self):
        body = self.mutation_body()
        status, _, data = self.request('POST', '/api/pass', {**body, 'content_sha256': '0' * 64})
        self.assertEqual((status, data['code']), (409, 'stale_candidate'))
        for raw in (b'{bad', b'{"candidate_id":"a","candidate_id":"b"}', b'[]', b'{"x":NaN}', b'\xff'):
            with self.subTest(raw=raw):
                self.assertEqual(self.request('POST', '/api/pass', raw=raw)[0], 400)
        self.assertEqual(self.request('POST', '/api/pass', body, {'Content-Type': 'text/plain'})[0], 415)
        self.assertEqual(self.request('POST', '/api/pass', body, {'Transfer-Encoding': 'chunked'})[0], 400)
        self.assertEqual(self.request('POST', '/api/pass', body, {'Content-Length': '65537'})[0], 413)

    def test_no_environment_source_or_arbitrary_asset_read(self):
        for path in ('/.env', '/store.py', '/importer.py', '/../../.env', '/%2e%2e/.env',
                     '/staging/solidgeo/candidates.jsonl', '/api/image/../../.env',
                     '/api/image/SOLIDGEO_TEST_001/scene', '/api/image/unknown/source'):
            with self.subTest(path=path):
                self.assertEqual(self.request('GET', path)[0], 404)
        self.assertEqual(self.request('OPTIONS', '/api/pass')[0], 403)


if __name__ == '__main__':
    unittest.main()
