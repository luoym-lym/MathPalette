from new_tools import *
import copy
from partial_style import object_paths
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A'
def point(name,xy,color):return {'type':'add_point','id':name,'xy':xy,'color':color}
def style(target,color,width=2,interval=None):
    d={'type':'set_object_style','target':target,'color':color,'linewidth_pt':width}
    if interval is not None:d['interval']={'path_id':'p0','path_sha256':'RESOLVE','start':interval[0],'end':interval[1],'wrap':False}
    return d
DESIGNS={
('Plane425','single_endpoint_radius_trap'):{'wrong':'D','actions':[
    {'type':'add_line','id':'radius_V_source_lower','endpoints':[[2.0,3.0],[1.0,2.0]],'color':'#EA580C','linestyle':'dashed'},
    {'type':'add_line','id':'radius_V_image_left','endpoints':[[2.0,3.0],[3.0,2.0]],'color':'#EA580C','linestyle':'dashed'}],
    'mechanism':'Two actual equal-radius vectors fromV to the lower source endpoint and left image endpoint form a real90-degree relation. A quarter-turn aboutV maps this one endpoint correctly but not the other. HypothesisD is the specific necessary-but-insufficient-condition error of admittingV in addition to true centresU,W. This differs from the earlier orderedendpoint pairing designs; only two unobstructed dashed radius lines are added.',
    'math':'V=(2,3),A=(1,2),C=(3,2): A-V=(-1,-1),C-V=(1,-1), both normsqrt2 and a+90degree turn mapsA->C. However the upper endpointB=(1,4) maps to(1,2), notD=(5,2), soV fails. U clockwise90 andW counterclockwise90 are the only true centres; correct optionC unchanged. Neither equal-length ticks nor rightangle symbols are added.',
    'roles':['First orange radius links actualV to the actuallower source endpoint.','Second orange radius links the sameV to the actualleft target endpoint.','Together they expose a true oneendpoint rotation relation whose misuse as a fullsegment mapping is the targeted error; no option or unrelated point is marked.']},
('Plane425','paired_endpoint_links'):{'wrong':'B','actions':[
    {'type':'add_line','id':'red_endpoint_correspondence','endpoints':[[1.0,2.0],[3.0,2.0]],'color':RED,'linestyle':'dashed'},
    {'type':'add_line','id':'blue_endpoint_correspondence','endpoints':[[1.0,4.0],[5.0,2.0]],'color':BLUE,'linestyle':'dashed'}],
    'mechanism':'Two explicit dashed correspondence links join A->C andB->D, replacing the first design\'s four standalone colored endpointdots. This spatially connects each ordered endpoint pair and can encourage accepting only the rotation aboutU, forgetting that the uncolored undirected segments also admit A->D,B->C aboutW. NewPNG and frozen hypothesisB before its own pair; no reuse of first-image outcomes.',
    'math':'A=(1,2),B=(1,4),C=(3,2),D=(5,2). U=(2,1) maps A->C,B->D by clockwise90. W=(3,4) maps A->D,B->C by counterclockwise90. T,V fail. Thus unique optionC remains; dashed colored overlays are added appearance links, not required vertex-correspondence labels.',
    'roles':['Red dashed auxiliary connects lower source endpointA to left image endpointC.','Blue dashed auxiliary connects upper source endpointB to right image endpointD.','Both links carry a concrete endpoint correspondence; no namedcentre or answeroption is highlighted.']},
('Plane425','endpoint_correspondence'):{'wrong':'B','actions':[
    point('red_source_endpoint',[1.0,2.0],RED),point('red_image_endpoint',[3.0,2.0],RED),
    point('blue_source_endpoint',[1.0,4.0],BLUE),point('blue_image_endpoint',[5.0,2.0],BLUE)],
    'mechanism':'Two colored endpoint pairs privilege the clockwise 90-degree rotation about U; the uncolored problem also permits swapped endpoint correspondence under the opposite rotation about W. Hypothesis is only U (B), induced by treating optional color correspondence as a required endpoint mapping.',
    'math':'Let source endpoints A=(1,2), B=(1,4), target C=(3,2), D=(5,2). U=(2,1) gives clockwise90 A->C,B->D; W=(3,4) gives counterclockwise90 A->D,B->C. T and V fail distance invariants. Thus C (either U or W) remains uniquely correct. Colors are appearance, never vertex labels/conditions.',
    'roles':['Red source A and target C encode one ordered endpoint pair.','Blue source B and target D encode the second ordered pair.','All four markers are required to encode a complete, misleading endpoint mapping without marking any answer option or centre.']},
('Plane471','three_side_chain'):{'wrong':'C','actions':[
    style('tileI',RED,3,(.25,.5)),style('tileIV',RED,3,(.75,1)),
    style('tileI',BLUE,3,(0,.25)),style('tileIII',BLUE,3,(.5,.75)),
    style('tileIV',GREEN,3,(0,.25)),style('tileII',GREEN,3,(.5,.75))],
    'mechanism':'Three equal-number pairs create the tempting partial placement I,IV above III,II: red9/9 horizontal, blue7/7 vertical, green6/6 vertical. It puts III into C but leaves the last horizontal5/4 mismatch. All six marks target numeric edge information rather than whole tiles or a target answer.',
    'math':'Unique valid placement is II,I / IV,III: shared3/3 across top,2/2 at left vertical,7/7 at right vertical,1/1 across bottom. Thus IV belongs in C, optionD. The marked alternative has unmatched5/4 on its bottom shared edge and is invalid. Numbers and orientation unchanged; no false equality symbols added.',
    'roles':['Red pair targets the two edges labeled9 on I andIV.','Blue pair targets I bottom7 and III top7.','Green pair targets IV bottom6 andII top6.','Every pair encodes one true equal-label adjacency in the deceptive partial layout; the final unmatched pair remains legible and uncolored.']},
('Plane250','diagonal_vertical_basis'):{'wrong':'43','actions':[
    style('path0_0',RED,2),style('path3_1',RED,2),style('path0_1',BLUE,2),style('path3_3',BLUE,2)],
    'mechanism':'Two color pairs incorrectly bind diagonal units in Fin to vertical units in Tin. Fin has5 diagonals totaling25 so diagonal=5; substituting5 for Tin vertical basis instead of3 leads3*5+4*5+2*4=43. Only four segment overlays, all original geometry stays fixed.',
    'math':'Fin gives5d=25 =>d5. Pin gives5d+4v=37 =>v3. Rin gives6v+5h=38 =>h4. Tin has3d+4v+2h=15+12+8=35 uniquely. Two target vertical segments are colored to look equivalent to two known diagonal segments; equal colors are not length givens.',
    'roles':['Red Fin diagonal path0_0 pairs with Tin vertical path3_1.','Blue Fin diagonal path0_1 pairs with Tin vertical path3_3.','Both pairs carry the same wrong basis correspondence at separate examples, while untouched segments retain enough information to recover the actual basis.']},
('Plane313','false_hole_clock_correspondence'):{'wrong':'C','actions':[
    style('o4',RED,2),style('o5',BLUE,2),style('o6',GREEN,2),
    style('o0',RED,3,(31/64,33/64)),style('o0',BLUE,3,(4/64,7/64)),style('o0',GREEN,3,(57/64,60/64))],
    'mechanism':'Three colored hole boundaries pair with three small clock-rim sectors at9(red),2(blue),4(green). The blue/green pair preserves the two-hour5/7 gap but red1->9 is off byone hour compared with the same9-hour rotation taking5->2,7->4. This targets actual angular correspondence rather than option text.',
    'math':'The hole positions are1,5,7 so circular clockwise gaps are4,2,6. Only optionA={4,6,12} has the same cyclic gaps up to rotation. C={2,4,9} has gaps2,5,5 and cannot result. Geometry, hole fill, numbers and rotation centre remain frozen. Rim intervals refer to the same64-edge frozen contour; colors imply misleading correspondence only.',
    'roles':['Red circle hole1 pairs with the rim near9.','Blue circle hole5 pairs with the rim near2.','Green circle hole7 pairs with the rim near4.','Three holes and three rim intervals each supply one endpoint of a positional correspondence, no full-option emphasis.']}
}
cfg,ad=adapter()
for token in sys.argv[1:]:
    qid,vid=token.split('/')
    item=copy.deepcopy(DESIGNS[(qid,vid)])
    check=eligibility(qid);assert check['eligible'],check
    metadata=ad.inspect_question(qid);renderer=PluginRenderer(cfg,ad,{qid:metadata});record=ad.records[qid]
    capture=ad.scene(qid)
    try:
        capture.fig.canvas.draw()
        for action in item['actions']:
            if 'interval' in action:action['interval']['path_sha256']=next(p['sha256'] for p in object_paths(capture,action['target']) if p['id']=='p0')
    finally:capture.close()
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':item['mechanism'],'intent':'Predeclared target error '+item['wrong'],'params':{'actions':item['actions']}}
    relatives=[record['image'],record['scene'],record['script'],record['original_image'],*record.get('runtime_dependencies',[])]
    inputs={str((ROOT/'PlaneGeometry'/p).relative_to(ROOT)):file_hash(ROOT/'PlaneGeometry'/p) for p in sorted(set(relatives))}
    normal,data,digest=renderer.render(plugin);normal2,data2,digest2=renderer.render(normal,frozen=True)
    assert normal2==normal and data2==data and digest2==digest
    assert inputs=={str((ROOT/'PlaneGeometry'/p).relative_to(ROOT)):file_hash(ROOT/'PlaneGeometry'/p) for p in sorted(set(relatives))}
    folder=HERE/qid/vid;folder.mkdir(parents=True,exist_ok=False)
    (folder/'candidate.png').write_bytes(data);write(folder/'plugin.json',normal)
    write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':item['wrong'],'correct_answer':record['answer'],'mechanism':item['mechanism'],'mathematical_solution':item['math'],'marker_roles':item['roles'],'source_dataset':record['source_dataset'],'source_key':record['source_key'],'source_revision':record.get('source_revision'),'formal_record':record,'created_at':datetime.now(timezone.utc).isoformat(),'review_status':'PRIMARY_ONLY_REQUIRES_NEW_INDEPENDENT_SECOND_REVIEW'})
    write(folder/'render_check.json',{'question_id':qid,'eligibility_recheck':check,'baseline_matches_formal':True,'schema_normalized':True,'twice_byte_identical':True,'pixel_sha256':digest,'png_sha256':file_hash(folder/'candidate.png'),'design_sha256':file_hash(folder/'design.json'),'plugin_sha256':file_hash(folder/'plugin.json'),'frozen_inputs':inputs,'isolation':ISOLATION})
    print(qid,vid,'rendered',flush=True)
