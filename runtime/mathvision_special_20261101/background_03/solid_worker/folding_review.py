from pathlib import Path
import json,os,sys
sys.dont_write_bytecode=True
TASK=Path(__file__).resolve().parent
for k,n in {'TEMP':'temp','TMP':'temp','MPLCONFIGDIR':'mpl_cache','XDG_CACHE_HOME':'cache'}.items():os.environ[k]=str(TASK/n)
BASE=TASK.parents[1]
sys.path.insert(0,str(BASE))
from runtime_isolation import install
install(TASK/'render_tmp')
PROJECT=next(p for p in TASK.parents if (p/'MATHPALETTE_PROTOCOL.md').is_file())
e1=(1,0,0);e2=(0,1,0);e3=(0,0,1)
configs={
 'Solid166':{'faces':[['T0','T1','B0'],['B0','T1','B1'],['T1','T2','B1'],['B1','T2','B2'],['T2','T3','B2'],['B2','T3','B3'],['T0','A','T1'],['B2','B3','D']], 'seed':{'T0':e1,'T1':e2,'B0':e3},'edges':{'x':['B3','D'],'1':['T3','B3'],'2':['T2','T3'],'3':['T0','A'],'4':['T0','B0'],'5':['B0','B1']},'answer':'5','targets':{'netedge15':'x','netedge11':'1'}},
 'Solid203':{'faces':[['n0','n1','n2'],['n0','n2','n3'],['n2','n3','n4'],['n2','n4','n5'],['n4','n5','n6'],['n5','n6','n7'],['n6','n7','n8'],['n6','n8','n9']], 'seed':{'n0':e1,'n2':e2,'n3':e3},'edges':{'x':['n8','n9'],'A':['n7','n8'],'B':['n5','n7'],'C':['n0','n1'],'D':['n0','n3'],'E':['n3','n4']},'answer':'E','targets':{'line_20':'x','line_24':'A'}}}
for qid,c in configs.items():
    vertices=c['seed'].copy();steps=[]
    while True:
        progress=False
        for i,a in enumerate(c['faces']):
            if not all(v in vertices for v in a):continue
            for j,b in enumerate(c['faces']):
                common=set(a)&set(b)
                if len(common)!=2:continue
                old=next(v for v in a if v not in common);new=next(v for v in b if v not in common)
                proposed=tuple(-x for x in vertices[old])
                if new in vertices:assert vertices[new]==proposed
                else:
                    vertices[new]=proposed;steps.append({'known_face':i,'new_face':j,'shared_vertices':sorted(common),'opposite_vertices':[old,new],'assigned':proposed});progress=True
        if not progress:break
    assert all(v in vertices for f in c['faces'] for v in f)
    face_keys={tuple(sorted(vertices[v] for v in f)) for f in c['faces']};assert len(face_keys)==8
    edges={k:tuple(sorted(vertices[v] for v in edge)) for k,edge in c['edges'].items()}
    matches=[k for k,e in edges.items() if k!='x' and e==edges['x']];assert matches==[c['answer']]
    output={'question_id':qid,'review_level':'PRIMARY mathematical verification, not independent second review','method':'Regular octahedron vertices ±e1,±e2,±e3. Each triangular face has one vertex from each opposite pair. Across a shared edge the two third vertices are antipodal. Propagate this exact identity over the connected eight-face net; verify all eight face triples distinct.','seed':c['seed'],'propagation':steps,'folded_vertex_identities':vertices,'labelled_edge_endpoint_identities':edges,'unique_match_to_x':matches,'actual_selected_object_label_bindings':c['targets'],'geometry_preserved':True}
    p=TASK/qid/'bridge_terminal_edge_pair/folding_verification.json'
    with p.open('x',encoding='utf-8') as f:json.dump(output,f,ensure_ascii=False,indent=2);f.write('\n')
    print(qid,matches)
