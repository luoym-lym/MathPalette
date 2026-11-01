from tools_b import *
qid='Plane223';vid='large_spot_ring_correspondence';out=HERE/qid/vid
assert not (out/'tests').exists(),'This finite extension permits only the first pair on the frozen untested image.'
assert not (HERE/'extension_checkpoint.json').exists()
design=json.loads((out/'design.json').read_text(encoding='utf-8'));plugin=json.loads((out/'plugin.json').read_text(encoding='utf-8'));render=json.loads((out/'render_check.json').read_text(encoding='utf-8'))
assert design['expected_wrong_answer']=='C' and design['correct_answer']=='E'
hashes={name:file_hash(out/name) for name in ['candidate.png','plugin.json','design.json','primary_review.json','context.json','render_check.json','path_fingerprints_complete.json','untested_status.json']}
for name,key in [('candidate.png','png_sha256'),('plugin.json','plugin_sha256'),('design.json','design_sha256')]:assert hashes[name]==render[key]
original_evidence={str(p.relative_to(HERE)):file_hash(p) for p in HERE.rglob('*.json') if 'tests' not in p.parts}
elig=eligibility(qid);assert elig['eligible'],elig
cfg,ad=adapter();before=inputs(ad,qid);assert before==render['input_fingerprints']
context=ad.inspect_question(qid);renderer=PluginRenderer(cfg,ad,{qid:context})
n,png,pixels=renderer.render(plugin,frozen=True);n2,png2,pixels2=renderer.render(plugin,frozen=True)
assert n==n2==plugin and png==png2==(out/'candidate.png').read_bytes() and pixels==pixels2==render['pixel_sha256']
assert before==inputs(ad,qid)
write(HERE/'extension_context.json',context)
write(HERE/'extension_before_calls.json',{'created_at':now(),'question_id':qid,'variant_id':vid,'authorization':'Parent finite extension: test only this previously frozen never-tested draft, at most one two-call pair.','eligibility':elig,'immutable_expected_wrong_answer':'C','formal_answer':'E','frozen_existing_hashes':hashes,'original_primary_evidence_hashes':original_evidence,'fresh_context_path':str((HERE/'extension_context.json').relative_to(ROOT)),'fresh_context_sha256':file_hash(HERE/'extension_context.json'),'formal_PNG_noop_pixel_equal':True,'unchanged_existing_candidate_reproduced_twice_byte_identically':True,'frozen_schema_normalization_equal':True,'fresh_input_hashes_equal_original':True,'fresh_input_fingerprints':before,'actual_exact_PNG_viewed_again':True,'primary_human_check':'Four existing dot/ring contours only; original black/yellow fills, ring center and all positions remain clear. No newly found ambiguity prevents testing.','limits':'No new independent second review. Optional mark colors are appearance annotations, not changed black/yellow semantic fills.'})
print(json.dumps({'ready':True,'question_id':qid,'preset':'C','png_sha256':hashes['candidate.png'],'fresh_baseline_and_twice_exact_replay':True}),flush=True)
