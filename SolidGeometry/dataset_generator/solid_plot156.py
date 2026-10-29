"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid156:

    def __init__(self):
        self.__dict__.update({'id': 'Solid156', 'source_dataset': 'MathVision', 'question': 'The cube shown is built from equally sized bricks. The shortest side of one brick is $4 \\mathrm{~cm}$ long. What are the dimensions of one brick in $\\mathrm{cm}$?\nChoices:\nA:$4 \\times 6 \\times 12$\nB:$4 \\times 6 \\times 16$\nC:$4 \\times 8 \\times 12$\nD:$4 \\times 8 \\times 16$\nE:$4 \\times 12 \\times 16$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$4 \\times 6 \\times 12$', 'B': '$4 \\times 6 \\times 16$', 'C': '$4 \\times 8 \\times 12$', 'D': '$4 \\times 8 \\times 16$', 'E': '$4 \\times 12 \\times 16$'}, 'source_key': 'test:1225', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid156.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid156.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid156', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid156.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid156().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
