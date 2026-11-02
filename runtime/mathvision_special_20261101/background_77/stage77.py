from audit77 import *
import shutil
from datetime import datetime,timezone

scan_report=read(HERE/'global_prior_invocation_scan.json')
assert sum(x['exact'] for x in scan_report['embedded_images'])==0
exact=[x for x in scan_report['matches'] if {'png_sha','exact_b64','exact_file_bytes'} & set(x['match'])]
def is_transport(label):
    name=Path(label.split('!')[-1]).name.lower()
    return name in ('request.json','binding.json','summary.json') or bool(re.fullmatch(r'run_\d+(_started|_response)?\.json',name))
assert not [x for x in exact if is_transport(x['path'])]
bad=[x for x in scan_report['errors'] if {'png_sha','exact_b64','exact_file_bytes'} & set(x.get('matching',[])) or QID in x['path'] or VARIANT in x['path']]
assert not bad,bad
# Refresh every live invocation artifact immediately before copying/calls.
new_scan=[];api_files=0
for directory,dirs,files in os.walk(BASE):
    dirs[:]=[d for d in dirs if (Path(directory)/d).resolve()!=HERE]
    for name in files:
        p=Path(directory)/name
        if not is_transport(str(p)):continue
        api_files+=1
        try:data=p.read_bytes()
        except FileNotFoundError:continue
        if TARGET_SHA.encode() in data or base64.b64encode((SOURCE/'candidate.png').read_bytes()) in data:
            new_scan.append(dict(path=str(p),sha256=hashlib.sha256(data).hexdigest()))
        del data
assert not new_scan,new_scan
e=eligibility();assert e['eligible'] and e['original_approval_current']
initial=read(HERE/'eligibility_initial.json');assert e['current_content_sha256']==initial['current_content_sha256'] and e['source_hashes']==initial['source_hashes']
source_hashes=read(HERE/'source_input_hashes_initial.json')
assert {name:sha(SOURCE/name) for name in source_hashes}==source_hashes
replay=read(HERE/'offline/replay_verification.json')
assert replay['matches_tested_png_bytes'] and replay['two_delivery_replays_identical'] and replay['formal_inputs_unchanged'] and replay['png_sha256']==TARGET_SHA
assert sha(SOURCE/'candidate.png')==sha(SOURCE/'repeat.png')==TARGET_SHA
parent74=BASE/'background_74'
prior74hash={str(p.relative_to(parent74)):sha(p) for p in parent74.rglob('*') if p.is_file()}
target=HERE/QID/VARIANT;target.mkdir(parents=True,exist_ok=False)
for name,h in source_hashes.items():
    shutil.copyfile(SOURCE/name,target/name);assert sha(target/name)==h
now_utc=now()
primary={'checked_at':now_utc,'kind':'Fresh parent PRIMARY only, not independent second review','question_id':QID,'variant_id':VARIANT,'correct_answer':'C=151','immutable_preset':'D=192','source_JPG_formal_PNG_candidate_actually_viewed':True,'unique_math_proof':'Cylinder radius4,length6,volume96pi. The two actual cut-contact endpoints (0,0,-4),(6,0,4) are antipodal about center(3,0,0). Any plane through them contains the center; central inversion of the cylinder swaps the two sides. Each wedge volume48pi=150.796447..., uniquely closest C151. The actual frozen plane x=3+3z/4 also directly integrates to48pi. No need to claim two endpoints uniquely determine every arbitrary plane. The unchanged wrong maximum6 hypothesis gives96pi~301.59, uniquely closest listed D192.','every_marker':[{'target':'line_2','role':'Actual6cm top axial generator, providing maximum cut extent source.','human_preservation':'Existing edge only, same centerline;6cm printed dimension and8cm diameter fully readable.'},{'target':'cut_section','role':'Existing variable cuttrace receiver; shared blue relates actual maximal to varying extent.','human_preservation':'Existing dashed conic retained, no new face/cut/point/equality; all original cylinder contours visible.'}],'semantics':'Numerical volume, either cut side equal by symmetry, no paint/pattern-identity or added-condition ambiguity. Same color supplies an annotation comparison, no explicit equality.','concision':'Only2 useful real-object styles, no decorative extras','schema_noop_and_exact_replay':replay,'local_import_failure_fixed':'Executable own77 files resolve their own bootstrap; old74 audit command and HOLD remain unchanged.','limitations':['Two future observations only; no mechanism/causal/statistical claim.','No independent review or user Pass/Collect.']}
write('primary_parent_review.json',primary)
provenance={'checked_at':now_utc,'source_directory':str(SOURCE),'target_directory':str(target),'original_variant_id':VARIANT,'original_date':read(SOURCE/'design.json')['created_at'],'original_preset':read(SOURCE/'design.json')['expected_wrong_answer'],'frozen_source_and_copy_sha256':source_hashes,'copy_bytes_equal':True,'global_scan':str(HERE/'global_prior_invocation_scan.json'),'global_exact_embedded_requests':0,'global_exact_transport_matches':[],'global_target_related_malformed_errors':[],'immediate_current_transport_artifacts_scanned':api_files,'immediate_current_transport_matches':new_scan,'prior_actual_API_calls':0,'old_local_startup_import_failures_not_HTTP_calls':True,'old74_hashes_before_parent_testing':prior74hash,'fresh_eligibility':e,'fresh_exact_replay':replay,'new_designs':0,'old57_or74_files_edited':False}
(target/'reuse_provenance.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
gate={'checked_at':now_utc,'all_gates_passed':True,'actual_prior_API_calls':0,'image_sha256':sha(target/'candidate.png'),'design_sha256':sha(target/'design.json'),'plugin_sha256':sha(target/'plugin.json'),'preset':'D','correct':'C','requested_runs':2,'primary_review':str(HERE/'primary_parent_review.json'),'reuse_provenance':str(target/'reuse_provenance.json'),'no_retry_or_parameter_changes':True}
write('prelaunch_gate.json',gate)
print(json.dumps({'all_gates_passed':True,'global_exact_prior_requests':0,'immediate_transport_files':api_files,'frozen_copy_identical':True,'unique_answer':'C151','immutable_preset':'D192','new_API_calls':0}))
