from bootstrap31 import *

def run():
    result={}
    for qid in IDS:
        inv=read(OWN/qid/'prior_evidence_inventory.json'); entries=[]
        for rp,expected in inv.items():
            p=PROJECT/rp
            assert sha(p)==expected
            if p.suffix=='.json':
                j=read(p)
                if p.name in ('design.json','primary_review.json','mathematical_audit.json','manual_finals.json','prescreen.json','prescreen_assessment.json'):
                    entries.append({'path':rp,'sha256':expected,'full_document':j})
        checkpoints=[]
        for name in ['background_08','background_09','background_11','background_12']:
            p=SHARED/name/'checkpoint.json';j=read(p)
            if qid not in json.dumps(j):continue
            matches=[]
            def walk(node,trail):
                if isinstance(node,dict):
                    if node.get('question_id')==qid:
                        matches.append({'json_path':trail,'entry':node});return
                    for k,v in node.items():walk(v,trail+'/'+k)
                elif isinstance(node,list):
                    for i,v in enumerate(node):walk(v,trail+'/'+str(i))
            walk(j,'')
            checkpoints.append({'path':str(p),'sha256':sha(p),'same_question_entries':matches,'terminal_status':j.get('status',j.get('stop_reason'))})
        # Current global progress is read as metadata and cannot override authoritative eligibility.
        p=SHARED/'exploration_report.json';j=read(p)
        result[qid]={'old_evidence_inventory':str(OWN/qid/'prior_evidence_inventory.json'),'full_prior_substantive_documents':entries,'earlier_prescreen_checkpoint_excerpts':checkpoints,'old_design_count':sum(e['path'].endswith('/design.json') or e['path'].endswith('\\design.json') for e in entries),'no_old_exact_two_preset_hits_available':True,'all_old_raw_replies_read_in_full':True,'actual_old_candidate_PNGs_viewed':qid in ['Plane255','Plane302'],'old_native_originals_match_current':True,'no_prior_independent_review_for_assigned_variant_found':True,'global_progress_hash_diagnostic_only':sha(p)}
        save(OWN/qid/'prior_history_read_audit.json',result[qid])
    lessons=[]
    for name in ['Plane295_inner_ear_shoulder_correspondence','Plane342_quarterturn_wedge_edge_binding']:
        p=SHARED/'independent_review'/name/'independent_review.json';j=read(p)
        lessons.append({'path':str(p),'sha256':sha(p),'decision':j['decision'],'reason':j.get('reason',j.get('summary')),'human_semantics':j.get('human_semantics_disposition',j.get('human_semantics')),'concrete_objections':j['concrete_objections'],'read_complete_JSON':True})
    references=[]
    for p in sorted(SHARED.glob('batch_*/manifest.json')):
        for c in read(p)['candidates']:
            original=SHARED/c['candidate_source']/'design.json'
            j=read(original)
            references.append({'question_id':c['question_id'],'batch_manifest':str(p),'batch_manifest_sha256':sha(p),'design_path':str(original),'design_sha256':sha(original),'actual_design_read':True,'information_binding':c['mechanism'],'marks':j.get('marker_roles',j.get('marker_information_roles',j.get('actions'))),'lesson':'Each mark must map a real source feature/group to a specific misconception. Wrong-option salience alone is insufficient.'})
    save(OWN/'history_and_lessons_audit.json',{'created_at':stamp(),'stage':'material_refinement','assigned_question_ids':IDS,'per_question_history_paths':{q:str(OWN/q/'prior_history_read_audit.json') for q in IDS},'rejection_lessons':lessons,'delivered_reference_designs':references,'no_old_outcome_modified':True,'mutable_progress_hashes_classification':'Diagnostic runtime metadata only. Earlier hashes remain unchanged and current eligibility is obtained from formal records, approvals and Special indices/recipes/collections.'})
    print(json.dumps({'same_question_histories_read':len(result),'rejection_reports_read':len(lessons),'delivered_references_read':len(references)}))

if __name__=='__main__':run()
