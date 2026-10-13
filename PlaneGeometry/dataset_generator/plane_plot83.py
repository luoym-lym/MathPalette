"""Deterministic frozen-scene redraw. Importing does not write files."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parent
def _runtime():
    spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'mathverse_renderers\\runtime.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def finalize(fig,destination):
    return _runtime().finalize('plane',fig,destination)
def build_scene():
    return _runtime().build_scene('plane',ROOT/'scenes\\Plane83.json')
class Plane83:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'As shown in the figure, chord AC parallel radius OB, then the degree of angle OAB is ()\nChoices:\nA:25°\nB:50°\nC:60°\nD:30°', 'answer': 'A', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'id': 'Plane83', 'choices': {'A': '25°', 'B': '50°', 'C': '60°', 'D': '30°'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scenes\\Plane83.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'..\\..'/".runtime"/"mathverse_redraw"/'Plane83.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'mathverse_renderers\\runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('plane', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(Plane83().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
