from tools05 import *
from collections import Counter,defaultdict
qid='Plane164';vid='one_piece_partial_fit'
cfg,ad=adapter();check=eligibility(qid);assert check['eligible'],check
metadata=ad.inspect_question(qid);before=inputs(ad,qid);obs={o['id']:o['geometry'] for o in metadata['objects']}
cells=[g['points'] for oid,g in obs.items() if oid.startswith('piece0_') and oid.endswith('_square')]
counts=Counter(tuple(sorted((tuple(a),tuple(b)))) for pts in cells for a,b in zip(pts,pts[1:]+pts[:1]))
neighbors=defaultdict(list)
for (a,b),count in counts.items():
    if count==1:neighbors[a].append(b);neighbors[b].append(a)
start=min(neighbors);walk=[start];previous=None;current=start
while True:
    nxt=next(p for p in neighbors[current] if p!=previous)
    if nxt==start:break
    walk.append(nxt);previous,current=current,nxt
corners=[]
for i,p in enumerate(walk):
    a=walk[i-1];b=walk[(i+1)%len(walk)]
    if (p[0]-a[0])*(b[1]-p[1])!=(p[1]-a[1])*(b[0]-p[0]):corners.append(p)
segments=list(zip(corners,corners[1:]+corners[:1]));actions=[];bindings=[];roles=[]
snaps={tuple(p['xy']):p for p in metadata['snap_points']}
def transform(p):return (p[1]-1,14-p[0])
for i,(a,b) in enumerate(segments):
    for name,endpoints in [('source',[a,b]),('B_match',[transform(a),transform(b)])]:
        assert all(p in snaps for p in endpoints),(name,endpoints)
        mark='partial_'+name+str(i)
        actions.append({'type':'add_line','id':mark,'endpoints':[list(p) for p in endpoints],'color':'#DC2626','linestyle':'solid'})
        bindings.append({'mark_id':mark,'role':name+'_boundary_segment_'+str(i),'endpoints':list(endpoints),'exact_original_snap_points':[snaps[p] for p in endpoints]})
        roles.append(mark+' overlays one existing grid-boundary segment of '+('the first sourcepiece' if name=='source' else 'its correctly rotated eightcell match in B')+'. It is paired by index with '+('partial_B_match' if name=='source' else 'partial_source')+str(i)+'.')
mechanism='The complete eightcell boundary of the first sourcepiece is paired with its exact90degree clockwise match inside B. This is a concrete partial-fit correspondence: every symbol of that piece matches B, but the unmarked secondpiece does not. It targets accepting one correctly fitted component as sufficient for the entire two-piece assembly. No completeoption, optionletter, symbol or fill is colored.'
math='Exact enumeration of all four rotations and all integer placements inside a4x4 board gives four disjoint shape-tilings. Checking all16 glyphs yields exactly one placement for A and none for B,C,D,E. Even allowing reflection gives sixteen shape-tilings, with still exactly one complete solution A. In B the marked firstpiece matches all8 glyphs; its complement fails6 glyphs. Minimum mismatchcounts over rotation-only tilings areA0,B6,C5,D4,E5. See exact_tiling_audit.json for placements and every mismatch. The red boundary overlays change no square, glyph, position or connection.'
plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared wrong answer B','params':{'actions':actions}}
renderer=PluginRenderer(cfg,ad,{qid:metadata});normalized,png,digest=renderer.render(plugin);n2,png2,d2=renderer.render(normalized,frozen=True)
assert normalized==n2 and png==png2 and digest==d2 and before==inputs(ad,qid)
folder=HERE/qid/vid;folder.mkdir(parents=True,exist_ok=False)
write(folder/'context.json',metadata);write(folder/'eligibility_before_design.json',check);write(folder/'exact_marker_bindings.json',bindings);write(folder/'plugin.json',normalized);(folder/'candidate.png').write_bytes(png)
write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':'B','correct_answer':'A','formal_record':ad.records[qid],'created_at':datetime.now(timezone.utc).isoformat(),'mechanism':mechanism,'mathematical_solution':math,'marker_roles':roles,'human_gate':'All redsolid auxiliarylines coincide with existing component/grid boundaries; no cut or gridline is added at a new location. The original eightcell components, all sixteen glyphs in each option and every label remain unaltered.','review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_SECOND_REVIEW'})
write(folder/'render_check.json',{'baseline_pixel_match':True,'schema_normalized':True,'two_byte_identical_redraws':True,'pixel_sha256':digest,'png_sha256':file_hash(folder/'candidate.png'),'plugin_sha256':file_hash(folder/'plugin.json'),'design_sha256':file_hash(folder/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'no_source_writes':True,'marker_count':len(actions)})
print('rendered',qid,vid,'markers',len(actions),flush=True)
