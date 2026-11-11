"""Frozen Author Designed original. Importing has no rendering side effects."""
from pathlib import Path
import json, sys
import numpy as np
_HELPERS=Path(__file__).resolve().parents[1]
if str(_HELPERS) not in sys.path: sys.path.insert(0,str(_HELPERS))
from common_renderer import open_canvas, plot_curve, scatter_points, fill_polygon, label, finalize
_SCENE_PATH=_HELPERS/'scenes'/'Ana564.json'
class Ana564:
    def __init__(self):
        self.id='Ana564'
        self.source_dataset='Author Designed'
        self.question='Read the query point Q and sites A, B, C from the unit grid. Define d_1((x,y),(u,v))=|x-u|+|y-v|. Which site uniquely minimizes d_1(Q,site)? Answer with its letter.'
        self.query=self.question
        self.answer='B'
        self.answer_type='text'
        self.subject='Analytics'
        self.level=None
        self.scene_path=str(_SCENE_PATH)
        self.runtime_dependencies=['dataset_generator/common_renderer.py','dataset_generator/protocol.json','dataset_generator/scenes/Ana564.json']
    def get_scene(self):
        return json.loads(_SCENE_PATH.read_text(encoding='utf-8'))
    def draw(self,num=0,output_path=None):
        if output_path is None and isinstance(num,(str,Path)): output_path=num
        scene=self.get_scene()
        fig,ax=open_canvas(**scene['axes'])
        for obj in scene['objects']:
            if obj['type']=='curve':
                a=np.asarray(obj['points']); plot_curve(ax,a[:,0],a[:,1])
            elif obj['type']=='points':
                a=np.asarray(obj['points']); scatter_points(ax,a[:,0],a[:,1],open_marker=False)
            elif obj['type']=='polygon_region': fill_polygon(ax,obj['x'],obj['y'])
            else: raise ValueError(obj['type'])
        for v in scene['labels']: label(ax,v['x'],v['y'],v['text'],ha=v['ha'],va=v['va'])
        target=Path(output_path) if output_path else _HELPERS.parents[1]/'.runtime'/'reproduced'/'Analytics'/(self.id+'.png')
        return finalize(fig,target)
def draw(num=0,output_path=None): return Ana564().draw(num=num,output_path=output_path)
if __name__=='__main__': print(draw(output_path=sys.argv[1] if len(sys.argv)>1 else None))
