from review_bootstrap import *
import numpy as np
from PIL import Image
from collections import Counter

r=read(OWN/'native_render_audit.json');a=read(OWN/'native_artist_audit.json');frozen=read(CAND.parent/'adapter_input_hashes.json')
hash_checks={p:sha(PROJECT/p) for p in frozen}
assert hash_checks==frozen
r['adapter_manifest_all_entries_equal']=True
r['adapter_manifest_comparison_method']='Normalize actual files to the recorded project-relative-path -> SHA256 dictionary. All 3416 current file hashes equal the recorded hashes. The initial false value compared this flat path dictionary with a nested native adapter manifest; that was an audit representation error, not input drift.'
write('native_render_audit.json',r)

def arr(p):
    with Image.open(p) as im:return np.array(im.convert('RGBA'))
before=arr(OWN/'independent_noop.png');after=arr(CAND/'candidate.png')
changed=np.any(before!=after,axis=2);y,x=np.where(changed);p=np.column_stack([x+.5,y+.5])
matrix=np.array(read(OWN/'fresh_native_context.json')['canvas']['data_to_pixel'])
points={k:np.array(v) for k,v in read(PROJECT/'PlaneGeometry/dataset_generator/scenes/Plane427.json')['points'].items()}
def px(name):return (matrix@np.array([*points[name],1]))[:2]
def dist(ps,pa,pb):
    d=pb-pa;t=np.clip(((ps-pa)@d)/(d@d),0,1)
    return np.linalg.norm(ps-pa-t[:,None]*d,axis=1)
marked=np.minimum.reduce([dist(p,px(c),px(d)) for c,d in [('S','T'),('V','T'),('S','V')]])
unmarked=np.minimum.reduce([dist(p,px(c),px(d)) for c,d in [('R','S'),('T','R'),('T','U'),('U','V')]])
delta=np.max(np.abs(after[y,x,:3].astype(int)-before[y,x,:3].astype(int)),axis=1)
outside=marked>4
assert int(outside.sum())==325
assert np.all(unmarked[outside]<2)
gray=np.logical_and(before[y,x,0]==before[y,x,1],before[y,x,1]==before[y,x,2]) & np.logical_and(after[y,x,0]==after[y,x,1],after[y,x,1]==after[y,x,2])
assert np.all(gray[outside])
high=outside & (delta>1)
assert {(int(xx),int(yy)) for xx,yy in zip(x[high],y[high])}=={(243,224),(243,225),(243,226)}

coverage=[]
for target in ['o0','o1','o2']:
    orig=[s for path in a['before_paths'][target] for s in path['segments']]
    new=[s for path in a['after_paths'][target] for s in path['segments']]
    segments=[]
    covered={i:[] for i in range(len(orig))}
    for seg in new:
        ends=np.array([seg['control'][0],seg['control'][-1]])
        candidates=[]
        for i,old in enumerate(orig):
            oa,ob=np.array(old['control']);d=ob-oa
            t=((ends-oa)@d)/(d@d)
            residual=float(np.max(np.linalg.norm(ends-oa-t[:,None]*d,axis=1)))
            if residual<1e-12 and t.min()>-1e-12 and t.max()<1+1e-12:candidates.append((residual,i,t))
        residual,i,t=min(candidates,key=lambda q:q[0])
        covered[i].append(t.tolist())
        segments.append({'original_segment_index':i,'control':seg['control'],'style':seg['style'],'original_segment_parameters':t.tolist(),'max_perpendicular_residual':residual})
    for i,spans in covered.items():
        spans.sort()
        assert abs(spans[0][0])<1e-12 and abs(spans[-1][-1]-1)<1e-12
        assert all(abs(lo[1]-hi[0])<1e-12 for lo,hi in zip(spans,spans[1:]))
    coverage.append({'target':target,'all_original_segments_covered_without_geometry_addition':True,'exact_fragments':segments})
for c in coverage:
    target=c['target']
    for s in c['exact_fragments']:
        i=s['original_segment_index'];style=s['style']
        marked_style=(target=='o0' and i==1) or (target=='o1' and i==2)
        if target!='o2':
            assert style['color']==('#2563ebff' if marked_style else '#000000ff')
            assert style['linewidth_pt']==(2 if marked_style else 1)
            assert style['dash'][1] is None
        else:
            assert style['dash'][1]==[1.,1.65]
            assert style['linewidth_pt']==(1.5 if style['color']=='#dc2626ff' else 1)

redtail=np.array(a['after_paths']['o2'][0]['segments'][-1]['control'])
tail_length=float(np.linalg.norm(redtail[-1]-redtail[0]))
precision={'fully_compared_frozen_input_files':len(frozen),'all_3416_path_hashes_match':True,
 'segmentation_coverage':coverage,'original_arcs_exactly_identical':a['before_paths']['o3']==a['after_paths']['o3'] and a['before_paths']['o4']==a['after_paths']['o4'],
 'pixel_difference_classification':{'total_changed_pixels':int(changed.sum()),'within_4px_exact_selected_centerlines':int((~outside).sum()),'outside_centerline_tubes':int(outside.sum()),
 'outside_all_on_original_unselected_strokes_within_2px':True,'outside_all_grayscale_no_color_or_fill_added':True,
 'outside_channel_delta_histogram':dict(Counter(map(int,delta[outside]))),'one_level_AA_pixels':int((outside & (delta==1)).sum()),
 'R_original_closing_join_pixels':[q for q in r['changed_pixels_outside_4px_marked_segment_tubes'] if max(abs(u-v) for u,v in zip(q['before'][:3],q['after'][:3]))>1],
 'explanation':'Replacing triangle outlines with exact PathPatches changes rasterization on 322 gray AA pixels by one 8-bit channel level. The original polygon closing join at R becomes two butt-capped path ends, changing only (243,224),(243,225),(243,226) by 23,10,10. The original RS/RT centerlines, endpoint incidence, black 1pt width, readability and continuous apparent R corner remain. These are renderer AA/join differences, not a styled fourth edge, new intersection, cut or geometry change.',
 'no_claim_all_unselected_pixels_are_identical':True},
 'SV_unstyled_floating_tail':{'display_unit_length':tail_length,'pixel_length':tail_length*abs(matrix[0,0]),'reason':'The required end is 0.9999999999999999, not 1. The final floating-point-sized black tail is retained by the exact interval implementation. It has no native visible gap/cut/new condition.'},
 'native_text_boxes_unchanged':all(t['changed_pixels']==0 for t in r['text_boxes_pixel_comparison']),
 'all_original_text_artist_properties_and_fills_exactly_preserved':a['texts_exactly_preserved'] and a['fills_exactly_preserved']}
write('precision_and_AA_audit.json',precision)
print(json.dumps({k:v for k,v in precision.items() if k!='segmentation_coverage'},ensure_ascii=False,indent=2))
