import research_env as env
import json,sys,hashlib,io,copy
import numpy as np
from pathlib import Path
from inspect_sources import save,sha,now,eligibility,QIDS
sys.path.insert(0,str(env.PROJECT/'SolidGeometry/workbench'))
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer
from renderer_adapter import scene_png
from partial_style import object_paths
from workbench_io import load_config
from PIL import Image

RED,BLUE='#DC2626','#2563EB'
def style(target,color=RED,**kw):return {'type':'set_object_style','target':target,'color':color,**kw}
def partial(q,target,vertex,color=RED,fraction=.20):
 paths=json.loads((env.ROOT/q/'paths.json').read_text(encoding='utf-8'))[target]
 assert len(paths)==1 and len(paths[0]['segments'])==1
 ctx=json.loads((env.ROOT/q/'context.json').read_text(encoding='utf-8'))
 xy=next(x['xy'] for x in ctx['snap_points'] if x['id']==vertex)
 control=paths[0]['segments'][0]['control']; start=np.allclose(control[0],xy,rtol=0,atol=1e-12)
 assert start or np.allclose(control[-1],xy,rtol=0,atol=1e-12)
 lo,hi=(0.0,fraction) if start else (1-fraction,1.0)
 return style(target,color,linewidth_pt=2,interval={'path_id':paths[0]['id'],'path_sha256':paths[0]['sha256'],'start':lo,'end':hi,'wrap':False})
def point(q,vertex,color):
 ctx=json.loads((env.ROOT/q/'context.json').read_text(encoding='utf-8'))
 xy=next(x['xy'] for x in ctx['snap_points'] if x['id']==vertex)
 return {'type':'add_point','id':'r49_vertex_'+vertex,'xy':xy,'color':color,'filled':True,'size_pt2':50,'edge_linewidth_pt':1.0}

def specifications():
 specs=[]
 q='Solid80'; pairs=[('p001','U'),('p100','V'),('p111','W')]
 actions=[]; roles=[]
 for old,new in pairs:
  actions.extend([point(q,old,BLUE),point(q,new,RED)])
  roles.extend([f'Original surviving vertex {old}: old-count source on one of the three retained incident-edge remnants; paired along the existing remnant to {new}.',f'Actual cut vertex {new}: new-count receiver paired with {old}; one of the three distinct newly introduced corners.'])
 specs.append((q,'r49_three_edge_endpoint_count','11',actions,roles,
  'Compare the old and new endpoint of each of three retained original-edge remnants. Blue marks count retained old endpoints; red marks count the three genuinely new endpoints. The wrong operation retains the initial8 and simply adds3, forgetting that the cut removes p101.',
  'Old candidate puts a single dot at the removed phantom corner p101 and tests retaining that corner. New candidate never marks p101 or its phantom stubs: six real surviving endpoints form three source/receiver pairs along unchanged original edges. It targets unadjusted baseline8 plus three new endpoints, rather than continuing to count an explicitly marked removed vertex. The wrong result11 is prospective from this independent count rule, not a relabelled old miss.'))
 q='Solid89'; actions=[style(t,RED,linewidth_pt=2) for t in ['frontrim0','frontrim1','toprim0','toprim1','rightrim0','rightrim1']]
 roles=[f'{view} aperture {axis} unit side: member of the same two-side1x1 aperture correspondence across all three real axial bores; groups one independent3-unit bore volume in the mistaken sum.' for view in ['front','top','right'] for axis in ['first','second']]
 specs.append((q,'r49_three_aperture_volume_units','A',actions,roles,
  'Match the two existing unit-aperture rim directions at each of three genuine bores. The red L groups encode three congruent1x1 cross sections, each extruded through length3 given by the question; the proposed error adds three3-cell bore volumes as disjoint and subtracts270g, giving540g(A).',
  'Old assessment saved no design or API pair and rejected generic aperture emphasis/new junctions. This prospective design binds two exact original unit-rim sides per aperture as three matched cross-section units, with an explicit disjoint-volume accounting error. No tunnel depth is invented from the first-unit visible walls, and no central junction is drawn.'))
 q='Solid90'; actions=[style(t,RED,linewidth_pt=2) for t in ['diagp011p101','diagp101p000','diagp000p011']]+[style('diagp011p100',BLUE,linewidth_pt=2)]
 roles=['XY: first real face-diagonal source, square64, in the full three-source aggregation.','YZ: second real face-diagonal source, square81.','XZ: third real face-diagonal source, square55; original hidden dashes retained.','XA: requested body-diagonal receiver for the aggregate of three source squares; original hidden dashes retained.']
 specs.append((q,'r49_face_square_aggregate','10*sqrt(2)',actions,roles,
  'The complete red XYZ three-face-diagonal group supplies64+81+55=200; blue XA is the requested receiver. The proposed error takes sqrt200 as the body diagonal without the necessary division by2, incorrectly treating the face diagonals as independent orthogonal components.',
  'Old design matches only XZ and XA to copy the given sqrt55. New design includes all three actual given face diagonals as one aggregate and distinguishes the body-diagonal receiver. It predicts sqrt200 before calls from a double-counting rule, not either observed old final sqrt(-17)/9.'))
 q='Solid107'; paths=json.loads((env.ROOT/q/'paths.json').read_text(encoding='utf-8'))['AC'][0]
 actions=[style('AD',RED,linewidth_pt=2),style('CB',RED,linewidth_pt=2),style('AB',BLUE,linewidth_pt=2),style('DC',BLUE,linewidth_pt=2)]
 for color,lo,hi in [(RED,0.0,.5),(BLUE,.5,1.0)]:actions.append(style('AC',color,linewidth_pt=2,interval={'path_id':paths['id'],'path_sha256':paths['sha256'],'start':lo,'end':hi,'wrap':False}))
 roles=['AD=7: first member of false red face-bound pair7/4.','CB=4: second member of the red pair; its numeric label remains attached to CB, not AC.','AB=2: first member of false blue face-bound pair2/3.','DC=3: second member of the blue pair.','First half of existing dashed AC: red receiver for the incorrectly assigned7/4 triangle bound.','Second half of the SAME dashed AC: blue receiver for the incorrectly assigned2/3 bound; no intersection point is added.']
 specs.append((q,'r49_opposite_pair_face_bounds','10',actions,roles,
  'Group opposite known edges AD/CB(red7,4) and AB/DC(blue2,3), and bind the two groups to the two portions of AC. The error treats these two nonincident pairs as the triangles constraining AC, giving3<AC<5 and integerAC4. DB remains6 from its actual constraints, so sum10. Careful incidence checking still givesAC5 and total11.',
  'Old design directly pairs CB4 with all of AC in blue. New six-action design groups ALL FOUR known edges into two opposite-edge pairs and assigns their two distinct strict triangle bounds to AC portions. The result4 is derived from the intersection of false bounds, not a copied known4. There is no old DB/7 symmetry hypothesis and no observed9/12 is promoted. The same final target10 does not turn the new grouping into an unchanged PNG retry.'))
 q='Solid159'; actions=[]; roles=[]
 for vertex,targets,role in [('L',['edgeLF','edgeLR','edgeTL','edgeBL'],'degree4 source equatorial vertexL=5'),('T',['edgeTL','edgeTF','edgeTR'],'degree3 apex receiverT=1'),('B',['edgeBL','edgeBF','edgeBR'],'degree3 opposite-apex receiverB')]:
  for target in targets:
   actions.append(partial(q,target,vertex));roles.append(f'{target} portion at {vertex}: one actual incidence arm of the {role}; compare full local arm counts4 versus3, without adding or deleting any arm.')
 specs.append((q,'r49_face_incidence_divisor_transfer','16.5',actions,roles,
  'Match one four-arm equatorial star to each three-arm apex star using short existing-edge portions. The proposed error transfers equatorial face-incidence multiplicity4 to all five vertices, divides six face sums66 by4, and reports16.5. The true weighted sum is4*15+3*2=66, while the requested unweighted total is17.',
  'Old five vertex dots make the wrong L/R pair and T/F/B triple, predicting13 by swapping value-class multiplicities. New design retains the true apex/equator identity and numerical values, but compares actual local edge/face incidence4 versus3 and targets uniform-degree averaging16.5. It uses no vertex dots and no swapped-value class. This is a new mathematical error rule, not new colors on the old grouping.'))
 q='Solid171'; targets=['truncatedv15v16','truncatedv16v17','truncatedv15v17','truncatedv15v3']
 actions=[style(t,RED,linewidth_pt=2) for t in targets]
 roles=['First actual edge of the upper-front-right triangular cut face: one member of its3-edge boundary group.','Second actual edge of that same triangular face.','Third actual edge completing that same original face boundary.','Adjacent retained original cube-edge remnant: one-edge counting-unit source, compared to the entire red3-edge cut boundary.']
 specs.append((q,'r49_cut_face_edge_unit','20',actions,roles,
  'Compare the complete three-edge boundary of one actual triangular cut face with one adjacent original edge remnant in the same color. The proposed error replaces the3 new edges per corner by one boundary-unit per face, giving12+8=20 instead of12+8*3=36.',
  'Old assessment saved no candidate and rejected phantom-stub counting/new hidden edges. New design touches only four actual retained-body edges: three belonging to one existing cut face, one old-edge remnant. No phantom is restyled and no hidden edge is introduced. It tests an explicit unit-size/counting error distinct from counting old dashed corner remnants.'))
 q='Solid172'; actions=[]; roles=[]
 for vertex,targets in [('L',['edgeTL','edgeLF','edgeBL']),('R',['edgeTR','edgeFR','edgeBR'])]:
  for target in targets:
   actions.append(partial(q,target,vertex,BLUE));roles.append(f'{target} short visible arm at {vertex}: one of the matched three-visible-arm tripods; {"L=5 is source" if vertex=="L" else "R is receiver"}. The fourth actual incidenceLR stays black dashed and is not deleted.')
 specs.append((q,'r49_visible_tripod_apex_transfer','13',actions,roles,
  'Pair three visible-edge arms at L=5 with the three visible arms at R. Omitting the existing hidden LR from the colored local tripods can invite treating L/R as the apex pair, transferring5 toR and1 to the other three vertices, giving2*5+3*1=13. The black hiddenLR visibly refutes that degree3 role; the true apices areT/B.',
  'This question previously had only a source assessment, no saved candidate/preset/API pair. New design uses six short existing-edge portions with exact current Solid172 coordinates, not a copied Solid159 PNG or its dot design. Actual1/5 locations, full graph and independent rank5 proof were checked for this question before selecting the preset.'))
 return specs

def vec_snapshot(scene):
 return {'text':[{'text':t.get_text(),'position':list(t.get_position()),'color':str(t.get_color()),'transform':t.get_transform().get_matrix().tolist()} for t in scene.ax.texts],
  'filled_patches':[{'vertices':p.get_path().vertices.tolist(),'codes':p.get_path().codes.tolist() if p.get_path().codes is not None else None,'facecolor':list(p.get_facecolor()),'transform':p.get_transform().get_matrix().tolist()} for p in scene.ax.patches if p.get_fill()],
  'view':[list(scene.ax.get_xlim()),list(scene.ax.get_ylim())],'canvas':list(scene.fig.canvas.get_width_height())}
def render_one(spec):
 q,variant,preset,actions,roles,mechanism,difference=spec
 d=env.ROOT/q/variant;d.mkdir(parents=True,exist_ok=False)
 e=eligibility(q);assert e['eligible'];save(d/'eligibility_before_design.json',e)
 ctx=json.loads((env.ROOT/q/'context.json').read_text(encoding='utf-8'))
 config=load_config();adapter=RendererAdapter(config);renderer=PluginRenderer(config,adapter,{q:ctx})
 old=json.loads((env.ROOT/'global_old_binding_design_scan.json').read_text(encoding='utf-8'))
 old_designs=[x for x in old['designs'] if x['question_id']==q]
 save(d/'design_difference_audit.json',{'question_id':q,'variant_id':variant,'created_at_utc':now(),'old_design_paths_sha256':[{k:x[k] for k in ['path','sha256']} for x in old_designs],
  'substantive_new_information':difference,'prospective_geometric_error_rule':mechanism,'expected_wrong_answer':preset,
  'not_cosmetic_or_posthoc':True,'old_history_unchanged':True,'old_two_wrong_misses_not_relabelled':True,'no_retest_of_old_failed_aborted_PNG':True})
 plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':mechanism,'params':{'actions':actions}}
 normalized=renderer.normalize(plugin);assert normalized==plugin
 first,data,pixels=renderer.render(plugin);second,data2,pixels2=renderer.render(plugin)
 assert data==data2 and first==second==plugin and pixels==pixels2
 old_shas=[x['data'].get('image_sha256') for x in old['bindings'] if x.get('question_id')==q]
 assert hashlib.sha256(data).hexdigest() not in old_shas
 (d/'candidate.png').write_bytes(data);(d/'offline_repeat.png').write_bytes(data2)
 save(d/'plugin.json',plugin);save(d/'context.json',ctx)
 scene=adapter.scene(q)
 try:
  scene.fig.canvas.draw(); before=vec_snapshot(scene); bindings=[]
  for i,a in enumerate(actions):
   if a['type']=='set_object_style':
    paths=object_paths(scene,a['target'])
    bindings.append({'action_index':i,'target':a['target'],'original_object':next(o for o in ctx['objects'] if o['id']==a['target']),
     'paths':[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'controls':[x['control'].tolist() for x in p['segments']],'styles':[x['style'] for x in p['segments']]} for p in paths], 'action':a,'role':roles[i]})
   else:
    bindings.append({'action_index':i,'action':a,'exact_existing_snap':next(p for p in ctx['snap_points'] if p['xy']==a['xy']),'role':roles[i]})
  renderer.apply_actions(scene,plugin);scene.fig.canvas.draw();after=vec_snapshot(scene)
  assert before==after
 finally:scene.close()
 save(d/'marker_path_bindings.json',bindings)
 rgba=np.asarray(Image.open(io.BytesIO(data)).convert('RGBA')); marginal=[]
 for i,a in enumerate(actions):
  subset=copy.deepcopy(plugin);del subset['params']['actions'][i]
  _,less,_=renderer.render(subset)
  arr=np.asarray(Image.open(io.BytesIO(less)).convert('RGBA'));changed=np.any(arr!=rgba,axis=2)
  ys,xs=np.where(changed)
  marginal.append({'action_index':i,'changed_pixels_if_removed':int(changed.sum()),'bbox_xyxy':list(map(int,[xs.min(),ys.min(),xs.max()+1,ys.max()+1])) if len(xs) else None,'role':roles[i]})
  assert len(xs)>0,(q,i,'invisible action')
 save(d/'render_check.json',{'created_at_utc':now(),'schema_valid':True,'normalization_without_changes':True,'noop_matches_formal':True,
  'two_consecutive_offline_PNG_bytes_equal':True,'candidate_sha256':hashlib.sha256(data).hexdigest(),'repeat_sha256':hashlib.sha256(data2).hexdigest(),
  'pixel_sha256':pixels,'original_text_fill_view_canvas_snapshot_equal':before==after,'snapshots':{'before':before,'after':after},
  'per_action_visibility_ablations':marginal,'old_same_question_image_hashes':old_shas,'actual_candidate_native_view_status':'PENDING_MODEL_IMAGE_TOOL_VIEW; not inferred from renderer checks'})
 design={'question_id':q,'variant_id':variant,'branch':'SolidGeometry','stage':'material_refinement','created_at_utc':now(),'expected_wrong_answer':preset,
  'formal_correct_answer':e['formal_record']['answer'],'mechanism':mechanism,'material_difference':difference,'primary_math_proof_path':str(env.ROOT/q/'primary_math_proof.json'),
  'marker_roles':[{'action_index':i,'role':r} for i,r in enumerate(roles)],'candidate_png_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),
  'context_sha256':sha(d/'context.json'),'marker_path_bindings_sha256':sha(d/'marker_path_bindings.json'),'difference_audit_sha256':sha(d/'design_difference_audit.json'),
  'review_level':'PRIMARY_RESEARCH_ONLY; parent NEW independent review required; no approval/Pass/Collect/publication',
  'limits':['Two future observations do not prove mechanism, causal gain, statistics or marginal marker benefit.','No separate original controls were found; no repeated existing control is permitted.','Expected answer is immutable before both calls; incidental mentions or inconsistent final value/letter are misses.']}
 save(d/'design.json',design)
 print(json.dumps({'question_id':q,'variant_id':variant,'preset':preset,'actions':len(actions),'candidate_sha256':sha(d/'candidate.png'),'visible_pixels_each':[x['changed_pixels_if_removed'] for x in marginal]},ensure_ascii=False),flush=True)
if __name__=='__main__':
 selected=sys.argv[1:]
 for spec in specifications():
  if not selected or spec[0] in selected:render_one(spec)
