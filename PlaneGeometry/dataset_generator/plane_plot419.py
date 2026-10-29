"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Plane419:

    def __init__(self):
        self.__dict__.update({'id': 'Plane419', 'source_dataset': 'MathVision', 'question': 'A rectangular sheet of paper which measures $6 \\mathrm{~cm} \\times 12 \\mathrm{~cm}$ is folded along its diagonal (Diagram A). The shaded areas in Diagram B are then cut off and the paper is unfolded leaving the rhombus shown in Diagram C. What is the length of the side of the rhombus?\nChoices:\nA:$\\frac{7}{2} \\sqrt{5} \\mathrm{~cm}$\nB:$7.35 \\mathrm{~cm}$\nC:$7.5 \\mathrm{~cm}$\nD:$7.85 \\mathrm{~cm}$\nE:$8.1 \\mathrm{~cm}$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'PlaneGeometry', 'choices': {'A': '$\\frac{7}{2} \\sqrt{5} \\mathrm{~cm}$', 'B': '$7.35 \\mathrm{~cm}$', 'C': '$7.5 \\mathrm{~cm}$', 'D': '$7.85 \\mathrm{~cm}$', 'E': '$8.1 \\mathrm{~cm}$'}, 'source_key': 'test:1806', 'source_category': 'transformation geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Plane419.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Plane419.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Plane419', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Plane419.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Plane419().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
