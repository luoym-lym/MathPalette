"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane408:

    def __init__(self):
        self.__dict__.update({'id': 'Plane408', 'source_dataset': 'MathVision', 'question': 'Four ribbons each have width $10 \\mathrm{~cm}$. Each ribbon is $25 \\mathrm{~cm}$ longer than the next smallest ribbon. The ribbons are then arranged to form two different shapes as shown in the diagram. How much longer is the perimeter of the second shape than the perimeter of the first shape?\nChoices:\nA:$75 \\mathrm{~cm}$\nB:$50 \\mathrm{~cm}$\nC:$25 \\mathrm{~cm}$\nD:$20 \\mathrm{~cm}$\nE:$0 \\mathrm{~cm}$', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$75 \\mathrm{~cm}$', 'B': '$50 \\mathrm{~cm}$', 'C': '$25 \\mathrm{~cm}$', 'D': '$20 \\mathrm{~cm}$', 'E': '$0 \\mathrm{~cm}$'}, 'source_key': 'test:1744', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane408.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane408.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane408', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane408.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane408().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
