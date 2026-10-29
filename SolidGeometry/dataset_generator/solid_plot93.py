"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent

class Solid93:

    def __init__(self):
        self.__dict__.update({'id': 'Solid93', 'source_dataset': 'MathVision', 'question': 'Let $a>b$. If the ellipse shown rotates about the $x$-axis an ellipsoid $E_{x}$ with volume $\\operatorname{Vol}\\left(E_{x}\\right)$ is obtained. If it rotates about the $y$-axis an ellipsoid $E_{y}$ with volume $\\operatorname{Vol}\\left(E_{y}\\right)$ is obtained. Which of the following statements is true?\nChoices:\nA:$\\mathrm{E}_{\\mathrm{x}}=\\mathrm{E}_{\\mathrm{y}}$ and $\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{x}}\\right)=\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{y}}\\right)$\nB:$\\mathrm{E}_{\\mathrm{x}}=\\mathrm{E}_{\\mathrm{y}}$ but $\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{x}}\\right) \\neq \\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{y}}\\right)$\nC:$\\mathrm{E}_{\\mathrm{x}} \\neq \\mathrm{E}_{\\mathrm{y}}$ and $\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{x}}\\right)>\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{y}}\\right)$\nD:$\\mathrm{E}_{\\mathrm{x}} \\neq \\mathrm{E}_{\\mathrm{y}}$ and $\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{x}}\\right)<\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{y}}\\right)$\nE:$\\mathrm{E}_{\\mathrm{x}} \\neq \\mathrm{E}_{\\mathrm{y}}$ but $\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{x}}\\right)=\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{y}}\\right)$', 'answer': 'C', 'answer_type': 'choice', 'subject': 'SolidGeometry', 'choices': {'A': '$\\mathrm{E}_{\\mathrm{x}}=\\mathrm{E}_{\\mathrm{y}}$ and $\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{x}}\\right)=\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{y}}\\right)$', 'B': '$\\mathrm{E}_{\\mathrm{x}}=\\mathrm{E}_{\\mathrm{y}}$ but $\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{x}}\\right) \\neq \\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{y}}\\right)$', 'C': '$\\mathrm{E}_{\\mathrm{x}} \\neq \\mathrm{E}_{\\mathrm{y}}$ and $\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{x}}\\right)>\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{y}}\\right)$', 'D': '$\\mathrm{E}_{\\mathrm{x}} \\neq \\mathrm{E}_{\\mathrm{y}}$ and $\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{x}}\\right)<\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{y}}\\right)$', 'E': '$\\mathrm{E}_{\\mathrm{x}} \\neq \\mathrm{E}_{\\mathrm{y}}$ but $\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{x}}\\right)=\\operatorname{Vol}\\left(\\mathrm{E}_{\\mathrm{y}}\\right)$'}, 'source_key': 'test:253', 'source_category': 'solid geometry', 'source_revision': '2837ddb3f13abaf6b3997c12d80753e5470bd46a'})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / 'scenes/Solid93.json'

    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))

    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / 'Solid93.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/runtime.py')
        runtime = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(runtime)
        return runtime.draw(HERE / 'mathvision_renderers/shared_e4e003f51742cf00/items/Solid93', HERE / 'mathvision_renderers/shared_e4e003f51742cf00/native', output, formal_scene=self.scene_path, original_image=HERE / '../originals/Solid93.jpg')

    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print(Solid93().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
