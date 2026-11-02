import tools_local as t
def read(p):return t.json.loads(p.read_text(encoding='utf-8-sig'))
refs=[];delivered=set()
for i in range(1,10):
    p=t.BASE/f'batch_{i:02d}'/'manifest.json';data=read(p)
    for c in data['candidates']:
        delivered.add(c['question_id'])
        refs.append({'batch':p.parent.name,'question_id':c['question_id'],'mechanism':c.get('mechanism'),'candidate_sha256':c.get('candidate_sha256'),'expected_wrong_answer':c.get('expected_wrong_answer'),'reference_only':True})
pending={'Solid197','Plane295','Plane342'}
dispatch=read(t.BASE/'refinement_dispatch_20261102.json')
other={q for u in dispatch['units'] if u['unit']!='background_30' for q in u['question_ids']}
assert len(t.ASSIGNED)==8 and not(set(t.ASSIGNED)&(delivered|pending|other))
t.write(t.HERE/'scope_and_delivery_references.json',{'assigned_question_ids':t.ASSIGNED,'stage':'material_refinement','other_active_scopes_excluded':sorted(other),'delivered_excluded':sorted(delivered),'pending_excluded':sorted(pending),'disjoint_active':True,'old_terminal_scope_overlap_intentional':True,'delivered_reference_methods':refs,'reference_summary':'Use partial information correspondences or geometric groupings; every mark needs a role. No chosen wrong answer receives a bare isolated contour. Original controls can be wrong and no causal effect follows from two trials.'})
print(t.json.dumps(refs,ensure_ascii=False))
