"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid237:

    def __init__(self):
        self.__dict__.update({'id': 'Solid237', 'source_dataset': 'MathVision', 'question': 'The faces of a cube are painted in six different colors: red (R), white (W), green (G), brown (B), aqua (A), and purple (P). Three views of the cube are shown below. What is the color of the face opposite the aqua face?\nChoices:\nA:$\\text{red}$\nB:$\\text{white}$\nC:$\\text{green}$\nD:$\\text{brown}$\nE:$\\text{purple}\n$', 'answer': 'A', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$\\text{red}$', 'B': '$\\text{white}$', 'C': '$\\text{green}$', 'D': '$\\text{brown}$', 'E': '$\\text{purple}\n$'}, 'source_key': 'test:2760', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid237.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid237.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid237', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid237.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid237().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
