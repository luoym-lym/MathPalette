"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid235:

    def __init__(self):
        self.__dict__.update({'id': 'Solid235', 'source_dataset': 'MathVision', 'question': 'A one-cubic-foot cube is cut into four pieces by three cuts parallel to the top face of the cube. The first cut is $\\frac{1}{2}$ foot from the top face. The second cut is $\\frac{1}{3}$ foot below the first cut, and the third cut is $\\frac{1}{17}$ foot below the second cut. From the top to the bottom the pieces are labeled A, B, C, and D. The pieces are then glued together end to end as shown in the second diagram. What is the total surface area of this solid in square feet?\n\nChoices:\nA:6$\nB:$7$\nC:$\\frac{419}{51}$\nD:$\\frac{158}{17}$\nE:$11$', 'answer': 'E', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '6$', 'B': '$7$', 'C': '$\\frac{419}{51}$', 'D': '$\\frac{158}{17}$', 'E': '$11$'}, 'source_key': 'test:2704', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid235.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid235.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid235', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid235.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid235().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
