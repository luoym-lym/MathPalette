"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane355:

    def __init__(self):
        self.__dict__.update({'id': 'Plane355', 'source_dataset': 'MathVision', 'question': 'A rectangular strip of paper of dimensions $4 \\mathrm{~cm} \\times 13 \\mathrm{~cm}$ is folded as shown in the diagram. 2 rectangles are formed with areas $P$ and $Q$ where $P=2 Q$. What is the value of $x$?\nChoices:\nA:$5 \\mathrm{~cm}$\nB:$5.5 \\mathrm{~cm}$\nC:$6 \\mathrm{~cm}$\nD:$6.5 \\mathrm{~cm}$\nE:$4 \\sqrt{2} \\mathrm{~cm}$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$5 \\mathrm{~cm}$', 'B': '$5.5 \\mathrm{~cm}$', 'C': '$6 \\mathrm{~cm}$', 'D': '$6.5 \\mathrm{~cm}$', 'E': '$4 \\sqrt{2} \\mathrm{~cm}$'}, 'source_key': 'test:1216', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane355.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane355.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane355', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane355.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane355().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
