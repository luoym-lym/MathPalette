"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid103:

    def __init__(self):
        self.__dict__.update({'id': 'Solid103', 'source_dataset': 'MathVision', 'question': 'Two rectangular blocks and a cube are joined to form a larger rectangular block with volume $280 \\mathrm{~cm}^{3}$. The dark gray cube in the picture has volume $125 \\mathrm{~cm}^{3}$, and the smaller rectangular block has volume $75 \\mathrm{~cm}^{3}$. What is the area of the face marked with the question mark?\nChoices:\nA:$16 \\mathrm{~cm}^{2}$\nB:$18 \\mathrm{~cm}^{2}$\nC:$20 \\mathrm{~cm}^{2}$\nD:$24 \\mathrm{~cm}^{2}$\nE:$56 \\mathrm{~cm}^{2}$', 'answer': 'A', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$16 \\mathrm{~cm}^{2}$', 'B': '$18 \\mathrm{~cm}^{2}$', 'C': '$20 \\mathrm{~cm}^{2}$', 'D': '$24 \\mathrm{~cm}^{2}$', 'E': '$56 \\mathrm{~cm}^{2}$'}, 'source_key': 'test:344', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid103.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid103.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid103', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid103.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid103().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
