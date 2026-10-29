"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid212:

    def __init__(self):
        self.__dict__.update({'id': 'Solid212', 'source_dataset': 'MathVision', 'question': 'A white cylindrical silo has a diameter of 30 feet and a height of 80 feet. A red stripe with a horizontal width of 3 feet is painted on the silo, as shown, making two complete revolutions around it. What is the area of the stripe in square feet?\n\nChoices:\nA:$120$\nB:$180$\nC:$240$\nD:$360$\nE:$480$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$120$', 'B': '$180$', 'C': '$240$', 'D': '$360$', 'E': '$480$'}, 'source_key': 'test:2134', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid212.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid212.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid212', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid212.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid212().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
