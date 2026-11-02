from tools24 import *
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A'
def render(qid):
    cfg,ad=adapter();elig=eligibility(qid);assert elig['eligible'];before=inputs(ad,qid);m=ad.inspect_question(qid)
    sc=ad.scene(qid)
    try:
        sc.fig.canvas.draw();paths={o['id']:object_paths(sc,o['id']) for o in m['objects']}
    finally:sc.close()
    actions=[];roles=[]
    def part(oid,a,b,col,role,path_index=0):
        p=paths[oid][path_index];n=len(p['segments'])
        if a<0:a+=n
        if b is None:b=n
        assert 0<=a<b<=n
        actions.append({'type':'set_object_style','target':oid,'color':col,'linewidth_pt':2,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':a/n,'end':b/n,'wrap':False}})
        roles.append({'action_index':len(actions)-1,'target':oid,'path_index':path_index,'segment_start':a,'segment_end':b,'role':role,'exact_controls':[s['control'].tolist() for s in p['segments'][a:b]]})
    def whole(oid,col,role):
        actions.append({'type':'set_object_style','target':oid,'color':col,'linewidth_pt':2});roles.append({'action_index':len(actions)-1,'target':oid,'role':role})
    if qid=='Plane226':
        vid='r24_adjacent_hearts_pose_decoupling';expected='E'
        whole('board33heartbody',RED,'Upper heart of the genuinely adjacent vertical pair, both hearts pointing down. First source feature.')
        whole('board32heartbody',BLUE,'Lower heart of that adjacent pair. Its different color encodes the pair order, not a new symbol identity.')
        whole('option4_0heartbody',RED,'Left downward heart in E proposed as rotated position of the upper source heart, while its actual symbol heading was not rotated.')
        whole('option4_1heartbody',BLUE,'Right downward heart in E proposed as rotated position of the lower source heart; both retain heading incorrectly.')
        diff='Old design paired two nonadjacent stars with C and tested E/C against preset C. New design selects an actually adjacent vertical heart pair and maps its ordered positions to horizontal E, targeting decoupled position rotation versus symbol orientation. This removes the old false-adjacency premise; neither source star is marked. E appeared historically but is selected from this different rigid-motion hypothesis, not by relabeling an old image.'
        proof='A rigid motion rotating an adjacent vertical pair into a horizontal domino must rotate the entire symbols by +90 or -90 degrees. The two downward source hearts then point sideways; E has two downward hearts. The only pair of identical downward hearts in the source is column4 rows1-2. Other heart adjacency has different relative headings; the row4 pair has a club between. B matches row1 columns2-3 upright star and upright club without rotation. C has no adjacent stars. A would require an upright star with an upright spade immediately to its right after whole-domino rotation; neither star neighborhood supports that orientation (lower star is rotated20degrees). D heart+vertical diamond cannot preserve their headings after rotating the bottom-left horizontal neighboring pair. Thus B alone. All24 unordered source adjacencies can be checked with the frozen symbol poses; a new enumeration audit accompanies this design.'
    elif qid=='Plane242':
        vid='r24_disconnected_gray_arc_assembly';expected='D'
        part('image1_semicircle',0,2,RED,'First 90degree outer arc of the continuous gray semicircle. It is an open boundary portion, not a new interior cut.')
        part('image1_semicircle',2,4,BLUE,'Second adjacent 90degree outer arc of the same uncut source piece.')
        part('option3_0',0,2,RED,'D upper-right gray quarter proposed as one source half; congruent local arc but disconnected gray component.')
        part('option3_2',0,2,BLUE,'D lower-left gray quarter proposed as the other source half. It has the right total area but no connecting gray paper.')
        part('image1_quarter',0,2,GREEN,'Actual white90degree quarter arc, establishing the second physical source piece.')
        part('option3_1',0,2,GREEN,'D white90degree arc is a true congruent match, so the targeted defect is the disconnected gray piece, not the white area.')
        diff='Old B design matched one whole congruent gray semicircle plus ordered white45degree rays; it tested B/E against B. New D design instead matches a true white90degree quarter and the two equal90degree outer arc portions of the single gray source to two disconnected D gray quarters. The misconception is area-preserving fragmentation of an uncut piece, not angle-size tolerance; B and all old ray correspondences are removed.'
        proof='Both paper pieces have radius1. Gray is one connected180degree semicircle and white is one connected90degree quarter. A gray sectors total90degrees in two components; B gray180 but white45; C gray135; D gray180 in two disjoint90degree components; E gray one125..305 semicircle and white350..440 quarter, disjoint. Any rigid placement of a radius1 sector inside the equal-radius disk has its circular arc centered at the disk center; it cannot turn one semicircle into disconnected visible regions without overlap (forbidden) or cutting (not allowed). E alone meets both full geometry and connectivity. D preserves total gray/white areas but not the single gray shape. No new gray seam or cut is drawn in the source.'
    elif qid=='Plane215':
        vid='r24_diagonal_mirror_axis_binding';expected='E'
        whole('o3',RED,'Source whole horizontal semicircle diameter, first orientation-defining axis.')
        part('o1',-1,None,BLUE,'Existing source downward radial divider between black and white quarters, second orientation-defining feature.')
        whole('o221',RED,'E vertical semicircle diameter, paired by the false diagonal-mirror map instead of the true halfturn.')
        part('o219',0,1,BLUE,'E rightward radial divider, the exact false image of the source downward radius under reflection in y=-x.')
        diff='Old D design colored the source and D black/white quarter arcs to suppress the first horizontal flip, giving D/A. New E design removes every old arc mark and pairs straight diameter and black-white divider directions under (x,y)->(-y,-x), a single diagonal reflection. This is a different transformation error; E shares the correct black quarter location but fails the complete semicircle orientation, explicitly addressing the old audit warning that black-quarter matching alone is insufficient.'
        proof='Relative to card center the first leftward flip is H=diag(-1,1), then upward V=diag(1,-1). VH=-I; printed side returns. Source semicircle y<=0 therefore becomes y>=0 and source black lower-left quarter becomes black upper-right. Only A has BOTH. B left semicircle, C lower, E right all fail the enclosing semicircle; D upper semicircle has black upper-left and fails fill. The false map R=[0,-1;-1,0] sends the diameter horizontal to vertical and downward black-white divider rightward, matching E, but is not VH. No arrow or printed fill changes.'
    elif qid=='Plane225':
        vid='r24_animal_silhouette_visibility_repair';expected='A'
        for oid,col,role in [
          ('fold0_dog',RED,'Actual original dog body contour, including its asymmetric head/body orientation; first source animal.'),
          ('optionA_dog',RED,'A dog body retains precisely the original heading and sector position instead of the third reflected heading.'),
          ('fold0_dolphin',BLUE,'Actual original dolphin body contour provides an independent asymmetric nose/tail orientation in another sector.'),
          ('optionA_dolphin',BLUE,'A dolphin body preserves original nose/tail orientation and location, paired with source instead of applying all three reflections.')]:
            part(oid,0,None,col,role,3 if oid.endswith('dog') else 2);actions[-1]['linewidth_pt']=1
        diff='Old C design matched radial butterfly-sector borders in the first reflection; C/D missedC. New A design instead pairs original dog/dolphin asymmetric body silhouettes with retained original headings in A, discarding the whole odd reflection chain. Earlier UNTESTED r24_original_animal_heading_retention wrongly assumed p0 was each body: actual nativePNG only marked tiny dogears/dolphinfins, so it failed information coverage and received ZERO calls. This visibility repair selects actual14segment body paths p3dog/p2dolphin, removing all four small accessory marks. Color/width/preset are unchanged; the marked geometric feature and human heading information are substantively corrected before any calls.'
        proof='Reflecting a vector across an edge of direction u has matrix2uu^T-I. The three bold edges have unoriented directions120,60,120degrees in traversal order. Original artwork matrixF120 is sent by F120 to the shown canonical first imageI; the next two give F120F60=R120. Read complete animal transforms and distinct asymmetric dog/dolphin headings: A=F120 (original, det-1), B=R120 (correct, det+1), C=I, D=R240, E=R300. Only B equals the three-reflection result. Both animal feature positions/headings and all bold axes remain unchanged; annotation colors do not make physical matching givens.'
    elif qid=='Plane248':
        vid='r24_reflected_ordered_corner_binding';expected='E'
        part('source0',2,3,RED,'First source arrow downward side entering its convex tail corner; ordered edge1.')
        part('source0',3,4,BLUE,'First source arrow leftward bottom edge leaving that corner; ordered edge2. Together the source boundary turn is clockwise90degrees.')
        part('source1',2,3,RED,'Second identical source arrow same entering edge; confirms the two available pieces have the same ordered corner geometry.')
        part('source1',3,4,BLUE,'Second source same leaving edge; the relative turn cannot reverse under rotation.')
        part('option4',3,4,RED,'E rightward edge entering lower-right convex corner, false feature partner to first source downward side.')
        part('option4',4,5,BLUE,'E upward edge leaving that corner; the color-ordered turn reverses, suggesting a reflected piece if this false assignment were forced.')
        part('option4',8,9,RED,'E leftward edge entering upper-left corner, proposed second source partner.')
        part('option4',9,10,BLUE,'E downward edge leaving that corner, same reversed color-ordered turn as the first E pair.')
        diff='Old E design colored both entire source contours and the entire E contour uniformly red; it had weak information targeting and finals D/E against presetE. New design removes every whole contour highlight and instead binds two ordered edge pairs at the actual convex source tail corners to two E boundary corners whose red-to-blue turns have opposite sign. This is a specific false reflected-part assignment, with source handedness evidence and no added seam. Actual E has different valid rotated decompositions. Reusing presetE does not reuse the old image or salience mechanism.'
        proof='Each source arrow is the union of a unit-area isosceles right triangular head and a unit-square stem, totalarea2. Fresh polygon computation supplies explicit two-rotation/translation tilings of A,B,C,E. For D the long exposed diagonal has length2sqrt2; each piece can contribute at most one edge on this support line. At45degree source rotations two unit-axis edges total2 cannot cover2sqrt2, so both contributing edges must be the head edges of lengthsqrt2 under90degree rotations. They meet at the diagonal midpoint, forcing a finite set of placements; none can be a contained disjoint pair. Thus D alone is impossible. The marked source corner and marked E corners have opposite boundary traversal signs, but the source-to-E matching is an optional incorrect correspondence: it does not prevent E actual tiling. No interior partition or seam is drawn.'
    else:raise ValueError(qid)
    out=HERE/qid/vid;out.mkdir(exist_ok=False)
    inv=read(HERE/qid/'prior_history_inventory.json')
    for p in inv['prior_design_paths']:
        assert read(ROOT/p).get('variant_id')!=vid
    write(out/'design_difference_audit.json',{'stage':'material_refinement','question_id':qid,'variant_id':vid,'created_before_calls':now(),'all_prior_designs_raw_replies_presets_primary_reviews_read':True,'old_images_native_viewed':True,'independent_objections_found':inv['independent_review_paths'],'substantive_difference':diff,'not_a_palette_width_rename_crop_or_posthoc_preset_change':True,'proposed_actions':actions,'expected_wrong_answer':expected,'prior_inventory':str(HERE/qid/'prior_history_inventory.json')})
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':diff[:1000],'intent':'Frozen wrong hypothesis '+expected,'params':{'actions':actions}}
    pr=PluginRenderer(cfg,ad,{qid:m});norm,png,pix=pr.render(plugin);norm2,png2,pix2=pr.render(norm,frozen=True)
    assert (norm,png,pix)==(norm2,png2,pix2) and before==inputs(ad,qid)
    write(out/'context.json',m);write(out/'eligibility_before_design.json',elig);write(out/'plugin.json',norm);(out/'candidate.png').write_bytes(png)
    write(out/'path_fingerprints.json',{oid:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'exact_controls':[s['control'].tolist() for s in p['segments']]} for p in paths[oid]] for oid in sorted({a['target'] for a in actions})})
    write(out/'design.json',{'question_id':qid,'variant_id':vid,'created_at':now(),'stage':'material_refinement','expected_wrong_answer':expected,'correct_answer':ad.records[qid]['answer'],'mechanism':diff,'primary_math_proof':proof,'marker_roles':roles,'human_semantics':'Only existing contour styles; all original geometry, text and fill unchanged. Colors are correspondence annotations and not extra physical ink constraints. No new cut, region, condition or puzzle part. Actual native PNG primary review required before calls.','status':'PRIMARY_ONLY_REQUIRES_PARENT_NEW_INDEPENDENT_REVIEW'})
    write(out/'render_check.json',{'baseline_actual_noop_pixel_match':True,'formal_original_pixel_sha256':m['original_pixel_sha256'],'schema_defaults_normalized':True,'twice_byte_identical_render':True,'input_fingerprints':before,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pix,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'isolation':ISOLATION,'own_root_write_guard':True})
    print(qid,vid,expected,len(actions),file_hash(out/'candidate.png'),flush=True)
if __name__=='__main__':
    for q in sys.argv[1:]:render(q)
