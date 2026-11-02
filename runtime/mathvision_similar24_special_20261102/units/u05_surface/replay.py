from worker_env import *
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer,check_schema
from workbench_io import load_config,pixel_hash
from renderer_adapter import scene_png
config=load_config(PROJECT/'SolidGeometry/workbench/config.json')
adapter=RendererAdapter(config)
for qid,variant in [('Solid186','r05_three_patch_changed_area_binding'),('Solid226','r05_removed_roof_to_new_cut_faces')]:
    f=OWN/qid/variant
    design=load(f/'design.json')
    e=eligibility(qid); assert e['eligible']
    for p,h in load(f/'input_manifest.json')['source_manifest'].items(): assert sha(PROJECT/p)==h,(p,'changed')
    c=adapter.inspect_question(qid)
    assert c==load(f/'context.json')
    s=adapter.scene(qid)
    try: noop,np=scene_png(s)
    finally: s.close()
    assert np==pixel_hash(adapter.original_paths[qid])
    renderer=PluginRenderer(config,adapter,{qid:c})
    plugin=load(f/'plugin.json')
    check_schema(plugin,renderer.schema,renderer.schema)
    assert renderer.normalize(plugin)==plugin
    p,data,px=renderer.render(plugin)
    assert p==plugin and data==(f/'candidate.png').read_bytes()
    assert hashlib.sha256(data).hexdigest()==design['image_sha256'] and px==design['pixel_sha256']
    assert sha(f/'plugin.json')==design['plugin_sha256']
    (f/'independent_process_replay.png').write_bytes(data)
    save(f/'fresh_process_replay.json',{'at':now(),'pid':os.getpid(),'new_process':True,
      'fresh_schema_and_defaults':True,'context_exact_JSON_equal':True,'fresh_noop_pixels_match':True,
      'candidate_PNG_bytes_match':True,'plugin_exact_match':True,'pixel_sha256':px,
      'image_sha256':hashlib.sha256(data).hexdigest(),'design_sha256':sha(f/'design.json'),
      'environment':environment(),'source_manifest_unchanged':True,'eligibility':e},True)
    save(f/'primary_review_before_calls.json',{'at':now(),'role':'PRIMARY author review, not independent second review',
      'actual_native_PNG_viewed':True,'unique_correct_answer':design['correct_answer'],
      'full_proof_path':design['math_path'],'all_marks_reviewed':str(f/'marker_roles.json'),
      'all_marks_effective_and_useful':True,'fully_overwritten_actions':[],'conflicting_duplicate_target_actions':[],
      'readability':'All original cell seams/silhouette retained for Solid186. All 1/3/9 dimensions and cut-edge partial occlusion retained for Solid226. Colors identify real comparison boundaries. No fill, label, point or masking added.',
      'human_literal_reading':design['human_semantics'],'source_JPG_and_formal_PNG_viewed':True,
      'geometry_projection_visibility_frozen_separately':True,'frozen_wrong_preset':design['expected_wrong_answer'],
      'frozen_wrong_value':design['expected_wrong_value'],'image_sha256':sha(f/'candidate.png'),
      'design_sha256':sha(f/'design.json'),'independent_replay_path':str(f/'fresh_process_replay.json'),
      'decision':'eligible for exactly two original quicktest3 calls; success not presumed'},True)
    print(qid,'fresh independent process exact replay PASS',flush=True)

# Verify all old evidence that this unit read, with no restoration or mutation.
readcheck=[]
tracked=load(TASK/'history_index.json')['tracked_readonly_source_sha256']
for item in load(OWN/'read_ledger.json'):
    p=Path(item['path']); actual=sha(p)
    assert actual==item['sha256'],str(p)
    rel=str(p.relative_to(PROJECT)).replace('\\','/')
    expected=tracked.get(rel)
    if expected is not None: assert actual==expected,(rel,'history index mismatch')
    readcheck.append({'path':str(p),'sha256':actual,'unchanged':True,'matches_preparer_history_hash':expected==actual if expected else None})
save(OWN/'source_preservation_before_calls.json',{'at':now(),'files':readcheck,'all_unchanged':True,'restored_files':[]},True)

source=OLD/'harness/quicktest3_isolated.py'
original=source.read_bytes()
replacements=[(b'PROJECT = Path(__file__).resolve().parents[3]',('PROJECT = Path('+repr(str(PROJECT))+')').encode()),
              (b'target = HARNESS / directory',('target = Path('+repr(str(OWN/'ownruntime/harness'))+') / directory').encode())]
localized=original
for before,after in replacements:
    assert localized.count(before)==1
    localized=localized.replace(before,after)
reverse=localized
for before,after in reversed(replacements): reverse=reverse.replace(after,before)
assert reverse==original
hdir=OWN/'harness'; hdir.mkdir(exist_ok=True)
(hdir/'quicktest3_isolated.py').write_bytes(localized)
import difflib
diff=''.join(difflib.unified_diff(original.decode().splitlines(keepends=True),localized.decode().splitlines(keepends=True),fromfile=str(source),tofile=str(hdir/'quicktest3_isolated.py')))
(hdir/'localization.diff').write_text(diff,encoding='utf-8',newline='\n')
save(hdir/'localization_audit.json',{'source':str(source),'source_sha256':hashlib.sha256(original).hexdigest(),
 'localized_sha256':hashlib.sha256(localized).hexdigest(),'replacement_count':2,'reverse_replacement_bytes_equal':reverse==original,
 'changes':'Local PROJECT/cache paths only; original remote payload/model/thinking/systemprompt/timeout/response handling unchanged',
 'diff':str(hdir/'localization.diff')},True)
save(OWN/'checkpoint.json',{'at':now(),'status':'preflight_passed_pending_exact_two_tests','assigned':['Solid186','Solid226'],'calls':0,
 'questions':{q:{'status':'fresh_schema_noop_repeat_replay_and_primary_review_passed'} for q in ('Solid186','Solid226')}})
