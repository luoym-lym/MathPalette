from worker_env import *
from candidate_work import MATH245
import argparse
import copy

QID='Plane245';VARIANT='r03_ghost_legs_to_square_aperture';directory=OWN/QID/VARIANT
p=argparse.ArgumentParser();p.add_argument('mode',choices=['prepare','replay']);a=p.parse_args()

def prepare():
    directory.mkdir(parents=True,exist_ok=True)
    e=eligibility(QID);assert e['eligible'];write(directory/'eligibility_before_design.json',e,True)
    config,adapter,metadata,renderer=setup_renderer();ctx=metadata[QID]
    assert json.loads(json.dumps(ctx))==read(OWN/QID/'context.json')
    write(directory/'context.json',ctx,True)
    target=next(t for t in ctx['canvas']['targets'] if t['id']=='o114');path=target['partial_paths'][0]
    actions=[{'type':'set_object_style','target':'o105','color':'#DC2626','linewidth_pt':1.5},
             {'type':'set_object_style','target':'o106','color':'#2563EB','linewidth_pt':1.5}]
    roles=[{'action_index':0,'target':'o105','source_information':'Vertical dashed discarded-corner ghost leg, outside retained paper',
       'receiver':'A two vertical square-aperture sides','use':'Compare a removed old vertical boundary with a proposed resulting vertical hole boundary; intended erroneous retained-edge role transfer.'},
      {'action_index':1,'target':'o106','source_information':'Horizontal dashed discarded-corner ghost leg, outside retained paper',
       'receiver':'A two horizontal square-aperture sides','use':'Complete the two-direction old-boundary-versus-cut-boundary comparison; actual diagonal clip remains black.'}]
    for n,color in [(0,'#2563EB'),(1,'#DC2626'),(2,'#2563EB'),(3,'#DC2626')]:
        actions.append({'type':'set_object_style','target':'o114','color':color,'linewidth_pt':1.5,
          'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':n/4,'end':(n+1)/4,'wrap':False}})
        roles.append({'action_index':len(actions)-1,'target':'o114','edge_index':n,
          'source_information':'horizontal ghost leg' if n%2==0 else 'vertical ghost leg',
          'receiver':'This existing A aperture side','use':'Specifically propose this axis-parallel side as the reflected discarded corner leg; the actual reflected cut sides are oblique, so the correspondence is false.'})
    plugin={'plugin_schema_version':'1.0.0','question_id':QID,'category':'C','operation':'C_manual',
      'description':'Compare both discarded corner legs with the square-aperture side directions','intent':'','params':{'actions':actions}}
    from render_plugins import check_schema
    schema=read(PROJECT/'PlaneGeometry/workbench/plugin.schema.json');renderer.schema=schema
    check_schema(plugin,schema,schema);assert renderer.normalize(plugin)==plugin
    write(directory/'plugin_submitted.json',plugin,True);write(directory/'plugin.json',plugin,True);write(directory/'marker_roles.json',roles,True)
    from dataset_tools.mathvision_workbench import png_bytes
    from workbench_io import pixel_hash,environment_versions
    scene=adapter.scene(QID)
    try:noop=png_bytes(scene)
    finally:scene.close()
    (directory/'no_op.png').write_bytes(noop)
    original=PROJECT/'PlaneGeometry/image/Plane245.png';assert pixel_hash(noop)==pixel_hash(original)
    np,data,pix=renderer.render(plugin,frozen=True);np2,again,pix2=renderer.render(plugin,frozen=True)
    assert data==again and np==np2==plugin and pix==pix2
    (directory/'candidate.png').write_bytes(data);(directory/'repeat.png').write_bytes(again)
    prior=[]
    for f in (OWN/QID).glob('*/design.json'):
        d=read(f);assert d['image_sha256']!=sha(directory/'candidate.png')
        prior.append({'design_path':str(f),'design_sha256':sha(f),'image_sha256':d['image_sha256'],
          'full_manual_review':read(f.parent/'manual_final_review.json') if (f.parent/'manual_final_review.json').exists() else None})
    semantics='Only two dashed traces of already removed paper are colored at the source. Neither is an existing surviving source cut edge; every positive-length colored ghost segment lies in the removed quarter triangle. The actual source diagonal cut, folds, arrows and all retained boundaries stay black. A is the only colored sample and is impossible geometrically with or without intrinsic colored edging. Unchanged B remains uniquely possible. No color-bearing surviving source edge must be erased in B.'
    proof=copy.deepcopy(MATH245);del proof['color_readings'];proof['candidate_color_semantics']=semantics
    differences={'current_reference':'Solid167 current C01: two source feature groups mapped to corresponding two groups of candidate aperture boundaries. All nine actual current PNGs and plugin actions were read.',
      'old_design':'Old cut_vs_ghost_corner_edge_binding marked actual diagonal cut red and vertical ghost blue and paired them with A. This design leaves actual cut black and uses both perpendicular discarded ghost legs; it predicts the entire A square hole by retaining two removed old boundaries, not by combining a true cut with one uncut trace.',
      'r01':'r01 instead colored folding-motion arrows; here all operation indicators are unchanged black. Source information changes to absent old boundaries.',
      'r02':'r02 compared ghost legs with eight E outer corner-notch sides and predicted adding extra exterior cuts to a true central diamond. This design compares those legs with the four A central aperture sides and predicts replacing the diamond aperture with a square. It does not need extra exterior cuts or mislocating the centre corner. The receiving topology and specific error change, not just option salience or hue.',
      'prior_results_retained':'R01 B/B missed A. R02 B/A missed E; its incidental A is not reclassified or counted for this new input. This new candidate must have its own exact two complete responses against preset A.',
      'own_prior_full_reviews':prior,'semantics':semantics}
    write(directory/'reference_transfer_and_history_difference.json',differences,True)
    design={'created_at':now(),'question_id':QID,'variant_id':VARIANT,'correct_answer':'B','expected_wrong_answer':'A',
      'expected_wrong_value':'A: intact square outer boundary with one axis-aligned central square aperture',
      'mechanism':'Take both perpendicular dashed legs of the discarded corner as the two directions of the resulting central hole boundary, instead of reflecting the actual slanted clip. Red vertical ghost is paired with A two vertical hole sides and blue horizontal ghost with A two horizontal hole sides. The central location is retained, but the removed old boundaries are mistaken for retained cut boundaries, predicting square aperture A.',
      'mathematical_proof':proof,'marker_roles':roles,'reference_and_history':differences,'human_semantics':semantics,
      'image_sha256':sha(directory/'candidate.png'),'plugin_sha256':sha(directory/'plugin.json'),
      'status':'FROZEN_PRESET_BEFORE_BOTH_CALLS_PRIMARY_ONLY','fresh_independent_second_review_required':True}
    write(directory/'design.json',design,True)
    write(directory/'render_check.json',{'at':now(),'fresh_schema_sha256':sha(PROJECT/'PlaneGeometry/workbench/plugin.schema.json'),
      'fresh_schema_checked':True,'exact_normalization_equal':True,'noop_pixels_equal':True,'noop_bytes_equal':noop==original.read_bytes(),
      'two_candidate_bytes_equal':True,'image_sha256':sha(directory/'candidate.png'),'pixel_sha256':pix,
      'plugin_sha256':sha(directory/'plugin.json'),'design_sha256':sha(directory/'design.json'),
      'context_sha256':sha(directory/'context.json'),'environment':environment_versions()},True)
    print('Plane245 r03 prepared, preset A frozen')

def replay():
    config,adapter,metadata,renderer=setup_renderer()
    from render_plugins import check_schema
    schema=read(PROJECT/'PlaneGeometry/workbench/plugin.schema.json');renderer.schema=schema
    plugin=read(directory/'plugin.json');check_schema(plugin,schema,schema);assert renderer.normalize(plugin)==plugin
    assert json.loads(json.dumps(metadata[QID]))==read(directory/'context.json')
    np,data,pix=renderer.render(plugin,frozen=True);assert data==(directory/'candidate.png').read_bytes()
    (directory/'independent_process_replay.png').write_bytes(data)
    write(directory/'independent_process_replay.json',{'at':now(),'pid':os.getpid(),'fresh_process':True,
      'fresh_schema_and_defaults_exact':True,'exact_JSON_normalized_context_equal':True,'exact_candidate_bytes_equal':True,
      'image_sha256':sha(directory/'candidate.png'),'pixel_sha256':pix,'plugin_sha256':sha(directory/'plugin.json'),
      'design_sha256':sha(directory/'design.json'),'source_still_eligible':eligibility(QID)},True)
    print('Plane245 r03 independent process exact replay passed')

{'prepare':prepare,'replay':replay}[a.mode]()
