from research import *
import copy
import numpy as np
from delivery_bridge_adapter import RendererAdapter
from render_plugins import PluginRenderer
from renderer_adapter import scene_png
from partial_style import object_paths
from workbench_io import load_config, canonical_hash, environment_versions

RED='#DC2626'; BLUE='#2563EB'; GREEN='#16A34A'

PROOFS={
'Solid238': 'The two end triangles are BGJ and CFI. Rectangle ABJH gives BJ=AH=8. Rectangle FIDE gives its axial side ID=EF=8; all three lateral rectangles have this same axial length, so HJ=AB=BC=EF=8. G,J,H occur in that order along the same original straight boundary. Therefore GJ=GH-HJ=14-8=6. The original square at J gives BJ perpendicular JG. Volume=(8*6/2)*8=192. This uses rectangular faces and prism incidence, never screen lengths.',
'Solid241': 'Set A=(0,0,0), B=(a,0,0), D=(0,b,0), E=(0,0,h), with positive a,b,h. The rectangular prism gives tan(BAF)=h/a=tan30=1/sqrt3 and tan(DAH)=h/b=tan60=sqrt3. Thus a=sqrt3*h and b=h/sqrt3. At E, EG=(a,b,0), EC=(a,b,-h). Their dot product is a^2+b^2=(10/3)h^2, and their norm product is sqrt((10/3)*(13/3))*h^2. cosCEG=sqrt(10/13)=sqrt130/13, independent of positive scale. AB and AD are perpendicular; the two given angles lie in different vertical planes and cannot be subtracted as coplanar angles.',
'Solid242': 'The axial half cut leaves one curved lateral surface of area pi*r*h=60pi, two semicircular ends of total area pi*r^2=36pi, and one newly exposed rectangle of width2r=12 and height10, area120. All are boundary surfaces of the solid. Total=96pi+120. The actual top arc has length pi*r=6pi, while the actual diameter has length2r=12. Their colored comparison cannot change either length, the number of surfaces or the solid/cavity interpretation.',
'Solid243': 'Actual labels put A at the apex and B,C,D,E around the square base. Let common original edge length be s>0. Then AB=AD=s, while BD is the square diagonal s*sqrt2, not one of the eight original edges. Triangle ABD is right isosceles at A, so ABD=45deg uniquely. Equivalently its B cosine is1/sqrt2. The genuine side face ABC is equilateral, giving ABC=60deg; the genuine square-base triangle BCD gives CBD=45deg. However rays BA,BC,BD are not coplanar: with s=1 their scalar triple product has magnitude1/sqrt2. Hence subtracting60-45 is invalid.',
'Solid244': 'Use triangle ABC as tetrahedron base. AB and BC are perpendicular sides of the cuboid bottom rectangle; its area is half of that rectangle. H is above D, so the perpendicular height from H to planeABC equals the box height DH. Therefore V_ABCH=(1/3)*(1/2*AB*BC)*DH=V_box/6. V_ABCH=20 forces V_box=120 for every positive cuboid shape. No perspective ratio is needed.',
'Solid245': 'The two original full diameter segments give r=8/2=4 and R=20/2=10. The separate original vertical segment gives h=8. In a right frustum the true slant length is sqrt(h^2+(R-r)^2)=sqrt64+36=10. Lateral area=pi*(R+r)*L=140pi; the two full circular faces total pi*(R^2+r^2)=116pi. Total256pi uniquely. Neither the dotted diameters nor their page lengths are radii or slant lengths.',
'Solid246': 'The shown fold is the fixed vertical hinge OT. A lies on the moving top edge at perpendicular distance3 from that hinge; B is its outer endpoint at perpendicular distance6, from the card width. Opening from closed to45deg rotates each through pi/4. Their actual paths are circular arcs, so the difference is(6-3)*pi/4=3pi/4 inches. Height8 measures distance along the hinge, which does not affect the radial distance to that axis. No additional start position, center or trajectory is introduced.',
'Solid248': 'The original explicit r=3 label is attached to the center-to-rim segment OR, so the given is radius3, not diameter3. For a right cylinder V=pi*r^2*h; 45pi=9pi*h implies h=5 uniquely. The frozen drawing height5 is not used as a given. Top diameter6, if constructed, would not make r3 into d3.'}

def style(target,color,width=1.5):
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width}

def line(id,a,b,color,snaps):
    return {'type':'add_line','id':id,'endpoints':[snaps[a]['xy'],snaps[b]['xy']],'color':color,'linestyle':'dashed'}

def specs(qid,s):
    if qid=='Solid238':
        return ('r53_whole_span_to_hypotenuse','64\\sqrt{33}',
        [style('line_6',RED),style('line_9',RED)],
        ['GH is the actual full boundary carrying the given14; its internal J and both endpoints remain visible. This is the source of a total length, not a newly drawn dimension.', 'BG is the actual triangular-end hypotenuse and original dashed fold. It receives the erroneous whole-span length14 association; its role differs from the old GJ leg.'],
        'Erroneously assign BG=GH=14 while retaining BJ=8 and axial length8. Then GJ=sqrt(14^2-8^2)=2sqrt33 and V=(1/2)*8*(2sqrt33)*8=64sqrt33. The equality is the hypothesized solver mistake, never an added mathematical condition.',
        'Old subrange_14_binding isolated GJ and paired AH/BJ, preset448, first final1040, second call aborted. New design marks the whole GH and the different BG hypotenuse, omits the old AH/BJ blue pair and does not isolate GJ. It changes receiver identity and the erroneous geometric rule from un-subtracted leg to hypotenuse/Pythagoras. It is not a retry of the failed/aborted PNG.')
    if qid=='Solid241':
        return ('r53_cross_plane_angle_difference','\\frac{\\sqrt{3}}{2}',
        [style('line_0',GREEN),style('line_1',GREEN),line('r53_AF','A','F',RED,s),line('r53_AH','A','H',BLUE,s),line('r53_EC','E','C',RED,s),line('r53_EG','E','G',BLUE,s)],
        ['AB is the actual first reference edge of given30deg, highlighted as one baseline member.','AD is the actual perpendicular second reference edge of given60deg. Its original hidden dash remains; green grouping compares the two reference roles without declaring parallelism.','AF is the actual front-face diagonal used by givenBAF=30deg, exact named endpoints. Red supplies one source ray.','AH is the actual left-face diagonal used by givenDAH=60deg, exact named endpoints. Blue supplies the second source ray; dashed auxiliary appearance does not expose a missing physical edge.','EC is the actual space diagonal forming the first target ray at E, paired red with AF.','EG is the actual top-face diagonal forming the second target ray at E, paired blue with AH.'],
        'Illegally treat the two perpendicular green baseline directions as a common coplanar baseline, compute60-30=30, then transplant the red/blue source-ray angle to the target red/blue ray angleCEG. Return cos30=sqrt3/2. In the actual prism the source angleFAH has cosine sqrt3/4 and targetCEG has cosine sqrt130/13; neither is30deg.',
        'Old background18 assessment saved no design or calls because it found no clean metric correspondence. This design proposes an explicit6-ray/reference mapping and a fixed cross-plane subtraction error. It acknowledges the old objection and preserves all named endpoints and perpendicular prism structure; no equal-angle marks, arcs, plane assertion or changed source dimensions are introduced.')
    if qid=='Solid242':
        return ('r53_arc_width_to_cut_diameter','156\\pi',
        [style('arc_0',RED),style('line_3',RED)],
        ['The true top semicircular rim is the source boundary for the curved shell unrolled width pi*r=6pi.','The true bottom diameter is a boundary of the rectangular cut face and is the receiver for a mistaken same-width transfer; its actual width remains2r=12.'],
        'Transfer the curved-shell width pi*r=6pi to the flat rectangle, replacing its true diameter2r by pi*r. Erroneous total=60pi(shell)+36pi(ends)+(6pi)*10(cut)=156pi. This is a wrong boundary-role substitution, not an added equality or omitted surface.',
        'Old cut_face_membership restyled all4 rectangle boundaries dashed blue and both end rims red, preset96pi, finals96pi+120 twice. New design retains every original visible/hidden style, marks only one curved source rim and one straight receiver diameter, and keeps the rectangle counted with the wrong transferred width. Source/receiver groups and geometric misconception differ from the old surface-membership omission.')
    if qid=='Solid243':
        return ('r53_face_base_angle_subtraction','15',
        [style('line_0',RED),style('line_3',GREEN),line('r53_BD','B','D',BLUE,s)],
        ['BA is one true lateral edge of equilateral faceABC and the first target ray ofABD.','BC is the shared reference ray for the true60deg face angleABC and true45deg base angleCBD. It has a specific angular comparison role.','BD is the true square-base diagonal and second target ray, added as a dashed auxiliary between exact named B/D. It is not counted as an original pyramid edge.'],
        'Treat raysBA,BC,BD as coplanar and subtract angleCBD=45deg from angleABC=60deg, returningABD=15deg. In3D their scalar triple product is nonzero, so this difference rule is false; the actual target is45deg.',
        'Old equal_color_diagonal colored wholeABD and assigned diagonal the common edge length; old equilateral_capture colored wholeABC and confused its60deg withABD. Both had preset60 and45/45 finals. New design uses a shared BC reference and3distinct ray roles, preset15 from the specific invalid cross-plane subtraction60-45. It neither treatsBD as an eighth original edge nor merely recolors either old closed triangle.')

SKIPS={
'Solid244': 'The prospective half-rectangle-to-whole-base factor3 is exactly the old rectangular_base_capture mechanism/preset60 (old120/120). Adding AC would make the half-base explicit but would not produce a substantively different error; changing to BH-as-height would need an unknown box aspect ratio or pixel measurement. No new reliable predeclared number follows from actual givens. Skip without calls.',
'Solid245': 'Height8-to-slantL was already tested228pi versus256pi/256pi. A diameter20-to-L pairing changes the chosen scalar but supplies no independent structural correspondence beyond the same naked equal-length substitution; it is too weak to count as material refinement. Diameter/radius-run confusion needs a new explicit radial-run receiver not present as a source object, or just recolors existing full spans. No new dimensions/equality premises or tuned number are added. Skip without calls; not a blanket color ban.',
'Solid246': 'Whole width6 to AB is the old failed3pi/2 design (both3pi/4). Height8 is parallel to the hinge, not a radial source; its transfer would only assert false new equality. A chord-versus-arc design needs an added path linking successive positions; here that would invite a competing physical trajectory/center interpretation. Keep the actual opening motion and original A/B unchanged; no new trajectory, center or start-position premise. Skip without calls.',
'Solid248': 'Only explicit known metric is the radius3. Whole-diameter completion is the old20-preset failure (5/5). A new bottom diameter would repeat that same total-versus-half binding on a translated parallel base. Comparing unknown height h to r3 supplies no defined geometric transfer, and measuring the drawn height to change numbers is forbidden. No new materially distinct clean receiving object. Skip without calls.'}

def build(qid):
    current=eligibility(qid,OWN/qid/'eligibility_before_design.json')
    assert current['eligible']
    metadata=read(OWN/qid/'context.json')
    snaps={x['id']:x for x in metadata['snap_points']}
    variant,wrong,actions,roles,rule,difference=specs(qid,snaps)
    folder=OWN/qid/variant;folder.mkdir(exist_ok=True)
    assert not (folder/'design.json').exists() and not (folder/'tests').exists(), 'Frozen/tested designs are immutable'
    audit={'question_id':qid,'variant_id':variant,'created_at':now(),'material_difference':difference,'specific_wrong_geometric_rule':rule,'predeclared_hypothesis':wrong,'original_unique_solution':PROOFS[qid],'mark_information_roles':roles,'semantics':'Numerical geometry question, not picture completion or transported printed paper. Color compares actual segment/arc roles and is not an equality/angle/plane condition. Auxiliary diagonals have exact named endpoints and remain dashed. The original3D, projection, fills, point count, text and visibility are fixed. No wording or legend is added. A genuine human semantic failure still blocks testing regardless of schema/hits.','old_history_manifest':str(OWN/'history_inventory.json'),'formal_binding':current['formal_input_binding'],'approval_content_sha256':current['current_content_sha256']}
    if not (folder/'design_difference_audit.json').exists():
        dump(folder/'design_difference_audit.json',audit)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':variant,'intent':rule,'params':{'actions':actions}}
    dump(folder/'plugin_submitted.json',plugin)
    config=load_config();config['runtime_dir']=str(OWN/'state');config['output_dir']=str(OWN/'output')
    adapter=RendererAdapter(config)
    fresh=adapter.inspect_question(qid)
    assert fresh==metadata
    renderer=PluginRenderer(config,adapter,{qid:fresh})
    normalized=renderer.normalize(plugin)
    assert renderer.normalize(normalized)==normalized
    scene=adapter.scene(qid)
    bindings=[]
    try:
        _,noop=scene_png(scene)
        assert noop==fresh['original_pixel_sha256']
        for index,a in enumerate(normalized['params']['actions']):
            if a['type']=='set_object_style':
                paths=[{k:v for k,v in path.items() if k!='segments'} | {'segments':[{'control':seg['control'].tolist(),'style':seg['style']} for seg in path['segments']]} for path in object_paths(scene,a['target'])]
                bindings.append({'action_index':index,'action':a,'paths':paths})
            else:
                matched=[]
                for endpoint in a['endpoints']:
                    matched.append([x for x in fresh['snap_points'] if x['xy']==endpoint])
                assert all(matched)
                bindings.append({'action_index':index,'action':a,'exact_original_endpoint_bindings':matched})
    finally: scene.close()
    p1,b1,h1=renderer.render(normalized);p2,b2,h2=renderer.render(normalized)
    assert p1==p2==normalized and b1==b2 and h1==h2
    assert eligibility(qid)['formal_input_binding']==current['formal_input_binding']
    (folder/'draft_candidate.png').write_bytes(b1)
    (folder/'repeat.png').write_bytes(b2)
    dump(folder/'plugin.json',normalized)
    dump(folder/'fresh_context.json',fresh)
    dump(folder/'path_bindings.json',bindings)
    dump(folder/'render_check.json',{'created_at':now(),'schema_valid_and_defaults_normalized':True,'normalization_idempotent':True,'no_op_pixel_equals_formal':True,'two_sequential_draws_byte_identical':True,'png_sha256':sha(folder/'draft_candidate.png'),'pixel_sha256':h1,'fresh_context_matches_initial':True,'formal_binding_before':current['formal_input_binding'],'formal_binding_after':eligibility(qid)['formal_input_binding'],'renderer':'delivery_bridge_adapter.RendererAdapter + unchanged SolidGeometry.workbench.render_plugins.PluginRenderer','appearance_changes':renderer.appearance_changes(normalized),'environment':environment_versions(),'isolation':ISOLATION,'plugin_sha256':sha(folder/'plugin.json'),'path_bindings_sha256':sha(folder/'path_bindings.json'),'native_visual_review':'PENDING actual view before design.json freeze and calls'})
    dump(folder/'pending_design.json',{'question_id':qid,'variant_id':variant,'branch':'SolidGeometry','expected_wrong_answer':wrong,'primary_math_proof':PROOFS[qid],'specific_wrong_geometric_rule':rule,'design_difference':difference,'marker_roles':roles,'created_at':now(),'status':'PRECALL_DRAFT_PENDING_NATIVE_REVIEW'})
    print(qid,variant,'expected',wrong,'png',sha(folder/'draft_candidate.png'))

if __name__=='__main__':
    for qid in ['Solid238','Solid241','Solid242','Solid243']:
        build(qid)
    for qid,reason in SKIPS.items():
        dump(OWN/qid/'assessment.json',{'question_id':qid,'assessed_at':now(),'decision':'skip_no_new_calls','original_unique_solution':PROOFS[qid],'reason':reason,'sourceJPG_and_formalPNG_actually_viewed':True,'exact_scene_actually_read':True,'old_designs_presets_full_raw_responses_and_pngs_actually_read':True,'eligibility_initial':str(OWN/qid/'eligibility_initial.json'),'baseline_check':read(OWN/qid/'baseline_check.json'),'new_design_count':0,'new_call_count':0})
