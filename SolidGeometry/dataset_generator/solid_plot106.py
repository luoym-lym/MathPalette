"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid106:

    def __init__(self):
        self.__dict__.update({'id': 'Solid106', 'source_dataset': 'MathVision', 'question': 'A cylinder is $15 \\mathrm{~cm}$ high, and its base circumference is $30 \\mathrm{~cm}$. A path from point $A$ at the base to point $B$ at the top consists of vertical upward segments and horizontal circular arcs. It is shown in bold, with a solid line on the front and a dashed line at the back. What is the total length of the path?\nChoices:\nA:$45 \\mathrm{~cm}$\nB:$55 \\mathrm{~cm}$\nC:$60 \\mathrm{~cm}$\nD:$65 \\mathrm{~cm}$\nE:$75 \\mathrm{~cm}$', 'answer': 'E', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$45 \\mathrm{~cm}$', 'B': '$55 \\mathrm{~cm}$', 'C': '$60 \\mathrm{~cm}$', 'D': '$65 \\mathrm{~cm}$', 'E': '$75 \\mathrm{~cm}$'}, 'source_key': 'test:381', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid106.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid106.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid106', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid106.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid106().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
