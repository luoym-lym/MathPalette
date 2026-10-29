"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid219:

    def __init__(self):
        self.__dict__.update({'id': 'Solid219', 'source_dataset': 'MathVision', 'question': 'A unit cube is cut twice to form three triangular prisms, two of which are congruent, as shown in Figure 1. The cube is then cut in the same manner along the dashed lines shown in Figure 2. This creates nine pieces. What is the volume of the piece that contains vertex $ W$?\nChoices:\nA:$\\frac{1}{12}$\nB:$\\frac{1}{9}$\nC:$\\frac{1}{8}$\nD:$\\frac{1}{6}$\nE:$\\frac{1}{4}$', 'answer': 'A', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$\\frac{1}{12}$', 'B': '$\\frac{1}{9}$', 'C': '$\\frac{1}{8}$', 'D': '$\\frac{1}{6}$', 'E': '$\\frac{1}{4}$'}, 'source_key': 'test:2463', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid219.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid219.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid219', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid219.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid219().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
