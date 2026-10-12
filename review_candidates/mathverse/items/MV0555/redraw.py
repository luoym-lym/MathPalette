"""Deterministic frozen-scene redraw. Importing does not write files."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parent
def _runtime():
    spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def finalize(fig,destination):
    return _runtime().finalize('analytics_functions',fig,destination)
def build_scene():
    return _runtime().build_scene('analytics_functions',ROOT/'scene.json')
class MV0555:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'The angle theta is shown on the unit circle. Which pair consists of two expressions both equal to -cos(theta)?\nChoices:\nA:cos(pi+theta) and cos(pi-theta)\nB:cos(pi+theta) and cos(pi/2-theta)\nC:cos(pi/2-theta) and cos(2 pi-theta)\nD:cos(pi-theta) and cos(2 pi-theta)', 'answer': 'A', 'answer_type': 'choice', 'subject': 'Analytics', 'id': 'MV0555', 'choices': {'A': 'cos(pi+theta) and cos(pi-theta)', 'B': 'cos(pi+theta) and cos(pi/2-theta)', 'C': 'cos(pi/2-theta) and cos(2 pi-theta)', 'D': 'cos(pi-theta) and cos(2 pi-theta)'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0555.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('analytics_functions', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0555().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
