"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane271:

    def __init__(self):
        self.__dict__.update({'id': 'Plane271', 'source_dataset': 'MathVision', 'question': 'Both the figures on the right were made out of the same 5 pieces. The rectangle has dimensions $5 \\mathrm{~cm} \\times 10 \\mathrm{~cm}$. The other pieces are quarter circles with 2 different sized radii. What is the difference between the perimeters of the two figures?\nChoices:\nA:$2.5 \\mathrm{~cm}$\nB:$5 \\mathrm{~cm}$\nC:$10 \\mathrm{~cm}$\nD:$15 \\mathrm{~cm}$\nE:$20 \\mathrm{~cm}$', 'answer': 'E', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$2.5 \\mathrm{~cm}$', 'B': '$5 \\mathrm{~cm}$', 'C': '$10 \\mathrm{~cm}$', 'D': '$15 \\mathrm{~cm}$', 'E': '$20 \\mathrm{~cm}$'}, 'source_key': 'test:814', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane271.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane271.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane271', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane271.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane271().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
