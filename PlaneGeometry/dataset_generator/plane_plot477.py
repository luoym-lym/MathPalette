"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane477:

    def __init__(self):
        self.__dict__.update({'id': 'Plane477', 'source_dataset': 'MathVision', 'question': 'Each of the following four large congruent squares is subdivided into combinations of congruent triangles or rectangles and is partially shaded. What percent of the total area is shaded?\n\n\nChoices:\nA:$12\\frac{1}{2}$\nB:$20$\nC:$25$\nD:$33 \\frac{1}{3}$\nE:$37\\frac{1}{2}$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$12\\frac{1}{2}$', 'B': '$20$', 'C': '$25$', 'D': '$33 \\frac{1}{3}$', 'E': '$37\\frac{1}{2}$'}, 'source_key': 'test:2711', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane477.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane477.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane477', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane477.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane477().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
