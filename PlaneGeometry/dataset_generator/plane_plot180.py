"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane180:

    def __init__(self):
        self.__dict__.update({'id': 'Plane180', 'source_dataset': 'MathVision', 'question': 'A strip of paper is folded three times as shown. Determine $\\beta$ if $\\alpha=70^{\\circ}$.\nChoices:\nA:$140^{\\circ}$\nB:$130^{\\circ}$\nC:$120^{\\circ}$\nD:$110^{\\circ}$\nE:$100^{\\circ}$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$140^{\\circ}$', 'B': '$130^{\\circ}$', 'C': '$120^{\\circ}$', 'D': '$110^{\\circ}$', 'E': '$100^{\\circ}$'}, 'source_key': 'test:231', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane180.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane180.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane180', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane180.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane180().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
