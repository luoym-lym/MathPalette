"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane392:

    def __init__(self):
        self.__dict__.update({'id': 'Plane392', 'source_dataset': 'MathVision', 'question': 'The heart and the arrow are in the positions shown in the figure. At the same time the heart and the arrow start moving. The arrow moves three places clockwise and then stops and the heart moves four places anticlockwise and then stops. They repeat the same routine over and over again. After how many routines will the heart and the arrow land in the same place as each other for the first time?\nChoices:\nA:7\nB:8\nC:9\nD:10\nE:It will never happen', 'answer': 'E', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '7', 'B': '8', 'C': '9', 'D': '10', 'E': 'It will never happen'}, 'source_key': 'test:1612', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane392.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane392.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane392', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane392.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane392().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
