from tools34 import *
from math34 import scene_for
import copy

SPECS={
 'Plane257':{
  'variant_id':'r34_black_numerator_transfer', 'expected_wrong_answer':'D',
  'mechanism':'Bind the three actual black stripes of flag4 (a genuine3/5 example) to the three actual black unit squares of flag1. Transfer the black-component numerator3 while dropping the different denominator8, falsely adding flag1 and answering Three(D).',
  'old_new_difference':'Old unequal_flag_region_units styles all five unequal rectangular regions in flag5 and targets within-flag unequal-area unit counting. This new image leaves flag5 unchanged, explicitly matches two different flags via their three black components, and targets numerator transfer across unequal denominators. It is not old observed B plus cosmetic edits; immutable preset remains D for a new geometric rationale.',
  'prior_objection':'Old D preset missed B/B; no independent review for this question. New mechanism must preserve all black/white fills and must not make flag4 internal black-cell boundaries into new counted pieces.',
  'semantic_review':'The question asks for numerical filled black area, not transport/completion of a printed colored pattern. Thin existing boundary annotations do not change which regions are black or white. Every source stripe and receiver square remains distinguishable, no new region or relation glyph is introduced.'},
 'Plane336':{
  'variant_id':'r34_radial_sector_area_transfer','expected_wrong_answer':'4.5',
  'mechanism':'Group the three actual dividing chords as one six-ray radial frame around O. Their six equal-length halves have successive60-degree directions. Target extending the true equal radial-frame correspondence to false equal area of all six whole regions, assigning9/6 to each and3*(9/6)=4.5 gray.',
  'old_new_difference':'Earlier prescreen rejected merely counting three unlike rhombi and three triangles as six equal regions because it had no feature identity. The present design supplies an actual geometric correspondence: the six equal-length chord half-rays and their equal angular spacing, independently checked in primary_math_audit. It targets radial-sector-area confusion rather than simply coloring unlike region contours.',
  'prior_objection':'No earlier candidate or API pair exists. Rhombus corner extensions must remain obvious; no new spoke, equal-angle glyph, partition or fill is permitted.',
  'semantic_review':'All three styled lines are the existing dividing chords explicitly described in the question. Gray area remains defined by original fill. The true equal radial rays do not make whole sectors equal; no new condition claims that they do.'},
 'Plane340':{
  'variant_id':'r34_unit_frame_to_filled_regions','expected_wrong_answer':'2',
  'mechanism':'Use three matching open L corners of the three actual unit square frames. The unshaded left square supplies the unit-frame reference; the two frames containing gray receive the same cue. Target replacing each gray subregion by its whole containing unit-square area, returning2 instead of5/8+3/8=1.',
  'old_new_difference':'Earlier prescreen considered emphasizing the top/right gray pieces alone and found no counterpart. This variant binds the untouched full left unit square to both actual containing-square frames. Its hypothesis is the concrete frame-versus-filled-region area transfer, not isolated gray-piece salience or changed fill.',
  'prior_objection':'No old candidate/API exists (root_explore has context only). The line crossing K at x1.25, the white top triangle and the lower gray triangle must remain visible; no extra cut is allowed.',
  'semantic_review':'Existing open square-frame corners only. The text says all square sides are1, so that true frame correspondence adds no false relation. Gray area is still uniquely defined by unchanged fills and diagonal.'},
 'Solid184':{
  'variant_id':'r34_six_brick_component_normalization','expected_wrong_answer':'45',
  'mechanism':'Identify each of the six actual brick copies across the three paired assemblies by an open two-edge corner motif. Target treating the three displayed assembly areas as six complete brick surfaces and using(72+96+102)/6=45, forgetting the six contacting patches. Actual exposed-area sum is5S, not6S.',
  'old_new_difference':'Earlier prescreen found selected seam highlighting alone uninformative. This new design gives a six-component correspondence across all three orientations, using one actual exterior corner per original brick copy. No seam is emphasized or changed; normalization is grounded in repeated actual components, not numerical label or arbitrary option salience.',
  'prior_objection':'No earlier retained candidate/API pair. Every marked edge must belong to its stated brick, and the three original contact seams, numeric labels and 3D/projection/frozen visibility must remain unchanged.',
  'semantic_review':'An uncolored geometric brick remains the same brick with external contour annotations. No new face, cut, contact or material fill is introduced. Existing seams still distinguish all six copies; labels continue to denote assembled exterior surface areas.'}
}

SKIPS={
 'Plane212':{'decision':'skip_no_materially_new_clear_hypothesis','old':'Earlier Plane212 prescreen already rejected shared-leg restatement and false-size triangulation because it would create cutting givens or weaken the shaded example.',
             'considered':['Matching prototype triangle to its embedded gray copy only restates the true unit area1 and provides no new wrong correspondence.', 'Matching a half-cell to the entire prototype for30 would need a selective half-prototype partition or would ignore the explicit full two-cell-wide triangle. Styling existing grid lines alone does not communicate that new correspondence clearly.', 'Drawing an alternate tiling creates competing cutting regions; rejected before any rendering/call.'],
             'reason':'No concise new feature correspondence survives the no-new-cut and single-clear-unit requirements. Exact original count15 independently proved; no old design absence quota.'},
 'Plane338':{'decision':'skip_no_specific_geometric_wrong_target','old':'Earlier prescreen found only generic area/grid-scale emphasis, no grounded wrong correspondence.',
             'considered':['A bounding7x5 rectangle against the polygon gives area140 before subtraction, outside all supplied choices and no clear mistaken corner-area binding.', 'Pairing boundary partial cells merely by color cannot rigorously select any of96,76,88,104 without arbitrary rounding; no new preset is justified.', 'Adding a diagonal would be mathematically legitimate but supply correct triangulation, not a specific erroneous information correspondence.'],
             'reason':'Exact shoelace gives21grid cells=84; no material simple wrong-option mechanism found without moving labels/vertices, obscuring partial cells or inventing equality. No API.'},
 'Solid88':{'decision':'skip_no_legal_false_contact_receiver','old':'Earlier prescreen rejected added projected contact/cycle lines and unfounded exposed-edge styles.',
            'considered':['A full twelve-cube color count could suggest twelve drops but merely replaces contact count by object count; no concrete join counterpart transfers the information.', 'Matching a terminal exterior L to a true contact seam would assert an apparent unsupported extra contact and fail the actual-feature requirement.', 'Styling whole arms only groups a true tree structure and supports11; adding a cycle changes physical joins or diagnostic projection.'],
            'reason':'Contact enumeration gives exactly11. No concise actual seam correspondence causing a different count remains both useful and unambiguous. No geometry or counts changed, no API.'},
 'Solid226':{'decision':'skip_no_substantive_legal_new_notch_mechanism','old':'Old three_new_face_visibility_binding presetE produced correctC thenD(value1more), both misses. Six cut-edge motifs and full replies/PNGs reviewed.',
             'considered':['Binding full1-foot thickness to actual cut width is a useful true correspondence but supports the correct through-notch0.', 'Creating a rear-pocket interpretation would require an unshown rear wall/edge or changed frozen visibility; prohibited.', 'Restyling the same three exposed faces to seek E or relabeling to old observedD is an unchanged/cosmetic repeat and is excluded.', 'Marking only the front and top removed patches would require outlining absent material, potentially a false boundary; no unambiguous actual receiver.'],
             'reason':'Full-width notch loses three unit patches and gains three. No new simple targeted hypothesis distinct from the old failed face-count cue can preserve all diagnostic features.'}
}

def make(branch):
    engine=adapter(branch)
    if branch=='PlaneGeometry':
        from mathvision_plugins import PluginRenderer
    else:
        from render_plugins import PluginRenderer
    from partial_style import object_paths
    from workbench_io import pixel_hash
    for qid,spec in SPECS.items():
        if branch_of(qid)!=branch:continue
        folder=UNIT/qid/spec['variant_id'];folder.mkdir(parents=True,exist_ok=False)
        check=eligibility(qid);assert check['eligible'];write(folder/'eligibility_before_design.json',check)
        # Difference rationale is frozen before both rendering and API requests.
        write(folder/'design_difference_audit.json',{'stage':'material_refinement','question_id':qid,'variant_id':spec['variant_id'],'at':now(),**spec,
               'material_difference_asserted_before_render_and_calls':True,'pixel_hash_or_cosmetics_is_not_rationale':True,
               'all_old_design_and_raw_outcome_evidence':'../../history_inventory.json','new_parent_independent_review_required':True})
        context=engine.inspect_question(qid);write(folder/'fresh_context.json',context)
        scene=engine.scene(qid)
        try:
            scene.fig.canvas.draw()
            paths={obj['id']:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],
                    'segments':[seg['control'].tolist() for seg in p['segments']]} for p in object_paths(scene,obj['id'])] for obj in context['objects']}
        finally:scene.close()
        write(folder/'frozen_paths.json',paths)
        actions=[];roles=[]
        def style(target,role,start=None,end=None,width=2):
            action={'type':'set_object_style','target':target,'color':'#DC2626','linewidth_pt':width}
            if start is not None:
                p=paths[target][0]
                action['interval']={'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}
            actions.append(action);roles.append({'action_index':len(actions),'role':role,'target':target,'actual_path':paths[target]})
        def line(name,a,b,role):
            points=context['snap_points']; snaps=[]
            for xy in (a,b):
                matches=[p for p in points if p['xy']==list(xy)]
                assert matches,(qid,xy)
                snaps.append(matches[0])
            actions.append({'type':'add_line','id':name,'endpoints':[snaps[0]['xy'],snaps[1]['xy']],'color':'#DC2626','linestyle':'solid','linewidth_pt':1})
            roles.append({'action_index':len(actions),'role':role,'exact_fresh_snap_endpoints':snaps,'existing_edge_coverage':'Entire line lies on an existing black stripe outer boundary, never across an unmarked black interior.'})
        if qid=='Plane257':
            for target in ('f100','f130','f121'):
                style(target,'Receiver: one of the first flag\'s three genuine black unit squares; open bottom/right corner retains all8 black/white cells.',0,.5,width=1)
            for n,y in enumerate((0.,1.,2.)):
                line('r34_stripe_base_'+str(n),(11.,y),(13.5,y),'Source: full bottom edge of black stripe '+str(n+1)+', one of three actual black bands in the genuine3/5 fourth flag.')
                line('r34_stripe_side_'+str(n),(11.,y),(11.,y+.5),'Source: left side joins that stripe base into an open L, grouping one existing band rather than its five concealed black cells.')
        elif qid=='Plane336':
            for target in ('horiz','down1','down2'):
                style(target,'One full existing chord contributes two opposite equal radial half-rays about O; shared color groups the true six-ray frame. No angle/equality glyph or new dividing line.')
        elif qid=='Plane340':
            style('leftsquare','Source unit-square open bottom/right corner, actual side1 and area1 for the entire unshaded square.',0,.5)
            style('topsquare','Receiver top containing-square open right/top corner, actual side1; its gray subregion is5/8, not the whole square.',.25,.75)
            style('rightsquare','Receiver right containing-square open bottom/right corner, actual side1; its gray triangle is3/8, not the whole square.',0,.5)
        elif qid=='Solid184':
            style('stack001_stack101','Upper stacked brick: existing top-front length3 edge; paired with upper left vertical half.',width=1.5)
            style('stack000_stack001','Upper stacked brick: only z7..8 exterior vertical portion, ends at existing seam.',.5,1,width=1.5)
            style('stack000_stack100','Lower stacked brick: existing bottom-front length3 edge; paired with lower left vertical half.',width=1.5)
            style('stack000_stack001','Lower stacked brick: only z6..7 exterior vertical portion, ends at existing seam.',0,.5,width=1.5)
            style('wide000_wide001','Left wide-arrangement brick: exterior front-left height1 edge.',width=1.5)
            style('wide001_wide101','Left wide-arrangement brick: only x0..3 front-top length3 portion ending at existing seam.',0,.5,width=1.5)
            style('wide001_wide101','Right wide-arrangement brick: only x3..6 front-top length3 portion starting at existing seam.',.5,1,width=1.5)
            style('wide100_wide101','Right wide-arrangement brick: exterior front-right height1 edge.',width=1.5)
            style('long000_long001','Near long-arrangement brick: exterior front-left height1 edge.',width=1.5)
            style('long001_long101','Near long-arrangement brick: front-top length3 edge, paired with near vertical.',width=1.5)
            style('long011_long111','Far long-arrangement brick: back-top length3 edge, paired with far vertical.',width=1.5)
            style('long110_long111','Far long-arrangement brick: exterior far-right height1 edge.',width=1.5)
        plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':spec['mechanism'],'intent':spec['mechanism'],'params':{'actions':actions}}
        renderer=PluginRenderer(engine.config,engine,{qid:context})
        normalized=renderer.normalize(plugin)
        assert renderer.normalize(normalized)==normalized
        write(folder/'plugin_submitted.json',plugin);write(folder/'plugin.json',normalized)
        before=source_files(qid)
        n1,data1,pix1=renderer.render(normalized,frozen=True)
        n2,data2,pix2=renderer.render(normalized,frozen=True)
        assert n1==n2==normalized and data1==data2 and pix1==pix2 and source_files(qid)==before
        (folder/'candidate.png').write_bytes(data1);(folder/'repeat.png').write_bytes(data2)
        math_audit=read(UNIT/qid/'primary_math_audit.json')
        design={'question_id':qid,'variant_id':spec['variant_id'],'stage':'material_refinement','created_at':now(),
                'expected_wrong_answer':spec['expected_wrong_answer'],'correct_answer':math_audit['derived_answer'],
                **{k:v for k,v in spec.items() if k not in ('variant_id','expected_wrong_answer')},
                'marker_roles':roles,'mathematical_audit':str(UNIT/qid/'primary_math_audit.json'),
                'frozen_png_sha256':sha(folder/'candidate.png'),'frozen_pixel_sha256':pix1,'normalized_plugin_sha256':sha(folder/'plugin.json'),
                'pretest_only':True,'approval_status':'PRIMARY ONLY, unreviewed; NEW parent independent review required for any eventual delivery.'}
        write(folder/'design.json',design)
        write(folder/'render_check.json',{'at':now(),'schema_valid':True,'normalization_idempotent':True,'baseline_pixel_equal':True,
               'two_renders_byte_identical':True,'png_sha256':sha(folder/'candidate.png'),'pixel_sha256':pix1,
               'paths_from_actual_fresh_scene':True,'source_files_unchanged':True,'source_fingerprints':before,'isolation':ISOLATION,
               'exact_default_and_style_validation':'Approved original PluginRenderer normalization/schema and frozen render, no renderer edits.',
               'appearance_changes':{'world_geometry_changed':False,'projection_changed':False,'frozen_visibility_changed':False,'fill_text_geometry_changed':False,'original_linestyle_changed':False},
               'actual_native_png_view_pending':True})
        print(json.dumps({'question_id':qid,'variant_id':spec['variant_id'],'expected_wrong_answer':spec['expected_wrong_answer'],'markers':len(actions),'png':str(folder/'candidate.png'),'sha256':sha(folder/'candidate.png')}))

if __name__=='__main__':make(sys.argv[1])
