"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane462:

    def __init__(self):
        self.__dict__.update({'id': 'Plane462', 'source_dataset': 'MathVision', 'question': 'Consider these two geoboard quadrilaterals. Which of the following statements is true?\n\nChoices:\nA:$\\text{The area of quadrilateral I is more than the area of quadrilateral II.}$\nB:$\\text{The area of quadrilateral I is less than the area of quadrilateral II.}$\nC:$\\text{The quadrilaterals have the same area and the same perimeter.}$\nD:$\\text{The quadrilaterals have the same area, but the perimeter of I is more than the perimeter of II.}$\nE:$\\text{The quadrilaterals have the same area, but the perimeter of I is less than the perimeter of II.}$', 'answer': 'E', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$\\text{The area of quadrilateral I is more than the area of quadrilateral II.}$', 'B': '$\\text{The area of quadrilateral I is less than the area of quadrilateral II.}$', 'C': '$\\text{The quadrilaterals have the same area and the same perimeter.}$', 'D': '$\\text{The quadrilaterals have the same area, but the perimeter of I is more than the perimeter of II.}$', 'E': '$\\text{The quadrilaterals have the same area, but the perimeter of I is less than the perimeter of II.}$'}, 'source_key': 'test:2620', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane462.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane462.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane462', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane462.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane462().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
