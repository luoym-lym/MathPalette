from tools05 import *
from partial_style import object_paths
import copy
RED='#DC2626';BLUE='#2563EB'
def style(target,color=RED,width=2):return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width}
DESIGNS={
('Plane211','odd_partition_closed_cycle'):{'wrong':'B','point_groups':[('p0_',range(1,10,2),RED),('p2_',range(1,10,2),RED)],'actions':[],
 'mechanism':'The five odd-numbered source points are a red subgroup, paired with the same five vertices in B. B is exactly the closed cycle on that subgroup. This privileges the false interpretation of every second point as odd labels only, incorrectly closing 9 to1 instead of wrapping 9 to2 on the nine-point circle. Every colored point belongs to one end of this source-to-result subgroup correspondence; no route or optionletter is colored.',
 'math':'The increment is2 modulo9, so the ordered labels are1,3,5,7,9,2,4,6,8,1. Since gcd(2,9)=1 all nine points are visited and only E has these nine edges. B closes9 directly to1 and omits the even labels, violating the cyclic every-second-point rule. Colors add no vertices and no condition; all markers exactly coincide with existing labeled source/B vertices.',
 'roles':['For each n in1,3,5,7,9, source p0_n is colored at its exact original coordinate to encode membership in the tempting odd-label partition.','For each same n, option-B p2_n is colored at its exact original coordinate to bind that member to B\'s odd-only closed path.','Ten point overlays jointly encode the specific false subgroup correspondence. All54 original points, numberlabels and all original edges remain in place; no new distinct point is added.'],
 'human_gate':'Each newpoint is centered exactly on one existing point, so the nine-point source and all options retain the same distinct vertices. Every numeral, including9 and2 at the wrap, is unchanged and unobscured. The original black route and circle contours remain readable.'},
('Plane217','diagonal_pair_to_fold_axis_v1'):{'wrong':'A','actions':[style('o2',RED,1),style('o3',RED,1),style('o1',BLUE,1),style('o4',BLUE,1),style('o7',RED,2),style('o6',BLUE,2)],
 'mechanism':'Opposite diagonal hole pairs are colored red and blue, matched to the falling and rising diagonal fold axes in A. This binds each two-hole diagonal chord to a same-slope folding axis, confusing a chord joining holes with the perpendicular-bisector reflection axis. The four holes remain at the corners of a nonsquare rectangle, so A still cannot produce them.',
 'math':'Relative to the papercenter(10,8), the four holes are(+-1,+-0.55). Reflection in x=10 or y=8 preserves this set, giving C. Reflection in either paperdiagonal swaps absolute offsets1 and0.55, producing points absent from the diagram, so A fails. B and E use only vertical folds and would leave all hole heights equal for a single punch; D uses parallel diagonal folds and cannot give the shown two independent horizontal/vertical reflection symmetries. Thus C is unchanged and unique.',
 'roles':['o2 ando3 red are the existing top-left and bottom-right hole outlines, one falling diagonal pair.','o1 ando4 blue are the existing bottom-left and top-right outlines, the rising diagonal pair.','o7 red is the falling diagonal candidate foldline in A, falsely bound to the red holepair by direction.','o6 blue is the rising diagonal candidate foldline in A, falsely bound to the blue holepair by direction.','All six are endpoints of the two hole-pair-to-axis correspondences. The hole interiors and dashed foldline types are retained.'],
 'human_gate':'Only existing outlines are recolored. The tiny holes retain original1pt outline width and white interiors. The two optionA diagonals remain dashed, and no source foldline, extra hole, label, equality or other condition is added.'},
('Plane198','compressed_bottom_run_correspondence'):{'wrong':'B','actions':[style('G3_0'),style('G3_1'),style('G3_2'),style('B3_0'),style('B3_1'),style('G3_3',BLUE),style('B3_2',BLUE),style('B3_3',BLUE)],
 'mechanism':'The bottom row of G is partitioned into its three-white run(red outlines) and terminal black cell(blue outline). The bottom row of B is partitioned into a two-black run(red) and two-white run(blue). This supplies a compressed3:1-to2:2 run correspondence, preserving the apparent complement order but losing one interior cell. Other rows of B match the true complement. No wholeoption or letter is highlighted.',
 'math':'At every cell Y is the black/white complement of X, with no geometric rearrangement. Therefore the paired G image must be the cellwise complement of G. For G the four binary rows(black=1) are0010,1100,0110,0001; their complements are1101,0011,1001,1110. Only E has those rows. B instead has bottomrow1100 and differs at row4,col3. The colored outlines do not change any cellfill or position, so E remains unique.',
 'roles':['G3_0,G3_1,G3_2 red outlines mark membership in the source three-white bottomrun, each cell contributing one unit of its length.','B3_0,B3_1 red outlines identify the falsely paired two-black bottomrun, exposing the exact compressed correspondence.','G3_3 blue marks the remaining source blackcell.','B3_2,B3_3 blue mark the falsely paired two-white terminalrun.','Eight celloutline marks encode the erroneous runlength partition while preserving black/white fills and every cell boundary.'],
 'human_gate':'No fill is changed. All4x4 cellcounts, inputX/Y/G labels and optionletters remain clear. Outlines2pt stay within each existing border; white cells remain visibly white and black cells black.'}
}
def render(qid,vid):
    d=copy.deepcopy(DESIGNS[qid,vid]);cfg,ad=adapter();check=eligibility(qid);assert check['eligible'],check
    metadata=ad.inspect_question(qid);before=inputs(ad,qid);renderer=PluginRenderer(cfg,ad,{qid:metadata})
    snaps={p['id']:p for p in metadata['snap_points']};bindings=[]
    for prefix,nums,color in d.get('point_groups',[]):
        for n in nums:
            source=snaps[prefix+str(n)];identifier='mark_'+prefix+str(n)
            d['actions'].append({'type':'add_point','id':identifier,'xy':copy.deepcopy(source['xy']),'color':color})
            bindings.append({'mark_id':identifier,'source_snap_point':copy.deepcopy(source)})
    scene=ad.scene(qid)
    try:
        scene.fig.canvas.draw()
        paths={a['target']:[{k:p[k] for k in ['id','sha256','closed']} for p in object_paths(scene,a['target'])] for a in d['actions'] if a['type']=='set_object_style'}
    finally:scene.close()
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':d['mechanism'],'intent':'Predeclared wrong answer '+d['wrong'],'params':{'actions':d['actions']}}
    normalized,png,digest=renderer.render(plugin);n2,png2,digest2=renderer.render(normalized,frozen=True)
    assert normalized==n2 and png==png2 and digest==digest2
    assert before==inputs(ad,qid)
    folder=HERE/qid/vid;folder.mkdir(parents=True,exist_ok=False)
    write(folder/'context.json',metadata);write(folder/'eligibility_before_design.json',check);write(folder/'exact_marker_bindings.json',bindings);write(folder/'path_fingerprints_complete.json',paths)
    write(folder/'plugin.json',normalized);(folder/'candidate.png').write_bytes(png)
    write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':d['wrong'],'correct_answer':ad.records[qid]['answer'],'formal_record':ad.records[qid],'created_at':datetime.now(timezone.utc).isoformat(),'mechanism':d['mechanism'],'mathematical_solution':d['math'],'marker_roles':d['roles'],'human_gate':d['human_gate'],'review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_SECOND_REVIEW'})
    write(folder/'render_check.json',{'baseline_pixel_match':True,'schema_normalized':True,'two_byte_identical_redraws':True,'pixel_sha256':digest,'png_sha256':file_hash(folder/'candidate.png'),'plugin_sha256':file_hash(folder/'plugin.json'),'design_sha256':file_hash(folder/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'no_source_writes':True})
    print(qid,vid,'rendered',flush=True)
if __name__=='__main__':
    for token in sys.argv[1:]:render(*token.split('/'))
