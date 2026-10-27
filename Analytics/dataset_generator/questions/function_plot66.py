"""Deterministic frozen-scene redraw. Importing does not write files."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parent
def _runtime():
    spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'..\\mathverse_renderers\\runtime.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def finalize(fig,destination):
    return _runtime().finalize('analytics_functions',fig,destination)
def build_scene():
    return _runtime().build_scene('analytics_functions',ROOT/'..\\scenes\\Ana66.json')
class Ana66:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'A positive vertical rescaling of a polynomial is shown. Which expression has its real roots and end behavior?\nChoices:\nA:(x+5)(2x+3)(x-2)\nB:(x-5)(2x-3)(x+2)\nC:(-5x)(-3x/2)(2x)\nD:(5x)(3x/2)(-2x)', 'answer': 'A', 'answer_type': 'choice', 'subject': 'Analytics', 'id': 'Ana66', 'choices': {'A': '(x+5)(2x+3)(x-2)', 'B': '(x-5)(2x-3)(x+2)', 'C': '(-5x)(-3x/2)(2x)', 'D': '(5x)(3x/2)(-2x)'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'..\\scenes\\Ana66.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'..\\..\\..'/".runtime"/"mathverse_redraw"/'Ana66.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'..\\mathverse_renderers\\runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('analytics_functions', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(Ana66().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
