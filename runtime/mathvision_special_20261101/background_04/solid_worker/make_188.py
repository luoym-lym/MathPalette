from tools_local import *
from partial_style import object_paths
from fold_audit import diagonal_graph
qid='Solid188';vid='diagonal_feature_correspondence';check=eligibility(qid);assert check['eligible'],check
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A'
targets=[('given_diagonal0',RED),('Adiagonal0',RED),('given_diagonal1',GREEN),('Adiagonal1',GREEN),('given_diagonal2',BLUE),('Adiagonal2',BLUE)]
actions=[{'type':'set_object_style','target':target,'color':color,'linewidth_pt':2} for target,color in targets]
plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':'Match three actual face-diagonal features across the given cube and net A using three separate colors.','intent':'Predeclared false correspondence hypothesis A; colors are appearance only.','params':{'actions':actions}}
folder=TASK/qid/vid
report=AD.render_candidate(plugin,folder)
metadata=AD.inspect_question(qid);renderer=PluginRenderer(AD.config,AD,{qid:metadata})
normalized=json.loads((folder/'plugin.json').read_text(encoding='utf-8'))
n2,data2,pixels2=renderer.render(normalized,frozen=True)
assert normalized==n2 and data2==(folder/'candidate.png').read_bytes() and pixels2==report['pixel_sha256']
capture=AD.scene(qid)
try:
    capture.fig.canvas.draw()
    paths={t:[{'id':p['id'],'sha256':p['sha256'],'closed':p.get('closed')} for p in object_paths(capture,t)] for t,c in targets}
finally:capture.close()
roles=[{'target':t,'color':c,'role':r} for (t,c),r in zip(targets,[
    'Red source front-face diagonal is the first actual feature being compared.',
    'Red A leftmost diagonal supplies the proposed front-face image in the deceptive mapping.',
    'Green source top-face diagonal is the second actual feature being compared.',
    'Green A far-right diagonal supplies the proposed top-face image. Its endpoint orientation is the actual mismatch with the triangular loop.',
    'Blue source right-face diagonal completes the three-edge triangular loop on the given cube.',
    'Blue A lower-flap diagonal supplies the proposed third image; the red/blue pair really meets after folding, tempting acceptance before checking green closure.'
])]
design={'question_id':qid,'variant_id':vid,'expected_wrong_answer':'A','correct_answer':'D','created_at':datetime.now(timezone.utc).isoformat(),'mechanism':'Three differently colored feature pairs propose a cube-to-netA mapping. The red/blue pair genuinely shares a vertex after folding, but green does not close the triangle; intended specific error is accepting local face-feature matches without checking all endpoint identifications. No option label, face boundary or fill is highlighted.','mathematical_proof':'Given three diagonals connect three distinct cube vertices cyclically, hence their graph is a triangle (all degrees2). Explicit right-angle folding of the six-cell net gives A degrees[2,1,1,1,1], B degrees[3,1,1,1], C degrees[2,1,1,1,1], and D degrees[2,2,2]. Only D has the triangular incidence and the three mutually adjacent face diagonals; cube rotations match it to the given triangle. Frozen colors are not face/vertex equality conditions.','marker_roles':roles,'fold_graph_audit':diagonal_graph(qid),'formal_record':AD.records[qid],'target_path_fingerprints':paths,'status':'PRIMARY_DESIGN_ONLY; NEW_PARENT_INDEPENDENT_REVIEW_REQUIRED'}
write(folder/'design.json',design);write(folder/'eligibility_before_design.json',check)
write(folder/'normalized_frozen_replay.json',{'normalized_roundtrip_equal':True,'png_bytes_equal':True,'pixel_sha256':pixels2,'png_sha256':file_hash(folder/'candidate.png'),'plugin_sha256':file_hash(folder/'plugin.json'),'design_sha256':file_hash(folder/'design.json'),'target_path_fingerprints':paths})
print(json.dumps({'folder':str(folder),'png_sha256':file_hash(folder/'candidate.png'),'markers':len(actions),'expected_wrong_answer':'A'}))
