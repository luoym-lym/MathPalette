from tools_local import *
RED='#DC2626';BLUE='#2563EB'
def render(qid,vid):
    check=eligibility(qid);assert check['eligible'],check
    cfg,ad=adapter();before=inputs(ad,qid);meta=ad.inspect_question(qid);sc=ad.scene(qid)
    try:
        sc.fig.canvas.draw();paths={o['id']:object_paths(sc,o['id']) for o in meta['objects']}
    finally:sc.close()
    actions=[];roles=[]
    def part(oid,start,end,color,role):
        p=paths[oid][0];interval={'path_id':p['id'],'path_sha256':p['sha256'],'start':start/len(p['segments']),'end':end/len(p['segments']),'wrap':False}
        actions.append({'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2,'interval':interval})
        roles.append({'action_index':len(actions)-1,'target':oid,'segment_start':start,'segment_end':end,'role':role,'exact_controls':[s['control'].tolist() for s in p['segments'][start:end]]})
    if (qid,vid)==('Plane215','single_flip_quarter_correspondence'):
        part('o2',0,2,RED,'The input lower-left quarter-arc adjacent to the original black region; first concrete feature to track.')
        part('o2',2,4,BLUE,'The input lower-right quarter-arc adjacent to the white region; complementary feature, preserving the visible black/white division.')
        part('o216',2,4,RED,'D upper-left quarter-arc falsely paired with the input black-side quarter: a single upward flip preserves left/right, but the prior left flip must reverse it.')
        part('o216',0,2,BLUE,'D upper-right white-side quarter paired with the source white-side quarter; completes the false single-flip correspondence rather than an isolated option highlight.')
        expected='D'
        mechanism='Two differently colored original quarter-arcs pair the actual black-side and white-side printed features to D, following only the upward flip and neglecting the preceding leftward flip. The candidate retains all fills, arrow paths, blank-back cards and option orientations.'
        proof='Use local coordinates about the card centre with x right and y up. A left flip reflects (x,y) to (-x,y), exposing the plain back; the subsequent upward flip reflects the card coordinates to (-x,-y) and returns the printed side. The original printed semicircle occupies y<0 with black quarter x<0,y<0. The final printed semicircle therefore occupies y>0 with its black quarter x>0,y>0. Only A has upper semicircle and black right quarter. D has black left quarter and is the result of just the upward reflection. B and E have vertical semicircles, and C remains below. Original black fill and its white counterpart remain visibly unchanged; colored original outer arcs impose no new physical ink-continuity requirement.'
        human='Four partial style changes only, on existing outer arcs. They do not create cuts or regions. Black/white areas, the central radius, diameter, both original flip arrows, question mark and all option letters remain clear. The false correspondence can be rejected by the first horizontal reflection.'
    elif (qid,vid)==('Plane259','cap_stem_quarterturn_binding'):
        part('o10',0,1,RED,'Long horizontal top cap of the input 5; first orientation-defining feature.')
        part('o10',37,38,BLUE,'Long left upright stem of the input 5; second nonparallel orientation-defining feature.')
        part('o14',0,1,RED,'D right vertical cap edge: the source cap mapped by a clockwise quarter-turn instead of the required half-turn.')
        part('o14',37,38,BLUE,'D upper horizontal stem edge: companion of the same quarter-turn correspondence, not an independent answer cue.')
        expected='D'
        mechanism='Pair the actual cap and upright stem of 5 with their clockwise-quarter-turned copies in D using red and blue partial edges. Targets replacing two perpendicular reflections with a single 90-degree turn. The complete worked 4 reflections, both mirror lines and every original digit silhouette stay visible.'
        proof='The worked example shows reflection first in the vertical line and then in the horizontal line. Relative to the crossing, (x,y)->(-x,y)->(-x,-y), so the net linear transformation is a half-turn, preserving handedness. The same sequence sends the input upper-left 5 to an upside-down 5 in the lower-right field: its original horizontal cap becomes the lower horizontal cap pointing left, and its original left upright becomes the right downward stem. The exact source polygon is reflected in both coordinates and rescaled to the option size; C has this pair and the corresponding curved lobe. A is left-right reflected, B is only up-down reflected, and D/E place the cap vertically, so all fail. Only C is correct. Colored partial outlines leave all numeral black fills and white counters unchanged.'
        human='Four legal partial outline recolorings of existing long digit edges. No character, mirror, answer text or fill is moved/covered. Color does not assert a new mirror operation; the worked 4 and crossing lines still determine the unique two-reflection answer.'
    elif (qid,vid)==('Plane187','ordered_stripe_orientation_binding'):
        part('o18',0,1,RED,'A lower interior stripe of the actual step-one rotated pentagon, serving as the lower feature in an ordered pair.')
        part('o20',0,1,BLUE,'An upper interior stripe of the same actual pentagon; the pair carries the visible rising direction and order.')
        part('o81',0,1,RED,'C lower rising stripe proposed as the first feature copy when the outline next fills the hole.')
        part('o83',0,1,BLUE,'C upper rising stripe proposed as the companion feature copy; favors retaining rising line orientation rather than the required first closing rotation.')
        expected='C'
        mechanism='Link an ordered lower/upper stripe pair in the step-one pentagon to the rising stripe pair in C. Targets extrapolating the shown 21-degree rising orientation to the nearest rising aligned-outline diagram, rather than finding the first allowed pentagon-symmetry multiple. The slopes are qualitatively rising but are not asserted equal.'
        proof='A regular pentagon fills its fixed hole exactly at rotations divisible by 72 degrees. After n whole steps its rotation is 21n degrees, so 21n=72k. Dividing by 3 gives 7n=24k; hence the least positive n is 24 and the total rotation is 504 degrees, equivalent to 144 degrees. The initially horizontal paper lines then have undirected orientation 144 degrees (descending rightwards), which is B. The other option orientations are A72, C36, D108 and E0 degrees, all distinguishable from B144 modulo180. The given step-one lines have21degrees. Four colored existing stripes leave the polygon hole, all horizontal background lines and every option fully intact; no marked line is a new cut.'
        human='Only four existing stripe segments are recolored at 2pt. Lower/upper ordering gives both colors a role. No contour is recolored and no new partition or ink-continuity condition is given. Options remain distinguished by their unchanged actual stripe angles.'
    else:raise ValueError((qid,vid))
    out=HERE/qid/vid;out.mkdir(parents=True,exist_ok=False)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared wrong answer '+expected,'params':{'actions':actions}}
    pr=PluginRenderer(cfg,ad,{qid:meta});norm,png,pixels=pr.render(plugin);norm2,png2,pixels2=pr.render(norm,frozen=True)
    assert norm==norm2 and png==png2 and pixels==pixels2 and before==inputs(ad,qid)
    used={a['target'] for a in actions}
    write(out/'eligibility_before_design.json',check);write(out/'context.json',meta)
    write(out/'path_fingerprints.json',{o:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segment_count':len(p['segments']),'exact_controls':[s['control'].tolist() for s in p['segments']]} for p in paths[o]] for o in sorted(used)})
    write(out/'plugin.json',norm);(out/'candidate.png').write_bytes(png)
    write(out/'design.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'expected_wrong_answer':expected,'correct_answer':ad.records[qid]['answer'],'mechanism':mechanism,'mathematical_solution':proof,'human_semantics':human,'marker_roles':roles,'status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'})
    write(out/'render_check.json',{'question_id':qid,'baseline_pixel_match':True,'baseline_pixel_sha256':meta['original_pixel_sha256'],'schema_default_normalized':True,'two_byte_identical_redraws':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'geometry_fill_labels_unchanged':True})
    print(json.dumps({'question_id':qid,'variant':vid,'actions':len(actions),'png_sha256':file_hash(out/'candidate.png')}),flush=True)
if __name__=='__main__':render(sys.argv[1],sys.argv[2])
