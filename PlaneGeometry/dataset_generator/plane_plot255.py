"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane255:

    def __init__(self):
        self.__dict__.update({'id': 'Plane255', 'source_dataset': 'MathVision', 'question': 'A parallelogram is divided in two parts $P_{1}$ and $P_{2}$, as shown in the picture. Which sentence is always true?\nChoices:\nA:$P_{2}$ has a longer perimeter than $P_{1}$\nB:$P_{2}$ has a smaller perimeter than $P_{1}$\nC:$P_{2}$ has a smaller area than $P_{1}$\nD:$P_{1}$ and $P_{2}$ have the same perimeter\nE:$P_{1}$ and $P_{2}$ have the same area', 'answer': 'D', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$P_{2}$ has a longer perimeter than $P_{1}$', 'B': '$P_{2}$ has a smaller perimeter than $P_{1}$', 'C': '$P_{2}$ has a smaller area than $P_{1}$', 'D': '$P_{1}$ and $P_{2}$ have the same perimeter', 'E': '$P_{1}$ and $P_{2}$ have the same area'}, 'source_key': 'test:749', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane255.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane255.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane255', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane255.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane255().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
