"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane425:

    def __init__(self):
        self.__dict__.update({'id': 'Plane425', 'source_dataset': 'MathVision', 'question': 'One of the line segments shown on the grid is the image produced by a rotation of the other line segment. Which of the points $T, U, V$, $W$ could be the centre of such a rotation?\nChoices:\nA:only $T$\nB:only $U$\nC:either of $U$ and $W$\nD:any of $U, V$ and $W$\nE:any of $T, U, V$ and $W$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': 'only $T$', 'B': 'only $U$', 'C': 'either of $U$ and $W$', 'D': 'any of $U, V$ and $W$', 'E': 'any of $T, U, V$ and $W$'}, 'source_key': 'test:1871', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane425.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane425.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane425', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane425.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane425().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
