"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane246:

    def __init__(self):
        self.__dict__.update({'id': 'Plane246', 'source_dataset': 'MathVision', 'question': 'Machine $R$ rotates a square piece of paper as shown.\nMachine $S$ prints on the paper as shown.\nThe target picture is shown below the two machine diagrams.\nIn which order must the two machines be used to produce this picture?\nChoices:\nA:SRR\nB:RSR\nC:RSS\nD:RRS\nE:SRS', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': 'SRR', 'B': 'RSR', 'C': 'RSS', 'D': 'RRS', 'E': 'SRS'}, 'source_key': 'test:698', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane246.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane246.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane246', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane246.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane246().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
