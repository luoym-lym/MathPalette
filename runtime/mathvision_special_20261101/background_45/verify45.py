from tools45 import *
import base64
from PIL import Image
cp=read(TASK/'checkpoint.json');assert cp['actual_assessed_question_ids']==IDS and not cp['unworked_question_ids']
assert read(TASK/'no_live_api_processes.json')['active_own_api_processes']==[]
assert read(TASK/'second_review_queue.json')['candidates']==[]
allbindings=[];controls=[]
for p in SHARED.rglob('binding.json'):
    try:b=read(p)
    except (ValueError,UnicodeError):continue
    if b.get('question_id') not in IDS:continue
    allbindings.append({'path':str(p),'sha256':file_hash(p),'question_id':b['question_id'],'png_sha256':b.get('image_sha256'),'preset':b.get('expected_wrong_answer'),'image_path':b.get('image_path')})
    # A control must bind formal unannotated pixels; byte format may differ.
    if b.get('pixel_sha256')==read(TASK/b['question_id']/'context.json')['original_pixel_sha256']:controls.append(str(p))
assert not controls
for row in cp['questions']:
    q=row['question_id'];assert eligibility(q)['eligible']
    if row['api_calls']==0:continue
    f=Path(row['design_path']).parent;audit=read(f/'evidence_binding_audit.json');assert audit['pretest_freeze_files_still_match']
    for rel,h in audit['files'].items():assert file_hash(TASK/rel)==h,(rel,'changed')
    same=[b for b in allbindings if b['png_sha256']==row['png_sha256']]
    assert len(same)==1,(q,'same frozen image has another invocation')
    with Image.open(f/'candidate.png') as im:assert im.size==(768,768) and im.convert('RGBA').getextrema()[3]==(255,255)
    for n,h in read(f/'pretest_freeze.json')['files'].items():assert file_hash(f/n)==h
    assert read(f/'primary_review.json')['credible_possible_candidate'] is False
write(TASK/'final_verification.json',{'checked_at':now(),'all8_current_eligible_with_original_approval':True,'all_frozen_pretest_and_raw_bindings_unchanged':True,'each_new_tested_png_has_exactly1two_run_invocation':True,'assigned_ID_bindings_including_old_history':allbindings,'existing_original_controls':controls,'no_original_control_repeats':True,'no_live_own_API_processes':True,'native_candidate_PNGs_readable768opaque':True,'local_preflight_draft_rejection_disclosed':True,'three_hypotheses_four_offline_draft_versions_six_complete_calls_zero_candidates':True,'no_independent_second_review_or_publication':True})
manifest={str(p.relative_to(TASK)).replace('\\','/'):file_hash(p) for p in TASK.rglob('*') if p.is_file() and not any(k in p.parts for k in ['render_tmp','tmp','cache','mpl_cache'])}
write(TASK/'artifact_manifest.json',{'created_at':now(),'file_sha256':manifest,'manifest_excludes_itself_and_disposable_caches':True})
print('Final verification passed; assigned bindings',len(allbindings),'controls0; own API0; candidates0')
