"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid220:

    def __init__(self):
        self.__dict__.update({'id': 'Solid220', 'source_dataset': 'MathVision', 'question': 'A piece of paper containing six joined squares labeled as shown in the diagram is folded along the edges of the squares to form a cube.  The label of the face opposite the face labeled $ \\text{X}$ is:\nChoices:\nA:$\\text{Z}$\nB:$\\text{U}$\nC:$\\text{V}$\nD:$\\text{W}$\nE:$\\text{Y}$', 'answer': 'E', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$\\text{Z}$', 'B': '$\\text{U}$', 'C': '$\\text{V}$', 'D': '$\\text{W}$', 'E': '$\\text{Y}$'}, 'source_key': 'test:2507', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid220.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid220.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid220', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid220.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid220().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
