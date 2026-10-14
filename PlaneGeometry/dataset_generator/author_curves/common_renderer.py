"""Render frozen cubic paths, one editable object per intersection interval.

No fitting, sampling, equation evaluation, or writes on import. Intermediate
Bezier controls are geometry, never visible points or workbench snap targets.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch

ROOT = Path(__file__).resolve().parent


def validate_scene(scene):
    points = scene['points']
    objects = scene['objects']
    if len({o['id'] for o in objects}) != len(objects):
        raise ValueError('Duplicate curve segment ID')
    if any(np.asarray(p).shape != (2,) or not np.isfinite(p).all() for p in points.values()):
        raise ValueError('Invalid frozen point')
    for item in objects:
        if item['type'] != 'bezier_curve':
            raise ValueError('Unknown author curve object')
        vertices = np.asarray(item['vertices'], dtype=float)
        if vertices.ndim != 2 or vertices.shape[1] != 2 or len(vertices) < 4 or (len(vertices)-1) % 3 or not np.isfinite(vertices).all():
            raise ValueError('Invalid cubic path')
        if len(item['points']) != 2 or any(p not in points for p in item['points']):
            raise ValueError('Unknown curve boundary')
        if not np.allclose(vertices[[0,-1]], [points[p] for p in item['points']], atol=1e-9, rtol=0):
            raise ValueError('Curve boundary differs from frozen point')
        # Every cubic and every join has a nonzero, consistently oriented tangent.
        for i in range(0,len(vertices)-1,3):
            if min(np.linalg.norm(vertices[i+1]-vertices[i]),np.linalg.norm(vertices[i+3]-vertices[i+2])) < 1e-14:
                raise ValueError('Degenerate endpoint tangent')
        for i in range(3,len(vertices)-1,3):
            u,v=vertices[i]-vertices[i-1],vertices[i+1]-vertices[i]
            if np.dot(u,v) <= 0 or abs(u[0]*v[1]-u[1]*v[0]) > 1e-8*np.linalg.norm(u)*np.linalg.norm(v):
                raise ValueError('Nonsmooth cubic join')
    by_id={o['id']:o for o in objects}
    for condition in scene['constraints']:
        if condition['type'] != 'curve_chain':
            raise ValueError('Unknown author curve constraint')
        chain=[by_id[i] for i in condition['objects']]
        if chain[0]['points'][0] != condition['endpoints'][0] or chain[-1]['points'][1] != condition['endpoints'][1]:
            raise ValueError('Curve connectivity changed')
        for first,second in zip(chain,chain[1:]):
            if first['points'][1] != second['points'][0]:
                raise ValueError('Disconnected curve chain')
            a,b=np.asarray(first['vertices']),np.asarray(second['vertices'])
            u,v=a[-1]-a[-2],b[1]-b[0]
            if np.dot(u,v)<=0 or abs(u[0]*v[1]-u[1]*v[0])>1e-7*np.linalg.norm(u)*np.linalg.norm(v):
                raise ValueError('Nonsmooth intersection continuation')
    if sorted(i for c in scene['constraints'] for i in c['objects']) != sorted(by_id):
        raise ValueError('Curve chains must partition the objects')
    for label in scene['labels']:
        if label['type'] != 'vertex' or label['point'] not in points:
            raise ValueError('Invalid endpoint label')
    return True


def render_scene(scene):
    validate_scene(scene)
    protocol=json.loads((ROOT/'protocol.json').read_text(encoding='utf-8'))
    with matplotlib.rc_context({'font.family':'DejaVu Sans','svg.fonttype':'path','svg.hashsalt':'author-curves-v1'}):
        fig=plt.figure(figsize=protocol['figure']['figsize_in'],dpi=protocol['figure']['dpi'],facecolor='white')
        ax=fig.add_axes(protocol['figure']['axes_position'])
        ax.set(xlim=scene['view']['xlim'],ylim=scene['view']['ylim'],aspect='equal')
        ax.set_autoscale_on(False)
        ax.set_axis_off()
        for item in scene['objects']:
            vertices=item['vertices']
            codes=[MplPath.MOVETO]+[MplPath.CURVE4]*(len(vertices)-1)
            # A single patch per semantic interval, even for a long spiral.
            ax.add_patch(PathPatch(MplPath(vertices,codes),facecolor='none',edgecolor='#000000',
                                   linewidth=1,capstyle='butt',antialiased=True))
        for label in scene['labels']:
            ax.annotate(label['point'],scene['points'][label['point']],xytext=label['offset_pt'],
                        textcoords='offset points',ha=label['ha'],va=label['va'],fontsize=18,
                        fontstyle='italic',fontfamily='DejaVu Sans',color='black',annotation_clip=False)
    return fig,ax


def draw(scene_path,output_path):
    scene=json.loads(Path(scene_path).read_text(encoding='utf-8'))
    fig,_=render_scene(scene)
    output=Path(output_path)
    output.parent.mkdir(parents=True,exist_ok=True)
    try:
        with matplotlib.rc_context({'savefig.bbox':None,'svg.fonttype':'path','svg.hashsalt':'author-curves-v1'}):
            fig.savefig(output,dpi=100,facecolor='white',transparent=False,bbox_inches=None,pad_inches=0,
                        metadata={'Date':None} if output.suffix=='.svg' else {})
    finally:
        plt.close(fig)
    return output
