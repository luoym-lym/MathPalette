from worker_env import *
from candidate_work import MATH194,MATH245
import argparse
import copy

p=argparse.ArgumentParser();p.add_argument('question',choices=['Plane194','Plane245']);p.add_argument('mode',choices=['prepare','replay']);a=p.parse_args()
qid=a.question
variant={'Plane194':'r02_discarded_legs_to_square_aperture','Plane245':'r02_discarded_legs_to_extra_outer_notches'}[qid]
directory=OWN/qid/variant

def prepare():
    directory.mkdir(parents=True,exist_ok=True)
    e=eligibility(qid);assert e['eligible'];write(directory/'eligibility_before_design.json',e,True)
    config,adapter,metadata,renderer=setup_renderer();ctx=metadata[qid]
    assert json.loads(json.dumps(ctx))==read(OWN/qid/'context.json')
    write(directory/'context.json',ctx,True)
    targets={t['id']:t for t in ctx['canvas']['targets']}
    source_vertical,source_horizontal=('o7','o6') if qid=='Plane194' else ('o105','o106')
    receiver='o14' if qid=='Plane194' else 'o125'
    edges=[(0,'#2563EB'),(1,'#DC2626'),(2,'#2563EB'),(3,'#DC2626')] if qid=='Plane194' else [
        (1,'#DC2626'),(2,'#2563EB'),(4,'#2563EB'),(5,'#DC2626'),
        (7,'#DC2626'),(8,'#2563EB'),(10,'#2563EB'),(11,'#DC2626')]
    n_edges=4 if qid=='Plane194' else 12
    path=targets[receiver]['partial_paths'][0]
    actions=[{'type':'set_object_style','target':source_vertical,'color':'#DC2626','linewidth_pt':1.5},
             {'type':'set_object_style','target':source_horizontal,'color':'#2563EB','linewidth_pt':1.5}]
    roles=[{'action_index':0,'target':source_vertical,'source_information':'Existing vertical dashed ghost leg of the already removed triangular corner, not a surviving cut edge',
             'receiver':'Vertical E aperture sides' if qid=='Plane194' else 'Four vertical sides of E outer corner notches',
             'use':'Separate the removed original corner trace from the actual black diagonal cut. The intended false transfer treats this discarded trace as a resulting aperture/outer-notch boundary.'},
           {'action_index':1,'target':source_horizontal,'source_information':'Existing horizontal dashed ghost leg of the already removed triangular corner, not a surviving cut edge',
             'receiver':'Horizontal E aperture sides' if qid=='Plane194' else 'Four horizontal sides of E outer corner notches',
             'use':'Supply the second perpendicular discarded-edge direction for the same false boundary-role transfer.'}]
    for edge,color in edges:
        actions.append({'type':'set_object_style','target':receiver,'color':color,'linewidth_pt':1.5,
           'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':edge/n_edges,'end':(edge+1)/n_edges,'wrap':False}})
        roles.append({'action_index':len(actions)-1,'target':receiver,'edge_index':edge,
           'source_information':'Vertical discarded ghost leg' if color=='#DC2626' else 'Horizontal discarded ghost leg',
           'receiver':'This existing E aperture edge' if qid=='Plane194' else 'This existing E corner-notch edge',
           'use':'Concrete direction and removed-boundary role comparison. The pairing is a proposed false correspondence, not a new cut operation or an asserted equality.'})
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
      'description':'Compare discarded corner traces with existing candidate cut boundaries','intent':'','params':{'actions':actions}}
    from render_plugins import check_schema
    schema=read(PROJECT/'PlaneGeometry/workbench/plugin.schema.json');renderer.schema=schema
    check_schema(plugin,schema,schema);assert renderer.normalize(plugin)==plugin
    write(directory/'plugin_submitted.json',plugin,True);write(directory/'plugin.json',plugin,True)
    write(directory/'marker_roles.json',roles,True)
    from dataset_tools.mathvision_workbench import png_bytes
    from workbench_io import pixel_hash,environment_versions
    scene=adapter.scene(qid)
    try:noop=png_bytes(scene)
    finally:scene.close()
    (directory/'no_op.png').write_bytes(noop)
    original=PROJECT/'PlaneGeometry/image'/f'{qid}.png'
    assert pixel_hash(noop)==pixel_hash(original)
    np,data,pix=renderer.render(plugin,frozen=True);np2,again,pix2=renderer.render(plugin,frozen=True)
    assert data==again and np==np2==plugin and pix==pix2
    (directory/'candidate.png').write_bytes(data);(directory/'repeat.png').write_bytes(again)
    prior=[]
    for designpath in (OWN/qid).glob('*/design.json'):
        d=read(designpath);prior.append({'path':str(designpath),'sha256':sha(designpath),'image_sha256':d['image_sha256']})
        assert sha(directory/'candidate.png')!=d['image_sha256']
    semantics='Source color is confined to two dashed legs lying strictly in the removed corner except their cut endpoints. They outline absent/discarded material, not the surviving sheet. The actual diagonal cut and all surviving material boundaries remain black. Even a physical-color reading of those discarded edges leaves no finite colored surviving edge to transport. E alone receives new color, and E is already geometrically impossible; other samples, including the unique correct one, remain unmodified. No source fold/cut count, crease style, fill, or option geometry changes.'
    proof=copy.deepcopy(MATH194 if qid=='Plane194' else MATH245)
    proof['candidate_color_semantics']=semantics
    if 'color_readings' in proof:del proof['color_readings']
    mechanism={
      'Plane194':'Red/blue split the two discarded axis-aligned corner legs and map them to E square-hole sides. Predict accepting E as the central-corner result by mistaking discarded pre-cut boundary traces for surviving cut edges, and rejecting C (the competing central diamond) as impossible. The actual diagonal cut remains black and proves that this role transfer is false. This is not simply matching the true cut to C and reversing can/cannot.',
      'Plane245':'Map the red vertical and blue horizontal discarded-corner ghost legs to the four orthogonal outer corner notches in E, while the actual black diagonal cut still corresponds to the central diamond aperture. Predict double-counting one removed corner depiction as both the true central diamond cut and an extra four-corner right-angle clipping pattern, leading to E. This conflates absent old boundary with additional cut boundaries; the existing dashed ghosts are preserved so a careful reader rejects it.'}[qid]
    differences={'current_reference':'Current Solid167 C01: two existing source features and two candidate boundary groups are compared with red and blue; no old D color mapping is inherited.',
       'migration':'There is only one true source cut. Rather than inventing two cuts, this design distinguishes the two actual discarded corner traces and compares their directions/roles with existing E aperture or notch edges.',
       'earlier_r01':'r01 uses operation indicators (fold-axis guides for Plane194, motion arrows for Plane245). r02 uses only the two dashed legs of the removed corner. Therefore source geometry-role evidence changes, not just style. R01 pixels and all its output remain immutable.',
       'old_Plane245_attempt':'The old A design compared the actual diagonal cut and one vertical ghost leg with the A central square. This design does not color the actual cut, uses both ghost legs, and compares them with E exterior corner notches while retaining its true central diamond. That is a different receiving geometry and a double-counting hypothesis, not old input relabeling.',
       'old_Plane194_prescreen':'A prior untested prescreen warned that coloring ghost legs could be read as changing the cut. Here source true cut remains solid black, both ghosts remain dashed outside retained material, all four cut-corner constructions remain allowed, and no line is added. The proposed error is explicitly accepting the wrong E inner boundary by discarded-versus-surviving edge confusion.',
       'own_prior_designs':prior,'native_semantics':semantics}
    write(directory/'reference_transfer_and_history_difference.json',differences,True)
    expected='C' if qid=='Plane194' else 'E'
    design={'created_at':now(),'question_id':qid,'variant_id':variant,'correct_answer':e['formal_record']['answer'],
       'expected_wrong_answer':expected,'expected_wrong_value':'C: central diamond aperture incorrectly declared impossible' if qid=='Plane194' else 'E: a central diamond aperture plus four additional rectangular exterior corner notches',
       'mechanism':mechanism,'mathematical_proof':proof,'marker_roles':roles,'reference_and_history':differences,
       'human_semantics':semantics,'image_sha256':sha(directory/'candidate.png'),'plugin_sha256':sha(directory/'plugin.json'),
       'status':'FROZEN_PRESET_BEFORE_BOTH_CALLS_PRIMARY_ONLY','fresh_independent_second_review_required':True}
    write(directory/'design.json',design,True)
    write(directory/'render_check.json',{'at':now(),'fresh_schema_sha256':sha(PROJECT/'PlaneGeometry/workbench/plugin.schema.json'),
       'fresh_schema_checked':True,'exact_normalization_equal':True,'noop_pixels_equal':True,'two_candidate_bytes_equal':True,
       'noop_bytes_equal':noop==original.read_bytes(),'image_sha256':sha(directory/'candidate.png'),'pixel_sha256':pix,
       'plugin_sha256':sha(directory/'plugin.json'),'design_sha256':sha(directory/'design.json'),
       'context_sha256':sha(directory/'context.json'),'environment':environment_versions()},True)
    print(json.dumps({'prepared':str(directory),'actions':len(actions),'preset':expected},ensure_ascii=False))

def replay():
    config,adapter,metadata,renderer=setup_renderer()
    from render_plugins import check_schema
    schema=read(PROJECT/'PlaneGeometry/workbench/plugin.schema.json');renderer.schema=schema
    plugin=read(directory/'plugin.json');check_schema(plugin,schema,schema)
    assert renderer.normalize(plugin)==plugin
    assert json.loads(json.dumps(metadata[qid]))==read(directory/'context.json')
    np,data,pix=renderer.render(plugin,frozen=True)
    assert data==(directory/'candidate.png').read_bytes()
    (directory/'independent_process_replay.png').write_bytes(data)
    write(directory/'independent_process_replay.json',{'at':now(),'pid':os.getpid(),'fresh_process':True,
      'fresh_schema_and_defaults_exact':True,'exact_JSON_normalized_context_equal':True,'exact_candidate_bytes_equal':True,
      'image_sha256':sha(directory/'candidate.png'),'pixel_sha256':pix,'plugin_sha256':sha(directory/'plugin.json'),
      'design_sha256':sha(directory/'design.json'),'source_still_eligible':eligibility(qid)},True)
    print(qid+' r02 independent process exact replay passed')

{'prepare':prepare,'replay':replay}[a.mode]()
