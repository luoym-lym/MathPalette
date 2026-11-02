from bootstrap import *
import difflib
d=OWN/'Plane213/user233_boundary_spine_foot_transfer_v1'
replay=read(OWN/'offline_replay/replay_verification.json')
assert replay['matches_tested_png_bytes'] and replay['two_delivery_replays_identical']
assert replay['png_sha256']==sha(d/'candidate.png')
save(d/'primary_review.json',{'reviewed_at_utc':now(),'actual_candidate_png_viewed':True,'proceed_to_API_if_fresh_zero_prior_target_image_gate_passes':True,'correct_answer':'A','expected_wrong_answer':'C','unique_math':'Fresh current-edge exact-cover enumerations find A2 tilings and B/C/D/E0.','marker_necessity':'Each of the four red unit edges on each diagram expresses the full four-cell vertical spine; two blue unit edges on each diagram fix the two-cell foot and corner orientation. All source marks are exterior boundaries, no internal cut or imposed division.','human_readability':'Native768 PNG personally viewed;15 board cells, all five-cell options, unmarked grid lines and letters clear. Colors act as comparison cues; no new conditions/fills/shape or closed interior partition.','concision':'12 rendered unit-edge styles from user13 property edits; the split color and width edit of C_1 coalesced.','reference':'Current user Plane233 C01 copied byte-identically after verifying equal formal original PNGs.','old_history_read':'The only prior Plane213 design paired open internal U-notch with B, declaredB and endedC/B. Full two raw responses and all old design/plugin/primary_review personally read; oldB remains one-hit, never relabelled. This new exterior four-unit spine+two-unit foot correspondence comes from user current C01; newC was frozen before reading those old full raw responses.','new_independent_review_required':True,'old_evidence_unchanged':True})
source=OLD/'harness/quicktest3_isolated.py';raw=source.read_bytes()
before=b'PROJECT = Path(__file__).resolve().parents[3]'
after=('PROJECT = Path('+repr(ROOT.as_posix())+')').encode('utf-8')
assert raw.count(before)==1
relocated=raw.replace(before,after);assert relocated.replace(after,before)==raw
out=OWN/'harness';out.mkdir(exist_ok=False)
(out/'quicktest3_isolated.py').write_bytes(relocated)
save(OWN/'harness_relocation_audit.json',{'at_utc':now(),'canonical_source':str(source),'canonical_sha256':sha(source),'local_copy':str(out/'quicktest3_isolated.py'),'local_sha256':sha(out/'quicktest3_isolated.py'),'only_changed_line':'Local PROJECT root resolution; all remote profile/payload/credentials/system/model/thinking/no-token/no-timeout/retry logic untouched.','inverse_byte_replacement_exact':True})
(OWN/'harness_relocation.patch').write_text(''.join(difflib.unified_diff(raw.decode().splitlines(True),relocated.decode().splitlines(True))),encoding='utf-8')
print('Primary review and local-only harness relocation ready. NO API calls yet.')
