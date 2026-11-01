from tools_local import *
qid='Solid187';vid='paired_but_adjacent_edge_holes';folder=TASK/qid/vid
check=eligibility(qid);assert check['eligible'],check
context=json.loads((TASK/qid/'context.json').read_text(encoding='utf-8'))
roles=[];actions=[]
for targets,color,role in [([f'hole{i}_{j}' for i in [0,1] for j in range(3)],'#DC2626','All three sides of each half of target upper edge hole.'),([f'hole{i}_{j}' for i in [2,3] for j in range(3)],'#2563EB','All three sides of each half of target lower opposite edge hole.')]:
    for ident in targets:
        actions.append({'type':'set_object_style','target':ident,'color':color,'linewidth_pt':1.5});roles.append({'action_index':len(actions)-1,'target':ident,'role':role})
selected=[]
for o in context['objects']:
    if not o['styleable'] or not o['id'].startswith('Dboundary'):continue
    p=o['geometry']['points']
    if not all(.35-1e-8<=v[2]<=.65+1e-8 for v in p):continue
    if all(21.7-1e-8<=v[0]<=22.3+1e-8 for v in p):color='#DC2626';role='One of six original boundaries of D internal-hinge paired half-notches, bound to red target hole.'
    elif all(21-1e-8<=v[0]<=21.3+1e-8 for v in p) or all(24.7-1e-8<=v[0]<=25+1e-8 for v in p):color='#2563EB';role='One of six original boundaries of D outer left/right paired half-notches, bound to blue target hole.'
    else:continue
    selected.append(o['id']);actions.append({'type':'set_object_style','target':o['id'],'color':color,'linewidth_pt':1.5});roles.append({'action_index':len(actions)-1,'target':o['id'],'role':role})
assert len(selected)==12,selected
plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':'Bind two correctly partnered but adjacent D edge holes to two opposite target edge holes.','intent':'Preserving hole partners while overlooking the global opposite-edge relation.','params':{'actions':actions}}
AD.render_candidate(plugin,folder)
write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':'D','formal_correct_answer':'C','created_at':datetime.now(timezone.utc).isoformat(),'meaningfully_new_from':'false_cap_notch_partner (B hypothesis missed: D,C). This design tests a different error: D has two correctly completed edge holes but they are adjacent, whereas B had unmatched caps. It marks full U contours so edge holes are clear. No previous outcomes are reused as hits.','mechanism':'Two actual target edge holes are paired by red/blue full half-notch contours with the two genuinely joined D hole pairs. The local half pairing is valid, but their global positions are wrong: D edges are adjacent parallel instead of opposite parallel. Hypothesis D requires treating correct local closure as sufficient and ignoring global edge placement.','marker_roles':roles,'math_proof':'The preserved folded_notch_audit.json proves C alone has two complete holes on centrally opposite parallel edges. D has exactly two complete holes on adjacent parallel edges; A too is adjacent, B is incomplete and E has interior holes.','context_sha256':file_hash(TASK/qid/'context.json'),'candidate_png_sha256':file_hash(folder/'candidate.png'),'limits':['No calls for this new image yet.','Original source half-notch boundary visibility retained, including hidden dashes.','No original control, ablation or human performance claim.','Parent must commission new independent second review before delivery.']})
write(folder/'eligibility_before_design.json',check)
print(str(folder))
