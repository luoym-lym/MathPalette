"""Frozen author-designed original; importing writes no files."""
from pathlib import Path
import importlib.util, json, sys
ROOT=Path(__file__).resolve().parent
ITEM=ROOT/'author_expand24_v1/items/Plane518'
def _engine():
    p=ROOT/'author_expand24_v1/engine.py'
    spec=importlib.util.spec_from_file_location('_expand24_Plane518',p)
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m
def build_scene(): return _engine().capture(ITEM)
class Plane518:
    def __init__(self):
        row=next(json.loads(s) for s in (ROOT.parent/'dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if s.strip() and json.loads(s)['id']=='Plane518')
        for k,v in row.items():setattr(self,k,v)
        self.query=self.question;self.subject='PlaneGeometry';self.level=None
    def get_scene(self):return json.loads((ROOT/'scenes/Plane518.json').read_text(encoding='utf-8'))
    def build_scene(self):return build_scene()
    def draw(self,num=0,output_path=None):
        if output_path is None and isinstance(num,(str,Path)):output_path=num
        if output_path is None:raise ValueError('An explicit output path is required')
        target=Path(output_path).resolve()
        if target.suffix.lower()!='.png':raise ValueError('Use a PNG output')
        if target.is_relative_to(ROOT.parent) or target==Path(__file__).resolve():raise ValueError('Render outside formal source directories')
        target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(_engine().render(ITEM));return str(target)
    def redraw(self,output_path=None):return self.draw(output_path=output_path)
if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Provide a new output PNG path')
    Plane518().draw(output_path=sys.argv[1])
