import task_env
from task_env import OWN
from prepare import read,write
from designs import now
from workbench_io import load_config
from mathvision_adapter import RendererAdapter
from partial_style import object_paths,portion,evaluate
import numpy as np,math
from PIL import Image

ad=RendererAdapter(load_config())
for f in OWN.glob('Plane*/r48_*/design.json'):
    d=f.parent;design=read(f);q=design['question_id'];plugin=read(d/'plugin.json');sc=ad.scene(q)
    pix=np.asarray(Image.open(d/'candidate.png').convert('RGB'))
    result=[]
    try:
        for i,a in enumerate(plugin['params']['actions']):
            exact=True;coordinates=[];midpoints=[]
            if a['type']=='set_object_style':
                paths=object_paths(sc,a['target']);iv=a['interval'];path=next(p for p in paths if p['id']==iv['path_id']);exact=path['sha256']==iv['path_sha256'];n=len(path['segments'])
                for j,seg in enumerate(path['segments']):
                    lo=max(0,iv['start']*n-j);hi=min(1,iv['end']*n-j)
                    if hi>lo+1e-12:
                        c=portion(seg['control'],lo,hi);coordinates.extend(c.tolist());midpoints.append(evaluate(c,.5).tolist())
            else:
                coordinates=a['endpoints'];midpoints=[np.mean(coordinates,axis=0).tolist()]
            display=sc.ax.transData.transform(coordinates);xy=np.stack([display[:,0],768-display[:,1]],axis=1)
            low=np.maximum(0,np.floor(xy.min(axis=0)-4).astype(int));high=np.minimum(768,np.ceil(xy.max(axis=0)+5).astype(int))
            rgb=np.array([int(a['color'][k:k+2],16) for k in (1,3,5)])
            sub=pix[low[1]:high[1],low[0]:high[0]]
            exactpixels=int(np.all(sub==rgb,axis=2).sum())
            mids=[]
            for m in midpoints:
                t=sc.ax.transData.transform(m);x,y=int(round(t[0])),int(round(768-t[1]));sl=pix[max(0,y-5):min(768,y+6),max(0,x-5):min(768,x+6)]
                mids.append(int(np.all(sl==rgb,axis=2).sum()))
            result.append({'action_index':i,'type':a['type'],'target_or_id':a.get('target',a.get('id')),'path_fingerprint_exact':exact,'selected_geometry_full_precision':coordinates,'bbox_xyxy_exclusive':[int(low[0]),int(low[1]),int(high[0]),int(high[1])],'exact_palette_pixels_in_bbox':exactpixels,'mid_segment_exact_palette_pixels':mids,'actual_visible_at_each_segment_center':all(m>0 for m in mids),'role':design['marker_roles'][i]['role']})
        write(d/'marker_visibility_audit.json',{'question_id':q,'variant_id':design['variant_id'],'audited_at_utc':now(),'native_PNG_size':[768,768],'method':'Actual frozen PNG exact-palette pixels at each selected segment midpoint and geometry bbox, plus fresh actual path fingerprint binding; no new image or solver call.','markers':result,'all_path_hashes_exact':all(x['path_fingerprint_exact'] for x in result),'all_marks_visible_at_segment_centers':all(x['actual_visible_at_each_segment_center'] for x in result)})
        print(q,'marks',len(result),'path exact',all(x['path_fingerprint_exact'] for x in result),'all centers visible',all(x['actual_visible_at_each_segment_center'] for x in result),flush=True)
    finally:sc.close()
