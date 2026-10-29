"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane196:

    def __init__(self):
        self.__dict__.update({'id': 'Plane196', 'source_dataset': 'MathVision', 'question': 'Where is the Kangaroo?\nChoices:\nA:In the circle and in the triangle but not in the square.\nB:In the circle and in the square but not in the triangle.\nC:In the triangle and in the square but not in the circle.\nD:In the circle but in neither the square or the triangle.\nE:In the square but in neither the circle or the triangle.', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': 'In the circle and in the triangle but not in the square.', 'B': 'In the circle and in the square but not in the triangle.', 'C': 'In the triangle and in the square but not in the circle.', 'D': 'In the circle but in neither the square or the triangle.', 'E': 'In the square but in neither the circle or the triangle.'}, 'source_key': 'test:458', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane196.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane196.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane196', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane196.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane196().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
