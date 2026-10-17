"""Redraw the frozen user-approved original Solid76."""
from pathlib import Path
import sys
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'dataset_tools/geometry_dataset.py').is_file())
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from dataset_tools.geometry_dataset import read_json,renderer_for,draw_question

class Solid76:
    def __init__(self):
        self.id = 'Solid76'
        self.source_dataset = 'Author designed'
        self.source_key = 'solid80:net-edge-endpoint-identification'
        self.question = 'The figure shows a net of a cube. After folding, which of the following edges has no endpoint in common with edge AB?\nChoices:\nA: Edge CD\nB: Edge CE\nC: Edge DF\nD: None of these three edges'
        self.answer = 'C'
        self.answer_type = 'choice'
        self.choices = {'A': 'Edge CD', 'B': 'Edge CE', 'C': 'Edge DF', 'D': 'None of these three edges'}
        self.query = 'The figure shows a net of a cube. After folding, which of the following edges has no endpoint in common with edge AB?\nChoices:\nA: Edge CD\nB: Edge CE\nC: Edge DF\nD: None of these three edges'
        self.subject = 'SolidGeometry'
        self.level = None
        self.scene_path=Path(__file__).parent/'scenes/Solid76.json'
    def get_scene(self): return read_json(self.scene_path)
    def build_scene(self):
        fig,_=renderer_for('SolidGeometry').render_scene(self.get_scene())
        return fig,fig.axes[0]
    def draw(self,num=0,output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        return draw_question('SolidGeometry',self.scene_path,output_path)
    def redraw(self,output_path=None): return self.draw(output_path=output_path)

if __name__=='__main__': print(Solid76().draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
