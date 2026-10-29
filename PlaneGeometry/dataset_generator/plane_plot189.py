"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane189:

    def __init__(self):
        self.__dict__.update({'id': 'Plane189', 'source_dataset': 'MathVision', 'question': "Which numbers are written in the area that belongs to the rectangle and to the circle but doesn't belong to the triangle?\nChoices:\nA:5 and 11\nB:1 and 10\nC:13\nD:3 and 9\nE:6, 7, and 4", 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '5 and 11', 'B': '1 and 10', 'C': '13', 'D': '3 and 9', 'E': '6, 7, and 4'}, 'source_key': 'test:406', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane189.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane189.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane189', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane189.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane189().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
