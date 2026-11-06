"""HTTP transport with a total wall-clock deadline; no credentials in argv/logs."""
import base64
from http.client import IncompleteRead
import io
import json
from pathlib import Path
import subprocess
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener, HTTPRedirectHandler

class RequestDeadlineExceeded(TimeoutError):
    pass

def request_once(url, body, key, max_bytes, deadline_seconds=120, partial_path=None):
    process = subprocess.Popen([sys.executable, '-X', 'utf8', '-B', str(Path(__file__).resolve()), '--worker'],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    payload=json.dumps({'url':url,'body':base64.b64encode(body).decode('ascii'),
                        'key':key,'max_bytes':max_bytes,'partial_path':str(partial_path) if partial_path else None}).encode('utf-8')
    try:
        stdout, stderr=process.communicate(payload, timeout=deadline_seconds)
    except subprocess.TimeoutExpired:
        process.kill()
        process.communicate()
        raise RequestDeadlineExceeded(f'Local HTTP request cancelled after {deadline_seconds} seconds') from None
    if process.returncode:
        # Do not forward subprocess tracebacks, which could contain request data.
        raise OSError('HTTP transport worker failed')
    result=json.loads(stdout)
    if result['kind']=='response':
        return result['status'],base64.b64decode(result['body'])
    if result['kind']=='incomplete':
        raise IncompleteRead(base64.b64decode(result['body']))
    if result['kind']=='http_error':
        raise HTTPError(url,result['status'],'HTTP error',{},io.BytesIO(base64.b64decode(result['body'])))
    raise URLError(result['error'].replace(key,'[REDACTED]'))

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):
        return None

def worker():
    settings=json.loads(sys.stdin.buffer.read())
    req=Request(settings['url'],data=base64.b64decode(settings['body']),
                headers={'Authorization':'Bearer '+settings['key'],'Content-Type':'application/json'})
    limit=settings['max_bytes']
    try:
        with build_opener(NoRedirect()).open(req,timeout=None) as response:
            chunks=[]
            size=0
            partial=open(settings['partial_path'],'wb') if settings.get('partial_path') else None
            try:
                while size<=limit:
                    chunk=response.read1(min(65536,limit+1-size))
                    if not chunk: break
                    chunks.append(chunk)
                    size+=len(chunk)
                    if partial: partial.write(chunk); partial.flush()
            finally:
                if partial: partial.close()
            body=b''.join(chunks)
            expected=response.headers.get('Content-Length')
            if expected and len(body)<int(expected) and len(body)<=limit:
                raise IncompleteRead(body,int(expected)-len(body))
            result={'kind':'response','status':response.status,'body':base64.b64encode(body).decode('ascii')}
    except IncompleteRead as exc:
        result={'kind':'incomplete','body':base64.b64encode(exc.partial[:limit]).decode('ascii')}
    except HTTPError as exc:
        result={'kind':'http_error','status':exc.code,'body':base64.b64encode(exc.read(16384)).decode('ascii')}
    except Exception as exc:
        result={'kind':'error','error':str(exc).replace(settings['key'],'[REDACTED]')}
    sys.stdout.buffer.write(json.dumps(result).encode('utf-8'))

if __name__=='__main__':
    if sys.argv[1:]!=['--worker']:
        raise SystemExit('Transport module; call request_once().')
    worker()
