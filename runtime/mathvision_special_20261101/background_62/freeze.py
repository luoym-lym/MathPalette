from bootstrap import install,OWN,PROJECT,SESSION
install()
from gates import sha,load,save,now,eligibility
from pathlib import Path
import sys,json,re,ast,difflib,gc

def supplemental_scan():
    targets={q['PNG_sha256']:q['question_id'] for q in load(SESSION/'background_62_assignment.json')['questions']}
    dup=[];total=0
    for p in SESSION.rglob('*.png'):
        if p.is_relative_to(OWN):continue
        total+=1;h=sha(p)
        if h in targets:dup.append({'path':str(p),'sha256':h,'question_id':targets[h]})
    hits=[];api_read=0
    for line in (OWN/'scan/all_file_hashes.jsonl').open(encoding='utf-8'):
        r=json.loads(line)
        if not r['API_artifact']:continue
        p=Path(r['path']);api_read+=1;t=p.read_text(encoding='utf-8',errors='replace')
        for x in dup:
            if x['path'].lower() in t.replace('\\\\','\\').lower() or x['path'].replace('\\','/').lower() in t.lower():hits.append({'evidence':str(p),'duplicate_PNG':x})
        # Resolve --image bindings as well as explicit image_path strings.
        candidates=[a or b for a,b in re.findall(r'--image\s+(?:"([^"]+)"|(\S+))',t)]
        try:
            d=json.loads(t)
            if isinstance(d,dict):candidates += [d[k] for k in ('image_path','candidate_image','png_path') if isinstance(d.get(k),str)]
        except ValueError:pass
        for s in candidates:
            pth=Path(s);pth=pth if pth.is_absolute() else PROJECT/pth
            if pth.is_file():
                h=sha(pth)
                if h in targets:hits.append({'evidence':str(p),'resolved_image':str(pth),'sha256':h})
    d={'at':now(),'PNG_files_hashed':total,'exact_frozen_PNG_duplicates':dup,'API_artifacts_checked':api_read,'actual_launch_or_binding_matches':hits,'passed':not hits}
    save(OWN/'zero_call_duplicate_path_scan.json',d)
    print(json.dumps(d,ensure_ascii=False));assert not hits

def frozen_copy():
    assert load(OWN/'zero_prior_invocation_scan.json')['zero_old_call_gate_pass']
    assert load(OWN/'zero_call_duplicate_path_scan.json')['passed']
    prep=load(SESSION/'preparation62.json');changed=[]
    allprior={**prep['frozen52_readonly_file_hashes_before_after'],**prep['formal_source_hashes_before_after']}
    for p,h in allprior.items():
        current=sha(p)
        if current!=h:changed.append({'path':p,'expected':h,'current':current})
    save(OWN/'preparation_hash_freshness.json',{'checked_at':now(),'files_checked':len(allprior),'changes':changed})
    assert not changed
    hashes=load(OWN/'readonly_initial_hashes.json');hashes.update(allprior)
    for item in load(SESSION/'background_62_assignment.json')['questions']:
        q=item['question_id'];e=eligibility(q,'qualification_before_copy.json');assert e['eligible']
        fresh=OWN/q/'fresh_validation';review=load(fresh/'fresh_primary_review.json');assert review['passes_fresh_primary_gates']
        src=Path(item['source_directory']);dest=OWN/q/item['variant_id'];dest.mkdir(parents=True,exist_ok=False)
        eq=[]
        # All frozen candidate files remain byte-identical, including old internal absolute paths.
        for p in src.iterdir():
            if not p.is_file():continue
            b=p.read_bytes();to=dest/p.name;to.write_bytes(b)
            assert to.read_bytes()==b
            eq.append({'source':str(p),'copy':str(to),'sha256':sha(p),'copy_sha256':sha(to),'byte_equal':True});hashes[str(p)]=sha(p)
        support=OWN/q/'frozen_support';support.mkdir(exist_ok=False)
        for name in ['primary_math_proof.json','full_source_materials.json','old_history_read.json','exact_paths.json','fresh_context.json','formal_record.json','baseline_check.json']:
            p=src.parent/name;b=p.read_bytes();(support/name).write_bytes(b)
            eq.append({'source':str(p),'copy':str(support/name),'sha256':sha(p),'byte_equal':(support/name).read_bytes()==b})
        d=load(dest/'design.json');assert d['variant_id']==item['variant_id'] and d['created_at_utc']==item['frozen_created_at_utc'] and str(d['expected_wrong_answer'])==item['expected_wrong_answer']
        save(dest/'reuse_provenance.json',{'at':now(),'continuation_of':'background_52','not_new_design_or_mechanism':True,'original_variant_id':d['variant_id'],'original_created_at_utc':d['created_at_utc'],'original_preset':d['expected_wrong_answer'],'original_source_directory':str(src),'all_copy_equality':eq,'new_tests_directory':str(dest/'tests'),'whole_task_zero_invocation_scan':str(OWN/'zero_prior_invocation_scan.json'),'duplicate_path_scan':str(OWN/'zero_call_duplicate_path_scan.json'),'fresh_primary_review':str(fresh/'fresh_primary_review.json'),'current_qualification':str(OWN/q/'qualification_before_copy.json'),'approval_fingerprint':e['current_content_sha256'],'preserved_old_internal_absolute_paths':True,'new_independent_parent_review_required_if_doublehit':True})
        print('COPIED',q,len(eq),sha(dest/'candidate.png'))
    save(OWN/'readonly_initial_hashes.json',hashes)

def harness():
    # Use the existing isolated harness functions unmodified. Only module path
    # constants are replaced when this wrapper executes their original source.
    source=SESSION/'harness/quicktest3_isolated.py';s=source.read_text(encoding='utf-8')
    tree=ast.parse(s)
    assignments={'PROJECT':repr(str(PROJECT)),'HARNESS':repr(str(OWN/'harness'))}
    # Change path constants to Path literals; all function ASTs stay exact.
    lines=s.splitlines(keepends=True)
    for n in reversed(tree.body):
        if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name) and n.targets[0].id in assignments:
            name=n.targets[0].id;lines[n.lineno-1:n.end_lineno]=[name+' = Path('+assignments[name]+')\n']
    t=''.join(lines)
    pos=t.index('sys.dont_write_bytecode = True')
    t=t[:pos]+"sys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nfrom bootstrap import install\ninstall()\n"+t[pos:]
    dest=OWN/'harness/quicktest3_isolated.py';dest.parent.mkdir(exist_ok=True);dest.write_text(t,encoding='utf-8')
    def fns(x):return {n.name:ast.dump(n,include_attributes=False) for n in ast.parse(x).body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
    assert fns(s)==fns(t)
    save(OWN/'harness_isolation_audit.json',{'source':str(source),'source_sha256':sha(source),'isolated_path':str(dest),'isolated_sha256':sha(dest),'all_function_ASTs_identical_including_runtime_path_run_tests_and_main':True,'path_and_guard_only_diff':list(difflib.unified_diff(s.splitlines(),t.splitlines())),'model_thinking_systemprompt_profile_payload_credential_no_timeout_no_token_override_no_retry_unchanged':True,'not_invoked_for_key_or_connectivity_check':True})
    print('HARNESS_READY',sha(dest))

if __name__=='__main__':
    if sys.argv[1]=='duplicates':supplemental_scan()
    if sys.argv[1]=='copy':frozen_copy();harness()
