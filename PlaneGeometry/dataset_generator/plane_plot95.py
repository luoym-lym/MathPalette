"""Frozen Author designed curve question; no writes on import."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parent
def _renderer():
    spec=importlib.util.spec_from_file_location('_author_curves',ROOT/'author_curves/common_renderer.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def build_scene():
    return _renderer().render_scene(json.loads((ROOT/'scenes/Plane95.json').read_text(encoding='utf-8')))
class Plane95:
    def __init__(self):
        self.id='Plane95'
        self.source_dataset='Author designed'
        self.question='Starting at E, which endpoint is reached along the same smooth curve, without switching curves at any crossing?'
        self.query=self.question
        self.answer='B'
        self.answer_type='text'
        self.subject='PlaneGeometry'
        self.level=None
        self.scene_path=ROOT/'scenes/Plane95.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))
    def build_scene(self):
        return build_scene()
    def draw(self,num=0,output_path=None):
        if output_path is None and isinstance(num,(str,Path)):output_path=num
        destination=Path(output_path) if output_path else ROOT.parents[1]/'.runtime/author_designed_redraw/Plane95.png'
        return _renderer().draw(self.scene_path,destination)
    def redraw(self,output_path=None):
        return self.draw(output_path=output_path)
if __name__=='__main__':
    import sys
    print(Plane95().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
