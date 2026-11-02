from worker_env import *
from candidate_work import MATH245
import argparse
import copy

QID='Plane245';VARIANT='r04_fold_axes_to_square_aperture';directory=OWN/QID/VARIANT
p=argparse.ArgumentParser();p.add_argument('mode',choices=['prepare','replay']);a=p.parse_args()

def prepare():
    directory.mkdir(parents=True,exist_ok=True)
    e=eligibility(QID);assert e['eligible'];write(directory/'eligibility_before_design.json',e,True)
    config,adapter,metadata,renderer=setup_renderer();ctx=metadata[QID]
    assert json.loads(json.dumps(ctx))==read(OWN/QID/'context.json')
    write(directory/'context.json',ctx,True)
    path=next(t for t in ctx['canvas']['targets'] if t['id']=='o114')['partial_paths'][0]
    actions=[{'type':'set_object_style','target':'o1','color':'#DC2626','linewidth_pt':1.5},
             {'type':'set_object_style','target':'o53','color':'#2563EB','linewidth_pt':1.5}]
    roles=[{'action_index':0,'target':'o1','source_information':'Original first horizontal fold-axis guide in initial square',
       'receiver':'Two horizontal sides of A aperture','use':'Source hinge orientation is compared with a candidate cut-boundary orientation. Intended mistake copies a fold crease direction into the aperture, instead of reflecting the slanted cut.'},
      {'action_index':1,'target':'o53','source_information':'Original second vertical fold-axis guide in the intermediate rectangle',
       'receiver':'Two vertical sides of A aperture','use':'Supply the second orthogonal hinge direction to the same proposed fold-axis-to-hole-side substitution.'}]
    for n,color in [(0,'#DC2626'),(1,'#2563EB'),(2,'#DC2626'),(3,'#2563EB')]:
        actions.append({'type':'set_object_style','target':'o114','color':color,'linewidth_pt':1.5,
          'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':n/4,'end':(n+1)/4,'wrap':False}})
        roles.append({'action_index':len(actions)-1,'target':'o114','edge_index':n,
          'source_information':'First horizontal fold axis' if n%2==0 else 'Second vertical fold axis',
          'receiver':'This existing A aperture side','use':'Match the axis orientation as a specific false boundary role transfer. Same color proposes a comparison; it adds no actual parallelism or cutting condition.'})
    plugin={'plugin_schema_version':'1.0.0','question_id':QID,'category':'C','operation':'C_manual',
      'description':'Compare both hinge-axis directions with square-aperture sides','intent':'','params':{'actions':actions}}
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
    semantics='Both colored source objects are the original dashed hinge guides, with curved instruction arrows visibly crossing them. They indicate where each next fold is performed; the first guide is omitted in the rectangle, and the second guide is omitted in the cut quarter, so their conventional instructional role is already explicit in the original stages. No surviving source material edge, gray fill, actual cut or discarded trace is colored. Coloring the impossible A aperture cannot make its shape obtainable, and unchanged B is still the unique valid result. Treating A colors as physical edging only further excludes A. These guides do not introduce a printed pattern to preserve.'
    proof=copy.deepcopy(MATH245);del proof['color_readings'];proof['candidate_color_semantics']=semantics
    differences={'current_reference':'Current Solid167 C01 uses two source features and two receiving aperture groups, red/blue. All nine current reference PNGs/plugins were read; no old D mapping inherited.',
      'old_attempt':'The old A design sources were a true diagonal cut and one discarded ghost leg. Both remain black here; two operation hinge guides supply the source directions instead.',
      'r01':'R01 mapped folding MOTION to aperture edges (first upward arrow -> vertical red, second rightward arrow -> horizontal blue). Here source HINGE axes are used (first horizontal hinge -> horizontal red, second vertical hinge -> vertical blue). Motion and hinge are perpendicular; this changes the actual information relationship and which physical role is mistaken for a cut edge, rather than just exchanging color names.',
      'r02_r03':'Those used discarded old perimeter legs in the final clipped-corner diagram. This uses pre-fold crease axes and leaves both discarded legs untouched black. Crease-as-cut substitution differs from retaining removed old perimeter or adding outer corner cuts.',
      'previous_off_preset_answers_not_reclassified':'Prior R03 E/A is retained as a miss against A. A single matching old response is never counted toward this new pair.',
      'own_prior_full_reviews':prior,'semantics':semantics}
    write(directory/'reference_transfer_and_history_difference.json',differences,True)
    design={'created_at':now(),'question_id':QID,'variant_id':VARIANT,'correct_answer':'B','expected_wrong_answer':'A',
      'expected_wrong_value':'A: intact square outer boundary with one axis-aligned central square aperture',
      'mechanism':'Replace the reflected slanted cutting boundary with the horizontal first hinge and vertical second hinge directions. Red first horizontal fold guide pairs with A horizontal aperture sides; blue second vertical guide pairs with A vertical sides. This predicts a square aperture aligned with the paper axes, A, instead of the true central diamond B.',
      'mathematical_proof':proof,'marker_roles':roles,'reference_and_history':differences,'human_semantics':semantics,
      'image_sha256':sha(directory/'candidate.png'),'plugin_sha256':sha(directory/'plugin.json'),
      'status':'FROZEN_PRESET_BEFORE_BOTH_CALLS_PRIMARY_ONLY','fresh_independent_second_review_required':True}
    write(directory/'design.json',design,True)
    write(directory/'render_check.json',{'at':now(),'fresh_schema_sha256':sha(PROJECT/'PlaneGeometry/workbench/plugin.schema.json'),
      'fresh_schema_checked':True,'exact_normalization_equal':True,'noop_pixels_equal':True,'noop_bytes_equal':noop==original.read_bytes(),
      'two_candidate_bytes_equal':True,'image_sha256':sha(directory/'candidate.png'),'pixel_sha256':pix,
      'plugin_sha256':sha(directory/'plugin.json'),'design_sha256':sha(directory/'design.json'),
      'context_sha256':sha(directory/'context.json'),'environment':environment_versions()},True)
    print('Plane245 r04 prepared, preset A frozen')

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
    print('Plane245 r04 independent process exact replay passed')

{'prepare':prepare,'replay':replay}[a.mode]()
