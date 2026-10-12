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
class MV0161:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'As shown in the figure, , If the ratio of the distance from the bulb to the vertex of the triangle ruler to the distance from the bulb to the corresponding vertex of the triangular ruler projection is 2.0:5.0, Then the corresponding edge length of the projection triangle is ()\nChoices:\nA:8cm\nB:20cm\nC:3.2cm\nD:10cm', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'id': 'MV0161', 'choices': {'A': '8cm', 'B': '20cm', 'C': '3.2cm', 'D': '10cm'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0161.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('plane_extended', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0161().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
