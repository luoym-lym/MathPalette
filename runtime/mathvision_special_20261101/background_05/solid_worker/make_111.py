from tools_local import *
from collections import deque
qid='Solid111'; vid='local_corner_to_wrong_net';folder=TASK/qid/vid
check=eligibility(qid);assert check['eligible'],check
source_path=next(ROOT/'SolidGeometry'/p for p in AD.records[qid]['runtime_dependencies'] if p.endswith('/scene.json'))
source=json.loads(source_path.read_text(encoding='utf-8-sig'))
def neg(v):return tuple(-x for x in v)
folds={}
for letter in 'ABCDE':
    faces=[o for o in source['objects'] if o['type']=='face' and o['id'].startswith(letter+'_cell')]
    cells={}
    for face in faces:
        parts=face['id'].split('_');cell=(int(parts[1][4:]),int(parts[2]));prefix=face['id'][:-5]
        hatched=any(o['id'].startswith(prefix+'_hatch') for o in source['objects'])
        cells[cell]='H' if hatched else 'G' if face['semantic_color']=='#cccccc' else 'W'
    seed=next(iter(cells));basis={seed:((1,0,0),(0,1,0),(0,0,1))};todo=deque([seed])
    while todo:
        cell=todo.popleft();u,v,n=basis[cell]
        for (dx,dy),trip in [((1,0),(neg(n),v,u)),((-1,0),(n,v,neg(u))),((0,1),(u,neg(n),v)),((0,-1),(u,n,neg(v)))]:
            other=(cell[0]+dx,cell[1]+dy)
            if other in cells and other not in basis:basis[other]=trip;todo.append(other)
    assert len(basis)==6 and len({b[2] for b in basis.values()})==6
    pairs=[];seen=set()
    for cell,trip in basis.items():
        if cell in seen:continue
        partner=next(c for c,b in basis.items() if b[2]==neg(trip[2]));seen.update([cell,partner])
        pairs.append({'cells':[list(cell),list(partner)],'colors':[cells[cell],cells[partner]],'equal':cells[cell]==cells[partner]})
    folds[letter]={'cells':{str(k):v for k,v in cells.items()},'opposite_pairs':pairs,'valid':all(p['equal'] for p in pairs)}
assert [k for k,v in folds.items() if v['valid']]==['E'],folds
actions=[]
roles=[]
for ids,color,role in [(['givenedge3','D_netedge5'],'#DC2626','Source H/W seam paired with D local H0/W1 hinge.'),(['givenedge5','D_netedge1','D_netedge3'],'#2563EB','Source H/G seam paired with the two free D edges that close the H0/Gbelow1 seam.'),(['givenedge7','D_netedge6'],'#16A34A','Source W/G seam paired with D W1/Gbelow1 hinge.')]:
    for ident in ids:
        actions.append({'type':'set_object_style','target':ident,'color':color,'linewidth_pt':2})
        roles.append({'action_index':len(actions)-1,'target':ident,'role':role})
plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':'Match the visible three-face corner to a locally compatible but globally invalid net corner.','intent':'Necessary local corner compatibility mistaken for full opposite-face compatibility.','params':{'actions':actions}}
AD.render_candidate(plugin,folder)
write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':'D','formal_correct_answer':'E','created_at':datetime.now(timezone.utc).isoformat(),'mechanism':'Three seam colors bind the source H/W/G corner to D H0/W1/Gbelow1. This local corner really folds correctly, but the remaining opposite faces in D have W/G mismatches; hypothesis is choosing D from necessary local compatibility without checking all three opposite pairs.','marker_roles':roles,'math_proof':'Exhaustively fold each of the six face normals by 90 degrees across net hinges. Only E has H/H, G/G, W/W on its three opposite pairs. D has H/H, W/G, W/G. The matched D corner itself is locally compatible under a rotation, so no false explicit geometric condition is drawn.','math_evidence':folds,'input_binding_sha256':file_hash(TASK/qid/'context.json'),'candidate_png_sha256':file_hash(folder/'candidate.png'),'limits':['No model calls yet.','No original control or per-marker ablation has been run.','Border colors are optional annotations, not additional face colors.','This is primary research review only; parent must commission a new independent review before delivery.']})
write(folder/'eligibility_before_design.json',check)
write(folder/'math_fold_audit.json',folds)
print(json.dumps({'candidate':str(folder),'valid_nets':[k for k,v in folds.items() if v['valid']],'roles':len(roles)}))
