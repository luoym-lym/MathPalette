import task_env
from task_env import OWN,BASE
from inspect_sources import read,save,sha,QIDS
from datetime import datetime,timezone
from pathlib import Path
import numpy as np

dispatch=read(BASE/'refinement_dispatch_20261102.json')
unit=next(u for u in dispatch['units'] if u['unit']=='background_44')
assert unit['question_ids']==QIDS
overlaps=[{'unit':u['unit'],'question_ids':sorted(set(QIDS)&set(u['question_ids']))}
          for u in dispatch['units'] if u['unit']!='background_44' and set(QIDS)&set(u['question_ids'])]
assert not overlaps
save(OWN/'scope_audit_final.json',{'checked_at_utc':datetime.now(timezone.utc).isoformat(),
    'dispatch_path':str(BASE/'refinement_dispatch_20261102.json'),
    'dispatch_sha256':sha(BASE/'refinement_dispatch_20261102.json'),
    'reserved_unit':unit,'exact8_assignment_match':True,'other_refinement_unit_overlaps':overlaps,
    'all_new_files_only_under':str(OWN),'main_ledger_read_only_no_state_update':True})

folder=OWN/'Plane415/r44_exposed_radius_to_contact_seam'
paths=read(folder/'path_fingerprints.json')
source=np.array(paths['leftbigupper'][0]['controls'][-1])
receiver=np.array(paths['rightbigright'][0]['controls'][-1])
styled=np.array(paths['rightbigleft'][0]['controls'][0])
assert np.allclose(source+[7,0],receiver,atol=1e-13)
assert np.allclose(receiver,styled[::-1],atol=1e-13)
save(folder/'shared_seam_ownership_clarification.json',{
    'purpose':'Exact object-owner clarification; frozen design/preset/image/request/response bytes unchanged.',
    'source_material_piece':'leftbigupper, whose selected vertical closing radius is translated by(7,0) into rightbigright vertical closing radius.',
    'visible_style_target':'rightbigleft first radius: this is the SAME geometric seam, with reversed path direction, shared by both upper quarter pieces. The later-drawn owner is styled to make the shared seam visible.',
    'source_controls':source.tolist(),'actual_same_piece_receiver_controls':receiver.tolist(),
    'styled_common_seam_controls':styled.tolist(),'coincident_reversed_paths_verified':True,
    'primary_wording_qualification':'same-piece translation refers to the co-owning rightbigright material radius; it does not claim that the entire leftbigupper quarter translates to the rightbigleft quarter.',
    'mechanism_unchanged':'One10cm exposed radius is wrongly retained as a perimeter contribution after it becomes a shared internal seam.',
    'not_posthoc_preset_or_mechanism_change':True,'outcome_unchanged':'10/20; immutable preset10 missed as a pair.'})

checkpoint=read(OWN/'checkpoint.json')
checkpoint['scope_audit']=str(OWN/'scope_audit_final.json')
checkpoint['Plane415_shared_seam_owner_precision']=str(folder/'shared_seam_ownership_clarification.json')
save(OWN/'checkpoint.json',checkpoint)
manifest={str(p.relative_to(OWN)):{'sha256':sha(p),'bytes':p.stat().st_size} for p in OWN.rglob('*')
          if p.is_file() and not any(x in p.relative_to(OWN).parts for x in ['cache','tmp','mpl_cache','render_tmp']) and p.name!='evidence_manifest.json'}
save(OWN/'evidence_manifest.json',{'created_at_utc':datetime.now(timezone.utc).isoformat(),'files':manifest,
     'excluded_runtime_caches':['cache','tmp','mpl_cache','render_tmp'],'all_outputs_confined_to_own_root':True})
print('Exact8 scope has no other refinement overlap. Plane415 co-owned seam clarified without changing any frozen evidence. Checkpoint/manifest complete.')
