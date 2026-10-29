"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid233:

    def __init__(self):
        self.__dict__.update({'id': 'Solid233', 'source_dataset': 'MathVision', 'question': 'A shape is created by joining seven unit cubes, as shown. What is the ratio of the volume in cubic units to the surface area in square units?\n\nChoices:\nA:1 : 6\nB:7 : 36\nC:1 : 5\nD:7 : 30\nE:6 : 25', 'answer': 'D', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '1 : 6', 'B': '7 : 36', 'C': '1 : 5', 'D': '7 : 30', 'E': '6 : 25'}, 'source_key': 'test:2690', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid233.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid233.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid233', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid233.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid233().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
