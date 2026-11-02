import task_env
from task_env import OWN
from prepare import read,write
import numpy as np
from PIL import Image
for f in OWN.glob('Plane*/r48_*/design.json'):
    d=f.parent;design=read(f);plugin=read(d/'plugin.json');old=read(d/'marker_visibility_audit.json');ctx=read(d/'context.json')
    matrix=np.asarray(ctx['canvas']['data_to_pixel'],dtype=float);pix=np.asarray(Image.open(d/'candidate.png').convert('RGB'),dtype=float)
    markers=[]
    for m,a in zip(old['markers'],plugin['params']['actions']):
        rgb=np.array([int(a['color'][k:k+2],16) for k in (1,3,5)],dtype=float);hue=rgb-rgb.mean();hue/=np.linalg.norm(hue)
        geometry=np.asarray(m['selected_geometry_full_precision']);mid=(geometry[0]+geometry[-1])/2;coord=matrix@np.r_[mid,1];x,y=np.round(coord[:2]).astype(int)
        patch=pix[max(0,y-6):min(768,y+7),max(0,x-6):min(768,x+7)]
        chroma=patch-patch.mean(axis=2,keepdims=True);norm=np.linalg.norm(chroma,axis=2);cosine=np.einsum('ijk,k->ij',chroma,hue)/np.maximum(norm,1e-9)
        count=int(((cosine>.98)&(norm>12)).sum())
        markers.append({'action_index':m['action_index'],'target_or_id':m['target_or_id'],'midpoint_data':mid.tolist(),'midpoint_pixel':coord[:2].tolist(),'palette_hue_pixels_at_center':count,'visible_chromatic_stroke':count>0,'exact_path_binding':m['path_fingerprint_exact'],'role':m['role']})
    write(d/'marker_chroma_audit.json',{'question_id':design['question_id'],'variant_id':design['variant_id'],'method':'Actual native PNG palette hue direction after removing neutral gray component (cosine>.98, chroma norm>12), near every straight selected segment midpoint. Original fills are neutral. Thin antialiased strokes need not contain an exact palette RGB pixel.','earlier_exact_palette_audit_retained_as_diagnostic':True,'earlier_false_exact_RGB_absence_does_not_establish_invisibility':True,'markers':markers,'all_visible':all(x['visible_chromatic_stroke'] for x in markers),'all_path_bindings_exact':all(x['exact_path_binding'] for x in markers)})
    print(design['question_id'],'all visible',all(x['visible_chromatic_stroke'] for x in markers),'zero indices',[x['action_index'] for x in markers if not x['visible_chromatic_stroke']])
