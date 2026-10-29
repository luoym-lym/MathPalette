"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane338:

    def __init__(self):
        self.__dict__.update({'id': 'Plane338', 'source_dataset': 'MathVision', 'question': 'On a sheet of paper a grid is drawn such that each of the squares has sides $2 \\mathrm{~cm}$ long. How big is the area of the grey shaded quadrilateral $A B C D$?\nChoices:\nA:$96 \\mathrm{~cm}^{2}$\nB:$84 \\mathrm{~cm}^{2}$\nC:$76 \\mathrm{~cm}^{2}$\nD:$88 \\mathrm{~cm}^{2}$\nE:$104 \\mathrm{~cm}^{2}$', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$96 \\mathrm{~cm}^{2}$', 'B': '$84 \\mathrm{~cm}^{2}$', 'C': '$76 \\mathrm{~cm}^{2}$', 'D': '$88 \\mathrm{~cm}^{2}$', 'E': '$104 \\mathrm{~cm}^{2}$'}, 'source_key': 'test:1102', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane338.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane338.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane338', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane338.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane338().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
