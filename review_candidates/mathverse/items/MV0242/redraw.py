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
class MV0242:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'For the concave pentagon shown, find m \\angle W.\nChoices:\nA:38\nB:58\nC:76\nD:152', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'id': 'MV0242', 'choices': {'A': '38', 'B': '58', 'C': '76', 'D': '152'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0242.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('plane_arrows', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0242().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
