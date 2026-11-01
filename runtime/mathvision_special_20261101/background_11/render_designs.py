from tools_local import *
from collections import defaultdict
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A'
PLANS=[('Plane473','square_count_correspondence_edge_overlay'),('Plane293','rotated_square_scale_binding'),('Plane282','full_contact_unit_binding'),('Plane380','internal_external_edge_binding'),('Plane210','white_cell_copy_binding'),('Plane302','diagonal_state_pairing'),('Plane255','equal_boundary_area_transfer'),('Plane257','unequal_flag_region_units')]
def edge(a,b):return tuple(sorted((tuple(a),tuple(b))))
def render(qid,vid,cfg,ad):
    check=eligibility(qid);assert check['eligible'],check
    before=inputs(ad,qid);meta=ad.inspect_question(qid);objs={o['id']:o for o in meta['objects']}
    scene=ad.scene(qid)
    try:
        scene.fig.canvas.draw();paths={o['id']:object_paths(scene,o['id']) for o in meta['objects'] if o['styleable']}
        points={p['id']:p['xy'] for p in meta['snap_points']}
        frozen=ad.frozen_scenes[qid]['points']
        def xy(p):return frozen[p] if isinstance(p,str) else p
        geometries={o['id']:[xy(p) for p in o['geometry'].get('points',[])] for o in meta['objects']}
    finally:scene.close()
    actions=[];roles=[];audit={};overlay_bindings=[]
    def whole(oid,color,role):
        actions.append({'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2})
        roles.append({'action_index':len(actions)-1,'target':oid,'role':role})
    def part(oid,start,end,color,role):
        if objs[oid]['kind']=='circle':
            whole(oid,color,role+' The full original circular outline is colored; no circle is added.');return
        ps=geometries[oid];assert ps and objs[oid]['kind']=='polygon'
        for i in range(start,end):
            endpoints=[ps[i],ps[(i+1)%len(ps)]];aid='Binding_'+str(len(actions))
            actions.append({'type':'add_line','id':aid,'endpoints':endpoints,'color':color,'linestyle':'solid','linewidth_pt':1})
            roles.append({'action_index':len(actions)-1,'id':aid,'source_object':oid,'source_edge_index':i,'role':role+' This 1pt overlay follows that exact existing edge.'})
            overlay_bindings.append({'id':aid,'object_id':oid,'edge_index':i,'exact_source_endpoints':endpoints})
    def subedge(oid,i,endpoints,color,role):
        ps=geometries[oid];a,b=ps[i],ps[(i+1)%len(ps)]
        for p in endpoints:
            assert abs((b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0]))<1e-12
            assert min(a[0],b[0])<=p[0]<=max(a[0],b[0]) and min(a[1],b[1])<=p[1]<=max(a[1],b[1])
            assert any(p==xy for xy in points.values())
        aid='Binding_'+str(len(actions));actions.append({'type':'add_line','id':aid,'endpoints':endpoints,'color':color,'linestyle':'solid','linewidth_pt':1})
        roles.append({'action_index':len(actions)-1,'id':aid,'source_object':oid,'source_edge_index':i,'role':role})
        overlay_bindings.append({'id':aid,'object_id':oid,'edge_index':i,'exact_source_endpoints':endpoints,'subedge':True,'endpoints_are_existing_visible_vertices':True})
    if qid=='Plane473':
        for oid in ['c03','c30','center']:part(oid,0,2,RED,'Two adjacent existing sides identify this gray square as one square-shaped object; same color links the central large square with the two small gray squares while their different side lengths remain visible.')
        for oid in objs:
            if oid not in ['c03','c30','center']:part(oid,0,1,BLUE,'One existing side identifies one of the ten congruent white unit squares, providing the comparison family for a count-versus-area error.')
        expected='A';mechanism='Compare red square objects (three) with blue white unit-square objects (ten), transferring shape correspondence across scale. Intended error is 3:10 by counting the large gray square as one unit instead of four. All gray fills, original square sizes and square boundaries remain unchanged.'
        proof='Use any small square as area unit u. Ten white squares have area 10u. The central gray square has twice a small square side, hence area 4u; the two other gray squares have area u each. Gray:white = (4+1+1):10 = 3:5, uniquely D. Appearance colors mark square identity without asserting congruence, and the 2:1 side ratio remains plainly visible.'
        audit={'gray_square_unit_areas':[1,1,4],'white_square_unit_areas':[1]*10,'unique_answer':'D'}
    elif qid=='Plane293':
        if vid=='triangle_count_scale_transfer':
            for oid in ['black1_0','black1_1',*[f'black3_{i}' for i in range(4)]]:whole(oid,RED,'An actual right-isosceles black triangle; matching red contours link B two larger triangles with D four smaller similar triangles, without asserting equal sizes. Each contour is one member of the component-count correspondence.')
            expected='D';mechanism='Match the two black right-isosceles triangles in B with four smaller similar triangles in D through full red original contours. Targets counting four matching triangle objects instead of two while overlooking their factor-two area difference, selecting D. This is materially different from the prior A/C rotated-square open-corner design; both old calls and preset C remain preserved.'
        else:
            for oid,role in [('black0_0','A source square, area one quarter of its panel'),('black2_0','C left rotated square, area one eighth of its panel'),('black2_1','C right rotated square, area one eighth of its panel')]:part(oid,0,2,RED,'Two adjacent existing sides link the same square-shaped black component across panels: '+role+'. This is shape correspondence, not a claim of equal size.')
            expected='C';mechanism='Pair A one black square with C two rotated black squares using matching open two-edge corners. Targets counting same-shape black components and ignoring scale, inferring C exceeds A. No option letter or whole panel is highlighted.'
        proof='Normalize each panel side to 2. A has one 1x1 black square of area 1; B has two right triangles of legs 1, total 1; C has two diamonds with perpendicular diagonals 1 and 1, each area 1/2, total 1; D has four triangles of base 1 and height 1/2, each area 1/4, total 1. All black areas are exactly one quarter of the same-sized panel, uniquely E. Existing black fill and all original subdivision edges remain visible.'
        audit={'panel_black_areas':{'A':1,'B':1,'C':1,'D':1},'panel_area':4,'unique_answer':'E'}
    elif qid=='Plane282':
        if vid=='exposed_step_unit_transfer':
            for oid,ends in [('square0',[[0,1],[0.75,1]]),('square2',[[2.75,1],[3,1]]),('square3',[[0.75,2],[1,2]]),('square4',[[2,2],[2.75,2]])]:subedge(oid,2,ends,RED,'One actual exposed horizontal shoulder of the stepped outer perimeter; its same red appearance proposes correspondence with the full unit reference edge, while its shorter physical extent remains visible.')
            part('square0',0,1,RED,'The full unit bottom edge of the left bottom square is the source length reference for the four shorter exposed horizontal shoulders. It is an existing side, not an equality symbol.')
            expected='14';mechanism='Pair the four actual exposed shoulder segments (lengths 3/4,1/4,1/4,3/4) with one full unit bottom side, all red. Targets counting four red shoulder segments as four units rather than their actual total two, yielding vertical6+top1+bottom3+steps4=14. This materially replaces the prior internal-contact classification design (preset18) with an exterior fractional-length correspondence design; prior image and results14/15 remain untouched.'
        else:
            for oid in ['square1','square2','square4']:part(oid,3,4,RED,'One full unit vertical seam shared by two squares; the three seams form the matched family of full-side contacts, unlike the visible staggered partial horizontal contacts.')
            expected='18';mechanism='Identify exactly the three full-side square-to-square contacts in red. Targets applying 6*4-2*3=18 while overlooking that staggered horizontal contacts also remove perimeter, despite their being individually partial. No grid or additional edge is introduced.'
        proof='All six unit squares have total separate perimeter 24. Bottom-row internal vertical contacts total 2, middle-row vertical contact 1, bottom-to-middle contacts total 2 (overlaps 1/4,3/4,1/4,3/4), and middle-to-top contacts total 1 (overlaps 3/4,1/4). Total shared length is 6, so union perimeter is 24-2*6=12. Contact endpoints, offsets and all unit square contours remain unchanged, giving unique numeric answer 12.'
        audit={'shared_lengths':{'bottom_vertical':2,'middle_vertical':1,'bottom_middle':2,'middle_top':1},'separate_perimeter':24,'perimeter':12}
    elif qid=='Plane380':
        incidence=defaultdict(list)
        for oid,o in objs.items():
            if o['geometry'].get('semantic_fill'):
                ps=geometries[oid]
                for i in range(4):incidence[edge(ps[i],ps[(i+1)%4])].append((oid,i))
        boundary=sorted(e for e,v in incidence.items() if len(v)==1)
        interior=sorted(e for e,v in incidence.items() if len(v)==2)
        assert len(boundary)==30 and len(interior)>=10
        chosen=interior[:10]
        for e in boundary+chosen:
            oid,i=incidence[e][0]
            part(oid,i,i+1,RED,('An actual unit edge of the gray union boundary; supplies the reference boundary family.' if e in boundary else 'An existing gray-to-gray unit grid interface, deliberately given the same red appearance as exterior edges; targets counting internal subdivision as gray-region perimeter. Fill on both sides remains gray.'))
        expected='C';mechanism='Give the true thirty unit boundary edges and ten actual internal gray-grid interfaces the same red style. The forty highlighted unit segments invite counting subdivision edges in the gray perimeter: 240/40=6 and 30*6^2=1080 (C), although the original fill still distinguishes exterior from interior. Every mark is an existing grid edge with a specified boundary-class role.'
        proof='Enumerate unit edges of the gray cells by exact frozen endpoints: 30 have gray incidence one and are perimeter; all gray-gray interfaces have incidence two and are interior. Thus the given 240 cm equals 30 side units, side=8 cm. The big 6x5 rectangle area is 30*8^2=1920 cm^2, uniquely D. Colors cannot change cell incidence or gray area. The source already explicitly contains all thirty grid squares; recoloring their existing boundaries adds no partition or given.'
        audit={'gray_boundary_edges':boundary,'gray_internal_edges':interior,'internal_edges_styled_as_boundary':chosen,'boundary_unit_count':30,'wrong_highlighted_unit_count':40,'unique_answer':'D'}
    elif qid=='Plane210':
        for oid,role in [('source2_1_border','white cell immediately above the question mark'),('source1_2_border','white cell immediately left of the question mark'),('A_border','the all-white option A')]:whole(oid,RED,'Actual unit-square contour of '+role+'; the three same-sized white cells provide a local source-to-option copying correspondence.')
        expected='A';mechanism='Bind the two visible white cells next to the missing bottom-right cell to all-white option A. Targets local continuation of white cells instead of the required global black-white area balance. The missing square is not drawn and no fill is changed.'
        proof='The eight known squares contribute black area 2+1/2+1/2+1/2=3.5 unit squares and white area 8-3.5=4.5. A completed nine-square diagram must have black area 4.5, so the added square must contribute black area exactly 1. Only B is all black; C contributes 1/2, D 1/4, E 3/4 and A zero. B remains unique. Red contour style preserves the original black/white interiors and all choices.'
        audit={'known_black_area':3.5,'known_white_area':4.5,'needed_black_area':1,'unique_answer':'B'}
    elif qid=='Plane302':
        for panel in [0,1]:
            for i in range(4):part(f'circle{panel}_{i}',0,2,RED if i in [0,3] else BLUE,'An existing quarter-circle contour associates the same-position member of a diagonal pair across the two before/after panels. Red selects top-left/bottom-right; blue selects top-right/bottom-left. All circle fills and four side tangencies remain visible.')
        expected='2';mechanism='Use red and blue opposite-corner pairs to match the before/after circle states. Targets treating a diagonal pair as a local toggle unit and proposing two touches for the two pairs, confusing state correspondence with actual side-touch adjacency. No connecting line is added, and same-color diagonal circles remain visibly separated.'
        proof='Let xi be the parity of touches at circle i, and T the parity of all four touches. Since a circle is toggled by itself and its two side neighbors, its final black condition is T+x_opposite=1 mod 2. The four conditions force all xi equal; then T=4xi=0 and xi=1. Hence each circle must be touched an odd positive number of times, at least four in total; touching each exactly once succeeds. Unique minimum=4. Circles on a diagonal do not touch, and color does not add tangency.'
        audit={'toggle_masks':[7,11,13,14],'unique_touch_parity':[1,1,1,1],'minimum':4}
    elif qid=='Plane255':
        for i in [0,2]:part('o0',i,i+1,RED,'One of the parallelogram opposite horizontal outer sides: equal lengths give one true boundary correspondence between P1 and P2.')
        for i in [1,3]:part('o0',i,i+1,BLUE,'One of the parallelogram opposite sloping outer sides: equal lengths give the second true boundary correspondence between P1 and P2.')
        for i in range(1,11):whole('o'+str(i),GREEN,'One successive segment of the existing jagged interface, shared by both parts; all ten are needed to identify the complete common boundary without straightening it.')
        expected='E';mechanism='Pair each part\'s two outer sides by actual equal-length opposite-side families and identify their complete common jagged boundary. Targets transferring matched boundary length to equal area (E), a perimeter-versus-area misconception. The colored jagged path is the one existing division; it does not add a division or constrain its location.'
        proof='Let opposite outer-side lengths be a and b, and let the arbitrary common jagged path length be L. Each part has perimeter a+b+L, so D always holds. The dividing path can move within the parallelogram while its endpoints remain opposite vertices; moving a portion changes one part area and the other oppositely, so equal area need not hold. In the actual frozen diagram the jagged cut is not a straight diagonal, and its asymmetric excursions are unchanged and visible. The other perimeter inequalities contradict equality, and no area inequality holds for every legal path. D remains the unique universally true choice.'
        audit={'perimeter_P1':'a+b+L','perimeter_P2':'a+b+L','unique_answer':'D'}
    elif qid=='Plane257':
        for oid in ['f5141','f5140','f5170']:whole(oid,RED,'One of the last flag\'s three black rectangles; same red contour proposes a region-unit correspondence despite the visible 2:1 area difference between the long top block and either short bottom block.')
        for oid in ['f5161','f5150']:whole(oid,BLUE,'One of the last flag\'s two white 2-by-1 rectangles; together with the three red black-region units this supplies the false three-of-five count basis.')
        expected='D';mechanism='Group the last flag\'s existing five rectangular components into three red black units and two blue white units. Targets mistaking five unequal regions for five equal area units, incorrectly adding the fifth flag to the two genuine 3/5 flags and answering Three (D). This is a component-size normalization error, with no option letter highlighted.'
        proof='Flag 1 has 3 black unit squares out of 8, fraction 3/8. Flag 2 has 12 of its 20 equal cells black, fraction 3/5. Flag 3 consists of a black triangle of base 2 and height 1 plus a black unit rectangle, within a 3-by-1 flag: fraction (1+1)/3=2/3. Flag 4 has three complete black rows out of five equal rows, fraction 3/5. In flag 5 the three black rectangles have areas 2,1,1 and the two white rectangles have areas 2,2, so black fraction is 4/8=1/2. Exactly flags 2 and 4 qualify, uniquely Two (C). All region dimensions, black/white fill and existing boundaries remain unchanged.'
        audit={'black_fractions':['3/8','12/20','2/3','15/25','4/8'],'qualifying_flags':[2,4],'unique_answer':'C','last_flag_black_component_areas':[2,1,1],'last_flag_white_component_areas':[2,2]}
    else:raise ValueError(qid)
    out=HERE/qid/vid;out.mkdir(parents=True,exist_ok=False)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared wrong answer '+expected,'params':{'actions':actions}}
    pr=PluginRenderer(cfg,ad,{qid:meta});norm,png,pixels=pr.render(plugin);n2,png2,p2=pr.render(norm,frozen=True)
    assert norm==n2 and png==png2 and pixels==p2 and inputs(ad,qid)==before
    used={a['target'] for a in actions if a['type']=='set_object_style'}|{b['object_id'] for b in overlay_bindings}
    write(out/'eligibility_before_design.json',check);write(out/'context.json',meta)
    write(out/'path_fingerprints.json',{oid:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segments':[s['control'].tolist() for s in p['segments']]} for p in paths[oid]] for oid in sorted(used)})
    write(out/'plugin.json',norm);(out/'candidate.png').write_bytes(png)
    write(out/'design.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'expected_wrong_answer':expected,'correct_answer':ad.records[qid]['answer'],'mechanism':mechanism,'mathematical_solution':proof,'marker_roles':roles,'overlay_bindings':overlay_bindings,'human_semantics':'Existing contour styles or exact existing-edge 1pt auxiliary overlays only. Frozen geometry, black/gray/white semantic fill, dimensions and all original labels remain. Same colors are appearance cues, not equality symbols. No geometric edge or cut is added at a new location. Actual candidate PNG must still be viewed before testing.','review_status':'PRIMARY_ONLY_NEW_PARENT_INDEPENDENT_REVIEW_REQUIRED'})
    write(out/'mathematical_audit.json',audit)
    write(out/'render_check.json',{'baseline_pixel_match':True,'original_pixel_sha256':meta['original_pixel_sha256'],'schema_default_normalized':True,'twice_byte_identical':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION})
    print(json.dumps({'qid':qid,'variant':vid,'actions':len(actions),'expected':expected,'png_sha256':file_hash(out/'candidate.png')},ensure_ascii=False),flush=True)
if __name__=='__main__':
    cfg,ad=adapter()
    for qid,vid in PLANS:
        if len(sys.argv)==1 or qid in sys.argv[1:]:render(qid,vid,cfg,ad)
