"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane237:

    def __init__(self):
        self.__dict__.update({'id': 'Plane237', 'source_dataset': 'MathVision', 'question': 'Five cars are labelled with the numbers 1 to 5 . They drive in the direction of the arrow.\nFirst the last car overtakes the two cars in front of it.\nThen the now second to last car overtakes the two in front of it.\nIn the end the car that is now in the middle overtakes the two in front of it.\nIn which order do the cars now drive?\nChoices:\nA:$1,2,3,4,5$\nB:$2,1,3,5,4$\nC:$2,1,5,3,4$\nD:$3,1,4,2,5$\nE:$4,1,2,5,3$', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$1,2,3,4,5$', 'B': '$2,1,3,5,4$', 'C': '$2,1,5,3,4$', 'D': '$3,1,4,2,5$', 'E': '$4,1,2,5,3$'}, 'source_key': 'test:666', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane237.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane237.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane237', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane237.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane237().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
