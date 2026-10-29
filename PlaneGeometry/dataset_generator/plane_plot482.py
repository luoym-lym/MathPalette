"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane482:

    def __init__(self):
        self.__dict__.update({'id': 'Plane482', 'source_dataset': 'MathVision', 'question': 'Each square in a $3 \\times 3$ grid is randomly filled with one of the $4$ gray-and-white tiles shown below on the right.\nWhat is the probability that the tiling will contain a large gray diamond in one of the smaller $2\\times 2$ grids? Below is an example of one such tiling.\nChoices:\nA:$\\frac{1}{1024}$\nB:$\\frac{1}{256}$\nC:$\\frac{1}{64}$\nD:$\\frac{1}{16}$\nE:$\\frac{1}{4}$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$\\frac{1}{1024}$', 'B': '$\\frac{1}{256}$', 'C': '$\\frac{1}{64}$', 'D': '$\\frac{1}{16}$', 'E': '$\\frac{1}{4}$'}, 'source_key': 'test:2792', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane482.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane482.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane482', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane482.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane482().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
