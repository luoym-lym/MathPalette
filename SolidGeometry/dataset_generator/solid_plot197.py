"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid197:

    def __init__(self):
        self.__dict__.update({'id': 'Solid197', 'source_dataset': 'MathVision', 'question': 'A cube has sides of length $10 \\mathrm{~cm}$. Identical square stickers are placed: one sticker in the centre of each face of the cube, and one across each edge, so that the stickers meet at their corners, as shown in the diagram. What is the total area in $\\mathrm{cm}^{2}$ of the stickers used?', 'answer': '225', 'answer_type': 'number', 'subject': 'SolidGeometry', 'source_key': 'test:1877', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid197.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid197.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid197', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid197.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid197().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
