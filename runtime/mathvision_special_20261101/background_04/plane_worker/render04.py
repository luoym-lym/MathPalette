from tools04 import *
import copy
RED='#DC2626';BLUE='#2563EB'
def style(target,color=RED,width=2,interval=None):
    a={'type':'set_object_style','target':target,'color':color,'linewidth_pt':width}
    if interval:a['interval']={'path_id':'p0','path_sha256':'RESOLVE','start':interval[0],'end':interval[1],'wrap':False}
    return a
DESIGNS={
('Plane238','punch_to_intermediate_fold_cell'):{
 'wrong':'D',
 'actions':[style('o135'),style('o17',interval=(2/3,1)),style('o18',interval=(2/3,1)),style('o23',interval=(3/6,4/6)),style('o24',interval=(3/6,4/6))],
 'mechanism':'The actual punchcontour is paired by red with the top-row cell immediately to the right of the secondfold axis in the intermediate6x3 strip. The finalhole is actually in the middle column of the three-column packet; the marked intermediatecell is the adjacent leftcolumn of that right-half packet. This targets a specific stage-to-stage one-column localization error. Unlike the earlier originalcell15 design, this image leaves all numberedcells unmarked and supplies the false correspondence only between consecutive folded diagrams.',
 'math':'After top-to-bottom folding, intermediate top-rowcells combine original rows3,4. Folding left-to-right atx11 pairs columnsc and7-c. The final punch atpacketmiddlecolumn comes from intermediatecolumn5 (x12..13) and mirrors to2, yielding14,17,20,23 (C). The marked intermediatecolumn4 (x11..12) instead mirrors to3, yielding15,16,21,22 (D). Outline colors never change the actualpunch, foldarrows or positions.',
 'roles':['o135 red is the existing actual finalpunch contour, retaining blackfill.','o17 y2..3 is the leftboundary of the false intermediate top-row cell(column4).','o18 y2..3 is its rightboundary.','o23 x11..12 is its bottomboundary.','o24 x11..12 is its topboundary.','The four short existing-grid overlays identify one intermediate position; finalpunch is the other end of that positional pairing. No original numeral or option is marked.'],
 'human_gate':'All36 originalnumerals and their cellboundaries remain black. Foldaxes/arrows, paperlayers, gridcounts and punchposition are unchanged. The red cell is an appearance correspondence only; it is not a second punch or a cut.'},
('Plane314','perimeter_to_path_unit'):{
 'wrong':'E',
 'actions':[style('tile6',RED,2),style('thick_snake0',RED,2)],
 'mechanism':'A complete smallest-square perimeter is paired by red with one unit of the indicated path. The given80cm is the perimeter, so this pair targets misbinding the80cm whole-perimeter measure as the path-unit length, producing21*80=1680cm (E) instead of dividing by4.',
 'math':'The smallest tile perimeter80 gives side20cm. In smallestsideunits the eleven pathsegments have lengths1,1,2,2,2,2,2,3,4,1,1 summing21. Hence length420cm, optionC unique. A perimeter80 must not be substituted for one side. Originalhead, eye, topology and all tile boundaries remain unchanged.',
 'roles':['tile6 redoutline marks exactly the entire perimeter of a smallesttile, the geometric quantity whose80cm is stated.','thick_snake0 red marks a single smallestside length along the actual path, the location where the whole-perimeter quantity could be wrongly substituted.','The two overlays together carry a perimeter-to-pathunit binding; no option or irrelevanttile is colored.'],
 'human_gate':'The connected snake/path and head remain readily identifiable even with one short segment colored. No new path, lengthlabel, equality or other mathematicalcondition is added.'},
('Plane225','retained_butterfly_sector'):{
 'wrong':'C',
 'actions':[style('fold1_radius1'),style('fold1_radius2'),style('optionC_radius1'),style('optionC_radius2')],
 'mechanism':'Two colored sector boundaries in the already shown first reflection pair with the same two boundaries around the butterfly in optionC. This encodes preservation of one feature sector between the first and third images, privileging the tempting error that the two further reflections restore the first image. In fact their axes are not parallel, so their composition rotates the first image120 degrees.',
 'math':'The source is fold0. Fold1 is the already shown first reflection, treated as canonicalidentity. The next axes are60 and120 degrees; reflection120 composed with reflection60 is rotation120. Its matrix=[[-1/2,-sqrt(3)/2],[sqrt(3)/2,-1/2]], which equals only optionB. The asymmetrically decorated six sectors distinguish all five options, so B remains unique. C is the first image unchanged, not the third.',
 'roles':['fold1_radius1 bounds the right side of the first-reflection butterfly sector.','fold1_radius2 bounds its left side.','optionC_radius1 is the right boundary of the same butterfly sector in C.','optionC_radius2 is its left boundary.','All four boundary overlays encode one closed feature sector correspondence; no wholehexagon, label, optionletter or unrelated sector is highlighted.'],
 'human_gate':'Colored radial boundaries preserve all six animal pictures, all three bold reflectionedges, and their order. No text or condition is added. The final image is still uniquely determined by the bold axes.'},
('Plane238','hole_to_inner_column_cell'):{
 'wrong':'D',
 'actions':[style('o135'),style('o2',interval=(3/6,4/6)),style('o3',interval=(3/6,4/6)),style('o10',interval=(2/6,3/6)),style('o11',interval=(2/6,3/6))],
 'mechanism':'The existing punched-hole boundary is red, paired with the four existing boundaries of originalcell15. This is a concrete false hole-to-cell correspondence, encouraging the columnshift that selects the central pair3/4 rather than true columns2/5. It predicts the fourfold orbit15,16,21,22 (D), while fold arrows and original numbers remain legible.',
 'math':'Number r,c is6(r-1)+c with top rowr1. Horizontal fold pairs rowsr and7-r; subsequent vertical fold pairs columnsc and7-c. The hole at final topmiddle square corresponds to original rows3,4 and cols2,5, giving14,17,20,23 uniquely optionC. The marked cell15 has rows3,4 and cols3,4 orbit15,16,21,22, a different orbit (D). Outline recoloring neither moves the punch nor makes cell15 pierced as a condition.',
 'roles':['o135 is the existing actual punch contour, unchanged black fill with red outline.','o2 intervaly3..4 is the left boundary of cell15.','o3 intervaly3..4 is its right boundary.','o10 intervalx2..3 is its lower boundary.','o11 intervalx2..3 is its upper boundary.','The four short overlays together identify exactly one gridcell without touching or highlighting its numeral; source punch provides the other end of the positional pairing.'],
 'human_gate':'All36 numerals, grid lines, fold axes/arrows and hole position stay unchanged. Five short appearance marks carry one false spatial correspondence, with no extra holes or cut lines.'},
('Plane240','false_four_to_five_hour_gap'):{
 'wrong':'A',
 'actions':[style('o4',RED),style('o5',BLUE),style('o0',RED,3,( (11/12)-(1/64), (11/12)+(1/64))),style('o0',BLUE,3,(.5-1/64,.5+1/64))],
 'mechanism':'Red hole1 pairs with the clockrim at4; blue hole5 pairs with the rim at9. The two small clocksectors encode the wrong five-hour targetgap4/9, whereas the two fixed holes are four hours apart. This is angular correspondence information, not a selected answerlabel.',
 'math':'The holes display1 and5 initially, so their angular separation is4*30=120 degrees (or240 the otherway). A rigidrotation preserves this. ChoiceA4/9, B5/10 and E7/12 have five-hour separation; D6/9 has three. Only C5/9 has four, so C is unique and unchanged. Red/blue outlines impose no actual numbered correspondence.',
 'roles':['o4 red outline singles out the existing1 hole as first angular feature.','o5 blue outline singles out the existing5 hole as second angular feature.','A short red interval of clockrim o0 centered near4 supplies the first false targetposition.','A short blue riminterval near9 supplies the second targetposition.','Everymark is one endpoint of a two-feature correspondence. Black disc fill and white holes stay untouched.'],
 'human_gate':'Numerals and hole interiors are unchanged and clear. No added numeral, symbol, equality, anglecondition or changed cut boundary.'}
}
def render(qid,vid):
    d=copy.deepcopy(DESIGNS[qid,vid]);cfg,ad=adapter();check=eligibility(qid);assert check['eligible']
    metadata=ad.inspect_question(qid);renderer=PluginRenderer(cfg,ad,{qid:metadata});r=ad.records[qid];before=inputs(ad,qid)
    scene=ad.scene(qid)
    try:
        scene.fig.canvas.draw()
        for a in d['actions']:
            if 'interval' in a:a['interval']['path_sha256']=next(p['sha256'] for p in object_paths(scene,a['target']) if p['id']=='p0')
        paths={a['target']:[{k:p[k] for k in ['id','sha256','closed'] if k in p} for p in object_paths(scene,a['target'])] for a in d['actions']}
    finally:scene.close()
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':d['mechanism'],'intent':'Predeclared wrong answer '+d['wrong'],'params':{'actions':d['actions']}}
    normalized,png,digest=renderer.render(plugin);n2,png2,digest2=renderer.render(normalized,frozen=True)
    assert normalized==n2 and png==png2 and digest==digest2
    assert before==inputs(ad,qid)
    folder=HERE/qid/vid;folder.mkdir(parents=True,exist_ok=True)
    if not (folder/'context.json').exists():write(folder/'context.json',metadata)
    if not (folder/'eligibility_before_design.json').exists():write(folder/'eligibility_before_design.json',check)
    write(folder/'path_fingerprints_complete.json',paths)
    write(folder/'plugin.json',normalized);(folder/'candidate.png').write_bytes(png)
    write(folder/'design.json',{'question_id':qid,'variant_id':vid,'expected_wrong_answer':d['wrong'],'correct_answer':r['answer'],'formal_record':r,'created_at':datetime.now(timezone.utc).isoformat(),'mechanism':d['mechanism'],'mathematical_solution':d['math'],'marker_roles':d['roles'],'human_gate':d['human_gate'],'review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_SECOND_REVIEW'})
    write(folder/'render_check.json',{'baseline_pixel_match':True,'schema_normalized':True,'two_byte_identical_redraws':True,'pixel_sha256':digest,'png_sha256':file_hash(folder/'candidate.png'),'plugin_sha256':file_hash(folder/'plugin.json'),'design_sha256':file_hash(folder/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'no_source_writes':True})
    print(qid,vid,'rendered',flush=True)
if __name__=='__main__':
    for token in sys.argv[1:]:render(*token.split('/'))
