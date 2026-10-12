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
class MV0121:
    def __init__(self):
        self.__dict__.update({'source_dataset': 'MathVerse', 'question': 'The diagram is a central cross-section of a right circular conical umbrella. D is the centre of its circular rim, and the handle AP is perpendicular to the rim plane and bisects angle BAC. The symmetric braces satisfy AE = AF and DE = DF. Using the marked lengths in centimetres, find the required oil-paper area, ignoring seams.\nChoices:\nA:48 cm²\nB:70π cm²\nC:2400π cm²\nD:2500π cm²', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'id': 'MV0121', 'choices': {'A': '48 cm²', 'B': '70π cm²', 'C': '2400π cm²', 'D': '2500π cm²'}})
        self.query=self.question
        self.level=None
        self.scene_path=ROOT/'scene.json'
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding="utf-8"))
    def build_scene(self):
        return build_scene()
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        destination=Path(output_path) if output_path else (ROOT/'../../../..'/".runtime"/"mathverse_redraw"/'MV0121.png').resolve()
        spec=importlib.util.spec_from_file_location("mathverse_runtime",ROOT/'../../shared/runtime.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        if self.subject=="Analytics":
            fig,ax=self.build_scene();return finalize(fig,destination)
        return module.draw('plane_extended', self.scene_path, destination)
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__=="__main__":
    import sys
    print(MV0121().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
