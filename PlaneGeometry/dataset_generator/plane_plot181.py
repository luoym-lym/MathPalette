"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane181:

    def __init__(self):
        self.__dict__.update({'id': 'Plane181', 'source_dataset': 'MathVision', 'question': "A rectangular piece of paper $A B C D$ with the measurements $4 \\mathrm{~cm} \\times 16 \\mathrm{~cm}$ is folded along the line $\\mathrm{MN}$ so that point $C$ coincides with point $A$ as shown. How big is the area of the quadrilateral ANMD'?\nChoices:\nA:$28 \\mathrm{~cm}^{2}$\nB:$30 \\mathrm{~cm}^{2}$\nC:$32 \\mathrm{~cm}^{2}$\nD:$48 \\mathrm{~cm}^{2}$\nE:$56 \\mathrm{~cm}^{2}$", 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$28 \\mathrm{~cm}^{2}$', 'B': '$30 \\mathrm{~cm}^{2}$', 'C': '$32 \\mathrm{~cm}^{2}$', 'D': '$48 \\mathrm{~cm}^{2}$', 'E': '$56 \\mathrm{~cm}^{2}$'}, 'source_key': 'test:247', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane181.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane181.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane181', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane181.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane181().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
