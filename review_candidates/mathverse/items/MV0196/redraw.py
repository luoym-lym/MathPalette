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
class MV0196:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'The circles are concentric, and chord AB of the outer circle is tangent to the inner circle. Using the measurement shown (in metres), find the area of the annulus.\nChoices:\nA:16 m²\nB:8π m²\nC:64 m²\nD:16π m²', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'id': 'MV0196', 'choices': {'A': '16 m²', 'B': '8π m²', 'C': '64 m²', 'D': '16π m²'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0196.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('plane_extended', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0196().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
