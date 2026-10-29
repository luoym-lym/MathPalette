"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane424:

    def __init__(self):
        self.__dict__.update({'id': 'Plane424', 'source_dataset': 'MathVision', 'question': 'A triangular piece of paper is folded along the dotted line shown in the left-hand diagram to form the heptagon shown in the right-hand diagram. The total area of the shaded parts of the heptagon is $1 \\mathrm{~cm}^{2}$. The area of the original triangle is $1 \\frac{1}{2}$ times the area of the heptagon. What is the area of the original triangle, in $\\mathrm{cm}^{2}$?', 'answer': '3', 'answer_type': 'number', 'subject': 'PlaneGeometry', 'source_key': 'test:1864', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane424.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane424.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane424', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane424.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane424().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
