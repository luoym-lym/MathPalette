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
class MV0550:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': "In the plotted coordinates, one x-unit is 10 meters of width and one y-unit is 10 meters of length. Elena knows that Lea has a garden with an area of 100 square meters. She does not know the specific width, $w$, and length, $l$ of the garden. The graph below represents the widths that correspond to possible lengths of Lea's garden. As the possible width of Lea's garden increases, what does its possible length approach?\nChoices:\nA:$\\infty$\nB:$0$\nC:$10$\nD:$120$", 'answer': 'B', 'answer_type': 'choice', 'subject': 'Analytics', 'id': 'MV0550', 'choices': {'A': '$\\infty$', 'B': '$0$', 'C': '$10$', 'D': '$120$'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0550.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('analytics_functions', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0550().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
