"""Memory-bounded checkpoint finalization. Standard library only, no project imports."""
import os, sys, json, hashlib, mmap
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F

HERE=Path(__file__).resolve().parent; BASE=HERE.parent;PROJECT=HERE.parents[2];BRANCH=PROJECT/'SolidGeometry'
sys.dont_write_bytecode=True
for key,name in {'TEMP':'tmp','TMP':'tmp','TMPDIR':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():
    target=HERE/name;target.mkdir(exist_ok=True);os.environ[key]=str(target)
def check(p):
    if p is not None and not isinstance(p,int) and not Path(os.fsdecode(p)).resolve().is_relative_to(HERE):raise PermissionError('Write outside background_55')
def guard(event,args):
    if event=='open' and args[2]&(os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
sys.addaudithook(guard)
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for c in iter(lambda:f.read(65536),b''):h.update(c)
    return h.hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False).encode()).hexdigest()
def write(p,d):
    with Path(p).open('x',encoding='utf-8',newline='\n') as f:json.dump(d,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
def row(p,q):
    with Path(p).open('r',encoding='utf-8-sig') as f:
        for line in f:
            if line.strip():
                r=json.loads(line)
                if r.get('id',r.get('question_id'))==q:return r
    return None
def top_entry(p,key):
    # Read just the exact top-level object value, without decoding the 18MB source-notes document.
    with Path(p).open('rb') as f,mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ) as m:
        needle=json.dumps(key).encode();pos=m.find(needle)
        assert pos>=0,key
        pos=m.find(b':',pos+len(needle))+1
        while m[pos] in b' \n\r\t':pos+=1
        assert m[pos]==ord('{')
        start=pos;depth=0;quoted=False;escape=False
        while pos<len(m):
            c=m[pos]
            if quoted:
                if escape:escape=False
                elif c==92:escape=True
                elif c==34:quoted=False
            elif c==34:quoted=True
            elif c in [123,91]:depth+=1
            elif c in [125,93]:
                depth-=1
                if depth==0:return json.loads(m[start:pos+1])
            pos+=1
        raise ValueError('Unterminated note object')

ids=['Solid195','Solid200','Solid205','Solid206','Solid207','Solid208','Solid209','Solid210']
old=read(HERE/'old_evidence_inventory.json');old_final={}
for q,files in old.items():
    old_final[q]=[dict(**f,current_sha256=sha(PROJECT/f['path']),unchanged=sha(PROJECT/f['path'])==f['sha256']) for f in files]
assert all(f['unchanged'] for files in old_final.values() for f in files)
write(HERE/'old_evidence_preservation_final.json',dict(checked_at=now(),scoped_question_ids=ids+['Solid96','Solid163'],files=old_final,all_unchanged=True))

current={};preservation={};baseline=read(HERE/'eligibility_start.json')
approvals=read(PROJECT/'provenance/approvals.json')['approvals']
for q in ids:
    r=row(BRANCH/'dataset.jsonl',q);before=baseline[q];files={}
    for p in before['scoped_files']:files[p]=sha(BRANCH/p)
    notes=top_entry(PROJECT/'provenance/source_notes.json',q)
    payload=dict(branch='SolidGeometry',record=r,files=files,source_notes=notes)
    a=approvals[q];accepted=row(BRANCH/'special_variant/accepted_index.jsonl',q);collected=row(BRANCH/'special_variant/collected_index.jsonl',q)
    special=BRANCH/'special_variant'/q
    plugins=list((special/'plugins').glob('*.json'));images=list((special/'images').glob('*.png'))
    collection=read(special/'collection.json') if (special/'collection.json').is_file() else None
    rootrow=row(PROJECT/'question_bank.jsonl',q)
    eligible=r['source_dataset']=='MathVision' and a.get('reviewer')=='user' and bool(a.get('instruction')) and bool(a.get('approved_at_utc')) and digest(payload)==a['content_sha256'] and not accepted and not collected and not plugins and not images and not (collection and collection.get('current')) and not rootrow.get('special_plugins')
    assert eligible,q
    initial=read(HERE/q/'source_hashes_initial.json');checks={p:dict(before=h,current=sha(PROJECT/p),unchanged=sha(PROJECT/p)==h) for p,h in initial.items()}
    assert all(v['unchanged'] for v in checks.values()),q
    preservation[q]=checks
    current[q]=dict(checked_at=now(),question_id=q,record_sha256=digest(r),record=r,approval=a,current_content_sha256=digest(payload),approval_matches=True,eligible=eligible,
       accepted=accepted,collected=collected,collection=collection,plugins=[str(p) for p in plugins],images=[str(p) for p in images],root_special_plugins=rootrow.get('special_plugins'),scoped_files=files)
write(HERE/'eligibility_final.json',current)
write(HERE/'source_preservation_final.json',dict(checked_at=now(),all_scoped_source_hashes_unchanged=True,checks=preservation,
    scope='Current assigned formal record/image/original/scene/script/dependencies, approval and shared helper inputs. No claim about unrelated concurrent workspace changes. Runtime progress hashes are diagnostic only; no old snapshots rewritten.'))

# Correct the untested Solid208 slice-detail error while retaining the original audit.
m=read(HERE/'Solid208/primary_math.json');m['original_inaccurate_audit_sha256']=sha(HERE/'Solid208/primary_math.json')
m['integrals']=['1/48','1/8 = 6/48']
m['proof']='In the actual coordinates, D=(0,1,0), M=(1/2,0,0), N=(1,1,1/2) determine2x+y-4z=1, also meeting BF atP=(1,0,1/4). The full section isD-M-P-N. The small solid height=(2x+y-1)/4 above base region2x+y>=1. For0<=x<=1/2, the y-integral over1-2x..1 isx^2/2; its x-integral is1/48. For1/2<=x<=1, the y-integral over0..1 isx/2-1/8; its x-integral is1/8. Total7/48, larger41/48, answer89. The initial incorrect split is preserved separately and has no candidate/API dependency.'
first=F(1,2)*F(1,2)**3/3;second=(F(1,4)-F(1,8))-(F(1,16)-F(1,16))
assert first==F(1,48) and second==F(1,8) and first+second==F(7,48)
write(HERE/'Solid208/primary_math_v2.json',m)

q='Solid195';d=HERE/q/'r55_two_arc_procedure_unit_binding';test=next((d/'tests').iterdir());summary=read(test/'summary.json');design=read(d/'design.json')
assert summary['two_completed'] and summary['expected_wrong_answer']=='3' and sha(d/'candidate.png')==summary['image_sha256'] and sha(d/'design.json')==summary['design_sha256']
assert sha(test/'request.json')==summary['request_body_sha256'] and sha(test/'design_snapshot.json')==sha(d/'design.json')
manual=[]
for i,answer in [(1,'7'),(2,'6')]:
    raw=test/f'run_{i:02d}_response.json';r=read(raw);parsed=read(test/f'run_{i:02d}.json');bind=read(test/f'run_{i:02d}_started.json')
    assert parsed['status']=='completed' and parsed['response_sha256']==sha(raw) and bind['request_body_sha256']==summary['request_body_sha256']
    manual.append(dict(run_index=i,manually_read_complete_final=True,complete_answer_text=r['choices'][0]['message']['content'],manual_final_answer=answer,unambiguous_preset_hit=False,
      finish_reason=r['choices'][0]['finish_reason'],raw_response_path=str(raw.relative_to(PROJECT)),raw_response_sha256=sha(raw),
      notes='Final7; invalid cancellation of spatial turns and a seven-step trace.' if i==1 else 'Final6 matches formal answer, but narrative falsely flattens the six junctions to a planar hexagon with60degree turns. Correct final does not validate its reasoning.'))
write(d/'manual_final_review.json',dict(expected_wrong_answer_immutable='3',image_sha256=summary['image_sha256'],design_sha256=summary['design_sha256'],results=manual,two_target_hits=False,actual_calls=2,no_API_retry=True,no_posthoc_preset_change=True))

reasons={
 'Solid200':'The actual24-rotation proof has one compatible orientation,18 forced whites,5 forced grays and4 free cells. The12 repeated whites make a raw double-subtraction count negative(-3); hidden-center omission would predict8 but has no visible source/receiver. New gray-count marks would risk material identity. No credible concise wrong correspondence retained; related Solid163 old prescreens independently reproduced, not cloned.',
 'Solid205':'Actual side-by-side joining keeps axial height and doubles circumference. Source seams can only identify the true same-height correspondence. The proposed additive-air-volume200 mechanism repeats the already failed Solid96 rim-to-volume transfer; pairing height to circumference would be an arbitrary unrelated role with no clean original receiver. No real unfolded rectangle is drawn to support a new axial-unit hypothesis. No cosmetic copy or calls.',
 'Solid208':'Exact plane gives real quarter-pointP onBF, not a midpoint. The old triangleD-M-N preset23 pair ended7/29, not23. New half/quarter matching cannot supply one consistent wrong plane: keepingD,M,N fixesP at1/4, while treatingP as1/2 contradicts that plane. An added fake midpoint is forbidden; different arbitrary triangulations of a nonplanar four-point cap give different wrong volumes. No defensible single new preset retained.',
 'Solid209':'The full sphere tangencies forcecot(alpha)=24/23 and foot distance312/23. A90degree guess yields13 but contradicts the sphere distances. The desired small-sphere tangency foot is not a shown silhouette/equator point; mapping an actual visible contour to that foot would falsely identify the geometry. Adding a hidden center/foot construction through the visible spheres is not a simple human-clear original correspondence. No right-angle mark or new tangent drawn.',
 'Solid210':'CorrectR7,slant10,axis sqrt51 uniquelyC. Radius10-as-base and complementary108degree arc errors match no option. The only natural offered same-radius wrong optionD is the exact old radius-to-axis mechanism, which already returnedC/C against presetD. Adding a correct arc/circumference mark to it supplies no substantially new wrong geometry. A/E require unmotivated arithmetic or option salience. No cosmetic retry.'}
assessments=[]
names={'Solid195':'r55_two_arc_procedure_unit_binding','Solid206':'r55_equilateral_end_to_ridge_prism_binding','Solid207':'r55_source_halfside_to_full_panel_scale'}
for q in ids:
    a=dict(question_id=q,assessed=True,native_formal_PNG_and_source_JPG_viewed=True,current_eligible=current[q]['eligible'],original_approval_current=current[q]['current_content_sha256'],
      baseline_check=str((HERE/q/'baseline_check.json').relative_to(PROJECT)),primary_math_path=str((HERE/q/('primary_math_v2.json' if q=='Solid208' else 'primary_math.json')).relative_to(PROJECT)),
      old_evidence_paths_and_hashes=str((HERE/'old_evidence_inventory.json').relative_to(PROJECT)))
    if q in names:
        cd=HERE/q/names[q];files={p.name:sha(p) for p in cd.iterdir() if p.is_file() and p.name in ['candidate.png','repeat.png','design.json','plugin.json','design_difference_audit.json','primary_visual_marker_review.json','render_check.json','context.json']}
        a.update(candidate_path=str(cd.relative_to(PROJECT)),candidate_files_sha256=files,design_difference_audit=str((cd/'design_difference_audit.json').relative_to(PROJECT)),primary_marker_native_review=str((cd/'primary_visual_marker_review.json').relative_to(PROJECT)))
        if q=='Solid195':a.update(status='tested_preset_miss',expected_wrong_answer='3',manual_finals=['7','6'],actual_API_calls=2,evidence_summary=str((test/'summary.json').relative_to(PROJECT)),two_target_hits=False)
        else:a.update(status='frozen_native_reviewed_untested_due_host_memory_failure',actual_API_calls=0,expected_wrong_answer=read(cd/'design.json')['expected_wrong_answer'],not_a_failed_or_aborted_API_image=True)
    else:a.update(status='screened_no_distinct_human_clear_hypothesis',reason=reasons[q],actual_API_calls=0)
    assessments.append(a);write(HERE/q/'assessment_final.json',a)

failures=read(HERE/'local_failures.json');failures['failures'].append(dict(phase='Solid206_pre_API_current_approval_read',error='MemoryError while catalog.content read/decode of provenance/source_notes.json, before subprocess launch.',actual_API_calls_for_this_candidate=0,no_started_API_evidence=True,
    external_host_resource_snapshot=dict(free_physical_KiB=279064,free_virtual_KiB=237788,total_visible_KiB=32987452,total_virtual_KiB=94676152,source_notes_bytes=18192378),
    disposition='Stop genuine resource failure/checkpoint; no model/API error or retry. All8 questions have been assessed,195pair complete,206/207frozen untested.'))
write(HERE/'failures_final.json',failures)
queue=dict(stage='material_refinement',unit='background_55',created_at=now(),candidates=[],credible_two_hit_count=0,requires_NEW_parent_second_review_before_any_delivery=True,
    reason='Only tested new pair195missed preset3 in both finals7/6; two further native-reviewed drafts have zero API calls due host-memory failure. No historical pair promoted.')
write(HERE/'second_review_queue.json',queue)
checkpoint=dict(unit='background_55',stage='material_refinement',finished_at=now(),status='checkpointed_host_resource_failure_all8_assessed',
    stop_reason='Eight assigned questions assessed. A genuine host resource failure prevented launching Solid206; no further API work attempted. Available virtual memory237788KiB. This was NOT an external API error.',
    actual_assessed_question_ids=ids,unworked_question_ids=[],unworked_ids=[],API_test_unworked_ids=['Solid206','Solid207'],
    assessed_count=8,new_design_count=3,completed_candidate_pairs=1,actual_API_calls=2,API_errors=0,API_aborts=0,API_retries=0,credible_two_hit_count=0,
    old_vs_new=dict(old={'Solid195':'no design/calls','Solid200':'no design/calls; related163same exact enumeration family','Solid205':'no design/calls; related96v1rejected beforeAPI,v2D/Dmissed presetA',
      'Solid206':'no design/calls','Solid207':'no design/calls','Solid208':'old preset23,full finals7/29; both wrong but both misses','Solid209':'no design/calls','Solid210':'old presetD,full finalsC/C; misses'},
      new={'Solid195':'True six-step route grouped into3two-arc units; preset3,full finals7/6,MISS','Solid206':'Real equilateral end-face correspondence and2s ridge as false prism length; preset216sqrt6,frozen untested','Solid207':'Source true6half-side paired to full12Aedge; preset108,frozen untested','others':'Skipped with independently proved answers and exact geometric/material reasons; no cosmetic trials'}),
    assessments=assessments,raw_binding_audit=str((d/'manual_final_review.json').relative_to(PROJECT)),full_manual_finals=manual,
    source_final=str((HERE/'source_preservation_final.json').relative_to(PROJECT)),old_evidence_final=str((HERE/'old_evidence_preservation_final.json').relative_to(PROJECT)),
    eligibility_final=str((HERE/'eligibility_final.json').relative_to(PROJECT)),failures=str((HERE/'failures_final.json').relative_to(PROJECT)),second_review_queue=str((HERE/'second_review_queue.json').relative_to(PROJECT)),
    source_and_old_scoped_hashes_unchanged=True,current_all8_approval_and_MathVision_noPass_noCollect_noSpecialCompletion=True,
    process_closure=dict(own195helper_pid=17164,own195exit=read(d/'process_completed.json'),own_API_processes_expected_live=[],own_process_snapshot_path=str((HERE/'process_audit_final.json').relative_to(PROJECT))),
    formal_state_changed=False,approval_Pass_Collect_delivery_actions=False,nested_agents_threads_worktrees=False,
    limitations=['No original controls existed for the new195pair and none were repeated. No incremental-effect or mechanism-confirmation claim.',
       'All primary math/native/marker reviews are by the designer. No independent second review performed; parent must create a NEW independent task for any future qualifying possibility.',
       'Solid208 initial split-integral detail was wrong though total/answer correct; initial file retained, correction and authoritative v2 saved.',
       '206/207 are not failed API candidates and have never been sent; any parent continuation must preserve this distinction and the immutable image/preset bytes.'])
write(HERE/'checkpoint.json',checkpoint)
print(json.dumps({k:checkpoint[k] for k in ['status','actual_assessed_question_ids','new_design_count','completed_candidate_pairs','actual_API_calls','credible_two_hit_count','API_test_unworked_ids']},ensure_ascii=False))
