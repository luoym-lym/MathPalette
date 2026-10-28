#!/usr/bin/env python3
"""Fresh process replay into independent runtime outputs; never fit or edit scenes."""
import concurrent.futures,hashlib,json,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
RUN=ROOT/'.runtime/protocol_redraw'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def one(row):
 d=ROOT/row['scene'];item=d.parent;out=RUN/'independent_repeat'/row['id'];out.mkdir(parents=True,exist_ok=True)
 before={p.name:sha(p) for p in (d,item/'protocol_review.json',ROOT/'review_candidates/mathvision/shared/protocol_renderer.py')}
 command=[sys.executable,'-B',str(ROOT/'review_candidates/mathvision/shared/protocol_renderer.py'),str(item),'--output-dir',str(out)]
 proc=subprocess.run(command,cwd=ROOT,capture_output=True,text=True)
 (out/'process.log').write_text(proc.stdout+proc.stderr)
 after={p.name:sha(p) for p in (d,item/'protocol_review.json',ROOT/'review_candidates/mathvision/shared/protocol_renderer.py')}
 result={'id':row['id'],'command':command,'returncode':proc.returncode,'input_hashes':before,'inputs_stable':before==after}
 if proc.returncode==0:
  result['comparison']={n:{'current':sha(item/n),'fresh_replay':sha(out/n),'byte_equal':sha(item/n)==sha(out/n)} for n in ('image.png','image.svg')}
  from PIL import Image
  import numpy as np
  result['png_pixels_equal']=bool(np.array_equal(np.array(Image.open(item/'image.png')),np.array(Image.open(out/'image.png'))))
 (out/'independent_check.json').write_text(json.dumps(result,indent=2)+'\n')
 return result
if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--ids',nargs='*');ap.add_argument('--workers',type=int,default=3);args=ap.parse_args()
 rows=[json.loads(x) for x in (ROOT/'review_candidates/mathvision/index.jsonl').read_text().splitlines()]
 if args.ids:rows=[r for r in rows if r['id'] in args.ids]
 results=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
  for r in pool.map(one,rows):
   results.append(r)
   if len(results)%25==0:print('replayed',len(results),flush=True)
 (RUN/'audit').mkdir(parents=True,exist_ok=True)
 (RUN/'audit/independent_repeat.json').write_text(json.dumps({'count':len(results),'items':results},indent=2)+'\n')
 print('Done',len(results))

 if __name__=='__main__': raise SystemExit(any(r['returncode'] or not r['inputs_stable'] or not r.get('png_pixels_equal') or not all(c['byte_equal'] for c in r.get('comparison',{}).values()) for r in results))
