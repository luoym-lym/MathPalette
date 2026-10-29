"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane421:

    def __init__(self):
        self.__dict__.update({'id': 'Plane421', 'source_dataset': 'MathVision', 'question': "A parallelogram contains two identical regular hexagons. The hexagons share a common side, and each has two sides touching the sides of the parallelogram. What fraction of the parallelogram's area is shaded?\nChoices:\nA:$\\frac{2}{3}$\nB:$\\frac{1}{2}$\nC:$\\frac{1}{3}$\nD:$\\frac{1}{4}$\nE:$\\frac{3}{5}$", 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$\\frac{2}{3}$', 'B': '$\\frac{1}{2}$', 'C': '$\\frac{1}{3}$', 'D': '$\\frac{1}{4}$', 'E': '$\\frac{3}{5}$'}, 'source_key': 'test:1844', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane421.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane421.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane421', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane421.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane421().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
