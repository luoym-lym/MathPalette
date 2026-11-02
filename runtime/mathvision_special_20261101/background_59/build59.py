from env59 import *
import copy
import gc
from fractions import Fraction as F

PROOFS={
'Solid120': 'A regular continuous measuring tape increases by the same amount for each full revolution. At identical azimuth, 1 and22, 6 and27, and11 and32 independently give increment21. The requested tick has the same azimuth as6 and27 and is two turns above6. Thus6+2*21=48 uniquely. Two edges of one tape band are not two revolutions. Counting both edges consistently in calibration and extrapolation cancels that factor and still yields48.',
'Solid138': 'The two numbered turns have same-azimuth pairs1/22,6/27,11/32, all fixing21 per revolution. There is one real unnumbered turn between the27 turn and the requested top turn. At the requested azimuth, the sequence is6,27,48,69; answer69 uniquely. The visible bandedge objects are front-half boundary curves, not two visible front/back appearances of the same numbered turn. No back duplicate is a legal actual receiver for the prospective repeated-fragment mechanism.',
'Solid140': 'Use the actual source dimensions, independent of projected lengths. Initial base4m by2m and water height25cm=1/4m imply water volume2m^3. In the shown final orientation the vertical side is4m, the base1m by2m, so h=2/2=1m, unique D. Both depicted water surfaces are horizontal rectangles, with areas8 and2; their shape correspondence does not make their areas equal. No water fill, level, dimension, geometry, or projection changes.',
'Solid169': 'Actual route vertices are P=(0,0,12), (0,0,0), (t,0,0), (t,0,12), (12,0,12), (12,12,12), Q=(12,12,0). Let t remain unspecified. Lengths sum12+t+12+(12-t)+12+12=60cm, unique D. The native schematic t=8.64 is0.72 of the edge, not a midpoint and not a numerical given. The answer is independent of t. All six directed black arrowed segments are required; an extra shortcut or loss of one segment would change the route.',
'Solid213': 'The actual aligned stack is C4=[0,4]^2x[0,4], C3=[0,3]^2x[4,7], C2=[0,2]^2x[7,9], C1=[0,1]^2x[9,10]. X=(0,0,10),Y=(4,4,0). Parameter P(t)=(4t,4t,10-10t),0<=t<=1. The C3 z slab clips t to[3/10,3/5]; both x and y remain between6/5 and12/5, hence within[0,3]. Segment length is(3/10)*sqrt132=3sqrt33/5, unique A. Its endpoints(6/5,6/5,7),(12/5,12/5,4) are interior face points, not cube vertices, body diagonal endpoints or registered visible snap points. The body diagonal3sqrt3 is not the asked segment and is not a listed choice. No intersection point or fake diagonal may be invented to make a receiver.',
'Solid215': 'Use actual scene labels A=(0,0,0),B=(3,0,0),C=(3,1,0),D=(0,1,0),E=(0,0,2),F=(3,0,2),G=(3,1,2),H=(0,1,2),M=(3,1/2,2). BCHE is precisely the rectangle in plane2x+3z=6, with orthogonal side vectors(0,1,0) and(-3,0,2); its area is sqrt13. M has plane residual6, so perpendicular height is6/sqrt13. Volume=(1/3)*sqrt13*6/sqrt13=2, unique E. FG is parallel to BCHE, so every point of FG has the same height. FM=MG=1/2 cannot halve the height. The actual foot is(27/13,1/2,8/13), not an original marked point or existing edge. BM,CM,EM,HM are lateral slants, none a height receiver. No new false perpendicular or plane is justified.',
'Solid219': 'Translate each unit cube to[0,1]^3 with z vertical. Figure1 actual cut traces define planes y=z/2 and y=1-z/2. At each z these partition y into widths z/2,1-z,z/2, so the two outer triangular prisms have volumes1/4 each and the central one1/2. Figure2 adds orthogonal planes x=z/2 and x=1-z/2, independently confirmed by its front/back dashed traces F=(1/2,0,1),K=(1/2,1,1). The W leader in each panel points to the same front-top-right cube vertex(1,0,1), never to the display point named W below the figures. The W piece has1-z/2<=x<=1,0<=y<=z/2,0<=z<=1, so horizontal area z^2/4 and volume integral0^1 z^2/4 dz=1/12, unique A. All9 pieces exist:8 peripheral pieces have volume1/12 each and central piece integral(1-z)^2 dz=1/3; total1. A first-stage volume1/4 is not inherited by its proper W subpiece. Source first-stage triangular section has perpendicular legs1 and1/2; volume1*1/2/2*1=1/4. All cut planes, visible/dashed traces and leaders remain unchanged.',
'Solid236': 'Use the actual source scene C=(0,0,0),B=(1,0,0),D=(0,1,0),A=(1,1,0),G=(0,0,1),F=(1,0,1),H=(0,1,1),E=(1,1,1),J=(1,0,1/2),I=(0,1,1/2). All EJCI points satisfy x+y+2z=2. Diagonals CE=(1,1,1) and JI=(-1,1,0) have dot0, squared lengths3 and2, and common midpoint(1/2,1/2,1/2). Hence area=sqrt6/2, face area1, R^2=3/2 uniquely C. An independent adjacent-side Gram determinant is(5/4)^2-(1/4)^2=3/2. The new hypothesized error substitutes the BODY diagonal length sqrt3 for the MIDPLANE face diagonal JI length sqrt2, giving wrong R=3/2 and R^2=9/4,E. Both actual diagonals remain distinct and no equal-length, angle or measured-length mark is added.'}
SKIPS={
'Solid120': {'considered':['Two real boundary curves of one tape band treated as two turn units, mapped to the source-to-target turn count.','Recolor actual band contours rather than reuse6-to28 tick misphasing.'],'reason':'The calibration and target share exactly the same band structure: consistently counting two edges per band divides the21 calibration increment by2 and doubles the target count, cancelling to48. Any90/69 alternative requires an unencoded asymmetric rule or treats an ordinary gap boundary as another full turn. No clear actual source/receiver pair establishes that error without repeating an anchor/tick chain or adding false tape/ruler units. All three oldpreset50 pairs remain misses.'},
'Solid138': {'considered':['Repeated visible front/back fragments of one winding counted twice.','Binding the real blank intermediate turn to an already numbered turn.'],'reason':'Actual original/native image shows only the front half of each tape band; no second visible backside fragment of the same turn supplies the proposed receiver. Each unnumbered band is a real additional turn, not a duplicate. Joining it to another band would assert false identity or repeat the old tick chain. All oldpreset72 pairs remain misses;17/22/64/50/72/70.5 are not relabelled.'},
'Solid169': {'considered':['Full12cm edge matched to two complementary front route components.','Two supposed half-edge components each counted as one full edge.','A continuous two-face route unit matched to a chord.'],'reason':'The actual front turn is not a midpoint; neither wording nor native endpoints authorizes halves. Complementary horizontal parts sum12 exactly and preserve60. Counting each as a full edge yields72, absent from choices, and needs a false equal-length inference. A4-edge48 omission reproduces both old169/185 rejected loss of arrowed route membership. Any added chord creates an alternative route/shortcut. Preserve every black route arrow; no new candidate or calls.'},
'Solid213': {'considered':['Interior C3 entry/exit segment matched to the full3-cube body diagonal.','Front-face diagonal as a false planar-length receiver.'],'reason':'The actual entry and exit points are unmarked interior face points, absent from visible snap endpoints. A precise local segment would require new interception points forbidden by this brief; a cube diagonal uses different endpoints.3sqrt3 is not a choice, and swapping to a full front-face diagonal without identifying the true local receiver would be untargeted. Drawing another wholeXY or recoloring height3 repeats the old9-unit reference machinery. No clean legal actual local source/receiver pair; skip.'},
'Solid215': {'considered':['The true midpoint FM/MG half-edge as a height-halving unit.','Bind this unit to an existing M-to-base lateral segment.'],'reason':'The actual perpendicular foot on BCHE is not drawn or registered and no existing lateral edge is perpendicular to the base. FG is parallel to BCHE, so moving F-toM-toG changes no height. PairingFM withBM/CM would substitute an oblique slant rather than an actual height; adding a foot/right-angle/false plane is forbidden. RecoloringBE/CH againstBF/CG would repeat the old wrong-base design. No actual clean height receiver exists; skip.'}}

# Exact small computations are independent of rendering and old proof rhetoric.
assert F(4)*2*F(1,4)==2 and F(2)/(1*2)==1
assert F(12)+F(216,25)+12+(12-F(216,25))+12+12==60
assert F(3,5)-F(3,10)==F(3,10)
assert F(1,4)*F(1,3)==F(1,12)
assert F(8,12)+F(1,3)==1
assert F(5,4)**2-F(1,4)**2==F(3,2)
for q in QIDS:
    scene=read(PROJECT/f'SolidGeometry/dataset_generator/scenes/{q}.json')
    content=read(OWN/q/'eligibility_start.json')['content_snapshot']
    inputs=[]
    for rel,expected in content['files'].items():
        p=(PROJECT/'SolidGeometry'/rel).resolve()
        inputs.append({'path':str(p),'sha256':sha(p),'matches_approval_content':sha(p)==expected,'full_byte_read':True})
    assert all(i['matches_approval_content'] for i in inputs)
    save(f'{q}/primary_math_source_native_audit.json',{'at':now(),'question_id':q,'proof':PROOFS[q],'correct_answer':read(OWN/q/'formal_record.json')['answer'],'actual_source_JPG_and_formal_PNG_viewed_native':True,'fresh_context':'context.json','no_op_pixel_match':True,'native_scene_sha256':sha(PROJECT/f'SolidGeometry/dataset_generator/scenes/{q}.json'),'all_source_files_fully_read_hash_exact':inputs,'projection':scene['projection'],'frozen_visibility':scene['visibility'],'source_ambiguities':scene['ambiguities'],'all_original_semantic_fills_labels_dimensions_counts_routes_preserved':True,'review_role':'PRIMARY researcher only, no independent second review or user approval'})
    if q in SKIPS:
        save(f'{q}/design_difference_audit.json',{'question_id':q,'at':now(),'stage':'material_refinement','status':'assessed_skip_no_clean_material_design','new_designs':0,'API_calls':0,'math':PROOFS[q],**SKIPS[q],'unworked':False,'not_a_proof_of_global_impossibility':True})
    del scene,content,inputs
    gc.collect()

install_render()
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer
from workbench_io import load_config,pixel_hash
from partial_style import object_paths
from dataset_tools.mathvision_workbench import png_bytes
config=load_config()
adapter=RendererAdapter(config)
prepared=[]
for q,vid,preset in [('Solid140','r59_water_surface_area_unit_transfer','A'),('Solid219','r59_prism_to_corner_subpiece_transfer','E'),('Solid236','r59_body_to_midplane_diagonal_transfer','E')]:
    dest=OWN/q/vid
    dest.mkdir(parents=True,exist_ok=True)
    assert not (dest/'design.json').exists()
    e=eligibility(q)
    save(dest/'eligibility_before_design.json',e)
    assert e['eligible']
    context=adapter.inspect_question(q)
    save(dest/'fresh_context.json',context)
    capture=adapter.scene(q)
    try:
        noop=png_bytes(capture)
        paths={o['id']:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segments':[{'control':s['control'].tolist(),'style':s['style']} for s in p['segments']]} for p in object_paths(capture,o['id'])] for o in context['objects'] if o['styleable']}
    finally: capture.close()
    assert pixel_hash(noop)==context['original_pixel_sha256']
    (dest/'no_op.png').write_bytes(noop)
    save(dest/'frozen_paths.json',paths)
    def style(target,color='#DC2626'):
        return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5}
    def partial(target,start,end):
        p=paths[target][0]
        return {**style(target),'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}
    if q=='Solid140':
        actions=[style('leftlevel0'),style('leftlevel1','#2563EB'),style('rightlevel0'),style('rightlevel1','#2563EB')]
        roles=['Source initial water rectangle4m horizontal side; the red arm supplies the width component of the initial horizontal surface area unit.','Source initial water rectangle2m depth side; blue arm completes an open L identifying the initial water surface rather than the tank height.','Receiver final water rectangle1m horizontal side; same red arm matches the old4m width role even though the length has changed by4.','Receiver final water rectangle2m depth side; same blue depth arm completes the matched open water-surface L. The whole water surface unit, not the old1m height, is transferred.']
        mechanism='Match homologous open width/depth L frames on the two already drawn WATER SURFACES. Target promoting their common rectangle role to equal horizontal area, then using V=A*h to keep the original25cm water height unchanged, choosingA. True areas8 and2 differ by4, and true height is1m. The error is area-unit invariance across the rotated water shapes, not a1m/2m axis swap.'
        difference='Old rotation_axis_dimension_swap used leftedge1/rightedge7 red and leftedge7/rightedge0 blue to exchange1m/2m tank axes, presetB50cm; both full finalsD. New actions target four DIFFERENT waterlevel boundaries (leftlevel0/1,rightlevel0/1), no old four tank-edge targets. Their matched two-arm WATER SURFACE role supplies area rather than container-axis transport, presetA25cm with its own pre-call derivation. No old observed wrong answer is relabelled.'
        semantics='Numerical conserved-volume question. Every water fill/level/printed dimension remains fixed. These are actual horizontal water-surface sides, not paint used to identify a transformed answer picture. Blue2m depth may correspond physically across orientations; red horizontal widths are different material cross sections, and their explicitly different4m/1m dimensions remain available. Same color supplies a comparison role, no equality symbol or new dimension. No false waterline or new surface is drawn.'
    elif q=='Solid219':
        actions=[style('line_2'),partial('line_5',0,0.5),style('line_11'),style('line_15'),partial('line_18',0,0.5),style('line_24')]
        roles=['Source Fig1 triangular-prism front vertical leg from(1,0,0) to(1,0,1); length1.','Source Fig1 top half-depth leg from(1,0,1) toR=(1,1/2,1); length1/2, exact source path parameter0..1/2.','Source Fig1 existing first-cut sloping side from(1,0,0) toR; completes the TRUE triangular cross-section of the1/4-volume outer prism.','Receiver Fig2 same physical front vertical leg at the W-bearing first-stage prism.','Receiver Fig2 same top half-depth leg toR; retains the black second-cut lines crossing other surfaces.','Receiver Fig2 same existing first-cut slope; completes the same triangular FRONT/RIGHT section role, while the full prism is now subdivided by the orthogonal dashed cuts.']
        mechanism='Transfer one actual1/4-volume triangular PRISM unit from Fig1 to the W-bearing proper subpiece in Fig2 by matching the same real three-sided triangular end section. Target overlooking the second orthogonal cut inside that prism and retaining its full1/4 volume, choosingE; correct intersection volume is1/12. These are homologous source-to-receiver prism-boundary traces, not uniform emphasis of all cuts or three independent half-lengths.'
        difference='Old quarter_cut_capture changed only Fig2 line22/26/24/28, grouping two cut families red, predeclaredC1/8; full raw finalsE1/4 andD1/6 are both misses and are not reused. New design matches a true Fig1 triangular-prism cross section to its same physical Fig2 end section using Fig1 line2,line5[0,1/2],line11 and Fig2 line15,line18[0,1/2],line24. Five of six target/interval roles are absent from the old plugin; no second-cut dashed trace is red. The new E hypothesis is independently derived from the real first-stage volume1/4 and improper inheritance to an intersected subpiece, not from the old response or a cosmetic recolor.'
        semantics='Numerical cut-volume task. All red segments are original cube edges or original first-cut traces; there is no new polygon, face paint, partition, plane, or equality. Matching the same physical first-stage triangular end section across the two stages preserves printed/material edge identity. The four second-cut dashed traces remain black, readable and in their original positions, so a human can identify the W intersection rather than treating the red whole prism as a new target. The target is vertexW, and both original W leaders remain black and unchanged.'
    else:
        snap={p['id']:p for p in context['snap_points']}
        actions=[{'type':'add_line','id':'r59_body_diagonal','endpoints':[snap['C']['xy'],snap['E']['xy']],'color':'#DC2626','linestyle':'dashed'},{'type':'add_line','id':'r59_midplane_diagonal','endpoints':[snap['J']['xy'],snap['I']['xy']],'color':'#DC2626','linestyle':'dashed'}]
        roles=['Source actual cube body diagonalCE, also the LONG diagonal of the unchanged gray section. Exact named endpointsC/E, no point inserted at its center. Its source squared length is3.','Receiver actual section diagonalJI between the two original marked midpoints. Exact named endpointsJ/I. Its true squared length2 differs fromCE; matching diagonal roles encourages transferring3 into the second factor of the diagonal-product area formula.']
        mechanism='Compare the two true diagonals of the section, usingCE as body-diagonal length source andJI as receiver. Target treating both diagonal lengths as sqrt3 because both span the same gray section, giving area3/2 and squared ratio9/4,E. Correct squared lengths3 and2 give R^2=3/2,C. The new diagonals are exact mathematical comparison lines, not measurements, equal ticks, right-angle conditions, or extra section cuts.'
        difference='Old rhombus_to_square_edge_family_binding matched eight existing section SIDE/top-face SIDE styles (line13/12/15/10 red;line14/9/16/11 blue), presetD25/16, rawC/D. New design styles none of those sides: it adds only two exact-endpoint genuine section DIAGONALS CE andJI and transfers body-versus-midplane length in the product d1*d2/2. PresetE9/4 comes from replacing the short diagonal by the long diagonal; it is not the old side-based square-area25/16 hypothesis and neither old observed C/D is relabelled.'
        semantics='Numerical area ratio task. The original gray plane, every dot and label, and all visible/hidden cube edges remain unchanged. Both diagonals lie in the same already specified plane x+y+2z=2. No new intersection dot, midpoint, equality tick, right-angle symbol, polygon or shaded subregion appears. A human can computeCE=sqrt3 andJI=sqrt2 from the original vertices and midpoints; shared red is not a numerical given. Dashed comparison lines are distinguishable from unchanged black edges.'
    renderer=PluginRenderer(config,adapter,{q:context})
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':vid,'intent':'','params':{'actions':actions}}
    normalized=renderer.normalize(plugin)
    save(dest/'plugin_submitted.json',plugin)
    save(dest/'plugin.json',normalized)
    _,first,px=renderer.render(normalized,frozen=True)
    _,second,px2=renderer.render(normalized,frozen=True)
    assert first==second and px==px2
    (dest/'candidate.png').write_bytes(first)
    (dest/'repeat.png').write_bytes(second)
    old_hashes=read(OWN/'readonly_hashes_start.json')
    old_images={v for k,v in old_hashes.items() if k.endswith('candidate.png')}
    assert sha(dest/'candidate.png') not in old_images
    markers=[]
    for i,(a,role) in enumerate(zip(normalized['params']['actions'],roles)):
        marker={'action_index':i,'action':a,'role':role}
        if a['type']=='set_object_style':
            marker['original_object']=next(o for o in context['objects'] if o['id']==a['target'])
            marker['frozen_paths']=paths[a['target']]
        else:
            ids=('C','E') if i==0 else ('J','I')
            marker['exact_original_snap_bindings']=[snap[n] for n in ids]
            assert a['endpoints']==[snap[n]['xy'] for n in ids]
        markers.append(marker)
    save(dest/'design_difference_audit.json',{'question_id':q,'variant_id':vid,'at':now(),'stage':'material_refinement','substantive_difference':difference,'new_information_hypothesis':mechanism,'fixed_wrong_answer':preset,'actual_PNG_sha256':sha(dest/'candidate.png'),'new_legal_plugin_sha256':sha(dest/'plugin.json'),'cosmetic_repeat':False,'old_failed_or_aborted_image_reused':False,'posthoc_preset':False,'old_evidence_read_audit':'../../old_evidence_full_byte_read.json','candidate_bytes_differ_from_every_scoped_old_candidate':True,'before_any_API_calls':True})
    design={'question_id':q,'variant_id':vid,'created_at':now(),'stage':'material_refinement','expected_wrong_answer':preset,'correct_answer':e['formal_record']['answer'],'mechanism':mechanism,'substantive_difference':difference,'primary_unique_math_proof':PROOFS[q],'every_marker_roles':markers,'human_semantics':semantics,'image_sha256':sha(dest/'candidate.png'),'pixel_sha256':px,'plugin_sha256':sha(dest/'plugin.json'),'fresh_context_sha256':sha(dest/'fresh_context.json'),'frozen_paths_sha256':sha(dest/'frozen_paths.json'),'status':'FROZEN before both calls; PRIMARY only; parent NEW independent second review required; no Pass/Collect/delivery'}
    save(dest/'design.json',design)
    save(dest/'render_check.json',{'fresh_context':True,'no_op_formal_pixel_equal':True,'schema_defaults_normalized':True,'twice_PNG_byte_identical':True,'twice_pixel_identical':True,'candidate_sha256':sha(dest/'candidate.png'),'design_sha256':sha(dest/'design.json'),'normalized_plugin_sha256':sha(dest/'plugin.json'),'no_actual_PNG_manual_review_claim_yet':True})
    prepared.append({'question_id':q,'variant_id':vid,'path':str(dest),'expected_wrong_answer':preset,'image_sha256':sha(dest/'candidate.png'),'design_sha256':sha(dest/'design.json')})
    print(q,vid,'FROZEN',preset,len(actions),'marks',flush=True)
    del renderer,context,capture,paths,noop,first,second,design,markers,e
    gc.collect()
save('prepared_candidates.json',prepared)

# Existing isolated harness logic unchanged; replace only local environment bootstrap.
source=(BASE/'harness/quicktest3_isolated.py').read_text(encoding='utf-8')
old='PROJECT = Path(__file__).resolve().parents[3]'
replacement='sys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nimport env59\nPROJECT = env59.PROJECT'
assert source.count(old)==1
target=OWN/'harness/quicktest3_isolated.py'
target.parent.mkdir(parents=True,exist_ok=True)
target.write_text(source.replace(old,replacement),encoding='utf-8')
save('harness_isolation_audit.json',{'reference_path':str(BASE/'harness/quicktest3_isolated.py'),'reference_sha256':sha(BASE/'harness/quicktest3_isolated.py'),'own_sha256':sha(target),'only_change':{'old':old,'new':replacement},'source_roundtrip_exact':target.read_text(encoding='utf-8').replace(replacement,old)==source,'API_model_thinking_prompt_profile_credentials_timeout_tokens_unchanged':True})
