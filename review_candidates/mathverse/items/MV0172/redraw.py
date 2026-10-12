"""Deterministic frozen-scene redraw. Importing does not write files."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parent
def _runtime():
    spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def finalize(fig,destination):
    return _runtime().finalize('plane',fig,destination)
def build_scene():
    return _runtime().build_scene('plane',ROOT/'scene.json')
class MV0172:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'As shown in the figure, E and F are the midpoints of AB and AD respectively. then tanC is equal to ()\nChoices:\nA:\\frac{3}{4}\nB:\\frac{4}{3}\nC:\\frac{3}{5}\nD:\\frac{4}{5}', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'id': 'MV0172', 'choices': {'A': '\\frac{3}{4}', 'B': '\\frac{4}{3}', 'C': '\\frac{3}{5}', 'D': '\\frac{4}{5}'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0172.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('plane', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0172().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
