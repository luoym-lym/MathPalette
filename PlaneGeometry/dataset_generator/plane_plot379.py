"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane379:

    def __init__(self):
        self.__dict__.update({'id': 'Plane379', 'source_dataset': 'MathVision', 'question': 'A dark disc with two holes is placed on the dial of a watch as shown in the diagram. The dark disc is now rotated so that the number 10 can be seen through one of the two holes. Which of the numbers could one see through the other hole now?\nChoices:\nA:2 and 6\nB:3 and 7\nC:3 and 6\nD:1 and 9\nE:2 and 7', 'answer': 'A', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '2 and 6', 'B': '3 and 7', 'C': '3 and 6', 'D': '1 and 9', 'E': '2 and 7'}, 'source_key': 'test:1483', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane379.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane379.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane379', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane379.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane379().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
