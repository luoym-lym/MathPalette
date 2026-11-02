from tools import *
import itertools
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A'
qid=sys.argv[1]
assert qid in ('Plane461','Plane474','Plane475')
check=eligibility(qid);assert check['eligible'],check
cfg,ad=adapter();before=inputs(ad,qid);meta=ad.inspect_question(qid)
scene=ad.scene(qid)
try:
    scene.fig.canvas.draw()
    paths={o['id']:object_paths(scene,o['id']) for o in meta['objects'] if o['styleable']}
finally:scene.close()
actions=[];roles=[]
def style(oid,color,role,edge=None):
    a={'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2}
    if edge is not None:
        p=paths[oid][0];n=len(p['segments'])
        a['interval']={'path_id':p['id'],'path_sha256':p['sha256'],'start':edge/n,'end':(edge+1)/n,'wrap':False}
    actions.append(a);roles.append({'action_index':len(actions)-1,'target':oid,'edge_index':edge,'role':role})
def line(label,a,b,color,role):
    snaps=meta['snap_points']
    pa=next(p for p in snaps if p['xy']==list(a));pb=next(p for p in snaps if p['xy']==list(b))
    actions.append({'type':'add_line','id':label,'endpoints':[pa['xy'],pb['xy']],'color':color,'linestyle':'solid'})
    roles.append({'action_index':len(actions)-1,'role':role,'endpoint_snap_ids':[pa['id'],pb['id']]})
if qid=='Plane461':
    vid='punch_to_outer_corner_correspondence';expected='C'
    style('o13',RED,'Actual punch circle at X in the twice-folded sheet; source of the four reflected hole copies.')
    for oid,pos in [('o33','upper left'),('o34','upper right'),('o35','lower left'),('o36','lower right')]:
        style(oid,RED,'C '+pos+' existing hole outline, paired with the punched hole as an outer-corner unfolding copy. The false correspondence treats the left edge of the folded sheet as an original outer edge instead of the vertical fold.')
    mechanism='Five original hole outlines form a concrete one-to-four punch-to-hole correspondence. It favors C by mistaking the left vertical fold boundary for an outer edge; it does not color a choice box, letter, or unrelated outline.'
    proof='Normalize the original rectangle to [0,4] x [0,2]. Bottom-to-top maps y to 2-y on the moving half, leaving the stack in y in [1,2]. Left-to-right maps x to 4-x on the moving half, leaving x in [2,4]. The final punch lies near (2.25,1.75), as its frozen local coordinates (12.25,5.45) are 0.25 from the folded left side and 0.25 from its top. Reverse the folds: (2.25,1.75), (1.75,1.75), (2.25,0.25), (1.75,0.25). In B these are translated by +6 along x, giving its four exact centers (7.75/8.25,0.25/1.75). C instead has x=0.25/3.75 relative to its box, wrongly near outside edges; D is near both axes; E is near outside x and central y; A is not symmetric about both axes. Only B is the complete correct reflected orbit.'
    semantics='Only the pre-existing circle outlines are recolored. The punch X remains visible; every circle center, radius, white interior, original fold arrow, dashed fold line and option label is unchanged. These are proposed visual correspondences, not new holes, cuts, or a condition that physical red ink must survive a fold. No whole option is boxed. Native-size small circles require an explicit visual check.'
    math={'unique_correct':'B','normalized_expected_hole_centers':[[1.75,.25],[2.25,.25],[1.75,1.75],[2.25,1.75]]}
elif qid=='Plane474':
    vid='four_bar_to_three_wide_edge_binding';expected='D'
    # Each unit cell is a separate frozen path. Four/five contiguous side
    # intervals make four logical open edge traces without any new cuts.
    for k in range(4):style('bar4_'+str(k),RED,'The left side of unit '+str(k+1)+' in the actual four-unit source bar; together the four intervals expose its complete long side.',3)
    for k in range(5):style('bar5_'+str(k),BLUE,'The left side of unit '+str(k+1)+' in the actual five-unit source bar, the anchor for a true vertical five-unit fit in D.',3)
    for k in range(5):style('board3_0'+str(k),BLUE,'D left outside edge unit '+str(k+1)+', paired with the source five-unit bar as a feasible first placement.',3)
    for k in range(3):style('board3_'+str(k)+'4',RED,'D top outside edge unit '+str(k+1)+', falsely paired with the longer four-unit bar as if the next bar had to be horizontal. The visible length mismatch encourages a greedy false impossibility judgement.',2)
    mechanism='Bind the actual five-unit source bar to D\'s five-high left side, then bind the four-unit source bar to D\'s three-wide top side. Targets rejecting D after a forced horizontal second placement instead of allowing the remaining bars to rotate. All four traces are open existing outer edges, with no candidate partition or added pieces.'
    proof='The source pieces are straight 1-by-k bars for k=1,2,3,4,5. B has no horizontal or vertical run of five cells, so it cannot contain the five-bar. A, C, D and E each have an exact bar tiling; the attached exhaustive finite cell search saves one complete placement of each size in each feasible board and proves B infeasible. For D, place the five-bar vertically in its left column; put lengths 3 and 2 in the second column and lengths 4 and 1 in the third column. Thus the red horizontal placement is an optional failed placement, not a physical requirement. Only B is impossible. The options lack letters in the frozen PNG; A through E follow the original left-to-right five-choice order, which is preserved and disclosed.'
    semantics='Seventeen partial path styles implement four contiguous open edge traces. No outline closes a proposed piece, no interior gridline is added, and every one-unit division stays visible. Source lengths 4 and 5 and D\'s width3/height5 remain countable. Colors are proposed edge correspondences, not extra mandatory piece placements or a new dissection. The frozen source has no printed option letters, a pre-existing display limitation.'
    s=json.loads((HERE/qid/'source_scene_snapshot.json').read_text(encoding='utf-8'))
    boards=[]
    for j in range(5):
        cells=[]
        for o in s['objects']:
            if o['id'].startswith('board'+str(j)+'_'):
                xy=[s['points'][p] for p in o['points']];cells.append((int(min(p[0] for p in xy))-7*j,int(min(p[1] for p in xy))))
        boards.append(set(cells))
    def solve(cells,sizes):
        if not sizes:return [] if not cells else None
        anchor=min(cells)
        for k in sizes:
            for dx,dy in [(1,0),(0,1)]:
                for i in range(k):
                    start=(anchor[0]-i*dx,anchor[1]-i*dy);part={(start[0]+t*dx,start[1]+t*dy) for t in range(k)}
                    if part<=cells:
                        rest=solve(cells-part,tuple(n for n in sizes if n!=k))
                        if rest is not None:return [{'length':k,'cells':sorted(part)}]+rest
        return None
    solutions={chr(65+j):{'cells':sorted(c),'tiling':solve(c,(1,2,3,4,5))} for j,c in enumerate(boards)}
    assert [k for k,v in solutions.items() if v['tiling'] is None]==['B']
    math={'unique_correct':'B','exact_cover_solutions':solutions}
else:
    vid='equal_base_height_triangle_class_merge';expected='7'
    line('common_base',(0,0),(3,0),RED,'Common three-unit base of two actual dot triples; their identical base is the geometric basis of the proposed match.')
    line('endpoint_left',(0,0),(0,1),BLUE,'First triangle\'s one-unit vertical left leg; compare with the blue oblique leg of the second triangle, not a new equality condition.')
    line('endpoint_right',(0,1),(3,0),GREEN,'First triangle\'s long sloping side, paired visually with the second green side.')
    line('interior_left',(0,0),(1,1),BLUE,'Second triangle\'s sloping left side. Same blue links two equal-height apex configurations that have different metric side lengths.')
    line('interior_right',(1,1),(3,0),GREEN,'Second triangle\'s right side completes the proposed side-role correspondence. The shared base and common apex row encourage merging equal-area classes.')
    mechanism='Outline two actual dot-triple triangles with a shared red base, blue left sides and green right sides. Both have base3 and height1, but one has its apex over an endpoint and one over an interior point. Targets merging these two different congruence classes by equal base/height/area, producing 7 instead of8.'
    proof='Squared side-length triples completely classify triangles by SSS, independent of translations, turns and reflections. The 8-point two-row array has exactly the sorted triples (1,1,2), (1,2,5), (1,5,10), (1,4,5), (2,2,4), (2,4,10), (1,9,10), (2,5,9). Enumerating all 56 triples and excluding the eight collinear triples gives48 triangles in these8 classes. The marked endpoint-apex triangle has (1,9,10), whereas the interior-apex triangle has (2,5,9); equal area3/2 does not imply congruence. All8 original dots remain visible and their coordinates are unchanged. No crossing of new lines is marked as a dot; the task explicitly chooses3 of the8 points, so crossings do not add vertices.'
    semantics='Five thin solid auxiliary lines join only exact existing dot centers. They outline two examples of triangles the question already permits. There are no new point markers, text, filled regions, measurements or relation symbols. The common base passes through two original bottom-row dots; those dots must remain individually visible at native size. One unmarked crossing of colored sides is not one of the8 specified points. The target remains all triples of original dots, not merely the outlined triangles. Potential human confusion from that crossing will be checked and disclosed.'
    pts=[(x,y) for x in range(4) for y in range(2)];classes={};collinear=[]
    for tri in itertools.combinations(pts,3):
        a,b,c=tri
        if (b[0]-a[0])*(c[1]-a[1])==(b[1]-a[1])*(c[0]-a[0]):collinear.append(tri);continue
        ds=tuple(sorted((a[0]-b[0])**2+(a[1]-b[1])**2 for a,b in itertools.combinations(tri,2)))
        classes.setdefault(str(ds),[]).append(tri)
    assert len(classes)==8 and len(collinear)==8
    math={'unique_correct':'8','sss_classes':classes,'collinear_triples':collinear,'marked_noncongruent_classes':[[1,9,10],[2,5,9]],'merging_only_these_classes_would_give':7}
out=HERE/qid/vid;out.mkdir(parents=True,exist_ok=False)
plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared wrong answer '+expected,'params':{'actions':actions}}
pr=PluginRenderer(cfg,ad,{qid:meta});norm,png,pixels=pr.render(plugin);norm2,png2,pixels2=pr.render(norm,frozen=True)
assert norm==norm2 and png==png2 and pixels==pixels2 and before==inputs(ad,qid)
write(out/'eligibility_before_design.json',check);write(out/'context.json',meta)
write(out/'path_fingerprints.json',{o:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segment_count':len(p['segments']),'exact_controls':[s['control'].tolist() for s in p['segments']]} for p in paths[o]] for o in sorted({a['target'] for a in actions if a['type']=='set_object_style'})})
write(out/'plugin.json',norm);(out/'candidate.png').write_bytes(png)
write(out/'math_proof.json',math)
write(out/'design.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'expected_wrong_answer':expected,'correct_answer':ad.records[qid]['answer'],'mechanism':mechanism,'mathematical_solution':proof,'human_semantics':semantics,'marker_roles':roles,'status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'})
write(out/'render_check.json',{'question_id':qid,'baseline_pixel_match':True,'baseline_pixel_sha256':meta['original_pixel_sha256'],'schema_default_normalized':True,'two_byte_identical_redraws':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'geometry_fill_labels_unchanged':True})
print(json.dumps({'question_id':qid,'variant':vid,'actions':len(actions),'png_sha256':file_hash(out/'candidate.png')}),flush=True)
