from tools35 import *
assert BRANCH=='SolidGeometry'
from partial_style import object_paths,describe_paths
cfg,ad,Renderer=adapter()
specs=[
 {'q':'Solid156','v':'r35_axis_unit_to_whole_direct_count','wrong':'A',
  'difference':'Old interval_boundary_count_binding used 6 red midpoint dots versus 4 blue width-boundary dots to elicit a boundary/interval miscount. Its only complete final was C; run2 was aborted. This new design adds no dots and does not ask for four width intervals. It binds all THREE actual brick axes to parallel WHOLE-CUBE edges, targeting the different error of transferring repeat counts directly into brick side lengths instead of inversely. The new wrong rationale is the true counts depth:width:height=2:3:6, scaled directly so minimum2 becomes4, giving4:6:12=A. This is not the old observed C plus cosmetics, or a retry of the aborted image. Same target letter A arises from a different predeclared operation.',
  'hypothesis':'Match three real unit edges to three parallel whole-cube edges; mistakenly use repeat counts2:3:6 as dimensions and scale to shortest4, yielding4x6x12, A.',
  'proof':'All bricks are aligned in the actual source and frozen scene. The cube has 3 width columns, 2 depth strips and 6 height layers. Equal total edge lengths imply 3w=2d=6h=s. Hence h is shortest; h=4 gives s=24,w=8,d=12. The only listed dimensions are C:4x8x12. Color matches only axis direction and does not assert that a unit edge equals the full cube edge.',
  'actions':[
   ('fronthorizontal6','#DC2626',(0,1/3),'Width edge of the upper-left-front brick; matches the red whole width at rear top.'),
   ('topdepth0','#2563EB',(0,0.5),'Depth edge of that same brick; matches blue whole depth on opposite side.'),
   ('frontvertical0','#16A34A',(5/6,1),'Height edge of that same brick; matches green whole height at rear right.'),
   ('topwidth2','#DC2626',None,'Whole-cube width edge, three repetitions of the red unit width.'),
   ('topdepth3','#2563EB',None,'Whole-cube depth edge, two repetitions of the blue unit depth.'),
   ('rightvertical2','#16A34A',None,'Whole-cube height edge, six repetitions of the green unit height.')],
  'risks':['Colors could help solve correctly rather than cause the targeted inversion; no effectiveness assumed.','Unit-vs-whole color correspondence is directional, not an explicit equality condition. All 3/2/6 seams must remain countable.']},
 {'q':'Solid128','v':'r35_corner_ownership_mixed_rims','wrong':'81',
  'difference':'Old Solid128 was screened without a saved plugin/call; it considered generic inner-versus-outer rim emphasis without a concrete mapping. This design specifically binds the outside front run (including the corner position) to the inside return run (starting one cube inward). The corner-inclusion mismatch targets dividing36 equally into four nine-cube side allocations and then treating9 as the empty interior side, giving81. No finite square outline, centerline, extension or extra corner is drawn.',
  'hypothesis':'An open existing-edge correspondence mixes an outer wall run with an inward-offset return run; transfer the 36/4=9 corner-allocation count to interior side length and answer9^2=81.',
  'proof':'The actual source depicts a one-course, one-cube-thick wall turning a right corner. Let outer side contain n cubes. The square border has4n-4 cubes, because4corner cubes are counted twice by4full side runs. 4n-4=36 gives n=10. The square strictly inside is (10-2)x(10-2)=8x8, requiring64 new cubes. Equivalently 4m+4=36 gives inner side m=8. The drawing is deliberately a partial wall; its clipped lengths are not full side measurements.',
  'actions':[
   ('front_top','#DC2626',None,'Actual outside upper edge of the front wall; includes the visible corner cube before the inward return begins.'),
   ('return_inner_top','#DC2626',None,'Actual inward upper edge of the perpendicular return, anchored one cube inward; links to the first run at the real front-top subdivision, targeting mixed corner ownership.')],
  'risks':['The exact image contains only a wall section; no visual measured side9 is claimed. Wrong81 follows the corner-allocation misconception, not a read-off length.','Red edge color must not be described as a newly specified physical square boundary. Existing wall thickness and separate black outer return stay visible.']},
 {'q':'Solid192','v':'r35_five_visible_faces_opposite_exhaustion','wrong':'20',
  'difference':'Old Solid192 was screened with no saved candidate or calls. It rejected changing pips or highlighting only the shared seam. This new design never marks a pip: it assigns two open existing boundary edges to EACH of five visible faces, matching top-to-top and front-to-front across the dice. It targets the precise mistake that the five opposite faces exhaust the unseen faces, omitting the remaining unseen opposite pair of the left die. Thus35-15=20 rather than42-15=27.',
  'hypothesis':'Group the five visible faces by genuine orientation, prompting one opposite-face complement7 per displayed face. False exhaustiveness gives5*7-(1+2+4+6+2)=20; the missing left side-pair contributes7.',
  'proof':'Each ordinary die has total1+2+3+4+5+6=21 spots. Actual source/formal show left top1 and front2, and right top4,front6,side2; visible total15. Both dice total42, so all unseen spots total27. Opposite lookup alone accounts for left bottom6+rear5=11 and right bottom3+rear1+left5=9, total20. The left die also has two unseen opposite side faces summing7; including them gives27. This uses only ordinary dice and actual visible faces, without assuming hidden contact values individually.',
  'actions':[
   ('dicee2','#DC2626',None,'Far top edge of left top face (one spot); first leg of its open top frame.'),
   ('dicee3','#DC2626',None,'Left depth edge of left top face; second top-frame leg.'),
   ('dicee9','#DC2626',None,'Far top edge of right top face (four spots); matching top-frame first leg.'),
   ('dicee4','#DC2626',None,'Left depth edge of right top face; matching top-frame second leg; also an existing shared edge.'),
   ('dicee0','#2563EB',None,'Bottom edge of left front face (two spots); first front-frame leg.'),
   ('dicee5','#2563EB',None,'Left vertical edge of left front face; second front-frame leg.'),
   ('dicee7','#2563EB',None,'Bottom edge of right front face (six spots); matching front-frame first leg.'),
   ('dicee6','#2563EB',None,'Left vertical edge of right front face; matching front-frame second leg; existing shared seam.'),
   ('dicee13','#16A34A',None,'Far vertical edge of the only displayed side face (two spots); first side-frame leg.'),
   ('dicee10','#16A34A',None,'Bottom depth edge of that displayed side face; second side-frame leg.')],
  'risks':['The color does not communicate a rule that only marked faces count; the formal question still asks all unseen faces. A correct human can use42-visible total.','No causal effect assumed; the grouping may merely make the correct visible total easier. Every spot must remain black and readable.']}
]
for d in specs:
    q=d['q'];out=HERE/q/d['v'];e=eligibility(q);assert e['eligible']
    write(out/'design_difference_audit.json',{'question_id':q,'variant_id':d['v'],'stage':'material_refinement','created_at':now(),'before_any_API_calls':True,'material_difference':d['difference'],'predeclared_wrong_hypothesis':d['hypothesis'],'expected_wrong_answer':d['wrong'],'prior_evidence_manifest':str(HERE/'history_read_audit.json'),'old_variant_unchanged_retest':False,'cosmetic_or_posthoc':False,'primary_proof':d['proof'],'risks':d['risks']})
    m=ad.inspect_question(q);before=inputs(ad,q);scene=ad.scene(q);actions=[];roles=[]
    try:
        scene.fig.canvas.draw()
        for target,color,interval,role in d['actions']:
            paths=object_paths(scene,target);assert len(paths)==1
            path=paths[0];controls=[x['control'].tolist() for x in path['segments']]
            a={'type':'set_object_style','target':target,'color':color,'linewidth_pt':1.5}
            if interval is not None:a['interval']={'path_id':path['id'],'path_sha256':path['sha256'],'start':interval[0],'end':interval[1],'wrap':False}
            actions.append(a)
            roles.append({'action':a,'role':role,'stable_source_object':next(x for x in m['objects'] if x['id']==target),'full_precision_frozen_projected_controls':controls,'frozen_path_id':path['id'],'frozen_path_sha256':path['sha256'],'closed':path['closed'],'path_description':describe_paths(scene,target)})
    finally:scene.close()
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':d['hypothesis'],'intent':d['hypothesis'],'params':{'actions':actions}}
    renderer=Renderer(cfg,ad,{q:m});norm,data,pixels=renderer.render(plugin);norm2,data2,pixels2=renderer.render(norm,frozen=True)
    assert data==data2 and pixels==pixels2 and norm==norm2 and before==inputs(ad,q)
    write(out/'plugin.json',norm);(out/'candidate.png').write_bytes(data);write(out/'context.json',m)
    write(out/'render_check.json',{'question_id':q,'no_op_formal_pixel_equal':True,'deterministic_png_bytes_equal':True,'normalized_frozen_replay_equal':True,'png_sha256':hashlib.sha256(data).hexdigest(),'pixel_sha256':pixels,'original_pixel_sha256':m['original_pixel_sha256'],'frozen_inputs':before,'appearance_changes':renderer.appearance_changes(norm),'isolation':ISOLATION,'strict_own_root_guard_before_project_imports':True})
    write(out/'marker_geometry_audit.json',{'question_id':q,'variant_id':d['v'],'marker_roles':roles,'new_points':0,'new_lines':0,'changed_semantic_fill_text_geometry_projection_frozen_visibility':False,'all_marks_on_actual_existing_source_features':True,'human_semantics':'These are numerical size/counting questions. Recoloring actual edges does not change cube/brick membership, spots or mathematical quantities; no picture-content transformation is requested. No explicit equality/angle/parallel glyph or new physical region is added. Human clarity still requires actual native viewing, not only schema acceptance.'})
    write(out/'design.json',{'question_id':q,'variant_id':d['v'],'stage':'material_refinement','expected_wrong_answer':d['wrong'],'correct_answer':ad.records[q]['answer'],'created_at':now(),'predeclared_hypothesis':d['hypothesis'],'material_difference_from_old':d['difference'],'primary_unique_math_proof':d['proof'],'marker_roles':roles,'risks':d['risks'],'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_difference_audit_sha256':file_hash(out/'design_difference_audit.json'),'formal_question':ad.records[q]['question'],'approval_status':'UNREVIEWED primary design; parent must launch NEW independent review for any possible delivery.'})
    print(q,d['v'],'rendered',len(actions),'actions',flush=True)
