from tools_b import *
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A';ORANGE='#EA580C'
def style(target,color):return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':2}
DESIGNS={
('Plane223','large_spot_ring_correspondence'):{
 'expected_wrong_answer':'C',
 'mechanism':'The largest solid source dot and the source ring are paired, respectively, with the largest solid dot and ring in option C. This binds two concrete shape features across the stated color swap, inviting acceptance of C from local feature identity while overlooking their incompatible spatial separation and orientation. It is a two-feature false rigid correspondence, not standalone option highlighting; all original black/yellow fills stay intact.',
 'actions':[style('o5',RED),style('o30',RED),style('o7',BLUE),style('o32',BLUE)],
 'mathematical_solution':'After swapping black/yellow, the six solid dots and one annular dot must preserve their positions relative to the outer circle up to a single rotation. E is exactly the180-degree image: each dot vector relative to source center(8,6) negates to the corresponding E vector relative to(16.8,0), with all original radii and annulus radii identical. A contains an extra solid dot; B and D omit dots/the ring or contain too few dots. C has the same feature count but cannot be a rigid image: the center displacement from the radius0.25 largest solid dot to the unique ring is(1.55,-0.60) in the source, squared length2.7625, whereas in C it is(1.08,0.64), squared length1.5760. Rotation cannot change this distance. Thus E remains the sole possible answer. The source and C radii/ring shade are unmodified by the four contour annotations.',
 'marker_roles':['o5 red: source radius0.25 solid yellow dot, one anchor feature before color inversion.','o30 red: C radius0.25 solid black dot, the proposed counterpart after inversion.','o7 blue: source outer contour of the unique annular dot; inner black disc is untouched.','o32 blue: C outer annulus contour, proposed as the second counterpart; its yellow center remains unchanged.'],
 'human_gate':'Only four existing dot/ring boundaries receive legal2pt colored outlines. The black/yellow semantic interiors, all seven original feature positions, outer discs and all option letters are intact. No extra dot, hole, label or equality mark is added. Both colored source-to-option pairs have explicit feature roles.'},
('Plane226','separated_star_pair'):{
 'expected_wrong_answer':'C',
 'mechanism':'The two actual source stars in the same column but separated by an intervening club cell are paired by red and blue outlines with the two adjacent stars in option C. This targets treating selected parts as an adjacent domino while overlooking their true one-cell separation and unequal star orientations. It binds input symbols to candidate symbols rather than highlighting an option in isolation.',
 'actions':[style('board13star',RED),style('board11star',BLUE),style('option2_0star',RED),style('option2_1star',BLUE)],
 'mathematical_solution':'A legal piece is one pair of orthogonally adjacent unit cells, transformed rigidly. B is exactly the top-row upright star and upright club immediately to its right (column2 to3). A requires an upright star with an upright spade immediately to its right, absent in the grid; the lower star is itself rotated20 degrees and cannot become an upright star under the quarter-turns allowed by cell adjacency. C requires adjacent stars, but the only two stars are separated by one club cell. D requires the shown downward heart followed by a vertical diamond; the neighboring heart/diamond at the bottom left does not have the required orientation relative to its connecting line. E has two horizontally adjacent downward hearts; the two identical downward source hearts are vertically adjacent, so a quarter-turn makes both point sideways. Enumerating all24 undirected board-adjacencies in both orders and the four grid-preserving rotations, with the visible symbol orientations, matches only B. Source cells, all symbol contours, rotations, and fills are unchanged.',
 'marker_roles':['board13star red: first actual source star, top row column2.','board11star blue: second actual source star, third row column2, separated by the middle club.','option2_0star red: proposed first member of the false adjacent-star correspondence.','option2_1star blue: proposed second member; paired color does not move either source cell or grant adjacency.'],
 'human_gate':'Only the four existing star outlines are recolored/thickened within the whitelist. Their black semantic fills, orientation and count are retained. All cell boundaries, the intervening club, option labels and the given two-square piece are clear; no cut line or false relation symbol is added.'},
('Plane234','three_feature_match_ignores_gray'):{
 'expected_wrong_answer':'D',
 'mechanism':'Four ordered source rays (sunray3..6) are paired one by one with the four rays of option D using four fixed outline colors. The outer dark rays and first small white ray agree under a90-degree turn; the third ray is actually medium gray/length1.75 in the source versus short white/length1.5 in D. This targets accepting a nearly matching ordered part by binding its mismatched third ray to the wrong white partner. All semantic shades and lengths remain explicit.',
 'actions':[style('sunray3',RED),style('sunray4',BLUE),style('sunray5',GREEN),style('sunray6',ORANGE)],
 'edge_overlays':[('3ray0',RED),('3ray1',BLUE),('3ray2',GREEN),('3ray3',ORANGE)],
 'mathematical_solution':'Encode every ray by its preserved shade and radius: S=(white,1.5), M=(gray,1.75), L=(dark,2). Clockwise starting at sunray0 the cycle is M,M,L,L,S,M,L,S,S,S,M,L,L,M,S,L,S,S. The five option words in left-to-right(clockwise) order are A=LLSS, B=LMSL, C=MLMS, D=LSSL, E=SSLS. Enumerating all18 length4 cyclic windows gives only B=LMSL at sunray12..15. No A,C,D,E word occurs. A rigid turn preserves order, every ray length and shade, so B is unique. The candidate still visibly has source sunray5 gray and longer than the white third ray in D; the added outlines confer no new equality condition.',
 'marker_roles':['sunray3 red: source dark first endpoint ray.','3ray0 red: candidate D first dark ray proposed as its rotation partner.','sunray4 blue: source first small white ray.','3ray1 blue: D second ray, a true local feature match.','sunray5 green: source medium gray ray, the deliberately mismatched third input feature.','3ray2 green: D third ray, short and white, false correspondence partner.','sunray6 orange: source final dark endpoint ray.','3ray3 orange: D final dark ray, closing the four-feature ordered match.'],
 'human_gate':'All gray/white/dark fills, ray lengths, order, face and option letters remain unchanged and readable. The green third-ray pair visibly differs in fill and length; outline colors are optional correspondence annotations, not a new condition that colors must match. No ray is added or removed.'}
}
def render(qid,vid):
    d=copy.deepcopy(DESIGNS[qid,vid]);check=eligibility(qid);assert check['eligible'],check
    cfg,ad=adapter();before=inputs(ad,qid);meta=ad.inspect_question(qid);renderer=PluginRenderer(cfg,ad,{qid:meta})
    overlay_bindings=[]
    for oid,color in d.pop('edge_overlays',[]):
        geom=next(o['geometry'] for o in meta['objects'] if o['id']==oid)
        vertices=[c['point'] for c in geom['commands'] if c['op'] in ['move','line']]
        assert len(vertices)==3
        for j in range(2):
            action={'type':'add_line','id':'Pair_'+oid+'_edge'+str(j),'endpoints':vertices[j:j+2],'linestyle':'solid','color':color,'linewidth_pt':1}
            d['actions'].append(action)
            overlay_bindings.append({'action_id':action['id'],'fresh_original_object_id':oid,'fresh_exact_vertices':action['endpoints'],'role':'Overlay one existing triangular side of the proposed rotation partner; semantic fill and curved base remain intact.'})
    scene=ad.scene(qid)
    try:
        scene.fig.canvas.draw()
        targets=sorted({a['target'] for a in d['actions'] if a['type']=='set_object_style'}|{b['fresh_original_object_id'] for b in overlay_bindings})
        paths={oid:[{k:v for k,v in p.items() if k in ['id','sha256','closed','samples','segment_count']} for p in object_paths(scene,oid)] for oid in targets}
    finally:scene.close()
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':d['mechanism'],'intent':'Predeclared wrong answer '+d['expected_wrong_answer'],'params':{'actions':d.pop('actions')}}
    normalized,png,pixels=renderer.render(plugin)
    normalized2,png2,pixels2=renderer.render(normalized,frozen=True)
    assert normalized==normalized2 and png==png2 and pixels==pixels2
    assert before==inputs(ad,qid)
    dest=sys.argv[3] if len(sys.argv)>3 else vid
    out=HERE/qid/dest;out.mkdir(parents=True,exist_ok=False)
    write(out/'eligibility_before_design.json',check);write(out/'context.json',meta);write(out/'path_fingerprints_complete.json',paths)
    write(out/'plugin.json',normalized);(out/'candidate.png').write_bytes(png)
    write(out/'design.json',{'question_id':qid,'variant_id':dest,'created_at':now(),'correct_answer':ad.records[qid]['answer'],**d,'edge_overlay_bindings':overlay_bindings,'review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'})
    write(out/'render_check.json',{'question_id':qid,'baseline_pixel_match':True,'schema_default_normalized':True,'two_byte_identical_redraws':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'geometry_fill_labels_unchanged':True,'appearance_actions':normalized['params']['actions']})
    print(json.dumps({'qid':qid,'variant':vid,'png_sha256':file_hash(out/'candidate.png'),'rendered':True}),flush=True)
if __name__=='__main__':render(sys.argv[1],sys.argv[2])
