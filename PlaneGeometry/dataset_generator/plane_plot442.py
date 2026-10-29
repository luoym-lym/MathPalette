"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane442:

    def __init__(self):
        self.__dict__.update({'id': 'Plane442', 'source_dataset': 'MathVision', 'question': 'A dart board is a regular octagon divided into regions as shown. Suppose that a dart thrown at the board is equally likely to land anywhere on the board. What is the probability that the dart lands within the center square?\n\nChoices:\nA:$\\frac{\\sqrt{2} - 1}{2}$\nB:$\\frac{1}{4}$\nC:$\\frac{2 - \\sqrt{2}}{2}$\nD:$\\frac{\\sqrt{2}}{4}$\nE:$2 - \\sqrt{2}$', 'answer': 'A', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$\\frac{\\sqrt{2} - 1}{2}$', 'B': '$\\frac{1}{4}$', 'C': '$\\frac{2 - \\sqrt{2}}{2}$', 'D': '$\\frac{\\sqrt{2}}{4}$', 'E': '$2 - \\sqrt{2}$'}, 'source_key': 'test:2181', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane442.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane442.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane442', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane442.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane442().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
