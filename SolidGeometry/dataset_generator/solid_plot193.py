"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid193:

    def __init__(self):
        self.__dict__.update({'id': 'Solid193', 'source_dataset': 'MathVision', 'question': 'One face of a cardboard cube is cut along its diagonals, as shown.\nWhich of the following are not nets for this cube?\nChoices:\nA:1 and 3\nB:1 and 5\nC:2 and 4\nD:2 and 4\nE:3 and 5', 'answer': 'E', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '1 and 3', 'B': '1 and 5', 'C': '2 and 4', 'D': '2 and 4', 'E': '3 and 5'}, 'source_key': 'test:1843', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid193.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid193.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid193', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid193.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid193().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
