"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid126:

    def __init__(self):
        self.__dict__.update({'id': 'Solid126', 'source_dataset': 'MathVision', 'question': 'A rectangular section was cut out of a rectangular block as shown in the diagram. Find the decrease percentage of the surface area.\nChoices:\nA:Less than $12.5 \\%$\nB:$12.5 \\%$\nC:More than $12.5 \\%$, but less than $25 \\%$\nD:$25 \\%$\nE:More than $25 \\%$', 'answer': 'B', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': 'Less than $12.5 \\%$', 'B': '$12.5 \\%$', 'C': 'More than $12.5 \\%$, but less than $25 \\%$', 'D': '$25 \\%$', 'E': 'More than $25 \\%$'}, 'source_key': 'test:754', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid126.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid126.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid126', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid126.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid126().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
