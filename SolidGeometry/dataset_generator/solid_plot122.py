"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid122:

    def __init__(self):
        self.__dict__.update({'id': 'Solid122', 'source_dataset': 'MathVision', 'question': 'A pyramid is built from cubes, each with side length $10 \\mathrm{~cm}$. What is the length of the line drawn across the pyramid?\nChoices:\nA:$30 \\mathrm{~cm}$\nB:$60 \\mathrm{~cm}$\nC:$70 \\mathrm{~cm}$\nD:$80 \\mathrm{~cm}$\nE:$90 \\mathrm{~cm}$', 'answer': 'E', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$30 \\mathrm{~cm}$', 'B': '$60 \\mathrm{~cm}$', 'C': '$70 \\mathrm{~cm}$', 'D': '$80 \\mathrm{~cm}$', 'E': '$90 \\mathrm{~cm}$'}, 'source_key': 'test:674', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid122.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid122.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid122', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid122.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid122().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
