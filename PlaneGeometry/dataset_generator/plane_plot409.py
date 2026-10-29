"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane409:

    def __init__(self):
        self.__dict__.update({'id': 'Plane409', 'source_dataset': 'MathVision', 'question': 'Three congruent isosceles trapeziums are assembled to form an equilateral triangle with a hole in the middle, as shown in the diagram.\nWhat is the perimeter of the hole?\nChoices:\nA:$3 a+6 b$\nB:$3 b-6 a$\nC:$6 b-3 a$\nD:$6 a+3 b$\nE:$6 a-3 b$', 'answer': 'E', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$3 a+6 b$', 'B': '$3 b-6 a$', 'C': '$6 b-3 a$', 'D': '$6 a+3 b$', 'E': '$6 a-3 b$'}, 'source_key': 'test:1748', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane409.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane409.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane409', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane409.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane409().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
