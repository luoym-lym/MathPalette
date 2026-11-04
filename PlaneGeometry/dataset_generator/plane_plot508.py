"""Versioned author original. Import is side-effect free."""
from pathlib import Path
import importlib.util, json, sys
ROOT=Path(__file__).resolve().parent
DEP=ROOT / 'author_promote15_v1'
def _engine():
    path=DEP / 'native_renderer.py'
    spec=importlib.util.spec_from_file_location('author_promote15_native',path)
    mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod)
    return mod
def build_scene():
    s=json.loads((DEP / 'items/Plane508/scene.json').read_text(encoding='utf-8'))
    return _engine().capture(s,'connect')
class Plane508:
    def __init__(self):
        records=[json.loads(line) for line in (ROOT.parent/'dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if line.strip()]
        row=next(r for r in records if r['id']=='Plane508')
        for k,v in row.items(): setattr(self,k,v)
        self.query=self.question; self.subject='PlaneGeometry'; self.level=None
    def get_scene(self): return json.loads((ROOT/'scenes/Plane508.json').read_text(encoding='utf-8'))
    def build_scene(self): return build_scene()
    def draw(self,num=0,output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        if output_path is None: raise ValueError('Explicit output_path required')
        s=json.loads((DEP / 'items/Plane508/scene.json').read_text(encoding='utf-8')); data=_engine().render(s,'connect')
        target=Path(output_path); target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data); return str(target)
    def redraw(self,output_path=None): return self.draw(output_path=output_path)
if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Provide output PNG path')
    Plane508().draw(output_path=sys.argv[1])
