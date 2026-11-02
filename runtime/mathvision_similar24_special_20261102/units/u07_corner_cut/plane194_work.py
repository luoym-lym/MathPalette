from worker_env import *
from candidate_work import MATH194
import argparse

QID='Plane194'
VARIANT='r01_fold_axes_to_square_hole'
DIRECTORY=OWN/QID/VARIANT

def prepare():
    DIRECTORY.mkdir(parents=True,exist_ok=True)
    e=eligibility(QID);write(DIRECTORY/'eligibility_before_design.json',e,True);assert e['eligible']
    config,adapter,metadata,renderer=setup_renderer()
    ctx=metadata[QID]
    assert json.loads(json.dumps(ctx))==read(OWN/QID/'context.json')
    write(DIRECTORY/'context.json',ctx,True)
    targets={t['id']:t for t in ctx['canvas']['targets']}
    path=targets['o14']['partial_paths'][0]
    actions=[{'type':'set_object_style','target':'o1','color':'#DC2626','linewidth_pt':1.5},
             {'type':'set_object_style','target':'o3','color':'#2563EB','linewidth_pt':1.5}]
    roles=[
      {'action_index':0,'target':'o1','source_information':'First vertical fold-axis guide in the original square diagram',
       'receiver':'Two vertical sides of E central square aperture','use':'Propose folding-axis direction as the direction of hole sides; this is the false comparison, because hole sides are reflected from the diagonal cut, not from fold guides.'},
      {'action_index':1,'target':'o3','source_information':'Second horizontal fold-axis guide in the rectangle diagram',
       'receiver':'Two horizontal sides of E central square aperture','use':'Complete the orthogonal pair of folding-axis directions wrongly used as the aperture-edge directions.'}]
    for n,color in [(0,'#2563EB'),(1,'#DC2626'),(2,'#2563EB'),(3,'#DC2626')]:
        actions.append({'type':'set_object_style','target':'o14','color':color,'linewidth_pt':1.5,
           'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':n/4,'end':(n+1)/4,'wrap':False}})
        roles.append({'action_index':len(actions)-1,'target':'o14','edge_index':n,
          'source_information':'horizontal second fold guide' if n%2==0 else 'vertical first fold guide',
          'receiver':'existing E aperture side','use':'A concrete direction comparison supporting the false acceptance of E as the central-corner result, displacing the central diamond C. This changes no geometry and asserts no new cut.'})
    plugin={'plugin_schema_version':'1.0.0','question_id':QID,'category':'C','operation':'C_manual',
      'description':'Compare the two perpendicular fold-axis directions with the square-hole sides',
      'intent':'','params':{'actions':actions}}
    from render_plugins import check_schema
    schema=read(PROJECT/'PlaneGeometry/workbench/plugin.schema.json');renderer.schema=schema
    check_schema(plugin,schema,schema);assert renderer.normalize(plugin)==plugin
    write(DIRECTORY/'plugin_submitted.json',plugin,True);write(DIRECTORY/'plugin.json',plugin,True)
    write(DIRECTORY/'marker_roles.json',roles,True)
    from dataset_tools.mathvision_workbench import png_bytes
    from workbench_io import pixel_hash,environment_versions
    scene=adapter.scene(QID)
    try:noop=png_bytes(scene)
    finally:scene.close()
    (DIRECTORY/'no_op.png').write_bytes(noop)
    assert pixel_hash(noop)==pixel_hash(PROJECT/'PlaneGeometry/image/Plane194.png')
    p,a,ph=renderer.render(plugin,frozen=True);p2,b,ph2=renderer.render(plugin,frozen=True)
    assert a==b and p==p2==plugin and ph==ph2
    (DIRECTORY/'candidate.png').write_bytes(a);(DIRECTORY/'repeat.png').write_bytes(b)
    transfer={'reference':'Current Solid167 C01 distinguishes two real source features red/blue and corresponding two candidate groups. The current A option, all nine current PNGs and their actual plugins were inspected.',
       'transfer':'This question has one freely placed corner cut, so inventing a second cut or fixing a corner is prohibited. The two actual orthogonal fold-axis guides instead supply source directions, mapped to E aperture sides.',
       'old_history':'No tested old candidate exists for Plane194. Old prescreen correctly rejected simply coloring a real cut and C diamond as a route to declaring C impossible: that would need unsupported polarity inversion.',
       'material_difference_from_old_prescreen':'This design does not pair the real cut with C. It pairs fold-axis directions with the geometrically wrong E square aperture. The prospective mistake accepts E as the central-corner result and rejects its competing central aperture C. A/B/D outer-boundary cases remain distinct. Thus the proposed C error is a cut-edge-versus-fold-axis confusion, not merely reading cannot as can.',
       'all_corner_types_preserved':['original outer/outer -> A','fold/outer -> B','outer/fold -> D','fold/fold -> C'],
       'no_new_given':'Neither fold guide selects which quarter-sheet corner is cut. The source actual cut and discarded-corner ghost legs remain black.',
       'semantic_check':'The colored dashed source guides already denote future fold axes: each is shown only in its own construction stage and omitted in the subsequent quarter-square. They are conventional operation guides, not transported paper surface edging. No source material outline is colored. All physically possible samples A/B/C/D are completely unchanged. Coloring E cannot make its square aperture realizable under either external-annotation or colored-edging reading. E stays the unique impossible sample.',
       'limitations':'Prediction is prospective and fallible; no model response has yet been seen for these pixels. Same logical family as Plane245 is applied to a different formal question and its own independently checked source.'}
    write(DIRECTORY/'reference_transfer_and_history_difference.json',transfer,True)
    design={'created_at':now(),'question_id':QID,'variant_id':VARIANT,'correct_answer':'E','expected_wrong_answer':'C',
       'expected_wrong_value':'C: intact square outer boundary and one central diamond aperture, incorrectly declared unobtainable',
       'mechanism':'Red vertical fold-axis and blue horizontal fold-axis guides are direction-matched to E axis-aligned square-hole sides. Predict the solver falsely accepts E as the fold/fold central-corner result, leaving C as the allegedly impossible central-hole alternative. A/B/D retain their separate outer-boundary cut cases. The error replaces the true reflected diagonal-cut boundary with the two folding-axis directions.',
       'mathematical_proof':MATH194,'marker_roles':roles,'reference_and_history':transfer,
       'literal_color_reading':'No moving source paper boundary is colored. The only colored option E is impossible already by geometry; A/B/C/D remain unmarked and have the explicit constructions in the four-case proof. Colors on conventional dashed folding guides do not prescribe any new cut or printed pattern.',
       'image_sha256':sha(DIRECTORY/'candidate.png'),'plugin_sha256':sha(DIRECTORY/'plugin.json'),
       'status':'FROZEN_PRESET_BEFORE_BOTH_CALLS_PRIMARY_ONLY','fresh_independent_second_review_required':True}
    write(DIRECTORY/'design.json',design,True)
    write(DIRECTORY/'render_check.json',{'at':now(),'fresh_schema_sha256':sha(PROJECT/'PlaneGeometry/workbench/plugin.schema.json'),
       'fresh_schema_checked':True,'exact_normalization_equal':True,'noop_pixels_equal':True,
       'noop_bytes_equal':noop==(PROJECT/'PlaneGeometry/image/Plane194.png').read_bytes(),'two_candidate_bytes_equal':True,
       'image_sha256':sha(DIRECTORY/'candidate.png'),'pixel_sha256':ph,'plugin_sha256':sha(DIRECTORY/'plugin.json'),
       'design_sha256':sha(DIRECTORY/'design.json'),'context_sha256':sha(DIRECTORY/'context.json'),'environment':environment_versions()},True)
    print(json.dumps({'prepared':str(DIRECTORY),'actions':len(actions),'preset':'C'},ensure_ascii=False))

def replay():
    config,adapter,metadata,renderer=setup_renderer()
    from render_plugins import check_schema
    schema=read(PROJECT/'PlaneGeometry/workbench/plugin.schema.json');renderer.schema=schema
    plugin=read(DIRECTORY/'plugin.json');check_schema(plugin,schema,schema)
    assert renderer.normalize(plugin)==plugin
    assert json.loads(json.dumps(metadata[QID]))==read(DIRECTORY/'context.json')
    p,data,pix=renderer.render(plugin,frozen=True)
    assert data==(DIRECTORY/'candidate.png').read_bytes()
    (DIRECTORY/'independent_process_replay.png').write_bytes(data)
    write(DIRECTORY/'independent_process_replay.json',{'at':now(),'pid':os.getpid(),'fresh_process':True,
       'fresh_schema_and_defaults_exact':True,'exact_JSON_normalized_context_equal':True,'exact_candidate_bytes_equal':True,
       'image_sha256':sha(DIRECTORY/'candidate.png'),'pixel_sha256':pix,
       'plugin_sha256':sha(DIRECTORY/'plugin.json'),'design_sha256':sha(DIRECTORY/'design.json'),
       'source_still_eligible':eligibility(QID)},True)
    print('Plane194 independent process exact replay passed')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['prepare','replay']);a=p.parse_args()
    {'prepare':prepare,'replay':replay}[a.mode]()
