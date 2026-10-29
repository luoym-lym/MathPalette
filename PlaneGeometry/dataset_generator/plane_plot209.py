"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane209:

    def __init__(self):
        self.__dict__.update({'id': 'Plane209', 'source_dataset': 'MathVision', 'question': 'Which of the houses shown use exactly the same building blocks?\nChoices:\nA:House 1 and 4\nB:House 3 and 4\nC:House 1, 4 and 5\nD:House 3, 4 and 5\nE:House 1, 2, 4 and 5', 'answer': 'A', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': 'House 1 and 4', 'B': 'House 3 and 4', 'C': 'House 1, 4 and 5', 'D': 'House 3, 4 and 5', 'E': 'House 1, 2, 4 and 5'}, 'source_key': 'test:511', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane209.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane209.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane209', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane209.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane209().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
