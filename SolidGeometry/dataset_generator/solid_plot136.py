"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid136:

    def __init__(self):
        self.__dict__.update({'id': 'Solid136', 'source_dataset': 'MathVision', 'question': 'A sheet of paper is divided into nine equal squares. It is folded as shown, first horizontally and then vertically, until the colored square is on top of the layers. The numbers from 1 to 9 are to be written, one in each square, so that after folding they are in ascending order, starting with 1 at the top. Which numbers should be written in place of $a, b$ and $c$ on the unfolded sheet?\nChoices:\nA:$a=9, b=5, c=3$\nB:$a=4, b=6, c=8$\nC:$a=7, b=5, c=3$\nD:$a=3, b=5, c=7$\nE:$a=6, b=4, c=7$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$a=9, b=5, c=3$', 'B': '$a=4, b=6, c=8$', 'C': '$a=7, b=5, c=3$', 'D': '$a=3, b=5, c=7$', 'E': '$a=6, b=4, c=7$'}, 'source_key': 'test:936', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid136.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid136.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid136', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid136.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid136().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
