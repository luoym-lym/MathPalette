import research_env as env
import json,difflib
from inspect_sources import save,sha,now,QIDS

def main():
 old={'Solid80':{'preset':'11','finals':['10','10'],'hits':0,'note':'Old removed-corner dot missed both times; no original control.'},
      'Solid90':{'preset':'sqrt(55)','finals':['sqrt(-17), explicitly no real solution','9'],'hits':0,'note':'Both wrong but neither matches original preset; not relabelled.'},
      'Solid107':{'preset':'10','finals':['9','12'],'hits':0,'note':'Both wrong but preset missed twice; unsupported right-angle/equality assertions in raw text are not source conditions.'},
      'Solid159':{'preset':'13','finals':['13','17'],'hits':1,'note':'One target hit only; no retry.'}}
 save(env.ROOT/'old_manual_final_review.json',{'created_at_utc':now(),'entire_raw_responses_manually_read':True,'all_four_old_PNGs_opened_original_detail':True,'results':old,
  'historical_parsefailures_in_relevant_evidence':[],'old_file_hash_index':'old_evidence_full_index.json','all_old_raw_bytes_read_only':True,'no_old_unreviewed_two_target_pair':True,
  'screened_only':{'Solid89':'Old background13 checkpoint: centered holes union7, no saved clean aperture hypothesis.','Solid163':'Old background16 full prescreen and primary_proofs rotation check read; no clean wrong count chosen.','Solid171':'Old background16 full prescreen read: rejected phantom edges/new hidden counting marks; no saved candidate.','Solid172':'Old background18 full assessment read: independent17, no saved design or calls.'}})
 notes={
 'Solid80':'Six dots coincide with existing U/V/W and three retained old endpoints. The removed phantom corner p101 has no new dot. Three existing remnants visibly pair old blue with new red endpoints. No dot is at a crossing or a new location. The cut triangle and all original dashed stubs remain readable. Count target is current physical vertices, unaffected by ink color.',
 'Solid89':'Three red L-shaped unit rim pairs are actually visible at the three distinct real apertures. Gray near walls, front far white opening and all other rims remain recognizable. Some red rim centers are overdrawn black by duplicate original contour artists; marginal-pixel checks confirm every action still visibly contributes. Unit depth3 comes from the question, not from the shown first-unit internal walls. No new bore or hidden center is drawn. Weight/material geometry does not acquire a color-transport restriction.',
 'Solid90':'All four X/Y/Z/A labels remain distinct. Three red face diagonals form exactly the given XYZ group; the blue dashed XA is the original requested body diagonal. Original solid/dashed differences, cube edges and unmarked projection crossing remain clear. No right-angle/equality mark is added. A careful human still uses the factor2 and obtains10.',
 'Solid107':'The four labels7,4,2,3 stay attached to original AD/CB/AB/DC. Two color pairs bind to distinct portions of the same hidden AC, with no dot at the color transition or DB crossing. The false pairs are visibly nonincident edges, so a human can reject their triangle interpretation using actual vertices. No equality or right angle is asserted; all six original tetrahedral edges remain traceable. The information role is pair-to-bound incidence transfer, not a direct4-label copy.',
 'Solid159':'Local red stars at L,T,B show respectively4,3,3 actual incidence arms. Each arm is a short portion of a real existing edge and all black continuations and original hidden LR persist. Original1 atT and5 atL are legible and only five vertices exist; screen crossing remains unmarked. Three local counts, with ten required arms, carry the prospective multiplicity4-to3 transfer; they do not change vertex classes or introduce equality conditions.',
 'Solid171':'One actual existing triangular cut face has its three edges red, and the adjacent old retained edge remnant is red. These are four separate actual remaining-body edges, visibly one long segment versus a triangle boundary. All original phantom dashed corner stubs remain black and are not counted as body edges. No original hidden edge is added, face fill changed or triangle erased. Colored ink cannot alter the numerical graph edge count36.',
 'Solid172':'Two blue three-visible-arm tripods are visible around L=5 andR; all six portions end on original edges. The fourth L/R incidence is the preserved black dashedLR, so careful degree checking identifiesL/R as equatorial, not apex vertices. T/B and the centralF are unchanged, and1/5 remain clearly located atT/L. Five vertices and six true triangular faces are traceable; color adds no new numerical or face condition.'}
 for q,note in notes.items():
  d=next((env.ROOT/q).glob('r49_*'))
  design=json.loads((d/'design.json').read_text(encoding='utf-8'));render=json.loads((d/'render_check.json').read_text(encoding='utf-8'))
  save(d/'primary_review.json',{'question_id':q,'variant_id':design['variant_id'],'review_level':'PRIMARY_ONLY; NOT independent second review','reviewed_at_utc':now(),
    'candidate_sha256':sha(d/'candidate.png'),'design_sha256':sha(d/'design.json'),'actual_source_JPG_and_formal_PNG_opened':True,'actual_frozen_candidate_native_768_opened':True,
    'unique_original_math_independently_checked':True,'formal_answer_preserved':True,'native_findings':note,
    'per_marker_groups':[{'action_index':r['action_index'],'information_role':r['role'],'visible_marginal_pixels':render['per_action_visibility_ablations'][r['action_index']]['changed_pixels_if_removed'],
      'legality':'exact original path interval or actual original vertex; schema/default validation passed','necessity':'counts one incidence/endpoint/rim side or binds one declared source/receiver; no empirically minimal-marker claim','human_semantics':'original count/label/object identity preserved; no new equality/right-angle/text/fill/geometry condition'} for r in design['marker_roles']],
    'annotation_semantics_lesson_applied_case_specifically':True,'legal_targeted_concise_human_clear_primary_judgment':True,'proceed_to_exact_two_calls':True,
    'limits':['Prospective mechanism is not proved by final-answer observations.','Human clarity is primary research judgment; parent NEW independent second review remains mandatory.']})
 save(env.ROOT/'Solid163/assessment.json',{'question_id':'Solid163','assessed':True,'status':'screened_no_clean_material_hypothesis','actual_source_JPG_and_formal_PNG_opened_native':True,
  'independent_math_path':str(env.ROOT/'Solid163/primary_math_proof.json'),'verified_all_24_rotations':True,'compatible_orientations':1,'forced_white_cubes':18,'forced_black_cubes':5,'free_cubes':4,'maximum_black':9,
  'considered_directions':[{'proposal':'bind repeated white cells across the two views, then duplicate-subtract them','finding':'True mapping has12 duplicated whites; raw face-based white tally30 would give negative remainder-3, not a credible maximum. Correctly matching whites helps identify their union rather than supporting a distinct reasonable wrong preset.'},
   {'proposal':'omit unseen center to predict8','finding':'There are4 free cells including center(1,1,1). Center omission would give8, but no allowed original visible object corresponds to that hidden center. Marking arbitrary shell rims would not convey the missing interior information; drawing a center/new hidden cube would change source display/count targets.'},
   {'proposal':'false stationary corner/face correspondence','finding':'As in old prescreen, false rotations either conflict with existing black/white cells or leave the same maximum9; no distinct defensible simple wrong-count mechanism.'}],
  'reason':'No clean targeted source/receiver annotation selected after exact constraints and original black/white identity review. Do not test arbitrary outline/vertex decoration or recolor semantic fill to force a quota.',
  'designs':0,'calls':0,'not_unworked':True,'not_a_claim_of_universal_impossibility':True})
 # Keep all provider/solver functions identical; only adapt copied harness root lookup to its extra directory level.
 source=env.SHARED/'harness/quicktest3_isolated.py'; target=env.ROOT/'harness/quicktest3_isolated.py';target.parent.mkdir(exist_ok=True)
 oldtext=source.read_text(encoding='utf-8');newtext=oldtext.replace('PROJECT = Path(__file__).resolve().parents[3]','PROJECT = Path(__file__).resolve().parents[4]')
 assert newtext!=oldtext and newtext.replace('PROJECT = Path(__file__).resolve().parents[4]','PROJECT = Path(__file__).resolve().parents[3]')==oldtext
 target.write_text(newtext,encoding='utf-8',newline='\n')
 save(env.ROOT/'harness_isolation_audit.json',{'shared_harness':str(source),'shared_sha256':sha(source),'own_harness':str(target),'own_sha256':sha(target),
  'only_source_change':'PROJECT parent index3=>4 for extra background_49 directory','diff':list(difflib.unified_diff(oldtext.splitlines(),newtext.splitlines(),lineterm='')),
  'solver_payload_API_profile_timeout_token_limits_parsers_no_retry_loop_unchanged':True,'guard_before_harness_import':'api_runner.py imports research_env before runpy execution','all_harness_cache_dirs_inside_own_root':True})
 print('Saved7 primary reviews, Solid163 concrete skip, old final review, isolated harness.')
if __name__=='__main__':main()
