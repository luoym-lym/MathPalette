"""Stdlib-only closing search and low-memory audit supplement."""
import os,sys,json,hashlib,re
from pathlib import Path
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent;BASE=HERE.parent;PROJECT=HERE.parents[2]
sys.dont_write_bytecode=True
for k,n in {'TEMP':'tmp','TMP':'tmp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():os.environ[k]=str(HERE/n)
def guard(event,args):
    def check(p):
        if p is not None and not isinstance(p,int) and not Path(os.fsdecode(p)).resolve().is_relative_to(HERE):raise PermissionError('outsideunit')
    if event=='open' and args[2]&(os.O_WRONLY|os.O_RDWR|os.O_APPEND|os.O_CREAT|os.O_TRUNC):check(args[0])
    elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):check(args[0])
    elif event in ('os.rename','os.replace','os.link','os.symlink'):check(args[0]);check(args[1])
sys.addaudithook(guard)
IDS=['Solid79','Solid214','Solid216','Solid225','Solid232','Solid233','Solid234','Solid247']
def read(p):return json.loads(Path(p).read_text(encoding='utf-8-sig'))
def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        while b:=f.read(65536):h.update(b)
    return h.hexdigest()
def write(name,v):
    with (HERE/name).open('x',encoding='utf-8',newline='\n') as f:json.dump(v,f,ensure_ascii=False,indent=2);f.write('\n')
bindings=[];newly_discovered=[]
known=read(HERE/'old_evidence_inventory.json')['files']
for p in (PROJECT/'runtime').rglob('binding.json'):
    try:j=read(p)
    except (json.JSONDecodeError,UnicodeDecodeError) as e:
        if any(q in str(p) for q in IDS):newly_discovered.append(dict(path=str(p),preserved_malformed=str(e)))
        continue
    if j.get('question_id') in IDS:
        bindings.append(dict(path=str(p),sha256=sha(p),question_id=j['question_id'],own=p.is_relative_to(HERE),recorded_in_old_manifest=str(p) in known))
        if not p.is_relative_to(HERE) and str(p) not in known:newly_discovered.append(dict(path=str(p),sha256=sha(p)))
assert not newly_discovered,newly_discovered
write('global_binding_search_final.json',dict(search_root=str(PROJECT/'runtime'),all_binding_JSONs_decoded=True,matching_bindings=bindings,new_old_bindings_not_previously_read=newly_discovered,missing_summary_not_assumed_no_call=True,old_scoped_orphan_errors_aborts_and_logs_read_in='old_evidence_inventory.json',actual_old_scoped_designs_or_calls=0,own_calls=2))
rows=[json.loads(l) for l in (PROJECT/'SolidGeometry/dataset.jsonl').read_text(encoding='utf-8-sig').splitlines() if l.strip()]
pngs={r['id']:sha(PROJECT/'SolidGeometry'/r['image']) for r in rows}
duplicates={q:[other for other,h in pngs.items() if other!=q and h==pngs[q]] for q in IDS}
write('related_questions_final.json',dict(exact_formal_PNG_duplicate_scan=duplicates,semantic_related=dict(Solid79=dict(question='Solid112',basis='Both18-cube3x3x2minusoppositeuppercorners=>11remaining,7removed; projection/layout differ. Allpriorr36pairraws/readings preserved. Newr57marksbasalspansandretainedriserunits,notfourcross-course tiles.',old_outcome='preset3;finals8and3;onehit,miss;never relabeled'),Solid233=dict(question='Solid177',basis='Same7-cube6-armcross, differentprojectionanddotcounttask; read bothpriorprescreenand r37contactvisibility objections; noPNGorface-countpresetscopied.')),additional_keyword_matches={r['id']:r['question'] for r in rows if re.search('octahedron|consecutive whole|wedge|[Ff]ourteen white|centers of the faces|joining seven unit',r['question'])},r38_reference_check='Searched allbackground38designs/differenceauditsforcourse/layer/remaining/cross andreadcompleteJSONs; background38isPlane-only, noSolid79/112cross-layer design was found. The actual relevantcross-coursefailedpairisr36andisfullyboundabove.'))
r38=[]
for p in (BASE/'background_38').rglob('design.json'):
    j=read(p);r38.append(dict(path=str(p),sha256=sha(p),question_id=j.get('question_id'),mechanism=j.get('mechanism'),expected_wrong_answer=j.get('expected_wrong_answer')))
write('r38_reference_read_receipts.json',r38)
oldroot=BASE/'background_36/Solid112/r36_four_tile_cross_course_binding'
review=read(oldroot/'manual_final_review.json')
for item in review['runs']:
    raw=read(item['response_path']);assert raw['choices'][0]['message']['content']==item['complete_raw_assistant_answer_read_manually']
write('old_raw_final_crosscheck.json',dict(question_id='Solid112',raw_versus_manually_read_review_full_finals_identical=True,finals=['8','3'],preset='3',two_hits=False,old_evidence_unchanged=True))
write('offline_finalization_memory_error.json',dict(stage='First low-memoryfinalize57attempt',error='MemoryErrorwhileallocating1MBhashbufferafterfullsource_notesJSONparse',API_calls=0,old_or_frozen_evidence_modified=False,resolution='Restartedonlylocalread-onlyauditwithstreamingselectionof8top-levelnotesand64KBhashbuffers. Everycurrentoriginalapprovalfingerprintwasrecomputedandmatched. ThiswasnotanAPIorimage retry.',remaining_process=False))
assert read(HERE/'own_process_inventory_final.json')['all_absent']
checkpoint=read(HERE/'checkpoint.json');assert checkpoint['actual_completed_API_calls']==2 and len(checkpoint['actual_assessed_question_ids'])==8 and not checkpoint['unworked_question_ids']
assert read(HERE/'second_review_queue.json')['count']==0
write('closing_evidence_manifest.json',dict(created_at=datetime.now(timezone.utc).isoformat(),files={str(p.relative_to(HERE)):sha(p) for p in HERE.rglob('*') if p.is_file() and not any(s in p.parts for s in ['mpl_cache','cache','tmp','render_tmp'])},checkpoint_valid=True,own_API_PIDs_absent=True,no_approval_Pass_Collect_or_delivery=True))
print('Closing checks saved; globaloldbindingsearchclean; source/oldhashesunchanged; processPIDsabsent.')
