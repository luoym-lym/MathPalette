from bootstrap import HERE, PROJECT, TASK, renderer_setup
from audit import IDS, read, save, sha, eligibility, record, now
import copy
import gc
import hashlib
import itertools
import json
import math
import shutil
import sys
from fractions import Fraction
from pathlib import Path

PROOFS = {
 'Solid134': {
  'answer':'A',
  'derivation':'The three front widths w and full exterior heights H are equal; the shown water heights satisfy hII>hI>hIII>0. For the rectangular vases V=w*d*h. VI=VIII=4 implies dIII/dI=hI/hIII>1. VII/VI=3/4 gives dII/dI=(3/4)*(hI/hII)<3/4<1. Therefore dIII>dI>dII. A alone has this ordering; B has I>III>II, C has I>II>III, D has II>III>I and E has all equal. The source diagram is expressly ordinal: pixel lengths are not exact measurements. Existence for A: w=1, full H=6, water heights (4,5,3), depths (1,3/5,4/3) give volumes (4,3,4) and the shown orders. Thus A is both necessary and feasible. No minimum/maximum is asked.',
  'native':'Personally viewed original JPG, formal 768 PNG, old tested PNG and r61 candidate. All three full front rectangles remain equal; the water order II>I>III, gray region membership, Roman labels and all five plan-depth orders remain visible. The source graytone identities were normalized in the already-approved formal image; this task does not change that normalization. Six red strokes lie on existing boundaries, no added region/water surface.',
  'semantics':'Full exterior heights are the source; E plan depths are the receivers. Same red identifies a comparison of unlike dimension roles, not a numerical equality stipulation. This question asks about water volumes and front/top dimensions, not reproduction of printed ink. Reading a red boundary as physical vessel edging still supplies no new volume or dimension and cannot make E satisfy 4/3/4 at the unchanged water heights. It does not recolor the gray water regions or create paint-count targets. Width, identity and water order remain the governing data.',
  'roles':[
   'front0edge3: full exterior height of I, not its partial water height; first source of the equal-front-height comparison.',
   'front1edge3: full exterior height of II; necessary middle member despite its distinct water level and volume.',
   'front2edge3: full exterior height of III; completes the original three-vase source comparison.',
   'option4vase0edge1: E depth of I, receiver for its full front height; cross-view dimension transfer is the intended false step.',
   'option4vase1edge1: E depth of II, receiver for the middle source; 3 liters is not suppressed.',
   'option4vase2edge1: E depth of III, final receiver; I/III identities are retained rather than swapped.'
  ]},
 'Solid165': {
  'answer':'B',
  'derivation':'Independently take unit-cube vertices P=(0,0,0), Q=(0,1,1), R=(1,1,1), S=(1,1,0) by following the actual diagonal/edge incidences. At P, PQ=(0,1,1), PS=(1,1,0), dot=1 and norms=sqrt(2), hence angle60. At Q, QP=(0,-1,-1) and QR=(1,0,0) have dot0. At R, RQ=(-1,0,0) and RS=(0,0,-1) have dot0. At S, SR=(0,0,1) and SP=(-1,-1,0) have dot0. The original arcs choose these four nonreflex angles, so the sum is60+90+90+90=330, uniquely B. Screen angles and the planar quadrilateral theorem are inapplicable. No optimization is asked.',
  'native':'Personally viewed source JPG, formal PNG, old red-loop PNG and r61 blue-local-ray PNG. All four original arcs remain distinct, the three hidden cube edges remain dashed, and all existing edges/diagonals retain their endpoints. The short blue intervals touch R on the two true perpendicular cube edges and P on its two distinct-face diagonals. The rest of the path remains black, so this is not the old complete-loop image.',
  'semantics':'Two real ray pairs are compared. A blue pair is neither an equal-angle glyph nor a right-angle box; the old arc at P still selects the actual spatial60-degree angle. Any interpretation as colored edges changes appearance only, with the cube and its four marked angles fixed. No printed-pattern output or painted-target count is involved.',
  'roles':[
   'cube011_cube111 interval0.75..1: source RQ ray near R, on the upper cube edge.',
   'cube110_cube111 interval0.75..1: source RS ray near R, supplies the other side of the genuine square-face90-degree angle.',
   'diagPQ interval0..0.25: receiver PQ near P, first face diagonal, with the original P arc still readable.',
   'diagPS interval0..0.25: receiver PS near P, second face diagonal, making the local true60-degree pair. Together the receivers invite a false transfer of90, predicting360=D.'
  ]},
 'Solid218': {
  'answer':'D',
  'derivation':'Three unit square faces fold to a trihedral cube corner: D is z=0 with vertices(0,0,0),(1,0,0),(1,1,0),(0,1,0); C is x=0; B is y=1. At their common corner, the three square90-degree face angles fix pairwise perpendicular incident unit edges. A, E and F close the remaining half faces z=1, x=1, y=0. Their hypotenuses join U=(0,0,1), V=(1,0,0), W=(1,1,1); every pair has squared distance2, matching the equilateral G. The seven original faces are exactly the boundary of [0,1]^3 intersected with x-y+z<=1. Its only omitted cube vertex is T=(1,0,1). The removed tetrahedron TUVW has three mutually perpendicular unit legs from T, determinant absolute1, so volume1/6. The closed folded solid therefore has volume1-1/6=5/6, uniquely D. Reflecting the whole fold cannot alter volume. F is the surviving right-triangular half of y=0, NOT the removed triangular base itself; the omitted base is its congruent complement, both area1/2. The complete face construction, rather than old solver narratives about eight midpoint cuts, verifies the folding. No optimization is asked.',
  'native':'Personally viewed original JPG, formal PNG, old G-outline candidate and frozen r61 PNG. All A..G labels and all18 existing net segments are readable. C remains a complete square; F remains an isosceles right triangle with its black hypotenuse; G remains an equilateral triangle with all its edges black. Four red strokes form two open L portions on existing boundaries, with no added line, closed subregion, face, fold or partition.',
  'semantics':'C top/left unit edges are the square-area source; F top/left unit legs are the receiver. Both actual right-angle leg pairs have length1; identical color adds no area equality. The erroneous step is dropping the triangular1/2 in the corresponding corner-removal base, yielding1-1/3=2/3=B. This is a numerical volume question, so even a physical red-ink reading of the net does not change the folded solid or volume. No extra painted area or missing puzzle piece is inferred.',
  'roles':[
   'line_1: actual upper unit side of square C, horizontal member of the source L.',
   'line_15: actual left unit side of C, vertical source member; C enclosed area remains1.',
   'line_2: existing D/F shared unit boundary, horizontal leg of receiver F; does not add a fold.',
   'line_11: existing left unit leg of F, vertical receiver member; together with line_2 it encloses no new region and F area remains1/2.'
  ]},
 'Solid223': {
  'answer':'14',
  'derivation':'Fold the actual net about shared unit edges with face2 normal+z, face6 normal-x, face4 normal+x, face5 normal-z, face1 normal+y and face3 normal-y. Thus opposite pairs are(2,5),(6,4),(1,3). Each folded cube corner chooses exactly one face of each pair, and all2^3 choices occur. Triples and sums are (2,6,1):9,(2,4,1):7,(5,6,1):12,(5,4,1):10,(2,6,3):11,(2,4,3):9,(5,6,3):14,(5,4,3):12. This exhaustive enumeration proves maximum<=14 and the actual corner(5,6,3) attains14. The four red flat-net junctions are only(6,2,3):11,(2,4,3):9,(6,2,1):9,(2,4,1):7; their maximum11 is the predeclared wrong answer and omits seam-created corners. No minimum is requested.',
  'native':'Personally viewed original JPG, formal PNG, old largest-face-dot candidate and r61 PNG at native768. All six numerals1..6, all square boundaries and all free edges remain readable. Exactly four allowed red points are centered on existing flat three-face hinge junctions; none is a numeral, an interior face-selection dot or a newly created geometric vertex. The dots do not conceal which incident unit edges continue.',
  'semantics':'The marked local junction set is a genuine input subset for comparison against all folded corners; its claimed exhaustiveness is the intended error. Each mark identifies a different true three-face junction, so no arbitrary dot or count cap is used. The question asks for the largest sum at a corner of the cube, not at a red point. Even if dots were physical ink, they do not add numbers or restrict the quantified corners; the seam corner14 remains eligible. They add no cuts, fixed partition or equality condition.',
  'roles':[
   'r61_vertex_0 at(1,1): real junction6/2/3, local sum11 and highest member of the misleading flat subset.',
   'r61_vertex_1 at(2,1): real junction2/4/3, local sum9; completes the lower pair rather than selecting only large numbers.',
   'r61_vertex_2 at(1,2): real junction6/2/1, local sum9, upper left member of the complete flat-junction set.',
   'r61_vertex_3 at(2,2): real junction2/4/1, local sum7; completes that source subset irrespective of value.'
  ]}
}

def primary():
    angles=[]
    pts=[(0,0,0),(0,1,1),(1,1,1),(1,1,0)]
    for i,p in enumerate(pts):
        a=[pts[(i-1)%4][k]-p[k] for k in range(3)]
        b=[pts[(i+1)%4][k]-p[k] for k in range(3)]
        cosine=sum(x*y for x,y in zip(a,b))/math.sqrt(sum(x*x for x in a)*sum(y*y for y in b))
        angles.append(math.degrees(math.acos(cosine)))
    assert abs(sum(angles)-330)<1e-10
    corners=[{'faces':list(t),'sum':sum(t)} for t in itertools.product((2,5),(6,4),(1,3))]
    assert max(x['sum'] for x in corners)==14
    for q,p in PROOFS.items():
        a=next(x for x in read(TASK/'background_69_assignment.json')['questions'] if x['question_id']==q)
        report={'question_id':q,'variant_id':a['variant_id'],'frozen_created_at':a['frozen_created_at'],'expected_wrong_answer_unchanged':a['expected_wrong_answer'],'reviewed_at_utc':now(),'review_level':'Fresh PRIMARY screening only; not independent second review, original approval or Pass/Collect','original_unique_math':p['derivation'],'derived_answer':p['answer'],'agrees_with_formal':str(record(q)['answer'])==p['answer'],'native_actual_image_inspection':p['native'],'actual_viewed_paths':[str(PROJECT/'SolidGeometry'/record(q)['original_image']),str(PROJECT/'SolidGeometry'/record(q)['image']),str(Path(a['source_directory'])/'candidate.png')],'human_semantics':p['semantics'],'every_marker_roles':[{'action_index':i,'role':s} for i,s in enumerate(p['roles'])],'native_readability_pass':True,'no_false_relation_symbol_or_added_condition':True,'geometry_projection_visibility_text_semantic_fills_counts_preserved':True,'old_outcomes':{'Solid134':['A','B'],'Solid165':['180 degrees','C (345 degrees)'],'Solid218':['B (2/3)','D (5/6)'],'Solid223':['14','14']}[q],'old_own_preset_doublehit':False,'reuse_is_new_mechanism':False,'limits':['Primary assessment is not an independent review or a human performance study.','No original control is required or repeated; any two observations establish observed hits only, not causal gain.','Zero-call and fresh-render gates are separate and must pass before copying/testing.'],'numerical_verification':{'Solid165':{'angles':angles,'sum':sum(angles)},'Solid223':{'all_eight_corners':corners,'maximum':14},'Solid218':{'cube_volume':'1','removed_determinant':'1','removed_volume':str(Fraction(1,6)),'remaining_volume':str(Fraction(5,6))}}.get(q)}
        save(HERE/q/'primary_math_native_marker_review.json',report)
    print('Four fresh primary math/native/every-marker reports saved')

def local_replay(q):
    eligibility(q,'before_replay')
    a=next(x for x in read(TASK/'background_69_assignment.json')['questions'] if x['question_id']==q)
    source=Path(a['source_directory'])
    renderer_setup()
    from delivery_bridge_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    from partial_style import describe_paths
    from renderer_adapter import scene_png
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    config=read(PROJECT/'SolidGeometry/workbench/config.json')
    config['dataset_file']=str(PROJECT/'SolidGeometry/dataset.jsonl')
    adapter=RendererAdapter(config)
    c=adapter.inspect_question(q)
    assert c==read(source/'context.json'), 'Fresh complete context mismatch'
    save(HERE/q/'context_fresh.json',c)
    plugin=read(source/'plugin.json')
    renderer=PluginRenderer(config,adapter,{q:c})
    normalized=renderer.normalize(plugin)
    assert normalized==plugin, 'Schema/default normalization changes frozen plugin'
    save(HERE/q/'schema_default_normalization.json',{'normalized_equals_frozen_plugin':True,'schema_sha256':sha(PROJECT/'SolidGeometry/workbench/plugin.schema.json'),'plugin_sha256':sha(source/'plugin.json')})
    observed=[]; paths={}
    for i in range(3):
        # Third pass deliberately reloads serialized saved plugin for offline replay.
        if i==2:
            plugin=read(source/'plugin.json')
            assert renderer.normalize(plugin)==normalized
        s=adapter.scene(q)
        try:
            noop,ph=scene_png(s)
            assert ph==c['original_pixel_sha256']
            if i==0: (HERE/q/'noop.png').write_bytes(noop)
            with mpl.rc_context(s.settings): s.fig.canvas.draw()
            if i==0:
                for action in normalized['params']['actions']:
                    if action['type']=='set_object_style': paths[action['target']]=describe_paths(s,action['target'])
                    else: assert any(p['xy']==action['xy'] for p in c['snap_points'])
                assert paths==read(source/'path_bindings.json')
            before_objects=copy.deepcopy(s.objects); before_snaps=copy.deepcopy(s.snap_points)
            text=[(t.get_text(),t.get_position()) for t in s.ax.texts]
            patches=list(s.ax.patches); fills=[(type(p).__name__,str(p.get_facecolor())) for p in patches]
            with mpl.rc_context(s.settings): renderer.apply_actions(s,normalized)
            assert before_objects==s.objects and before_snaps==s.snap_points
            assert text==[(t.get_text(),t.get_position()) for t in s.ax.texts]
            assert fills==[(type(p).__name__,str(p.get_facecolor())) for p in patches]
            if q!='Solid223': assert all(p.get_facecolor()[3]==0 for p in s.ax.patches if p not in patches)
            png,pixel=scene_png(s)
            expected=source/'candidate.png'
            assert png==expected.read_bytes(), 'Offline candidate bytes mismatch'
            assert png==(source/'repeat.png').read_bytes()
            target=HERE/q/('fresh_render_'+str(i+1)+'.png' if i<2 else 'offline_replay.png')
            target.write_bytes(png)
            observed.append({'pass':i+1,'purpose':'offline disk-plugin replay' if i==2 else 'fresh deterministic draw','path':str(target),'sha256':hashlib.sha256(png).hexdigest(),'pixel_sha256':pixel,'no_op_pixel_sha256':ph,'source_byte_exact':True})
            del noop,png
        finally: s.close();plt.close('all');gc.collect()
    save(HERE/q/'fresh_render_replay_audit.json',{'question_id':q,'created_at':now(),'renderer_adapter':str(TASK/'delivery_bridge_adapter.py'),'approved_plugin_renderer':str(PROJECT/'SolidGeometry/workbench/mathvision_plugins.py'),'no_op_formal_pixel_equality':True,'fresh_context_all_fields_exact':True,'path_binding_exact':True,'schema_default_normalization_exact':True,'repeat_png_byte_identity':True,'offline_replay_byte_exact':True,'original_objects_snaps_text_fills_unchanged':True,'appearance_changes':renderer.appearance_changes(normalized),'renders':observed})
    print(q,'fresh no-op/schema/path/repeat/offline bytes exact',flush=True)

def copy_frozen(q):
    a=next(x for x in read(TASK/'background_69_assignment.json')['questions'] if x['question_id']==q)
    zero=read(HERE/q/'zero_prior_call_certification.json')
    primary=read(HERE/q/'primary_math_native_marker_review.json')
    replay=read(HERE/q/'fresh_render_replay_audit.json')
    assert zero['reuse_eligible'] and primary['agrees_with_formal'] and replay['offline_replay_byte_exact']
    eligibility(q,'before_copy')
    src=Path(a['source_directory']); dst=HERE/q/a['variant_id']
    dst.mkdir(exist_ok=False)
    copies=[]
    for name,expected in a['frozen_source_files_sha256'].items():
        source=src/name; target=dst/name
        assert sha(source)==expected
        shutil.copyfile(source,target)
        assert sha(target)==expected
        copies.append({'original_path':str(source),'copied_path':str(target),'original_sha256':expected,'copied_sha256':sha(target),'byte_identical':True})
    save(dst/'reuse_provenance.json',{'question_id':q,'variant_id_unchanged':a['variant_id'],'original_created_at_unchanged':a['frozen_created_at'],'original_wrong_preset_unchanged':a['expected_wrong_answer'],'copied_at_utc':now(),'source_unit':'background_61','source_files_immutable':True,'internal_original_paths_preserved':True,'new_mechanism_count':0,'copies':copies,'fresh_current_eligibility':str(HERE/q/'eligibility_before_copy.json'),'primary_math_native_every_marker':str(HERE/q/'primary_math_native_marker_review.json'),'whole_task_zero_call_certification':str(HERE/q/'zero_prior_call_certification.json'),'schema_normalization_repeat_exact_offline_replay':str(HERE/q/'fresh_render_replay_audit.json'),'candidate_new_design':False,'status':'Frozen never-called draft byte-copy for its first pair only; PRIMARY research, no approval/delivery'})
    print(q,'original frozen inputs copied byte-identically, identity/date/preset/internal paths preserved',flush=True)

def harness():
    source=TASK/'harness/quicktest3_isolated.py'
    data=source.read_bytes()
    old=b'PROJECT = Path(__file__).resolve().parents[3]'
    new=b'PROJECT = Path(__file__).resolve().parents[4]'
    assert data.count(old)==1
    result=data.replace(old,new)
    dest=HERE/'harness/quicktest3_isolated.py'
    dest.write_bytes(result)
    assert result.replace(new,old)==data
    save(HERE/'audits/harness_relocation_byte_diff.json',{'source':str(source),'source_sha256':sha(source),'destination':str(dest),'destination_sha256':sha(dest),'exact_only_byte_replacement':{'before':old.decode(),'after':new.decode(),'count':1},'reverse_substitution_byte_exact':True,'remote_payload_profile_system_model_thinking_tokens_timeout_credentials_logic_unchanged':True})
    print('Harness relocated with sole PROJECT ancestry correction; remote logic byte-exact')

if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='primary': primary()
    elif mode=='replay':local_replay(sys.argv[2])
    elif mode=='copy':copy_frozen(sys.argv[2])
    elif mode=='harness':harness()
