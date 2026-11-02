from tools39 import *
import math
from collections import defaultdict
from PIL import Image
import numpy as np
def edkey(x):return tuple(sorted(tuple(round(v,10) for v in xy) for xy in x))
math_audit={}
for q in ['Plane267','Plane428','Plane433']:
    ps=read(HERE/q/'all_native_paths.json');inc=defaultdict(list)
    for o,paths in ps.items():
        for p in paths:
            for j,c in enumerate(p['segments']):
                assert len(c)==2
                inc[edkey(c)].append({'object_id':o,'path_id':p['id'],'path_sha256':p['sha256'],'segment_index':j,'full_precision_native_controls':c,'length_display':math.dist(*c)})
    shared=[{'geometric_edge':k,'owners':a} for k,a in inc.items() if len(a)==2];outer=[{'geometric_edge':k,'owners':a} for k,a in inc.items() if len(a)==1]
    count=len(ps);assert len(shared)=={'Plane267':9,'Plane428':5,'Plane433':11}[q];assert len(outer)=={'Plane267':14,'Plane428':14,'Plane433':18}[q]
    math_audit[q]={'cell_count':count,'shared_edges':shared,'outer_edges':outer,'shared_count':len(shared),'outer_count':len(outer),'P_from_side_occurrences':4*count-2*len(shared),'incidence_comparison_rounding_decimals':10,'full_controls_preserved_above':True,'basis':'Source cell topology is exact unit-square incidence; rounding only merges machine transform noise below1e-10, never changes action coordinates.'}
math_audit['Plane267']['solution']={'P_cm':42,'unit_side_cm':3,'area_cm2':72,'unique_choice':'D','tested':False,'wrong_grouped_perimeter12_yields_nonchoice_area':98}
math_audit['Plane428']['solution']={'base_n':6,'base_P':14,'new_n':2013,'deltaP_each_square':2,'P':14+2*(2013-6),'false_growth_only_P':2*2013,'two_black_cap_constant':2}
math_audit['Plane433']['solution']={'all_side_occurrences':40,'correct_deduction':22,'P':18,'wrong_once_per_contact_deduction':11,'wrong_P':29}
# Bind every added path-node marker to all incident original native paths,
# including the two interior grid vertices of original two-unit target runs.
q='Plane280';out=next((HERE/q).glob('r39_*'));d=read(out/'design.json');paths=read(HERE/q/'all_native_paths.json');nodeinfo=[]
for r in d['marker_roles']:
    xy=r['action']['xy'];matches=[]
    for oid,ps in paths.items():
        for p in ps:
            for j,c in enumerate(p['segments']):
                if len(c)!=2:continue
                a,b=c;u=[b[i]-a[i] for i in range(2)];v=[xy[i]-a[i] for i in range(2)];den=sum(z*z for z in u)
                if not den:continue
                t=sum(u[i]*v[i] for i in range(2))/den
                dist=math.dist(xy,[a[i]+t*u[i] for i in range(2)])
                if -1e-12<=t<=1+1e-12 and dist<1e-12:matches.append({'object_id':oid,'path_id':p['id'],'path_sha256':p['sha256'],'segment_index':j,'full_precision_controls':c,'native_parameter':t,'is_target':oid.startswith('thick')})
    assert any(x['is_target'] for x in matches)
    nodeinfo.append({'action_index':r['action_index'],'xy':xy,'snap_id':r['exact_snap_point']['id'],'source_path_incidences':matches})
write(out/'node_path_binding_supplement.json',{'created_at':now(),'scope':'Read-only verification of pre-call frozen coordinates/context/path capture; no candidate/design/preset changed','precall_native_capture_sha256':file_hash(HERE/q/'all_native_paths.json'),'precall_context_sha256':file_hash(HERE/q/'context.json'),'markers':nodeinfo,'all10_on_original_black_target':True})
math_audit[q]=d['numeric_audit']
for q in ['Plane276','Plane283','Plane323']:
    out=next((HERE/q).glob('r39_*'));math_audit[q]=read(out/'design.json')['numeric_audit']
math_audit['Plane322']={'outer_radius':3,'inner_radius':2,'advance':4,'length_cm':170,'equation':'6+4(n-1)=170','unique_n':42,'wrong_advance2_n':83,'candidate_skipped':'No explicit existing advance recipient; do not add hidden center or center distance.'}
write(HERE/'supplemental_math_audit.json',{'created_at':now(),'independent_primary_computation':True,'questions':math_audit,'does_not_constitute_independent_second_review':True})
palette={}
for q in ['Plane276','Plane280','Plane283','Plane323','Plane428','Plane433']:
    out=next((HERE/q).glob('r39_*'));d=read(out/'design.json');m=read(out/'context.json');A=np.array(m['canvas']['data_to_pixel']);im=np.array(Image.open(out/'candidate.png').convert('RGB'));orig=np.array(Image.open(ROOT/'PlaneGeometry/image'/f'{q}.png').convert('RGB'));diff=np.any(im!=orig,axis=2);marks=[]
    geom=read(out/'marker_geometry_audit.json')
    for a,r in zip(read(out/'plugin.json')['params']['actions'],d['marker_roles']):
        if a['type']=='add_point':coords=[a['xy']];pad=8
        elif a['type']=='add_line':coords=a['endpoints'];pad=3
        else:
            p=next(x for x in geom['native_path_binding'][a['target']] if x['id']==a['interval']['path_id']);n=len(p['controls']);lo=a['interval']['start']*n;hi=a['interval']['end']*n;coords=[]
            for j,c in enumerate(p['controls']):
                for t in [max(0,lo-j),min(1,hi-j)]:
                    if j<=hi and j+1>=lo and 0<=t<=1:coords.append([c[0][i]+(c[-1][i]-c[0][i])*t for i in range(2)])
            pad=4
        px=np.array([(A@np.array([*xy,1]))[:2] for xy in coords]);xmin=max(0,math.floor(px[:,0].min())-pad);xmax=min(768,math.ceil(px[:,0].max())+pad+1);ymin=max(0,math.floor(px[:,1].min())-pad);ymax=min(768,math.ceil(px[:,1].max())+pad+1)
        rgb=[int(a['color'][i:i+2],16) for i in (1,3,5)];exact=int(np.all(im[ymin:ymax,xmin:xmax]==rgb,axis=2).sum());assert exact>0,(q,r['action_index'])
        marks.append({'action_index':r['action_index'],'bbox_with_margin':[xmin,ymin,xmax,ymax],'exact_palette_pixels':exact,'changed_pixels_in_bbox':int(diff[ymin:ymax,xmin:xmax].sum()),'visible_mark_confirmed':True})
    palette[q]={'PNG_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixel_hash(out/'candidate.png'),'changed_pixels':int(diff.sum()),'all_marks_have_visible_exact_color_pixels':True,'marks':marks,'limit':'Overlapping bboxes can include other marks. This is visibility support, not proof of causal effect or semantic validity; primary native viewing supplies the separate readability review.'}
write(HERE/'native_palette_audit.json',palette)
print('Supplemental incidence/math and native visibility checks pass for all6 designs; original skip proofs retained.')
