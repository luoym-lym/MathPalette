"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane471:

    def __init__(self):
        self.__dict__.update({'id': 'Plane471', 'source_dataset': 'MathVision', 'question': 'Tiles I, II, III and IV are translated so one tile coincides with each of the rectangles $A, B, C$ and $D$. In the final arrangement, the two numbers on any side common to two adjacent tiles must be the same. Which of the tiles is translated to Rectangle $C$?\n\nChoices:\nA:$I$\nB:$II$\nC:$III$\nD:$IV$\nE:$\\text{ cannot be determined}$', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$I$', 'B': '$II$', 'C': '$III$', 'D': '$IV$', 'E': '$\\text{ cannot be determined}$'}, 'source_key': 'test:2680', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane471.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane471.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane471', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane471.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane471().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
