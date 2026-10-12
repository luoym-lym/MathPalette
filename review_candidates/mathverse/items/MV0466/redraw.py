"""Deterministic frozen-scene redraw. Importing does not write files."""
from pathlib import Path
import importlib.util
import json
ROOT=Path(__file__).resolve().parent
def _runtime():
    spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
def finalize(fig,destination):
    return _runtime().finalize('analytics_frozen',fig,destination)
def build_scene():
    return _runtime().build_scene('analytics_frozen',ROOT/'scene.json')
class MV0466:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'Describe the translation to get from x^2+y^2=4^2 to the graph shown.\nChoices:\nA:The graph has been translated 4 units downwards.\nB:The graph has been translated 4 units right.\nC:The graph has been translated 4 units left.\nD:The graph has been translated 4 units upwards.', 'answer': 'A', 'answer_type': 'choice', 'subject': 'Analytics', 'id': 'MV0466', 'choices': {'A': 'The graph has been translated 4 units downwards.', 'B': 'The graph has been translated 4 units right.', 'C': 'The graph has been translated 4 units left.', 'D': 'The graph has been translated 4 units upwards.'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0466.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('analytics_frozen', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0466().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
