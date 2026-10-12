"""Offline structural and pixel reproduction check; outputs only to explicit runtime path."""
from pathlib import Path
import json,sys,hashlib,importlib.util,tempfile,concurrent.futures,os,argparse
from PIL import Image,ImageChops
PACKAGE=Path(__file__).resolve().parent;ROOT=PACKAGE.parents[1]
sys.path.insert(0,str(ROOT))
def check(row):
 try:
  for key in ['candidate_path','image','original_image','scene','script','provenance','verification']:
   p=(ROOT/row[key]).resolve();assert p.is_relative_to(PACKAGE) and p.is_file(),key
  proof=json.loads((ROOT/row['verification']).read_text())['packaging']
  assert hashlib.sha256((ROOT/row['original_image']).read_bytes()).hexdigest()==proof['source_sha256']
  assert hashlib.sha256((ROOT/row['original_script']).read_bytes()).hexdigest()==proof['script_source_sha256']
  spec=importlib.util.spec_from_file_location('_candidate',ROOT/row['script']);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
  with tempfile.TemporaryDirectory() as td:
   target=Path(td)/'out.png';getattr(m,row['id'])().draw(output_path=target)
   assert ImageChops.difference(Image.open(target).convert('RGB'),Image.open(ROOT/row['image']).convert('RGB')).getbbox() is None,'Pixel mismatch'
  if '--formal' in sys.argv:
   from promotion import prepare
   qid={'PlaneGeometry':'Plane','SolidGeometry':'Solid','Analytics':'Ana'}[row['subject']]+str(9000+int(row['source_problem_index']))
   formal,writes,notes=prepare(ROOT,row,qid)
   with tempfile.TemporaryDirectory() as td:
    base=Path(td)
    for name,data in writes.items():
     p=base/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
    spec=importlib.util.spec_from_file_location('_formal',base/row['subject']/formal['script']);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    target=base/'out.png';getattr(m,qid)().draw(output_path=target)
    assert ImageChops.difference(Image.open(target).convert('RGB'),Image.open(ROOT/row['image']).convert('RGB')).getbbox() is None,'Formal pixel mismatch'
  return {'id':row['id'],'source_key':row['source_key'],'family':row['renderer_family'],'source_byte_identical':True,'pixels_identical':True}
 except Exception as e:return {'id':row['id'],'error':str(e)}
def main():
 os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'.runtime/matplotlib'));os.environ.setdefault('XDG_CACHE_HOME',str(ROOT/'.runtime/cache'))
 rows=[json.loads(l) for l in (PACKAGE/'index.jsonl').read_text().splitlines() if l];assert len(rows)==len({r['id'] for r in rows})==len({r['source_key'] for r in rows})
 with concurrent.futures.ProcessPoolExecutor(max_workers=8) as pool:results=list(pool.map(check,rows))
 parser=argparse.ArgumentParser();parser.add_argument('--formal',action='store_true');parser.add_argument('--output',type=Path,default=ROOT/'.runtime/mathverse_package_validation.json');args=parser.parse_args();out=args.output;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(results,indent=2));bad=[x for x in results if 'error' in x];print(json.dumps({'checked':len(results),'failed':len(bad),'failures':bad},indent=2));return bool(bad)
if __name__=='__main__':sys.exit(main())
