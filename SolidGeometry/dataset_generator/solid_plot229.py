"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid229:

    def __init__(self):
        self.__dict__.update({'id': 'Solid229', 'source_dataset': 'MathVision', 'question': 'Six squares are colored, front and back, (R = red, B = blue, O = orange, Y = yellow, G = green, and W = white). They are hinged together as shown, then folded to form a cube. The face opposite the white face is\n\nChoices:\nA:$\\text{B}$\nB:$\\text{G}$\nC:$\\text{O}$\nD:$\\text{R}$\nE:$\\text{Y}$', 'answer': 'A', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$\\text{B}$', 'B': '$\\text{G}$', 'C': '$\\text{O}$', 'D': '$\\text{R}$', 'E': '$\\text{Y}$'}, 'source_key': 'test:2605', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid229.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid229.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid229', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid229.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid229().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
