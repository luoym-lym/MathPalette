"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane456:

    def __init__(self):
        self.__dict__.update({'id': 'Plane456', 'source_dataset': 'MathVision', 'question': 'Each of the three large squares shown below is the same size.  Segments that intersect the sides of the squares intersect at the midpoints of the sides.  How do the shaded areas of these squares compare?\n\nChoices:\nA:$\\text{The shaded areas in all three are equal.}$\nB:$\\text{Only the shaded areas of }I\\text{ and }II\\text{ are equal.}$\nC:$\\text{Only the shaded areas of }I\\text{ and }III\\text{ are equal.}$\nD:$\\text{Only the shaded areas of }II\\text{ and }III\\text{ are equal.}$\nE:$\\text{The shaded areas of }I, II\\text{ and }III\\text{ are all different.}$', 'answer': 'A', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$\\text{The shaded areas in all three are equal.}$', 'B': '$\\text{Only the shaded areas of }I\\text{ and }II\\text{ are equal.}$', 'C': '$\\text{Only the shaded areas of }I\\text{ and }III\\text{ are equal.}$', 'D': '$\\text{Only the shaded areas of }II\\text{ and }III\\text{ are equal.}$', 'E': '$\\text{The shaded areas of }I, II\\text{ and }III\\text{ are all different.}$'}, 'source_key': 'test:2572', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane456.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane456.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane456', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane456.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane456().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
