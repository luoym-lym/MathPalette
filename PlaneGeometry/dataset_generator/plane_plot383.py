"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane383:

    def __init__(self):
        self.__dict__.update({'id': 'Plane383', 'source_dataset': 'MathVision', 'question': 'The robot in the diagram has been programmed to move in a straight line and, if it meets a wall (shown by bold lines), to turn right by $90^{\\circ}$ and then to continue straight on. If it cannot go straight or turn right it will stop. What will happen to this robot?\nChoices:\nA:It will stop at $\\mathrm{P} 2$.\nB:It will stop at P1.\nC:It will stop at $\\mathrm{T} 1$.\nD:It will stop at $S 1$.\nE:It will never stop.', 'answer': 'E', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': 'It will stop at $\\mathrm{P} 2$.', 'B': 'It will stop at P1.', 'C': 'It will stop at $\\mathrm{T} 1$.', 'D': 'It will stop at $S 1$.', 'E': 'It will never stop.'}, 'source_key': 'test:1541', 'source_category': 'combinatorial geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane383.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane383.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane383', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane383.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane383().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
