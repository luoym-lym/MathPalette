from tools28 import *
import itertools, math
R='#DC2626';O='#EA580C';G='#16A34A'
def project(qid,p):
    t=AD.scenes[qid]['projection'];v=[p[i]-t['origin'][i] for i in range(3)]
    return [sum(t['matrix'][j][i]*v[i] for i in range(3))+t['offset'][j] for j in range(2)]
def edges_on(qid,a,b):
    # Exact stored unit edges on a prescribed original straight edge chain.
    v=[b[i]-a[i] for i in range(3)];vv=sum(t*t for t in v);found=[]
    for obj in AD.scenes[qid]['objects']:
        if obj['type']!='segment' or obj.get('visibility')!='visible':continue
        pts=obj['points'];ts=[]
        for p in pts:
            t=sum((p[i]-a[i])*v[i] for i in range(3))/vv
            if t < -1e-10 or t>1+1e-10 or any(abs(p[i]-a[i]-t*v[i])>1e-10 for i in range(3)):break
            ts.append(t)
        if len(ts)==2 and abs(ts[0]-ts[1])>1e-10:found.append((min(ts),max(ts),obj))
    # Source mergedmaterial may duplicate coincident unit edges; one style action per stable object is retained if needed.
    found.sort(key=lambda e:e[:2]);covered=0
    for lo,hi,obj in found:
        assert lo<=covered+1e-9,(qid,a,b,'gap',covered,lo)
        covered=max(covered,hi)
    assert covered>=1-1e-9,(qid,a,b,'incomplete',covered)
    return [o for _,_,o in found]
def chain(qid,a,b,color,role):
    context=read(TASK/qid/'context.json');registry={o['id']:o for o in context['objects']}
    out=[]
    for obj in edges_on(qid,a,b):
        target=registry[obj['id']];assert target['styleable']
        out.append(({'type':'set_object_style','target':obj['id'],'color':color,'linewidth_pt':2},
                    {'role':role,'source_object_id':obj['id'],'world_endpoints':obj['points'],'projected_endpoints':[project(qid,p) for p in obj['points']],'frozen_geometry_sha256':canonical_hash(obj),'partial_paths':target.get('partial_paths',[]),'path_handling':'Whole native segment; partial interval not requested. Stable ID and full-precision frozen geometry bound.'}))
    return out
def point(qid,mid,p,role):
    return ({'type':'add_point','id':mid,'xy':project(qid,p),'color':O}, {'role':role,'world_anchor':p,'projected_xy':project(qid,p),'coordinate_basis':'Exact frozen projection applied to declared existing vertex or midpoint of an original visible edge; no new spatial point condition.','point_kind':'appearance annotation, not cube material'})

def make(qid,vid,preset,intent,new_vs_old,proof,marks,limits=None):
    folder=TASK/qid/vid
    if folder.exists():
        assert (folder/'design.json').is_file()
        print('Preserving previously frozen candidate',qid,vid,flush=True);return
    assert vid.startswith('r28_') and not folder.exists()
    check=eligibility(qid);assert check['eligible'];folder.mkdir()
    write(folder/'eligibility_at_design.json',check)
    # Audit is physically frozen BEFORE rendering and before calls, with an actual new geometric rationale.
    old=read(TASK/qid/'prior_history_full.json')
    olddesigns=[]
    for p,txt in old['full_text_records'].items():
        if Path(p).name=='design.json':
            d=json.loads(txt);olddesigns.append({'path':p,'variant_id':d.get('variant_id'),'preset':d.get('expected_wrong_answer'),'sha256':next(f['sha256'] for f in old['all_evidence_files'] if f['path']==p)})
    own_prior=[]
    for p in sorted((TASK/qid).glob('r28_*/manual_final_review.json')):
        r=read(p);own_prior.append({'review_path':str(p),'review_sha256':file_hash(p),'variant_id':p.parent.name,'preset':r['preset'],'complete_manual_finals':[x['manual_final_answer'] for x in r['manual_results']],'design_sha256':file_hash(p.parent/'design.json'),'PNG_sha256':file_hash(p.parent/'candidate.png')})
    audit={'stage':'material_refinement','question_id':qid,'variant_id':vid,'created_at':now(),'prior_history_file':str(TASK/qid/'prior_history_full.json'),'prior_history_sha256':file_hash(TASK/qid/'prior_history_full.json'),'all_same_question_history_read':True,'all_old_unique_pngs_native_viewed':True,'old_designs':olddesigns,'own_completed_material_refinement_history':own_prior,'new_information_grouping_or_misconception':new_vs_old,'predeclared_wrong_final':preset,'geometric_derivation_of_new_wrong_final':intent,'old_observed_wrong_answer_is_not_a_new_preset_rationale':True,'not_cosmetic_or_unchanged_repeat':True,'independent_objections_for_assigned_question':'None found in assignment, same-question directories, or exact question/variant report references. Prior prescreen objections are addressed in new mechanism.'}
    write(folder/'design_difference_audit.json',audit)
    # Deduplicate shared native edge actions without discarding the multiple information roles.
    unique={};roles=[]
    for action,role in marks:
        key=(action['type'],action.get('target',action.get('id')))
        if key in unique:
            roles[unique[key]]['roles'].append(role)
        else:
            unique[key]=len(roles);roles.append({'action':action,'roles':[role]})
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':vid,'intent':intent[:1000],'params':{'actions':[r['action'] for r in roles]}}
    report=AD.render_candidate(plugin,folder/'rendered')
    for name in ['candidate.png','plugin.json','render_check.json','context.json']:(folder/name).write_bytes((folder/'rendered'/name).read_bytes())
    design={'question_id':qid,'variant_id':vid,'stage':'material_refinement','created_at':now(),'expected_wrong_answer':preset,'correct_answer':str(AD.records[qid]['answer']),'intended_misconception':intent,'new_vs_old':new_vs_old,'unique_original_mathematics':proof,'each_marker_proof':roles,'frozen_png_sha256':file_hash(folder/'candidate.png'),'frozen_pixel_sha256':report['pixel_sha256'],'plugin_sha256':file_hash(folder/'plugin.json'),'difference_audit_sha256':file_hash(folder/'design_difference_audit.json'),'human_semantics':'Only legal appearance marks. No original face fill, text, unit count, labels, geometry, 3D projection or frozen visibility is changed. No equality, dimension label, pip, hidden edge, cut or puzzle piece is added. Colors are annotations, not new givens. Existing-edge open patterns preserve the original distinctions.','limits':limits or [],'review_status':'Primary author assessment only; NEW independent parent review required before eventual delivery.'}
    write(folder/'design.json',design)
    write(folder/'schema_and_marker_audit.json',{'actual_normalized_plugin':read(folder/'plugin.json'),'normalization_via':'Unchanged PluginRenderer.render called twice','deterministic_png_bytes':report['deterministic'],'baseline_pixel_match':report['baseline_matches_formal'],'marks':roles,'only_permitted_schema_actions':True,'appearance_changes':report['appearance_changes']})
    print(json.dumps({'qid':qid,'variant_id':vid,'preset':preset,'marks':len(roles),'image':str(folder/'candidate.png')}),flush=True)

if __name__=='__main__':
    q='Solid86';m=[]
    for i,z in enumerate([0.5,1.5,2.5]):m.append(point(q,'heightcell'+str(i),[4,0,z],'One midpoint for each of three actual height-unit intervals; the three-point reference rhythm.'))
    for i,y in enumerate([0,1,2]):m.append(point(q,'depthboundary'+str(i),[4,y,3],'One of THREE actual depth boundary vertices spanning only TWO unit intervals; matched rhythm can transfer height cell-count to depth.'))
    make(q,'r28_depth_vertices_as_cells','8','Pair the three height-unit midpoint anchors with the three depth-boundary anchors, confusing three boundary vertices with three depth cubes: 4*3*3/2-10=8 hidden white cubes.',
        'Old white_face_identity_swap paired white-face centers for false deduplication (preset3; finals14/1). This uses no material/face identity pairs. It changes the counting object to boundary vertices versus edge intervals on a depth chain; preset8 follows a new 3-versus2 dimension error, not either old final.',
        'The visible block is4wide,2deep,3high:24cubes,12white. White front cube cells(1,0,1),(2,0,0),(2,0,1),(2,0,2),(3,0,0); rear top adds(1,1,2),(2,1,2),(3,1,2); rear right lower adds(3,1,0),(3,1,1):10distinct. Thus hiddenwhite=2. Orange boundary marks do not alter white/gray ownership.',m)
    q='Solid109';m=[]
    m+=chain(q,[1,0,1],[4,0,1],O,'Central-front 3-unit horizontal cross-section span; one skin layer is excluded at each x end.')
    m+=chain(q,[1,0,1],[1,0,3],O,'Central-front 2-unit vertical cross-section span; one skin layer excluded at each z end. Open L, not a new hole.')
    m+=chain(q,[1,0,4],[1,4,4],O,'Entire4-unit depth chain matched to the reduced3-by2 cross-section; intended error fails to remove front/back skin.')
    make(q,'r28_interior_section_full_depth','24','Bind a genuine3-by2 interior-size front cross-section to the entire4-unit depth, omitting the two red depth skins:3*2*4=24 blue cubes.',
        'Old prescreen rejected blue material markers on exterior cells because no interior cube is visible. This avoids any blue or face fill: existing orange open edge spans encode three reduced cross-section dimensions versus the unreduced depth. This is a concrete partial-shell extrusion hypothesis, not a claim that a surface cube is blue.',
        'Source grid dimensions5by4by4. Blue cubes require all coordinates strictly inside boundary: x=1,2,3;y=1,2;z=1,2. Exactly3*2*2=12, independently enumerable. Orange edge marks do not assign material to a face.',m)
    q='Solid123';m=[]
    # Prototype spans are three unit edges each; each remains the original visible contour.
    m+=chain(q,[0,0,0],[0,0,3],G,'Longest leg of5-unit L prototype has3-unit span; matching the3-unit bar span can collapse volume to longest leg.')
    # The bar exemplar is shifted in frozen source. Derive its long boundary from exact native segments below.
    bar_edges=[o for o in AD.scenes[q]['objects'] if o['type']=='segment' and o['id'].startswith('examplebar')]
    if not bar_edges:bar_edges=[o for o in AD.scenes[q]['objects'] if o['type']=='segment' and o['id'].startswith('exampleBar')]
    assert bar_edges,'Missing exact bar prototype IDs'
    # Find an original chain along the bar length (3) among native endpoints.
    pts=sorted({tuple(p) for o in bar_edges for p in o['points']})
    choices=[]
    for a,b in itertools.combinations(pts,2):
        diff=[abs(a[i]-b[i]) for i in range(3)]
        if sum(d>1e-8 for d in diff)==1 and abs(max(diff)-3)<1e-8:
            try:ee=edges_on(q,a,b)
            except AssertionError:continue
            if all(o['id'].startswith(('examplebar','exampleBar')) for o in ee):choices.append((a,b))
    assert choices
    a,b=choices[0];m+=chain(q,a,b,G,'Complete3-unit dark bar exemplar long span; geometric3-unit counterpart of highlighted L leg, although their volumes differ5versus3.')
    make(q,'r28_L_leg_to_bar_span','15','Match the L prototype longest3-unit leg to the dark3-unit bar; confuse shared longest span with unit volume, counting each of the two Ls as3instead of5:27-2*3-2*3=15white.',
        'Old prescreen considered generic ownership reassignment and new subdivisions, rejected as confusing. New design changes no ownership and introduces no subdivision: two existing full-length prototype boundary chains establish a true equal3-unit span while targeting the false span-to-volume inference. L elbow and distinct light/dark fills remain intact.',
        'The assembled3cube has27cells. Light L pieces occupy two disjoint5-cell sets and dark bars two3-cell sets. The visible front/top/right material observations leave only one wholly hidden cell; no additional5-cellL or3-cellbar can be hidden. Exact compatible-placement enumeration is saved separately. Therefore27-10-6=11white. The3-unit leg is not the5-unit L volume.',m,['Material classes are shown at small original scale; native PNG inspection required.'])
    q='Solid125';m=[]
    m+=chain(q,[0,0,0],[3,0,0],R,'Whole reference cube front face horizontal3-unit extent, encoding one of six original big faces.')
    m+=chain(q,[0,0,0],[0,0,3],R,'Whole reference front face vertical3-unit extent; combined open L encloses no new region.')
    for a,b,role in [([6.5,2,1],[7.5,2,1],'one unit of back wall width'),([6.5,2,1],[6.5,2,2],'one unit of back wall height'),([6.5,0,1],[6.5,1,1],'one unit of side wall depth / floor depth'),([6.5,0,1],[6.5,0,2],'one unit of side wall height'),([6.5,0,1],[7.5,0,1],'one unit of floor width')]:m+=chain(q,a,b,R,'Unit-face sample: '+role+'; false one-unit-square to whole-big-face calibration.')
    make(q,'r28_big_face_to_unit_tile','18','Match the original whole3-by3face L to one-unit white tile Ls across three planes, then misapply9/6=1.5kg per BIG face to all12white UNIT faces:12*1.5=18kg.',
        'Old three_plane_area_binding mapped each ENTIRE2by2white plane to a whole3by3face, preset4.5; old finals8/3 and12 missed. New markers bind one-unit sample tiles (not entire white planes) to ONE original face and target a unit-of-area calibration error followed by counting12tiles. Geometry granularity and arithmetic mechanism change; neither old observed final is selected.',
        'Reference surface6*3^2=54unitarea. Three new white2by2planes have12unitarea. Uniform9kg/54 gives1/6kg per UNIT area and12/6=2kg. Big face costs1.5kg, but consists of9unit tiles; retained unit seams distinguish these sizes.',m)
    q='Solid129';m=[]
    # Full reference top face two outer sides, plus all four highest remaining unit tops.
    # Right cube is shifted along x by6.6 in this frozen source; derive using native panel bounds.
    s=AD.scenes[q];segments=[o for o in s['objects'] if o['type']=='segment']
    prefixes=sorted({o['id'].split('e')[0] for o in segments});print('Solid129prefixes',prefixes,flush=True)
    # Exact model offset determined from its panel1 edges, not screen measurement.
    right=[o for o in segments if o['id'].startswith('partial')]
    assert right
    offset=min(p[0] for o in right for p in o['points'])
    topz=max(p[2] for o in right for p in o['points'])
    m+=chain(q,[0,0,3],[3,0,3],O,'Reference top layer width3: one side of9-cell layer extent.')
    m+=chain(q,[0,0,3],[0,3,3],O,'Reference top layer depth3: perpendicular side of9-cell layer extent.')
    for x,y in [(0,0),(0,1),(0,2),(1,2)]:
        # Pick two visible consecutive sides of each highest top face, using frozen existing geometry.
        v=[(offset+x,y,topz),(offset+x+1,y,topz),(offset+x+1,y+1,topz),(offset+x,y+1,topz)]
        pairs=[]
        for i in range(4):
            try:edges_on(q,v[i],v[(i+1)%4]);edges_on(q,v[(i+1)%4],v[(i+2)%4])
            except AssertionError:continue
            pairs=[(v[i],v[(i+1)%4]),(v[(i+1)%4],v[(i+2)%4])];break
        assert pairs
        for a,b in pairs:m+=chain(q,a,b,O,'Highest-layer existing cube(%s,%s,2) top boundary; all4highest cubes grouped against9reference cells. Lower layers stay readable.'%(x,y))
    make(q,'r28_highest_layer_only','5','Match the complete nine-cell top layer with the four highest existing top cells; stop at9-4=5missing and omit the two missing cubes in the middle layer.',
        'Old Solid129 had no saved design or API calls; prior prescreen mentioned no specific new layer/cavity correspondence. This is an explicit whole-layer-to-highest-footprint comparison, selecting ALL four z=2cells, with specific omission of the two z=1gaps. No missing cube outlines or invented partitions are added.',
        'Source column heights by front-to-back row are[3,2,1],[3,2,1],[3,3,2]. Layers have9,7,4cubes, so missing=(9-9)+(9-7)+(9-4)=0+2+5=7. Existing top-level color patterns change attention, not height or occupied cells.',m)
    q='Solid143';m=[]
    for a,b,role in [([1,0,1],[1,1,1],'Left die hidden right-interface top depth edge; real seam, no hidden edge is drawn.'),([1,0,0],[1,0,1],'Left die hidden right-interface front vertical edge; second leg of interface open L.'),([2,0,1],[2,1,1],'Right die exposed right-face top depth edge; true parallel-plane counterpart.'),([2,0,0],[2,0,1],'Right die exposed right-face front vertical edge; transfer of its visible2pips is the targeted error.')]:m+=chain(q,a,b,G,role)
    make(q,'r28_interface_side_value_transfer','25','Pair the internal right-interface seam of the left die with the exposed two-pip right face of the right die. Transfer that visible2 to the occluded left die interface and subtract it twice:42-(1+2+4+6+2+2)=25.',
        'Old prescreen had no design/calls and rejected arbitrary pip/number salience. New two open parallel-face L motifs map a genuinely hidden interface boundary to an exposed same-oriented side plane. This targets hidden-vs-visible face ownership and value transfer; no pip is colored, added, removed or covered.',
        'Under the original ordinary1-through6dice interpretation, each die has21total pips. All15visible original pips are countable: lefttop1,leftfront2,righttop4,rightfront6,rightside2. Invisible sum42-15=27, independent of exact hidden orientation. The left right-interface remains invisible even when its existing seam edges are green.',m,['The formal source already assumes ordinary1–6dice; no alternative numbering is specified. Annotation color does not imply equal pip values.'])
