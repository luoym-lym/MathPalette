"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane235:

    def __init__(self):
        self.__dict__.update({'id': 'Plane235', 'source_dataset': 'MathVision', 'question': 'Each arrow represents a move to a neighbouring square. Which path leads from the bee to the flower?\nChoices:\nA:$\\downarrow \\rightarrow \\rightarrow \\downarrow \\downarrow \\downarrow$\nB:$\\downarrow \\downarrow \\rightarrow \\downarrow \\downarrow \\rightarrow$\nC:$\\rightarrow \\downarrow \\rightarrow \\downarrow \\rightarrow \\rightarrow$\nD:$\\rightarrow \\rightarrow \\downarrow \\downarrow \\downarrow \\downarrow$\nE:$\\rightarrow \\downarrow \\rightarrow \\downarrow \\downarrow \\rightarrow$', 'answer': 'E', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$\\downarrow \\rightarrow \\rightarrow \\downarrow \\downarrow \\downarrow$', 'B': '$\\downarrow \\downarrow \\rightarrow \\downarrow \\downarrow \\rightarrow$', 'C': '$\\rightarrow \\downarrow \\rightarrow \\downarrow \\rightarrow \\rightarrow$', 'D': '$\\rightarrow \\rightarrow \\downarrow \\downarrow \\downarrow \\downarrow$', 'E': '$\\rightarrow \\downarrow \\rightarrow \\downarrow \\downarrow \\rightarrow$'}, 'source_key': 'test:660', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane235.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane235.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane235', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane235.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane235().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
