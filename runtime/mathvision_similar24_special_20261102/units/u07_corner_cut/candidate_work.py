from worker_env import *
import argparse
import difflib
import copy

QID='Plane245'
VARIANT='r01_fold_motion_to_square_aperture'
DIRECTORY=OWN/QID/VARIANT

MATH194={
 'question_id':'Plane194','unique_correct_answer':'E','method':'Independent exact fold-orbit enumeration, source JPG and formal PNG viewed at native scale',
 'coordinate_setup':'Original square [-1,1]^2; perpendicular half folds leave Q=[0,1]^2, up to orientation. Every removal unfolds by (u,v)->(s*u,t*v) for s,t in {-1,+1}. A straight corner clip meets both adjacent sides at positive distances a,b. Its cut segment has two nonzero components.',
 'exhaustive_four_cases':[
  {'quarter_corner':[1,1],'unfolded_removal':'Four separate right triangles at all four original outer corners','sample':'A','construction':'Remove (1-u)/a+(1-v)/b<1 near (1,1), with 0<a,b<1; reflect across both axes. The outer boundary is an octagon.'},
  {'quarter_corner':[0,1],'unfolded_removal':'Two V notches at opposite top and bottom side midpoints','sample':'B','construction':'Remove u/a+(1-v)/b<1 near (0,1); reflection in u=0 joins two half triangles into one V notch; reflection in v=0 creates its opposite.'},
  {'quarter_corner':[1,0],'unfolded_removal':'Two V notches at opposite left and right side midpoints','sample':'D','construction':'Remove (1-u)/a+v/b<1 near (1,0); reflect in v=0, then u=0.'},
  {'quarter_corner':[0,0],'unfolded_removal':'One central diamond or axis-diagonal rhombus hole','sample':'C','construction':'Remove u/a+v/b<1 near (0,0); unfolded hole |x|/a+|y|/b<1. For a=b its vertices are (+/-a,0),(0,+/-a).'}],
 'exclusion_of_E':'Only the centre-centre corner can make a bounded internal hole. That hole has four oblique sides with directions (+/-a,+/-b); no side is parallel to an original sheet edge when a,b>0. E has four axis-parallel inner sides, so is not that hole. The other three cases meet the outer boundary, and cannot make E either. All A/B/C/D have explicit constructions above. Thus E is uniquely impossible.',
 'freedom_preserved':'The final displayed clipped corner is an illustrative possible corner, not an additional restriction to one fold-corner type. All four corners were enumerated; no annotation may choose one as a new given.'}

MATH245={
 'question_id':'Plane245','unique_correct_answer':'B','source_JPG_and_formal_PNG_actually_viewed':True,
 'original_geometry':'First horizontal half fold sends the bottom half upward. Second vertical half fold sends the left half rightward. The remaining quarter has bottom and left folded edges, and top and right original outer edges. In the final displayed square o104, the absent lower-left vertex (17,7.75) is the intersection of both fold lines.',
 'exact_coordinates':'Let that centre vertex be (0,0), and normalize original half-side to L=3/2. The cut joins (0,3/4) to (3/4,0), so the removed quarter triangle is x>=0,y>=0,x+y<3/4. Reflecting across x=0 and y=0 gives |x|+|y|<3/4.',
 'shape':'A single central diamond hole with vertices (+/-3/4,0),(0,+/-3/4). The original four corners (+/-3/2,+/-3/2) survive, since each has |x|+|y|=3>3/4.',
 'all_choices':{'A':'Axis-aligned square aperture has horizontal/vertical sides, not reflected slanted cut edges. Impossible.',
 'B':'Intact outer square plus one central diamond aperture. Exactly the derived shape.',
 'C':'No central aperture, and entire outer boundary is a diamond inscribed in the original square. Source central cut cannot remove original corners.',
 'D':'No central aperture; four outside corner notches. These cannot arise from the central quarter vertex.',
 'E':'Correct central aperture but additional outside corner notches. Those corners are untouched by the cut.'},
 'uniqueness':'Only B has both the unchanged outer square and exactly the central diamond hole.',
 'color_readings':'All source paper boundaries, fold dashes, ghost corner traces and actual diagonal cut remain black. Only the destination halves of two conventional curved folding instruction arrows are colored. A colored arrow is an instruction on the diagram, not transported paper ink; the arrow visibly traverses the hinge and has an arrowhead. A itself has a colored square aperture, but is already impossible by geometry. Under a literal colored-edging reading of A, it remains impossible. B and the complete material source are unchanged, so the same B remains possible. No colored source physical edge is absent from B.'}

def prepare():
    DIRECTORY.mkdir(parents=True,exist_ok=True)
    e=eligibility(QID);write(DIRECTORY/'eligibility_before_design.json',e,True);assert e['eligible']
    write(OWN/'Plane194/mathematical_audit.json',MATH194,True)
    write(OWN/'Plane245/mathematical_audit.json',MATH245,True)
    config,adapter,metadata,renderer=setup_renderer()
    ctx=metadata[QID]
    assert json.loads(json.dumps(ctx))==read(OWN/QID/'context.json')
    write(DIRECTORY/'context.json',ctx,True)
    targets={t['id']:t for t in ctx['canvas']['targets']}
    path=targets['o114']['partial_paths'][0]
    actions=[];roles=[]
    for start,end,color,source_role,destination in [
      (27,51,'#DC2626','Destination-side half of the original first/upward folding arrow','Two vertical sides of A aperture'),
      (79,103,'#2563EB','Destination-side half of the original second/rightward folding arrow','Two horizontal sides of A aperture')]:
        for n in range(start,end+1):
            action={'type':'set_object_style','target':f'o{n}','color':color,'linewidth_pt':1.5}
            roles.append({'action_index':len(actions),'target':action['target'],'source_information':source_role,
                          'receiver':destination,'use':'Make the motion direction of this one continuous instruction arrow visible as the source of an erroneous aperture-edge orientation comparison. Each frozen renderer segment contributes to that connected visible arrow half.',
                          'not_material_content':True})
            actions.append(action)
    for n,color in [(0,'#2563EB'),(1,'#DC2626'),(2,'#2563EB'),(3,'#DC2626')]:
        action={'type':'set_object_style','target':'o114','color':color,'linewidth_pt':1.5,
                'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':n/4,'end':(n+1)/4,'wrap':False}}
        roles.append({'action_index':len(actions),'target':'o114','edge_index':n,
                      'source_information':'rightward second fold motion' if n%2==0 else 'upward first fold motion',
                      'receiver':'This existing horizontal aperture side' if n%2==0 else 'This existing vertical aperture side',
                      'use':'Pair an actual folding-motion direction with an axis-parallel candidate aperture edge. This is the intended false comparison: reflected cut edges remain diagonal, not parallel to the paper-motion directions.'})
        actions.append(action)
    submitted={'plugin_schema_version':'1.0.0','question_id':QID,'category':'C','operation':'C_manual',
               'description':'Compare the two folding-motion directions with square-aperture edge directions',
               'intent':'','params':{'actions':actions}}
    from render_plugins import check_schema
    schema=read(PROJECT/'PlaneGeometry/workbench/plugin.schema.json')
    renderer.schema=schema
    check_schema(submitted,schema,schema)
    normalized=renderer.normalize(submitted)
    assert normalized==submitted
    write(DIRECTORY/'plugin_submitted.json',submitted,True)
    write(DIRECTORY/'plugin.json',normalized,True)
    write(DIRECTORY/'marker_roles.json',roles,True)
    source_scene=adapter.scene(QID)
    from dataset_tools.mathvision_workbench import png_bytes
    from workbench_io import pixel_hash,environment_versions
    try:noop=png_bytes(source_scene)
    finally:source_scene.close()
    (DIRECTORY/'no_op.png').write_bytes(noop)
    assert pixel_hash(noop)==pixel_hash(PROJECT/'PlaneGeometry/image/Plane245.png')
    plugin,a,ph=renderer.render(normalized,frozen=True)
    plugin2,b,ph2=renderer.render(normalized,frozen=True)
    assert a==b and ph==ph2 and plugin==plugin2==normalized
    (DIRECTORY/'candidate.png').write_bytes(a)
    (DIRECTORY/'repeat.png').write_bytes(b)
    hist=read(OWN/'history_audit.json')
    old=next(h for h in hist if h['question_id']==QID)
    for d in old['history_index_entry']['designs']:
        assert sha(DIRECTORY/'candidate.png')!=d['frozen_candidate_png_sha256']
    differences={'current_reference':'Solid167 current C01: red/blue distinguish two concrete source features and their two candidate groups; current target A, not historical D.',
       'transfer':'Two source folding motions (rather than two cuts, since this source has only one cut) supply distinct vertical/horizontal direction information; two pairs of A existing aperture edges receive those colors.',
       'not_reusing_failed_design':'The old cut_vs_ghost_corner_edge_binding colors the actual diagonal cut o104 red and discarded vertical ghost o105 blue. This candidate leaves those and all source material edges black, and instead colors instruction arrows o27..o51 and o79..o103. Its new hypothesis is conflating folding motion with aperture-edge orientation, not including an uncut ghost edge as a hole boundary.',
       'old_complete_finals':'The old exact frozen image was tested twice, giving B/B against preset A; it is preserved and never resubmitted.',
       'same_wrong_letter':'A remains the prospective wrong shape, but the source information and error hypothesis are materially different. Same wrong letter alone is not treated as new design evidence.',
       'scope_authorization':'User-authorized transfer from current nine references; no cross-question failed PNG reuse.',
       'old_designs':old['history_index_entry']['designs'],
       'candidate_png_sha256':sha(DIRECTORY/'candidate.png')}
    write(DIRECTORY/'reference_transfer_and_history_difference.json',differences,True)
    design={'question_id':QID,'variant_id':VARIANT,'created_at':now(),'correct_answer':'B','expected_wrong_answer':'A',
       'expected_wrong_value':'A: an unchanged square outer boundary with one axis-aligned central square hole',
       'mechanism':'Treat the upward first folding motion and rightward second folding motion as the two directions of the final aperture boundary. Red pairs the first/upward instruction-arrow destination half with the two vertical A aperture sides; blue pairs the second/rightward arrow destination half with the two horizontal A aperture sides. This predicts the axis-aligned square aperture A instead of reflecting the actual diagonal cut into the central diamond B.',
       'mathematical_proof':MATH245,'marker_roles':roles,'reference_and_novelty':differences,
       'schema_action_count':len(actions),'logical_information_groups':4,
       'human_semantics':'Arrow destination halves are conventional operation indicators, not paper markings. The source physical paper and cut are unchanged. Wrong sample A remains geometrically impossible whether its color is a comparison highlight or intrinsic ink; unchanged B is still uniquely possible.',
       'image_sha256':sha(DIRECTORY/'candidate.png'),'plugin_sha256':sha(DIRECTORY/'plugin.json'),
       'status':'FROZEN_PRESET_BEFORE_BOTH_CALLS_PRIMARY_ONLY','fresh_independent_second_review_required':True}
    write(DIRECTORY/'design.json',design,True)
    write(DIRECTORY/'render_check.json',{'checked_at':now(),'fresh_schema_sha256':sha(PROJECT/'PlaneGeometry/workbench/plugin.schema.json'),
       'normalization_exact':normalized==submitted,'source_noop_pixels_equal':True,'source_noop_bytes_equal':noop==(PROJECT/'PlaneGeometry/image/Plane245.png').read_bytes(),
       'two_candidate_bytes_equal':True,'candidate_png_sha256':sha(DIRECTORY/'candidate.png'),'candidate_pixel_sha256':ph,
       'context_sha256':sha(DIRECTORY/'context.json'),'design_sha256':sha(DIRECTORY/'design.json'),'plugin_sha256':sha(DIRECTORY/'plugin.json'),
       'environment':environment_versions(),'independent_process_replay':'PENDING'},True)
    print(json.dumps({'prepared':str(DIRECTORY),'actions':len(actions),'candidate_sha256':sha(DIRECTORY/'candidate.png')},ensure_ascii=False))

def replay():
    config,adapter,metadata,renderer=setup_renderer()
    plugin=read(DIRECTORY/'plugin.json')
    from render_plugins import check_schema
    schema=read(PROJECT/'PlaneGeometry/workbench/plugin.schema.json');renderer.schema=schema
    check_schema(plugin,schema,schema)
    assert renderer.normalize(plugin)==plugin
    assert json.loads(json.dumps(metadata[QID]))==read(DIRECTORY/'context.json')
    p,data,pix=renderer.render(plugin,frozen=True)
    assert data==(DIRECTORY/'candidate.png').read_bytes()
    (DIRECTORY/'independent_process_replay.png').write_bytes(data)
    write(DIRECTORY/'independent_process_replay.json',{'at':now(),'pid':os.getpid(),'fresh_process':True,'schema_and_defaults_exact':True,
       'exact_JSON_normalized_context_equal':True,'exact_candidate_bytes_equal':True,'png_sha256':sha(DIRECTORY/'candidate.png'),'pixel_sha256':pix,
       'plugin_sha256':sha(DIRECTORY/'plugin.json'),'design_sha256':sha(DIRECTORY/'design.json'),'source_still_eligible':eligibility(QID)},True)
    print('Independent process exact replay passed')

def copy_harness():
    original=OLD/'harness/quicktest3_isolated.py';dst=OWN/'harness/quicktest3_isolated.py'
    a=original.read_bytes();old=b'PROJECT = Path(__file__).resolve().parents[3]'
    new=('PROJECT = Path('+repr(str(PROJECT))+')').encode('utf-8')
    assert a.count(old)==1
    cache_old=b'HARNESS = Path(__file__).resolve().parent'
    cache_new=('HARNESS = Path('+repr(str(OWN/'ownruntime/harness_cache'))+')').encode('utf-8')
    assert a.count(cache_old)==1
    b=a.replace(old,new).replace(cache_old,cache_new)
    assert b.replace(new,old).replace(cache_new,cache_old)==a
    dst.parent.mkdir(exist_ok=True);dst.write_bytes(b)
    write(OWN/'harness/copy_audit.json',{'at':now(),'original_path':str(original),'original_sha256':sha(original),
          'copied_sha256':sha(dst),'only_PROJECT_and_local_cache_location_changed':True,'reverse_replacement_byte_equal':True,
          'remote_payload_modified':False,'diff':''.join(difflib.unified_diff(a.decode().splitlines(True),b.decode().splitlines(True),fromfile=str(original),tofile=str(dst)))},True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['prepare','replay','copy-harness']);args=p.parse_args()
    {'prepare':prepare,'replay':replay,'copy-harness':copy_harness}[args.mode]()
