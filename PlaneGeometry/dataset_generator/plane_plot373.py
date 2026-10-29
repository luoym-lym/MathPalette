"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane373:

    def __init__(self):
        self.__dict__.update({'id': 'Plane373', 'source_dataset': 'MathVision', 'question': 'A circle with radius 1 rolls along a straight line from point $K$ to point $L$, as shown, with $K L=11 \\pi$. In which position is the circle when it has arrived in $L$?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E', 'answer': 'E', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}, 'source_key': 'test:1405', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane373.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane373.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane373', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane373.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane373().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
