from tools_local import *
import math,itertools
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A'
def resolved(qid,oid,meta):
    obj=next(o for o in meta['objects'] if o['id']==oid)
    pts=obj['geometry'].get('points',[]);sc=read(ROOT/'PlaneGeometry'/read(HERE/qid/'formal_record.json')['scene'])
    return [sc['points'][p] if isinstance(p,str) else p for p in pts]
def build(qid,vid):
    check=eligibility(qid);assert check['eligible'];cfg,ad=adapter();before=inputs(ad,qid);meta=ad.inspect_question(qid)
    sc=ad.scene(qid)
    try:
        sc.fig.canvas.draw();paths={o['id']:object_paths(sc,o['id']) for o in meta['objects']}
    finally:sc.close()
    actions=[];roles=[]
    def whole(oid,color,role):
        actions.append({'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2});roles.append(role)
    def line(xy,color,role):
        actions.append({'type':'add_line','id':'Guide'+str(len(actions)),'endpoints':xy,'color':color,'linestyle':'dashed','linewidth_pt':1,'dash_pattern_pt':[3.7,1.6]});roles.append(role)
    def edge(oid,index,color,role):
        path=paths[oid][0];n=len(path['segments'])
        actions.append({'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2,'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':index/n,'end':(index+1)/n,'wrap':False}});roles.append(role)
    if qid=='Plane320':
        for idx in [0,2]:edge('o0',idx,RED,'One of the two equal radial legs of the original shaded triangle0, part of the source side-type correspondence.')
        edge('o0',1,BLUE,'The nonradial base of original triangle0; distinguishes the base from its equal legs.')
        for oid in ['o6','o7']:whole(oid,RED,'One equal radial leg of displayed triangle2, paired with the red radial legs of triangle0. The different spatial rays stay visible.')
        whole('o2',BLUE,'Base of displayed triangle2, paired with the blue base of triangle0. Congruence does not imply superposition.')
        expected='2';mechanism='Map the equal-leg/base structure of shaded triangle0 to displayed triangle2 in two colors. Targets treating the first emphasized congruent triangle as the first spatially coincident triangle, overlooking its 200-degree rotation. No angle or equality symbol is added.'
        proof='All radial legs have the same length, and each triangle spans100 degrees at A, with consecutive triangles rotated100 degrees counterclockwise. Triangle n has boundary-ray set {theta+100n,theta+100(n+1)}. Equality with triangle0 can preserve both rays only if100n is a multiple of360, first n=18. Swapping the rays would simultaneously require100n=100 and100n=-100 modulo360, impossible since200 is not0 modulo360. Thus the first full coincidence is18. The colors identify true side types only; they do not move the rays or original shade/labels.'
        clarity='Six existing object/interval styles pair true leg/base types across triangles0 and2. The shaded triangle0, A/B/C and numeric labels0,1,2,3 remain legible. No new edge, region or central angle is inserted.'
    elif qid=='Plane230':
        for tip,color in [(0,RED),(2,BLUE),(4,GREEN),(6,'#EA580C'),(8,RED)]:
            for idx in [(tip-1)%10,tip]:edge('irregular_pentagram',idx,color,'One of the two original boundary arms meeting at source tip '+str(tip)+'. The adjacent same-color pair identifies a local triangular lobe, without adding a base or closed cut. The separated first/fifth red lobes remain spatially distinct.')
        expected='5';mechanism='Group each original pair of exposed tip arms as one local triangular lobe. Targets confusing the five visible pointed lobes with the minimum number of full overlapping triangles; the five open V pairs do not draw any hidden base or assert a partition.'
        proof='The source has five convex tips. Every hull of three tips protrudes outside the original star, proved for all ten triples by polygon clipping in three_triangle_proof.json; a contained triangle can therefore include at most two tips, so two triangles cannot cover all five. The same audit gives an explicit cover by three triangles formed from the original supporting lines, verifies each is contained in the star, and verifies the full union equals the original star area. Thus the exact minimum is3; contour coloring does not alter this region.'
        clarity='Only ten existing contour intervals are recolored into five open V lobes. No lobe base, interior partition, additional triangle, vertex or fill is added. Each colored pair singles out a genuine exposed tip feature and the original star silhouette stays completely readable.'
    elif qid=='Plane335' and vid=='tangent_endpoint_pairs':
        pts=read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane335.json')['points']
        for key,color in [('0U',RED),('1U',RED),('0D',BLUE),('1D',BLUE)]:
            actions.append({'type':'add_point','id':'Port'+key,'xy':pts[key],'color':color,'filled':True,'size_pt2':50,'edge_linewidth_pt':1});roles.append('The '+key+' existing vertex is one endpoint of the red upper or blue lower common tangent pair. The two color pairs emphasize two valid nonintersecting joins, without drawing or claiming an invalid join.')
        expected='2';mechanism='Pair same-height upper and lower tangent endpoints in red/blue, inviting counting the two common exterior tangents and overlooking the two other valid joins to the unmarked near-right apex.'
        proof='Of nine vertex pairs, all three from 0L cross the left interior. The two far cross pairs 0U-1D and 0D-1U cross the right interior. The four surviving joins are 0U-1U,0D-1D,0U-1L,0D-1L. Thus exactly4 remain. Four point markers lie on existing vertices, add no line, and do not change either triangle or the single-join task.'
        clarity='Four small legal colored dots at existing upper and lower vertices; all original solid contours and both unmarked apex vertices stay visible. No invalid candidate connector is inserted into the source diagram.'
    elif qid=='Plane335':
        pts=read(ROOT/'PlaneGeometry/dataset_generator/scenes/Plane335.json')['points']
        for key,color in [('0U',RED),('0L',BLUE),('0D',GREEN)]:line([pts[key],pts['1L']],color,'One of the three left-vertex to near-right-vertex candidate correspondences: '+key+' to 1L. Its actual path remains visible; the middle blue connector crosses the left triangle and is invalid under the original condition.')
        expected='3';mechanism='Three colored candidate connectors exhaust the near-right apex correspondence, inviting counting the displayed three paths while overlooking the two far-right tangent paths and the invalid middle crossing. Targets visibility/vertex correspondence rather than an answer option.'
        proof='Of the nine vertex pairs, 0L to any right vertex enters the interior of the left triangle. The four 0U/0D to 1L or same-height far vertex (0U-1U,0D-1D) remain outside both interiors. The remaining cross pairs 0U-1D and 0D-1U enter the right triangle. Thus exactly four are legal. The three dashed guides are candidate joins, and their crossing behavior is plainly visible; no join is labelled valid.'
        clarity='Dashed colored candidate lines are distinct from the two original solid black triangle contours. They do not add a vertex or conceal any contour. One invalid candidate is visibly inside the left triangle; no extra stated condition is introduced.'
    elif qid=='Plane200':
        for oid in ['tri0','tri2','tri5']:whole(oid,RED,'One original outer-corner coin of the triangular arrangement, proposed as a moved-coin triad.')
        for oid in ['hex0','hex2','hex4']:whole(oid,RED,'One alternating target coin slot in the hexagon, paired with the source outer-corner triad; the three uncolored slots remain visible.')
        expected='3';mechanism='Pair the three source extremal coins with three alternating target slots. Targets the plausible but nonminimal move-three-corners recipe; all six identical coins in both arrangements retain their centers and radii.'
        proof='Translate the target hexagon center to (2,0): four centers then coincide with source (0,0),(4,0),(1,sqrt(3)),(3,sqrt(3)); move source (2,0) to (1,-sqrt(3)) and source (2,2sqrt(3)) to (3,-sqrt(3)). One move is impossible: leaving five source centers retains at least two vertices of the side-4 corner triangle, hence a diameter pair of the target hexagon of circumradius2; its midpoint fixes the center, and direct substitution leaves at most four coincident centers. The saved exhaustive pair-isometry audit checks every oriented source/target center pair and finds max overlap4. Therefore minimum moves2.'
        clarity='Only six original circle contours are red. Coins remain identical mathematical circles; color identifies a proposed source-to-slot correspondence, with no text asserting fixed identities. All original centers, tangencies and arrow are unchanged.'
    elif qid=='Plane244':
        for prefix in ['image1','image3']:
            for i in [0,1,2]:edge(f'{prefix}_{i}',2,RED,'Top bar of the actual U block, or the congruent left U subset of the eight-rectangle second pattern. Three contiguous original top edges form a single geometric feature.')
            for i in ([3,4] if prefix=='image1' else [5,6]):edge(f'{prefix}_{i}',0,BLUE,'Terminal bottom edge of one of the two actual U prongs, paired between source and the left local U in the eight-rectangle pattern.')
        expected='5';mechanism='Bind the source U top bar and its two feet to an exact local U in the second pattern. The local fit invites counting all five patterns as buildable, overlooking that this pattern has only eight small rectangles rather than ten. Open edge highlights avoid a new closed partition contour.'
        proof='The source block comprises five 2-by-1 rectangles. Patterns below contain10,8,10,10,10 rectangles. The eight-rectangle pattern cannot use exactly two blocks of area5 rectangles each. Exhaustive rigid lattice placement enumeration in tiling_math_audit.json supplies disjoint two-copy covers for each of the other four patterns, including 90-degree rotated copies in the final vertical pattern. Hence exactly four patterns can be made.'
        clarity='Ten partial color operations select existing top and foot boundary edges. No new cut is drawn and no complete colored source partition is enclosed. The three leftover rectangles in the eight-cell pattern, all other patterns and every original seam stay visible.'
    elif qid=='Plane289':
        data=read(HERE/qid/'completion_math_audit.json');tri=data['chosen_nonminimal_triangle']
        for i in range(3):line([tri[i],tri[(i+1)%3]],RED,'One side of a side-five hypothetical enclosing triangle. The three dashed red sides specify one feasible but nonminimal completion, without adding any unit-triangle seam or fill.')
        expected='18';mechanism='Present one feasible side-five completion as a dashed guide, inviting subtraction 25-7=18 instead of minimizing the enclosing triangle. This targets the local edge-extension choice and minimum-versus-feasible distinction.'
        proof='The seven fixed unit triangles are contained in an equilateral lattice triangle of side4, total16 elementary triangles, so adding9 suffices. Exhaustive enumeration of both orientations and every bounding lattice translation finds no containing triangle of side1,2,3. Any equilateral triangle tiled by these same unit triangles must have sides parallel to a unit edge and integer side length; thus the enumeration is exhaustive. The displayed side5 guide has25 cells, requiring18, and is deliberately nonminimal; it does not impose a new condition.'
        clarity='Only three dashed red auxiliary sides are added, distinct from all seven original solid black unit triangles. No new unit cell or semantic fill is added. The prompt asks a future completion, so a hypothetical enclosing guide does not assert a past cut. An independent reviewer should still assess the visible guide versus the counting target.'
    else:raise ValueError(qid)
    out=HERE/qid/vid;out.mkdir(parents=True,exist_ok=False)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':mechanism,'intent':'','params':{'actions':actions}}
    renderer=PluginRenderer(cfg,ad,{qid:meta});normalized,png,pix=renderer.render(plugin);n2,png2,pix2=renderer.render(normalized,frozen=True)
    assert png==png2 and pix==pix2 and normalized==n2 and before==inputs(ad,qid)
    write(out/'context.json',meta);write(out/'plugin.json',normalized);(out/'candidate.png').write_bytes(png)
    used={a['target'] for a in actions if 'target' in a}
    write(out/'path_fingerprints.json',{k:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'exact_segment_controls':[s['control'].tolist() for s in p['segments']]} for p in paths[k]] for k in sorted(used)})
    write(out/'design.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'expected_wrong_answer':expected,'formal_correct_answer':ad.records[qid]['answer'],'mechanism':mechanism,'primary_unique_math_proof':proof,'primary_human_clarity_assessment':clarity,'marker_roles':[{'action_index':i,'action':a,'role':r} for i,(a,r) in enumerate(zip(normalized['params']['actions'],roles))],'candidate_sha256':file_hash(out/'candidate.png'),'input_fingerprints_path':str(HERE/qid/'input_fingerprints.json'),'limitations':['Primary analysis only, no self approval or independent review.','No control call yet, no human study or statistical causal/per-marker claim.']})
    write(out/'render_check.json',{'baseline_pixel_match':True,'schema_and_defaults_normalized':True,'twice_byte_identical':True,'candidate_sha256':file_hash(out/'candidate.png'),'candidate_pixel_sha256':pix,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'frozen_sources_unchanged':True,'eligibility':check})
    print(qid,vid,file_hash(out/'candidate.png'),flush=True)
if __name__=='__main__':build(*sys.argv[1:3])
