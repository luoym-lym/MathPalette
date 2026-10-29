"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane366:

    def __init__(self):
        self.__dict__.update({'id': 'Plane366', 'source_dataset': 'MathVision', 'question': 'The two bold lines on the right are rotations of each other. Which of the given points could be the centre of this rotation?\nChoices:\nA:only $X$\nB:$X$ and $Z$\nC:$X$ and $T$\nD:only $T$\nE:$X, Y, Z$ and $T$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': 'only $X$', 'B': '$X$ and $Z$', 'C': '$X$ and $T$', 'D': 'only $T$', 'E': '$X, Y, Z$ and $T$'}, 'source_key': 'test:1345', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane366.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane366.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane366', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane366.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane366().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
