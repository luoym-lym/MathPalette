"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid97:

    def __init__(self):
        self.__dict__.update({'id': 'Solid97', 'source_dataset': 'MathVision', 'question': 'On a standard die the sum of the numbers on opposite faces is always 7. Two identical standard dice are shown in the figure. How many dots could there be on the non-visible right-hand face (marked with "?")?\nChoices:\nA:only 5\nB:only 2\nC:either 2 or 5\nD:either 1, 2, 3 or 5\nE:either 2,3 or 5', 'answer': 'A', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': 'only 5', 'B': 'only 2', 'C': 'either 2 or 5', 'D': 'either 1, 2, 3 or 5', 'E': 'either 2,3 or 5'}, 'source_key': 'test:278', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid97.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid97.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid97', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid97.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid97().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
