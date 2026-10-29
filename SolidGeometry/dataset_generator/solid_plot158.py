"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid158:

    def __init__(self):
        self.__dict__.update({'id': 'Solid158', 'source_dataset': 'MathVision', 'question': 'A 3-pyramid is a stack of the 3 layers of balls shown. A 4-pyramid, a 5-pyramid, and so on are defined in the same way. All the outside balls of an 8-pyramid are removed. What figure do the remaining balls form?\nChoices:\nA:3-pyramid\nB:4-pyramid\nC:5-pyramid\nD:6-pyramid\nE:7-pyramid', 'answer': 'B', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '3-pyramid', 'B': '4-pyramid', 'C': '5-pyramid', 'D': '6-pyramid', 'E': '7-pyramid'}, 'source_key': 'test:1319', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid158.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid158.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid158', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid158.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid158().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
