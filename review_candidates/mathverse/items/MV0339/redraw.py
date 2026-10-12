"""Deterministic frozen-scene redraw. Importing does not write files."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parent
def _runtime():
    spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def finalize(fig,destination):
    return _runtime().finalize('plane_arrows',fig,destination)
def build_scene():
    return _runtime().build_scene('plane_arrows',ROOT/'scene.json')
class MV0339:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'Find the true bearing of point B from point A.\nChoices:\nA: 090^\\circ T\nB: 180^\\circ T\nC: 049^\\circ T\nD: 041^\\circ T', 'answer': 'A', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'id': 'MV0339', 'choices': {'A': '090^\\circ T', 'B': '180^\\circ T', 'C': '049^\\circ T', 'D': '041^\\circ T'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0339.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('plane_arrows', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0339().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
