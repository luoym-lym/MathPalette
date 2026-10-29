"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane439:

    def __init__(self):
        self.__dict__.update({'id': 'Plane439', 'source_dataset': 'MathVision', 'question': 'In the array of $13$ squares shown below, $8$ squares are colored red, and the remaining $5$ squares are colored blue. If one of all possible such colorings is chosen at random, the probability that the chosen colored array appears the same when rotated $90^{\\circ}$ around the central square is $\\frac{1}{n}$, where $n$ is a positive integer. Find $n$.', 'answer': '429', 'answer_type': 'number', 'subject': 'PlaneGeometry', 'source_key': 'test:2080', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane439.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane439.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane439', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane439.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane439().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
