"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane186:

    def __init__(self):
        self.__dict__.update({'id': 'Plane186', 'source_dataset': 'MathVision', 'question': 'A rectangular piece of paper $A B C D$ is $5 \\mathrm{~cm}$ wide and $50 \\mathrm{~cm}$ long. It is white on one side and grey on the other. The strip is first folded as shown so that vertex $B$ coincides with $M$, the midpoint of edge $C D$. It is then folded so that vertex $D$ coincides with $N$, the midpoint of edge $A B$. What is the area of the visible white part in the diagram?\nChoices:\nA:$50 \\mathrm{~cm}^{2}$\nB:$60 \\mathrm{~cm}^{2}$\nC:$62.5 \\mathrm{~cm}^{2}$\nD:$100 \\mathrm{~cm}^{2}$\nE:$125 \\mathrm{~cm}^{2}$', 'answer': 'B', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$50 \\mathrm{~cm}^{2}$', 'B': '$60 \\mathrm{~cm}^{2}$', 'C': '$62.5 \\mathrm{~cm}^{2}$', 'D': '$100 \\mathrm{~cm}^{2}$', 'E': '$125 \\mathrm{~cm}^{2}$'}, 'source_key': 'test:292', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane186.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane186.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane186', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane186.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane186().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
