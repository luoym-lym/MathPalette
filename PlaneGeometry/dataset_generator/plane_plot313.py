"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane313:

    def __init__(self):
        self.__dict__.update({'id': 'Plane313', 'source_dataset': 'MathVision', 'question': 'A dark disc with three holes is placed on top of a dial of a watch (see diagram). Then the disc is rotated around its centre. Which numbers can be seen at the same time?\nChoices:\nA:4, 6 and 12\nB:1, 5 and 10\nC:2, 4 and 9\nD:3, 6 and 9\nE:5, 7 and 12', 'answer': 'A', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '4, 6 and 12', 'B': '1, 5 and 10', 'C': '2, 4 and 9', 'D': '3, 6 and 9', 'E': '5, 7 and 12'}, 'source_key': 'test:984', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane313.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane313.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane313', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane313.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane313().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
