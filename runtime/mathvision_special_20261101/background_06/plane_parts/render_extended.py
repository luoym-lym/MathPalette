from tools_local import *
from math_audits import grid_cells,edge
RED='#DC2626';BLUE='#2563EB'
def render(qid):
    check=eligibility(qid);assert check['eligible'],check
    cfg,ad=adapter();before=inputs(ad,qid);meta=ad.inspect_question(qid);scene=ad.scene(qid)
    try:
        scene.fig.canvas.draw();paths={o['id']:object_paths(scene,o['id']) for o in meta['objects']}
    finally:scene.close()
    actions=[];roles=[]
    def part(oid,start,end,color,role):
        p=paths[oid][0];actions.append({'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start/len(p['segments']),'end':end/len(p['segments']),'wrap':False}})
        roles.append({'action_index':len(actions)-1,'target':oid,'segment_start':start,'segment_end':end,'role':role})
    if qid=='Plane220':
        vid='separated_mirror_copy_binding';expected='A'
        part('o0',54,60,RED,'Source zigzag cut boundary, the star-like input feature.')
        part('o0',4,53,BLUE,'Source lower circular cut arc, first curved-feature range.')
        part('o0',61,110,BLUE,'Source upper circular cut arc, second curved-feature range.')
        for oid,side in [('o3','left'),('o4','right')]:
            part(oid,50,56,RED,'A '+side+' disconnected opening star-like tip, proposed mirror-copy partner for the source notch.')
            part(oid,0,49,BLUE,'A '+side+' disconnected opening circular arc, proposed copy of the source round cut feature.')
        mechanism='Map the source cut star-tip (red) and round arc (blue) to BOTH corresponding feature pairs in the two separate openings of A. Unlike the earlier C design, this binds two complete mirrored-looking copies and targets treating a cut meeting the fold as two disconnected holes. Actual fold intersection and all original connectivity remain visible.'
        proof='The source cut intersects the folded boundary at both circular-arc endpoints. Reflection across that boundary makes one connected opening: the two arc halves join in a central circle and the star-like feature is mirrored to both outer sides. D alone has one connected centrally rounded opening with matching left and right tips. A and B have two separate cutouts, E also has two separate openings, and C has only one outer tip and is not symmetric about its fold. Therefore D is unique. Outlining features in A changes no intersection with its fold or number of connected components.'
        human='Seven 2pt partial contour styles mark a source two-feature pair and its proposed two copy partners in A. No new cut or fold is added. The source still touches the folded edge, both A components are clearly separate, and D remains visible and unmarked.'
        subset_info=None
    elif qid=='Plane233':
        vid='two_U_partial_partition_binding';expected='B'
        low={(0,0),(0,1),(1,0),(2,0),(2,1)};high={(0,2),(0,3),(1,3),(2,2),(2,3)}
        subsets=[{(x+11,y+7) for x,y in low},{(x+11,y+7) for x,y in high}]
        board=grid_cells(meta,'given_');assert all(s<=board for s in subsets) and not subsets[0]&subsets[1]
        target=grid_cells(meta,'B_')
        def boundary(cells):
            counts={}
            for x,y in cells:
                for e in [edge((x,y),(x+1,y)),edge((x+1,y),(x+1,y+1)),edge((x+1,y+1),(x,y+1)),edge((x,y+1),(x,y))]:counts[e]=counts.get(e,0)+1
            return {e for e,n in counts.items() if n==1}
        selected={};groups=[('given_',subsets[0],'First actual U-shaped five-cell input-board patch.'),('given_',subsets[1],'Second actual disjoint U-shaped five-cell patch, reflected from the first.'),('B_',target,'B five-cell U, the proposed common part matched to the two source patches.')]
        group_evidence=[]
        for prefix,cells,role in groups:
            es=boundary(cells);matched=set();ids=[]
            for o in meta['objects']:
                if o['id'].startswith(prefix) and o['kind']=='segment' and edge(*o['geometry']['points']) in es:
                    selected.setdefault(o['id'],[]).append(role);matched.add(edge(*o['geometry']['points']));ids.append(o['id'])
            assert es==matched;group_evidence.append({'cells':sorted(cells),'boundary_target_ids':ids,'role':role})
        for oid,rr in selected.items():
            actions.append({'type':'set_object_style','target':oid,'color':RED,'linewidth_pt':2});roles.append({'action_index':len(actions)-1,'target':oid,'role':' '.join(rr)+' This existing unit edge is needed by the stated contour; shared boundaries are marked only once.'})
        mechanism='Bind TWO actual disjoint five-cell U patches in the input board to the congruent U pentomino B, using their full original boundary edges. Targets generalizing a valid partial two-copy arrangement to a full three-copy partition, despite the visibly non-U leftover cells. This is a genuinely new local-to-global correspondence with a different part and two placements; previous X mapping is retained unchanged.'
        proof='The 4x4-minus-one-corner board has 15 cells, so three congruent pentominoes are needed. Mathematical_enumeration.json enumerates all eight square-grid isometries, every placement, and every disjoint triple: A has2 tilings; B,C,D,E have0. The colored two U patches do occupy10 disjoint source cells, but their five-cell complement is disconnected and not another U. Other placements of B also have no complete triple. Thus A remains the unique answer. Existing grid edges receive color only; annotations do not force this partial partition or confer a condition that it extends.'
        human='Only existing source-grid and B-grid unit edges receive 2pt red contour style; repeated shared edges have one action. Every cell boundary and the missing corner remain visible. The five unselected remaining cells can be read directly, preventing any new mathematical ambiguity; no grid cell or puzzle piece is added or removed.'
        subset_info={'patches':group_evidence,'leftover_cells':sorted(board-set.union(*subsets))}
    else:raise ValueError(qid)
    out=HERE/qid/vid;out.mkdir(parents=True,exist_ok=False)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared wrong answer '+expected,'params':{'actions':actions}}
    pr=PluginRenderer(cfg,ad,{qid:meta});normalized,png,pixels=pr.render(plugin);n2,png2,pixels2=pr.render(normalized,frozen=True);assert normalized==n2 and png==png2 and pixels==pixels2 and before==inputs(ad,qid)
    used={a['target'] for a in actions};safe={o:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segment_count':len(p['segments']),'exact_controls':[s['control'].tolist() for s in p['segments']]} for p in paths[o]] for o in used}
    write(out/'eligibility_before_design.json',check);write(out/'context.json',meta);write(out/'path_fingerprints.json',safe);write(out/'plugin.json',normalized);(out/'candidate.png').write_bytes(png)
    write(out/'design.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'expected_wrong_answer':expected,'correct_answer':ad.records[qid]['answer'],'mechanism':mechanism,'mathematical_solution':proof,'human_gate':human,'marker_roles':roles,'subset_info':subset_info,'review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'})
    write(out/'render_check.json',{'question_id':qid,'baseline_pixel_match':True,'baseline_pixel_sha256':meta['original_pixel_sha256'],'schema_default_normalized':True,'two_byte_identical_redraws':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'geometry_fill_labels_unchanged':True,'helper_source_sha256':file_hash(Path(__file__))})
    print(json.dumps({'qid':qid,'variant':vid,'actions':len(actions),'rendered':True}),flush=True)
if __name__=='__main__':render(sys.argv[1])
