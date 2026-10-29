"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid96:

    def __init__(self):
        self.__dict__.update({'id': 'Solid96', 'source_dataset': 'MathVision', 'question': 'The curved surfaces of two identical cylinders are cut open along the vertical dotted line, as shown and then stuck together to create the curved surface of one big cylinder. What can be said about the volume of the resulting cylinder compared to the volume of one of the small cylinders?\nChoices:\nA:It is 2-times as big.\nB:It is 3-times as big.\nC:It is $\\pi$-times as big.\nD:It is 4-times as big.\nE:It is 8-times as big.', 'answer': 'D', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': 'It is 2-times as big.', 'B': 'It is 3-times as big.', 'C': 'It is $\\pi$-times as big.', 'D': 'It is 4-times as big.', 'E': 'It is 8-times as big.'}, 'source_key': 'test:264', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid96.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid96.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid96', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid96.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid96().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
