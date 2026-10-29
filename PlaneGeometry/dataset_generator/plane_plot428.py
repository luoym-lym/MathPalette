"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane428:

    def __init__(self):
        self.__dict__.update({'id': 'Plane428', 'source_dataset': 'MathVision', 'question': 'The diagram shows a shape made from six squares, each measuring $1 \\mathrm{~cm}$ by $1 \\mathrm{~cm}$. The shape has perimeter of length $14 \\mathrm{~cm}$. The zigzag shape is then continued until it has 2013 squares. What is the length, in $\\mathrm{cm}$, of the perimeter of the new shape?', 'answer': '4028', 'answer_type': 'number', 'subject': 'PlaneGeometry', 'source_key': 'test:1891', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane428.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane428.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane428', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane428.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane428().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
