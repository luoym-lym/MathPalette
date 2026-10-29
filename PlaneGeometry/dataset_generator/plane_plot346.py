"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane346:

    def __init__(self):
        self.__dict__.update({'id': 'Plane346', 'source_dataset': 'MathVision', 'question': 'A flag contains the dove-shaped design shown on a $4 \\times 6$ grid. The area of the design is $192 \\mathrm{~cm}^{2}$, and its perimeter consists of straight lines and circular arcs. What are the dimensions of the flag?\nChoices:\nA:$6 \\mathrm{~cm} \\times 4 \\mathrm{~cm}$\nB:$12 \\mathrm{~cm} \\times 8 \\mathrm{~cm}$\nC:$20 \\mathrm{~cm} \\times 12 \\mathrm{~cm}$\nD:$24 \\mathrm{~cm} \\times 16 \\mathrm{~cm}$\nE:$30 \\mathrm{~cm} \\times 20 \\mathrm{~cm}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$6 \\mathrm{~cm} \\times 4 \\mathrm{~cm}$', 'B': '$12 \\mathrm{~cm} \\times 8 \\mathrm{~cm}$', 'C': '$20 \\mathrm{~cm} \\times 12 \\mathrm{~cm}$', 'D': '$24 \\mathrm{~cm} \\times 16 \\mathrm{~cm}$', 'E': '$30 \\mathrm{~cm} \\times 20 \\mathrm{~cm}$'}, 'source_key': 'test:1173', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane346.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane346.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane346', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane346.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane346().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
