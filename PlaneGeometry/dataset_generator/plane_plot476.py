"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane476:

    def __init__(self):
        self.__dict__.update({'id': 'Plane476', 'source_dataset': 'MathVision', 'question': 'The diagram shows an octagon consisting of $10$ unit squares. The portion below $\\overline{PQ}$ is a unit square and a triangle with base $5$. If $\\overline{PQ}$ bisects the area of the octagon, what is the ratio $\\frac{XQ}{QY}$?\n\nChoices:\nA:$\\frac{2}{5}$\nB:$\\frac{1}{2}$\nC:$\\frac{3}{5}$\nD:$\\frac{2}{3}$\nE:$\\frac{3}{4}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$\\frac{2}{5}$', 'B': '$\\frac{1}{2}$', 'C': '$\\frac{3}{5}$', 'D': '$\\frac{2}{3}$', 'E': '$\\frac{3}{4}$'}, 'source_key': 'test:2706', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane476.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane476.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane476', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane476.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane476().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
