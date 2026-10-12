"""Deterministic frozen-scene redraw. Importing does not write files."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parent
def _runtime():
    spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'mathverse_renderers\\runtime.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def finalize(fig,destination):
    return _runtime().finalize('solid',fig,destination)
def build_scene():
    return _runtime().build_scene('solid',ROOT/'scenes\\Solid35.json')
class Solid35:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'As shown in the picture, and the lateral area of the cone-shaped tent roof (excluding the seams) is ()\nChoices:\nA:15πm^{2}\nB:30πm^{2}\nC:50πm^{2}\nD:75πm^{2}', 'answer': 'C', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'id': 'Solid35', 'choices': {'A': '15πm^{2}', 'B': '30πm^{2}', 'C': '50πm^{2}', 'D': '75πm^{2}'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scenes\\Solid35.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'..\\..'/".runtime"/"mathverse_redraw"/'Solid35.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'mathverse_renderers\\runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('solid', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(Solid35().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
