from bootstrap import *
import math,itertools
from runtime_isolation import install
isolation=install(OWN/'render_tmp')
sys.path.insert(0,str(ROOT/'SolidGeometry/workbench'))
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer
from workbench_io import load_config,pixel_hash,environment_versions
from dataset_tools.mathvision_workbench import png_bytes

for rel in ['MATHPALETTE_PROTOCOL.md','SolidGeometry/REDRAW_PROTOCOL.md','SolidGeometry/workbench/README.md','SolidGeometry/workbench/agent_prompt.md','SolidGeometry/workbench/plugin.schema.json','SolidGeometry/dataset_generator/protocol.json']:
 p=ROOT/rel;p.read_text(encoding='utf-8-sig');LEDGER[str(p)]=sha(p)
read(TASK/'references/Solid126/C01.json')
for p in (TASK/'references/Solid126').glob('*'):
 if p.is_file():LEDGER[str(p.resolve())]=sha(p)
history=read(TASK/'history_index.json')
for q in ['Solid186','Solid226']:
 for p in (U05/q).rglob('*.json'):
  if p.name in ['design.json','plugin.json','primary_mathematics.json','further_design_prescreen.json','manual_finals_and_binding_audit.json','fresh_context.json','native_scene_snapshot.json'] or p.name.endswith('_response.json'):read(p)
 entry=next(v for v in history['questions'] if v['question_id']==q)
 for d in entry['designs']:
  directory=ROOT/d['directory']
  for p in directory.rglob('*.json'):
   if p.name in ['design.json','plugin.json'] or p.name.endswith('_response.json'):read(p)
cfg=load_config(ROOT/'SolidGeometry/workbench/config.json')
cfg['runtime_dir']=str(OWN/'state');cfg['output_dir']=str(OWN/'output')
adapter=RendererAdapter(cfg)

def surface(voxels):
 dirs=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
 return sum(tuple(v[i]+d[i] for i in range(3)) not in voxels for v in voxels for d in dirs)
def grid_perimeter(cells):
 return sum((x+dx,y+dy) not in cells for x,y in cells for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
def style(target,color):return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5}

prepared=[]
for q in ['Solid186','Solid226']:
 e=eligibility(q);context=adapter.inspect_question(q)
 assert context==read(U05/q/'fresh_context.json')
 native=read(next(ROOT/'SolidGeometry'/p for p in e['formal_record']['runtime_dependencies'] if p.endswith('/scene.json')))
 assert native==read(U05/q/'native_scene_snapshot.json')
 folder=OWN/q;folder.mkdir(exist_ok=False)
 save(folder/'fresh_eligibility.json',e);save(folder/'context.json',context);save(folder/'native_scene_snapshot.json',native)
 capture=adapter.scene(q)
 try:noop=png_bytes(capture)
 finally:capture.close()
 assert pixel_hash(noop)==context['original_pixel_sha256']
 save(folder/'no_op_audit.json',{'formal_pixels_match':True,'current_context_matches_u05':True,'world_projection_and_visibility_native_snapshot_exact':True,'environment':environment_versions()})
 actions=[];roles=[];R='#DC2626';B='#2563EB'
 if q=='Solid186':
  vid='offline_trihedral_volume_to_paint'
  center0=(3.0,0.0,3.0);center1=(6.5,2.0,1.0)
  triads=[]
  for panel,center,length,directions in [('panel0',center0,3,[-1,1,-1]),('panel1',center1,2,[1,-1,1])]:
   arms=[]
   for axis in range(3):
    lo=min(center[axis],center[axis]+directions[axis]*length)
    hi=max(center[axis],center[axis]+directions[axis]*length)
    selected=[]
    for obj in context['objects']:
     if not obj['id'].startswith(panel):continue
     ps=obj['geometry']['points']
     if not all(isinstance(p,list) and len(p)==3 for p in ps):continue
     if not all(all(p[k]==center[k] for k in range(3) if k!=axis) for p in ps):continue
     if not all(lo<=p[axis]<=hi for p in ps):continue
     if abs(ps[0][axis]-ps[1][axis])!=1:continue
     assert obj['styleable'] and obj['geometry']['visibility']=='visible'
     selected.append(obj['id'])
     color=B if axis==2 else R
     actions.append(style(obj['id'],color))
     roles.append({'target':obj['id'],'world_points':ps,'panel':panel,'axis':'xyz'[axis],'color':color,'information_role':f'One existing unit segment of the {length}-unit {"vertical blue" if axis==2 else "horizontal red"} arm at a true {"outer convex" if panel=="panel0" else "inner concave"} trihedral vertex. All three arms identify three-dimensional cube dimensions, not a two-dimensional single face.'})
    assert len(selected)==length,(panel,axis,selected)
    direction=[0,0,0];direction[axis]=directions[axis]*length
    arms.append({'axis':'xyz'[axis],'unit_segments':selected,'length':length,'vector_from_vertex':direction})
   assert all(sum(a['vector_from_vertex'][i]*b['vector_from_vertex'][i] for i in range(3))==0 for a,b in itertools.combinations(arms,2))
   triads.append({'panel':panel,'center':center,'arms':arms,'three_axes_pairwise_perpendicular':True})
  assert len(actions)==15
  original=set(itertools.product(range(3),repeat=3))
  cut=set(itertools.product(range(1,3),range(2),range(1,3)))
  remaining=original-cut
  assert len(original)==27 and len(cut)==8 and len(remaining)==19 and surface(original)==surface(remaining)==54
  correct='A';wrong='C';wrong_value='6 litres'
  measure={'original_volume':27,'removed_volume':8,'remaining_volume':19,'original_surface':54,'remaining_surface':54,'correct_paint':9,'triads':triads,'forecasted_wrong_volume_scaled_paint_exact':'19/3','forecasted_wrong_nearest_given_option':'C=6 litres','nearest_choice_is_part_of_predicted_model_error_not_question_requirement':True}
  mechanism='Three mutually orthogonal source arms of length3 are compared with three actual concave cutout arms of length2. Forecasted two-stage error: use volume proportion (27-8)/27 for whole-surface paint, obtaining19/3 litres, then incorrectly choose the nearest listed6/C. The true whole surface stays54, so A9 remains uniquely correct. This is a tentative error forecast, not a justified approximation rule.'
  difference='Old u05 face-scale compared two perpendicular sides of a source front9-unit face at the lower-left/front corner with one recessed4-unit face. This draft instead selects the OTHER original outer top-front-right vertex, ALL THREE real axes, and the opposing inner trihedral cutout vertex: complete3D dimensions3,3,3 versus2,2,2, with no single face frame or lost/new12-area subtotal. Old source-axis targets are replaced, not relabelled; an extra independent spatial axis and different source vertex change the information object from face area to cubical volume.'
  limitation='The second nearest-choice step is a forecasted additional mistake, not guaranteed behavior. Original whole-surface wording has no rounding instruction. C was not chosen merely because it appeared once before. Purely offline draft: effectiveness and independent clarity review still untested.'
 else:
  vid='offline_open_rails_lateral_increment'
  points=native['points'];objects={o['id']:o for o in native['objects']}
  top_ids=['line_6','line_10','line_12','line_13','line_7'];bottom_id='line_5'
  chain=[(1,0,3),(1,4,3),(1,4,2),(1,5,2),(1,5,3),(1,9,3)]
  lengths=[]
  for target,a,b in zip(top_ids,chain,chain[1:]):
   ps=[points[p] if isinstance(p,str) else p for p in objects[target]['points']]
   assert {tuple(p) for p in ps}=={a,b}
   length=math.dist(a,b);lengths.append(length)
   actions.append(style(target,B));roles.append({'target':target,'world_points':ps,'length':length,'color':B,'information_role':'Consecutive segment of the complete existing open upper longitudinal rail; all five pieces together form11ft, rather than an area enclosure.'})
  ps=[points[p] for p in objects[bottom_id]['points']]
  assert {tuple(p) for p in ps}=={(1,0,0),(1,9,0)}
  actions.append(style(bottom_id,R));roles.append({'target':bottom_id,'world_points':ps,'length':9,'color':R,'information_role':'Existing unchanged lower longitudinal9ft rail, giving the former straight upper-span length without adding any ghost edge or enclosing a former face.'})
  assert lengths==[4,1,1,1,4] and sum(lengths)==11 and len(actions)==6
  profile=set(itertools.product(range(9),range(3)));new_profile=profile-{(4,2)}
  assert len(profile)==27 and len(new_profile)==26 and grid_perimeter(profile)==24 and grid_perimeter(new_profile)==26
  before=set(itertools.product(range(1),range(9),range(3)));after=before-{(0,4,2)}
  assert surface(before)==surface(after)==78
  correct='C';wrong='E';wrong_value='2 more square feet'
  measure={'bottom_rail_length':9,'top_rail_ordered_lengths':lengths,'top_rail_length':11,'rail_increment':2,'extrusion_width':1,'cross_section_area_before':27,'cross_section_area_after':26,'cross_section_perimeter_before':24,'cross_section_perimeter_after':26,'true_lateral_surface_increment':2,'true_front_and_back_area_increment':-2,'correct_total_surface_change':0,'before_total':78,'after_total':78,'colored_subgraph_components':2,'colored_subgraph_cycles':0,'no_added_lines':True}
  mechanism='The actual stepped upper rail is11ft while the unchanged bottom rail is9ft. This expresses the true profile-perimeter increase2 and, at given extrusion width1ft, the TRUE lateral-area subtotal increase2sqft. Forecasted error E reports that subtotal as the whole surface change, forgetting the two end-profile losses1+1. Correct2*26+26 equals original2*27+24=78, so C remains unique.'
  difference='Old front-plane loss used a blue CLOSED former27-area rectangle with an added ghost upper segment and a red localU to evoke27-to26 face area. This draft draws NO new line, removes the two end-height framers and the ghost segment, and organizes two disjoint ACTUAL OPEN ordered longitudinal rails: the whole upper4+1+1+1+4 path versus the one9ft lower span. Old removed-roof-vs-three-new-faces compared one square patch to three square patches. Here source and receiver are complete one-dimensional boundary paths and the lateral-prism relation P*width; not a mere oldE/B image relabel.'
  limitation='Some existing segments overlap the old face-frame design because the solid has few edges; the parent must independently judge whether the new complete open-path information object is sufficiently substantive. The same finalE was previously forecast for a DIFFERENT face-count hypothesis, which stays a failedE trial. No effect claim is made for this zero-call draft.'
 d=folder/vid;d.mkdir()
 plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':'Compare existing open geometric measurements','intent':'True source-receiver measurement comparison','params':{'actions':actions}}
 renderer=PluginRenderer(cfg,adapter,{q:context})
 normalized,data,px=renderer.render(plugin)
 n2,data2,px2=renderer.render(normalized,frozen=True)
 assert normalized==n2 and data==data2 and px==px2
 (d/'candidate.png').write_bytes(data);(d/'repeat.png').write_bytes(data2)
 save(d/'plugin.json',normalized);save(d/'plugin_submitted.json',plugin);save(d/'marker_roles.json',roles)
 save(d/'exact_geometry_and_measure_proof.json',measure)
 prior=[]
 for olddesign in sorted((U05/q).glob('*/design.json')):
  od=read(olddesign);op=read(olddesign.parent/'plugin.json')
  oldtargets={a.get('target',a.get('id')) for a in op['params']['actions']}
  newtargets={a['target'] for a in actions}
  assert sha(d/'candidate.png')!=od['image_sha256']
  prior.append({'directory':str(olddesign.parent),'preset':od['expected_wrong_answer'],'PNG_sha256':od['image_sha256'],'old_targets':sorted(oldtargets),'shared_targets':sorted(oldtargets&newtargets),'new_targets':sorted(newtargets-oldtargets),'removed_old_targets':sorted(oldtargets-newtargets)})
 save(d/'design_difference_audit.json',{'at_utc':now(),'substantive_difference':difference,'prior_u05_designs':prior,'all_old_raw_responses_read':True,'same_failed_PNG_not_reused':True})
 save(d/'reference_migration.json',{'reference':'Current user Solid126 C01 frozen in TASK/references','reference_PNG_sha256':sha(TASK/'references/Solid126/C01.png'),'method':'Actual existing red/blue edge groups compare real geometric quantities; no fills, text, false equalities, new geometry or new painting conditions.','current_ref_source_read':True})
 save(d/'design.json',{'created_at_utc':now(),'question_id':q,'variant_id':vid,'correct_answer':correct,'expected_wrong_answer':wrong,'expected_wrong_value':wrong_value,'mechanism':mechanism,'substantive_difference':difference,'limitation':limitation,'image_sha256':sha(d/'candidate.png'),'pixel_sha256':px,'plugin_sha256':sha(d/'plugin.json'),'status':'OFFLINE_UNTESTED_TENTATIVE_HYPOTHESIS; PARENT DECISION AND NEW INDEPENDENT REVIEW REQUIRED','actual_API_calls':0})
 save(d/'render_audit.json',{'fresh_context_schema_defaults':True,'original_noop_pixels_exact':True,'twice_candidate_PNG_byte_identity':True,'pixel_sha256':px,'PNG_sha256':sha(d/'candidate.png'),'only_existing_styles_no_added_or_deleted_geometry':True,'all_original_linestyles_and_fills_and_labels_unchanged':True,'environment':environment_versions(),'isolation':isolation,'fresh_independent_process_replay_required':True,'new_API_calls':0})
 assert eligibility(q)['current_content_sha256']==e['current_content_sha256']
 prepared.append({'question_id':q,'variant_id':vid,'directory':str(d),'PNG_sha256':sha(d/'candidate.png'),'tentative_wrong':wrong,'new_API_calls':0})
 print(json.dumps(prepared[-1],ensure_ascii=False),flush=True)
assert all(sha(Path(p))==h for p,h in LEDGER.items())
save('read_ledger.json',{'at_utc':now(),'all_read_sources_unchanged':True,'files_sha256':LEDGER})
save('prepared_offline_drafts.json',prepared)
