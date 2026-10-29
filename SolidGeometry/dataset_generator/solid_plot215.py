"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid215:

    def __init__(self):
        self.__dict__.update({'id': 'Solid215', 'source_dataset': 'MathVision', 'question': 'In the rectangular parallelepiped shown, $AB = 3, BC= 1,$ and $CG = 2$. Point $M$ is the midpoint of $\\overline{FG}$. What is the volume of the rectangular pyramid with base $BCHE$ and apex $M$?\n\nChoices:\nA:$1$\nB:$\\frac{4}{3}$\nC:$\\frac{3}{2}$\nD:$\\frac{5}{3}$\nE:$2$', 'answer': 'E', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$1$', 'B': '$\\frac{4}{3}$', 'C': '$\\frac{3}{2}$', 'D': '$\\frac{5}{3}$', 'E': '$2$'}, 'source_key': 'test:2220', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid215.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid215.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid215', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid215.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid215().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
