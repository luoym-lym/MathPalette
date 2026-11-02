from worker_env import *
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer,check_schema
from renderer_adapter import scene_png
from workbench_io import load_config,pixel_hash
config=load_config(PROJECT/'SolidGeometry/workbench/config.json')
adapter=RendererAdapter(config)
for qid,variant in [('Solid186','r05_face_scale_comparison'),('Solid226','r05_front_plane_loss')]:
    f=OWN/qid/variant;d=load(f/'design.json')
    e=eligibility(qid);assert e['eligible']
    for p,h in load(f/'input_manifest.json')['source_manifest'].items():assert sha(PROJECT/p)==h
    c=adapter.inspect_question(qid); assert c==load(f/'context.json')
    s=adapter.scene(qid)
    try: baseline,bp=scene_png(s)
    finally:s.close()
    assert bp==pixel_hash(adapter.original_paths[qid])
    renderer=PluginRenderer(config,adapter,{qid:c});p=load(f/'plugin.json')
    check_schema(p,renderer.schema,renderer.schema);assert p==renderer.normalize(p)
    pn,data,ph=renderer.render(p)
    assert data==(f/'candidate.png').read_bytes() and pn==p and ph==d['pixel_sha256']
    assert sha(f/'candidate.png')==d['image_sha256'] and sha(f/'plugin.json')==d['plugin_sha256']
    (f/'independent_process_replay.png').write_bytes(data)
    save(f/'fresh_process_replay.json',{'at':now(),'pid':os.getpid(),'new_process':True,
      'fresh_schema_and_default_normalization':True,'fresh_noop_pixels_match':True,'context_exact_JSON_equal':True,
      'candidate_PNG_bytes_match':True,'plugin_exact_match':True,'design_sha256':sha(f/'design.json'),
      'image_sha256':sha(f/'candidate.png'),'pixel_sha256':ph,'source_manifest_unchanged':True,'eligibility':e,'environment':environment()},True)
    save(f/'primary_review_before_calls.json',{'at':now(),'role':'PRIMARY author inspection only, not independent second review',
      'source_JPG_formal_PNG_and_candidate_native_PNG_actually_viewed':True,'all_mark_roles_reviewed':str(f/'marker_roles.json'),
      'readability':'Solid186 open red height and blue width motifs show true unit counts 3 and 2 on real square faces. Solid226 full blue original front perimeter and red existing notch U retain all 1/3/9 dimensions and the true opening. No fill or label changes.',
      'full_math_proof':d['math_path'],'unique_original_answer':d['correct_answer'],'semantic_review':d['human_semantics'],
      'all_marks_effective_and_useful':True,'no_overwritten_or_duplicate_actions':True,
      'source_to_receiver_difference':str(f/'design_difference_audit.json'),'frozen_wrong_preset':d['expected_wrong_answer'],
      'frozen_wrong_value':d['expected_wrong_value'],'design_sha256':sha(f/'design.json'),'image_sha256':sha(f/'candidate.png'),
      'decision':'eligible for exactly two original quicktest3 calls; no success presumed'},True)
    print(qid,'fresh schema/noop/exact independent replay PASS',flush=True)
