"""Deterministic frozen-scene redraw. Importing does not write files."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parent
def _runtime():
    spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def finalize(fig,destination):
    return _runtime().finalize('plane_curves',fig,destination)
def build_scene():
    return _runtime().build_scene('plane_curves',ROOT/'scene.json')
class MV0782:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'In triangle ABC above, AB = AC, E is the midpoint of line AB, and D is the midpoint of line AC. If AE = x, what is length BC?\nChoices:\nA: 6\nB: 8\nC: 2*x\nD: 4*x\nE: 4*x^2', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'id': 'MV0782', 'choices': {'A': '6', 'B': '8', 'C': '2*x', 'D': '4*x', 'E': '4*x^2'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0782.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('plane_curves', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0782().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
