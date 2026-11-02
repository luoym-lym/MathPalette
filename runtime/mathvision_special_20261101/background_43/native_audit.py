import env
from env import OWN
from prepare import read,dump,sha
import json,io,hashlib
from collections import defaultdict,Counter
import numpy as np
from PIL import Image

def snapshot(sc):
    from matplotlib.patches import Patch
    filled=[]
    for p in sc.ax.patches:
        color=np.asarray(p.get_facecolor()).tolist()
        if p.get_fill() and color[3]>0:
            filled.append({'vertices':p.get_path().vertices.tolist(),'codes':None if p.get_path().codes is None else p.get_path().codes.tolist(),'transform':p.get_transform().get_matrix().tolist(),'facecolor':color,'alpha':p.get_alpha()})
    texts=[{'text':t.get_text(),'position':list(t.get_position()),'transform':t.get_transform().get_matrix().tolist(),'font_size':t.get_fontsize(),'color':t.get_color(),'rotation':t.get_rotation()} for t in sc.ax.texts]
    return {'fills':filled,'texts':texts,'xlim':list(sc.ax.get_xlim()),'ylim':list(sc.ax.get_ylim()),'aspect':sc.ax.get_aspect(),'size':list(sc.fig.canvas.get_width_height())}

def main():
    adapter,config=env.renderer()
    from mathvision_plugins import PluginRenderer
    from partial_style import object_paths,portion
    from dataset_tools import mathvision_workbench as bridge
    for d in OWN.glob('Plane*/r43_*/design.json'):
        root=d.parent;q=read(d)['question_id'];plugin=read(root/'plugin.json')
        ctx=adapter.inspect_question(q);pr=PluginRenderer(config,adapter,{q:ctx})
        snapshots=[]
        original_png=bridge.png_bytes
        def observing_png(sc):
            snapshots.append(snapshot(sc))
            return original_png(sc)
        bridge.png_bytes=observing_png
        try:_,data,_=pr.render(plugin,frozen=True)
        finally:bridge.png_bytes=original_png
        assert data==(root/'candidate.png').read_bytes()
        assert len(snapshots)==2,len(snapshots)
        assert snapshots[0]==snapshots[1],q
        dump(root/'native_state_before.json',snapshots[0]);dump(root/'native_state_after.json',snapshots[1])
        sc=adapter.scene(q)
        try:
            region=np.zeros((768,768),dtype=bool);marks=[]
            for i,a in enumerate(plugin['params']['actions']):
                pieces=[]
                if a['type']=='add_point':
                    px=sc.ax.transData.transform(a['xy']);xy=np.array([px[0],768-px[1]])
                    radius=(a['size_pt2']**.5+a['edge_linewidth_pt'])*100/72/2+3
                    lo=np.floor(xy-radius).astype(int);hi=np.ceil(xy+radius).astype(int)
                    pieces=[(lo,hi)]
                else:
                    paths=object_paths(sc,a['target'])
                    for p in paths:
                        iv=a.get('interval');n=len(p['segments'])
                        for j,s in enumerate(p['segments']):
                            lo=max(0.,iv['start']*n-j) if iv else 0
                            hi=min(1.,iv['end']*n-j) if iv else 1
                            if hi<=lo:continue
                            control=portion(s['control'],lo,hi)
                            pix=sc.ax.transData.transform(control);pix[:,1]=768-pix[:,1]
                            low=np.floor(pix.min(axis=0)-5).astype(int);high=np.ceil(pix.max(axis=0)+5).astype(int)
                            pieces.append((low,high))
                bbox=[];mask=np.zeros((768,768),dtype=bool)
                for lo,hi in pieces:
                    lo=np.maximum(lo,0);hi=np.minimum(hi,768)
                    mask[lo[1]:hi[1]+1,lo[0]:hi[0]+1]=True
                    bbox.append([int(lo[0]),int(lo[1]),int(hi[0]),int(hi[1])])
                region|=mask
                array=np.asarray(Image.open(root/'candidate.png').convert('RGB'))
                palette=np.array(tuple(bytes.fromhex(a['color'][1:])))
                marks.append({'action_index':i,'data_action':a,'native_pixel_neighborhoods':bbox,'exact_color_pixels_in_own_neighborhood':int((np.all(array==palette,axis=2)&mask).sum()),'visible':bool((np.all(array==palette,axis=2)&mask).any())})
            before=np.asarray(Image.open(root/'noop.png').convert('RGBA'));after=np.asarray(Image.open(root/'candidate.png').convert('RGBA'))
            delta=np.abs(after.astype(int)-before.astype(int));changed=np.any(delta,axis=2);outside=changed&~region
            maxoutside=int(delta[outside].max()) if outside.any() else 0
            centercheck=[]
            if q=='Plane407':
                for xy in [[2.5714285714285716,1.3],[11.571428571428573,1.3],[19.285714285714285,1.3],[28.28571428571429,1.3]]:
                    p=sc.ax.transData.transform(xy);x,y=round(p[0]),round(768-p[1]);centercheck.append({'xy':xy,'pixel':[x,y],'before_RGBA':before[y,x].tolist(),'after_RGBA':after[y,x].tolist(),'still_black':bool((after[y,x,:3]==0).all())})
            route=[]
            if q=='Plane412':
                for obj in ctx['objects']:
                    if obj['geometry'].get('role')=='semantic_bold_route':
                        for art in sc.artists[obj['id']]:
                            route.append({'object':obj['id'],'captured_color':art.get_color(),'actual_captured_linewidth_pt':art.get_linewidth(),'frozen_semantic_field':obj['geometry'].get('semantic_linewidth_pt')})
            audit={'question_id':q,'pure_observer_capture_of_approved_PluginRenderer':True,'render_drawing_operations_modified':False,'exact_replayed_png_equal_frozen':True,'all_original_fill_paths_transforms_colors_unchanged':True,'all_original_text_positions_fonts_colors_unchanged':True,'frozen_view_aspect_canvas_unchanged':True,'per_marker':marks,'changed_pixels_outside_actual_marker_neighborhoods':int(outside.sum()),'maximum_channel_delta_outside':maxoutside,'outside_is_only_grayscale':bool(np.all(after[outside,:3].max(axis=1)==after[outside,:3].min(axis=1))) if outside.any() else True,'center_dot_readability':centercheck,'route_actual_style':route,'precision_note':'Partial-style path reserialization can alter antialiasing of otherwise unchanged contour pixels; exact outside deltas are recorded, not silently called pixel preservation.'}
            assert all(m['visible'] for m in marks),q
            audit['original_center_pixels_preserved']=all(c['still_black'] for c in centercheck)
            audit['requires_pre_call_hold']=not audit['original_center_pixels_preserved']
            dump(root/'native_render_audit.json',audit)
            print(json.dumps({k:audit[k] for k in ['question_id','changed_pixels_outside_actual_marker_neighborhoods','maximum_channel_delta_outside','center_dot_readability','route_actual_style']},ensure_ascii=False),flush=True)
        finally:sc.close()

if __name__=='__main__':main()
