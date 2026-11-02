from common68 import *
import difflib

source=BASE/'harness/quicktest3_isolated.py'
raw=source.read_bytes()
old=b'PROJECT = Path(__file__).resolve().parents[3]'
new=b'PROJECT = Path(__file__).resolve().parents[4]'
assert raw.count(old)==1
relocated=raw.replace(old,new)
out=HERE/'harness/quicktest3_isolated.py';out.parent.mkdir(exist_ok=True)
with out.open('xb') as f: f.write(relocated)
assert out.read_bytes().replace(new,old)==raw
write(HERE/'harness_relocation_byte_audit.json',dict(checked_at=now(),source=str(source),source_sha256=sha(source),relocated=str(out),relocated_sha256=sha(out),
    only_change='Local PROJECT root resolver parents[3] -> parents[4] for one extra background_68 path component',
    inverse_byte_replacement_equals_original=True,remote_payload_system_model_thinking_profile_api_private_credentials_max_tokens_timeout_retry_logic_unchanged=True,
    diff=list(difflib.unified_diff(raw.decode().splitlines(),relocated.decode().splitlines(),fromfile='original/harness/quicktest3_isolated.py',tofile='background_68/harness/quicktest3_isolated.py',lineterm=''))))
write(HERE/'manual_old_history_review.json',dict(checked_at=now(),reviewer_role='Primary research worker personally read all14 full original raw responses, including long Plane449 messages in contiguous character chunks; no tail-only grading',
    index=str(HERE/'scoped_old_full_finals_read.json'),
    outcomes=[
        dict(question_id='Plane271',variant='v01',preset='C',response_files_found=0,status='Saved old draft; not used here'),
        dict(question_id='Plane367',variant='solid_target',preset='D',finals=['C','A'],hits=0),
        dict(question_id='Plane367',variant='triangle_salience',preset='D',finals=['E','D'],hits=1),
        dict(question_id='Plane367',variant='zigzag_salience',preset='C',finals=['E','E'],hits=0),
        dict(question_id='Plane387',variant='lattice_basis',preset='5.5',finals=['4.75*sqrt(3)','4.5'],hits=0),
        dict(question_id='Plane387',variant='triangle_outline',preset='12',finals=['8.5','5.5'],hits=0),
        dict(question_id='Plane387',variant='unit_diamond',preset='5.5',finals=['7.5','3.5'],hits=0),
        dict(question_id='Plane449',variant='side_label_role_binding_clean',status='Pre-API reject: slot overlays hidden by later black shared-edge strokes'),
        dict(question_id='Plane449',variant='side_label_role_confusion',status='Pre-API reject: coincident slot-edge actions duplicated with no distinct visible role'),
        dict(question_id='Plane449',variant='visible_side_label_role_binding',preset='B',finals=['E','E'],hits=0,status='Old source-slot color conflicts explicitly preserved and resolved by frozen r60 true4/8 source pairs; no retest')],
    all_old_candidate_images_actually_viewed=True,all_old_failed_presets_preserved=True,
    independent_objections_read=['Plane263/v01: whole-figure color lacks targeted geometric correspondence','Plane192/v03: isolated route salience and competitor weakening','Plane233/two_U: closed source boundaries reasonably become incompatible fixed partition','Plane295/inner_ear: plausible intrinsic drawing ink and small diagnostic feature','Plane342/quarterturn: printed-card redV must transport but no option matches','Plane242/r24: physical paper-edge ink/adjacency ambiguity, false quarter-containment lemma corrected'],
    application_to_this_scope='Current four candidates evaluated against actual wording/PNG; no blanket color ban, no false numerical equality, no new cut/paint/target, all mark roles individually stated. These are primary judgments, not independent approvals.'))
print('Only local PROJECT resolver changed in harness; full manual old-history review saved',flush=True)
