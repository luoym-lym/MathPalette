from bootstrap import *
import runpy
q='Solid226';e=next(e for e in read(OWN/'first_pair_candidates.json') if e['question_id']==q)
source=Path(e['candidate_directory']);output=OWN/'fresh_replay'/q
save('local_replay_first_failure_226.json',{'at_utc':now(),'stage':'Before model request, canonical validator output.mkdir audit guard','original_command':'python -X utf8 -B units/u12_surface_material_followup/replay.py Solid226','error_class':'PermissionError','original_message':'u12 own-runtime write guard: '+str(output),'callsite':'canonical validate_candidate_replay.py line27 -> pathlib.mkdir -> unchanged bootstrap.guard line20','original_canonical_helper_unchanged':True,'model_API_calls_affected':0,'interpretation':'Exact rejected resolved path/OWN state at the original instant was not captured. No claimed root cause. Original failure retained; strict offline sequential diagnostic only, no relaxation or model retry.'})
runtime=ROOT/'runtime'
paths={'OWN':OWN,'runtime':runtime,'candidate':source,'output':output,'canonical_validator':OLD/'validate_candidate_replay.py'}
save('replay_preflight_diagnostic226.json',{'at_utc':now(),'paths':{k:{'str':str(p),'resolved_str':str(p.resolve()),'parts':list(p.resolve().parts),'exists':p.exists()} for k,p in paths.items()},'candidate_in_runtime':source.resolve().is_relative_to(runtime.resolve()),'output_in_runtime':output.resolve().is_relative_to(runtime.resolve()),'output_in_OWN':output.resolve().is_relative_to(OWN),'candidate_hash':sha(source/'candidate.png'),'expected_candidate_hash':e['PNG_sha256'],'canonical_validator_sha256':sha(OLD/'validate_candidate_replay.py'),'no_guard_path_or_renderer_code_changes':True})
assert output.resolve().is_relative_to(OWN) and source.resolve().is_relative_to(runtime.resolve())
sys.argv=['validate_candidate_replay.py','--question',q,'--candidate',str(source),'--output',str(output)]
runpy.run_path(str(OLD/'validate_candidate_replay.py'),run_name='__main__')
save('local_replay_resolution226.json',{'at_utc':now(),'fresh_strict_canonical_replay_passed':True,'replay_verification_sha256':sha(output/'replay_verification.json'),'candidate_hash':sha(source/'candidate.png'),'expected_hash':e['PNG_sha256'],'source_and_guard_unchanged':True,'cause_of_original_rejection_not_established':True,'model_API_calls':0})
