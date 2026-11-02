from review_bootstrap import *

def run():
    audit=load(TASK/'parent_audits/native_u09/audit.json')
    for k,v in audit.items():
        if k not in ('candidates','current_eligibility','preservation','Solid240_hold'):
            print('PARENT',k,canonical(v))
    print('PARENT candidate count',len(audit['candidates']))
    for c in audit['candidates']:
        print('PARENT CANDIDATE',canonical(c))
    primary=load(CANDIDATE/'primary_review.json')
    for k in ('information_and_native_human_review','history_and_novelty','limitations'):
        print('PRIMARY',k,canonical(primary[k]))
    for file in ('history_index.json','units/u09_octa_nets/history_selected.json','units/u09_octa_nets/history_read_audit.json'):
        v=load(TASK/file)
        print('HISTORY',file,'keys',list(v))
        if file=='history_index.json':
            for q in v['questions']:
                if q.get('question_id')=='Solid166':
                    save('old_history_index_Solid166.json',q)
                    print('SOLID166 OLD HISTORY',canonical(q))
            print('CROSS ID',canonical([c for c in v.get('cross_id_candidate_hash_collisions_involving_scope',[]) if 'Solid166' in canonical(c)]))
        else:
            print('HISTORY CONTENT',canonical(v))
    for file in ('all_true_free_seams.json','considered_but_not_rendered.json','r12_full_seam_context_x_four/manual_final_review.json'):
        print('RELATED',file,canonical(load(UNIT/'Solid166'/file)))

if __name__=='__main__': main(run)
