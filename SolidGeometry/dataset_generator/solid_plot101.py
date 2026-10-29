"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid101:

    def __init__(self):
        self.__dict__.update({'id': 'Solid101', 'source_dataset': 'MathVision', 'question': 'Each side of a die is marked with either 1,2 or 3 dots so that the probability of rolling a 1 is equal to $\\frac{1}{2}$, the probability of rolling a 2 is equal to $\\frac{1}{3}$ and the probability of rolling a 3 is equal to $\\frac{1}{6}$. Which of these pictures cannot be a picture of this particular die?\nChoices:\nA:A\nB:B\nC:C\nD:D\nE:E', 'answer': 'C', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}, 'source_key': 'test:327', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid101.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid101.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid101', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid101.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid101().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
