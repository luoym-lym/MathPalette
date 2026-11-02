import task_env
from task_env import OWN
from prepare import read,write
from datetime import datetime,timezone
d=OWN/'Plane479/r48_two_triangle_decomposition_omits_gray_wedge'
a=read(d/'frozen_evidence_audit.json')
decisions=[('1/3 (maps to C; final sentence has no letter)','Terminal value1/3 is unambiguous and equals choiceC, not preregisteredB=7/24. Its long looping narrative repeatedly misnames colored edges but ultimately includes the full pentagon via shoelace. Entire33,259-character final content was manually read, including the bounded middle supplement after tool-output truncation.'),('C; 1/3','Terminal choiceC and1/3 agree, notB=7/24. It eventually uses5/8+3/8 of a square to obtain1/3. Entire11,637-character content manually read; narrative mistakes are not reinterpreted as target hits.')]
runs=[]
for r,(answer,reason) in zip(a['runs'],decisions):
    runs.append({**r,'entire_raw_response_manually_read':True,'manual_terminal_answer':answer,'hits_unchanged_predeclared_preset':False,'manual_reason':reason})
write(d/'manual_final_review.json',{'question_id':'Plane479','variant_id':a['variant_id'],'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'preset_wrong_answer':'B','manual_runs':runs,'two_hits':False,'decision':'MISS','image_design_preset_unchanged':True,'first_call_elapsed_seconds':300.029,'second_call_elapsed_seconds':91.646,'long_first_call_completed_without_abort_timeout_override_or_retry':True,'no_mechanism_causal_or_statistical_claim':True,'parent_new_independent_review_required_for_any_future_candidate':True})
