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
class MV0622:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'The curve gives the time y, in hours, that an ingredient remains in the bloodstream versus initial dose. One x-unit represents 10 milligrams. What does its intersection with the horizontal line mean?\nChoices:\nA:It gives the time for a 4-milligram initial dose.\nB:It gives the dose at which the time becomes zero.\nC:It gives the initial dose for which the ingredient remains for 4 hours.\nD:It means the dose in milligrams equals the time in hours.', 'answer': 'C', 'answer_type': 'choice', 'subject': 'Analytics', 'id': 'MV0622', 'choices': {'A': 'It gives the time for a 4-milligram initial dose.', 'B': 'It gives the dose at which the time becomes zero.', 'C': 'It gives the initial dose for which the ingredient remains for 4 hours.', 'D': 'It means the dose in milligrams equals the time in hours.'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0622.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('analytics_functions', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0622().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
