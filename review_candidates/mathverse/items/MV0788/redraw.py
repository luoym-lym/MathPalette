"""Deterministic frozen-scene redraw. Importing does not write files."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parent
def _runtime():
    spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def finalize(fig,destination):
    return _runtime().finalize('plane_extended',fig,destination)
def build_scene():
    return _runtime().build_scene('plane_extended',ROOT/'scene.json')
class MV0788:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'In the diagram above, angle A is congruent to angle BED, and angle C is congruent to angle D. If the ratio of the length of AB to the length of EB is 5:1, and the area of the triangle BED is 5*a^2 + 10, what is the area of triangle ABC?\nChoices:\nA: 5*a^2 + 10\nB: 25*a^2 + 50\nC: 25*a^2 + 100\nD: 125*a^2 + 250\nE: cannot be determined', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'id': 'MV0788', 'choices': {'A': '5*a^2 + 10', 'B': '25*a^2 + 50', 'C': '25*a^2 + 100', 'D': '125*a^2 + 250', 'E': 'cannot be determined'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0788.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('plane_extended', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0788().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
