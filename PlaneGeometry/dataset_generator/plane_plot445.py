"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane445:

    def __init__(self):
        self.__dict__.update({'id': 'Plane445', 'source_dataset': 'MathVision', 'question': 'A paper triangle with sides of lengths 3, 4, and 5 inches, as shown, is folded so that point $A$ falls on point $B$. What is the length in inches of the crease?\nChoices:\nA:$1+\\frac{1}{2} \\sqrt{2}$\nB:$\\sqrt{3}$\nC:$\\frac{7}{4}$\nD:$\\frac{15}{8}$\nE:$2$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$1+\\frac{1}{2} \\sqrt{2}$', 'B': '$\\sqrt{3}$', 'C': '$\\frac{7}{4}$', 'D': '$\\frac{15}{8}$', 'E': '$2$'}, 'source_key': 'test:2215', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane445.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane445.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane445', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane445.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane445().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
