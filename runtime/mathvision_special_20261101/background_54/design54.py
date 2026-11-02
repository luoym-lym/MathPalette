from env54 import *
from fractions import Fraction as F
import math
from workbench_io import load_config, pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer

QIDS=read(BASE/'background_54_assignment.json')['question_ids']
proofs={
'Plane251':{'answer':'22.5','proof':'Write h=sqrt(3)/2, the altitude of an actual side1 grid triangle. The exact gray vertices are (2,0),(9/2,0),(9/2,5h),(2,4h). Parallel vertical sides have lengths4h and5h, separated by5/2. Trapezoid area=(5/2)(4h+5h)/2=45h/4. One smallest equilateral triangle has area h/2, hence gray area=45/2=22.5 units. The gray top is not horizontal; all fractional cells are included. No piece-count approximation is used.','new_error':'A side2 equilateral grid triangle has area4 of these units. Treating the matched complete side2 triangle as area1 gives (45/2)/4=45/8=5.625, a specific wrong numeric answer.'},
'Plane291':{'answer':'B','value':'3/8','proof':'Normalize the actual rectangle to [0,2]x[0,1]. The true diagonals intersect at(1,1/2). Gray0 vertices(0,0),(0,1),(1,1/2) have area1/2. Gray1 vertices(1,0),(2,0),(1,1/2) have area1/4. Their interiors are disjoint. Total gray3/4 divided by rectangle2 gives3/8, uniquely B.','new_error':'Transfer the full left side length1 to the visibly shorter center-to-bottom segment1/2 while retaining gray1 base1. Wrong gray1 area1/2 instead of1/4 produces(1/2+1/2)/2=1/2, D. The blue top-right and bottom-right unit spans are genuinely equal; red vertical spans differ by2.'},
'Plane293':{'answer':'E','proof':'Each panel side is2. A black unit square area1. B two right isosceles triangles legs1, each1/2, total1. C two diamonds with perpendicular diagonals1 and1, each1/2, total1. D four triangles each base1 and height1/2, each1/4, total1. Panel area4; every black area1/4. Unique E. Original component counts1,2,2,4 and their respective areas are preserved.','skip':'Previous A/C square-similarity open corners and B/D triangle-count full contours already test the obvious scale/object-count transfers. A new perimeter-as-area idea would reuse essentially the same B/D contours and merely extend their coloring to A/C, without a distinct local measured-area correspondence. Treating all black boundaries as unit strokes would add an arbitrary metric. No materially new simple matched-area hypothesis retained.'},
'Plane343':{'answer':'A','proof':'Tangency on each true side gives a+b=16,b+c=14,c+d=17,d+e=13,e+a=14. Alternating the odd-cycle equations gives2a=16-14+17-13+14=20. Unique solution(a,b,c,d,e)=(10,6,8,9,4), all positive. Each equation checks and10>9>8>6>4, uniquely A. Odd-cycle coefficient system has trivial kernel because sign alternation returns delta_a=-delta_a.','skip':'Actual formal PNG and source JPG both contain only the five-sided outline and labels16,14,17,13,14; NO circles, radius segments or tangency points are drawn. The brief prospective radius/touch-position binding is therefore not available. Adding inferred contact points/radii would assert solved constructions absent from the original; selecting longest edge17 alone is arbitrary wrong-option salience. No candidate/API.'},
'Plane345':{'answer':'C','value':'76cm','proof':'Let small long side L=10 and short side s. The top row has2 horizontal rectangles, so large width W=2L. The middle row has5 rotated rectangles, so W=5s. Thus s=2L/5=4. Height H=s+L+s=18, width20, perimeter2(20+18)=76, uniquely C. All9 rectangles have exactly10x4 dimensions and disjoint interiors in the frozen scene.','new_error':'Take exactly ONE actual long side from EACH of9 rectangles, transfer the given10cm to these nine equal edges across orientations, then mistake their aggregate9*10=90 for outer perimeter; E. Four selected lines are true internal seams, so they cannot legitimately contribute to perimeter. All short exterior edges remain visible for human correction.'},
'Plane346':{'answer':'D','value':'24cm x16cm','proof':'Use actual coordinates x=0..6,y=0..4 and radius2 quarter arcs. Upper boundary: y=2+sqrt(4-x^2) on[0,2], y=2+sqrt(4-(x-4)^2) on[2,4], y=4-sqrt(4-(x-6)^2) on[4,6]. Its integral is(4+pi)+(4+pi)+(8-pi)=16+pi. Lower boundary y=4-3x on[0,1], y=(4-x)/3 on[1,4], y=sqrt(4-(x-6)^2) on[4,6]. Its integral is5/2+3/2+pi=4+pi. Difference12 square grid units, exact cancellation of equal quarter disks. Area192 implies cell area16 and positive side4cm. Six intervals horizontally and4 vertically give24x16, uniquely D. C20x12 would count5 and3 INTERNAL LINES, not6 and4 intervals.','new_error':'Keep the valid cell side4cm but associate5 highlighted interior vertical lines with horizontal size and3 highlighted interior horizontal lines with vertical size:5*4 by3*4=20x12, C. Outer black frame and all6x4 intervals remain clear.'},
'Plane350':{'answer':'B','value':'1/2','proof':'Actual outer square side4, quadrants side2. Four shaded squares each side1, disjoint areas1 each. The two shaded right triangles have perpendicular legs2 and2, area2 each. Gray interiors do not overlap; total4*1+2*2=8 of16=1/2, uniquely B.','skip':'Considered a new linear-side-fraction error: a side1 small square treated as half a side2 quadrant would give4*2+2*2=12 of16=3/4(E). On this actual colored-part question, color on white boundaries can reasonably become additional colored material. A black-width-only pair would require overlapping nested L edges or nearly all quadrant/small-square outlines, offering no distinct readable unit transfer beyond existing structure. No clear useful new candidate retained; no blanket ban on color in other questions.'},
'Plane351':{'answer':'36','proof':'The side2 completion is the triangular grid in a regular hexagon of side2 unit sticks, as indicated by the visible interior triangle. Axial lattice vertices(q,r) satisfy max(abs(q),abs(r),abs(q+r))<=2:19 vertices. Unit-neighbor edges in three orientations have14 per orientation,42 total. Equivalently24 unit triangular faces give72 face-edge incidences; boundary12, so interior(72-12)/2=30, total42. The actual partial diagram contains exactly six individual gapped unit sticks: P0P1,P1P2,P2P3,P3P4,P4P2,P4P5; no duplicates. All six are members of the completed hexagonal lattice centered at(4,sqrt3), so42-6=36 additional.','skip':'Considered pairing one genuine triangle from the side1 hexagon with P2P3P4 plus a shared/exterior edge. This only locates a correct unit triangle. No4 complete side1 copies appear in the partial side2 diagram, so a4*12-6=42 error would require an author-invented grouping, and a total42-versus-additional36 cue would be generic emphasis without distinct information transfer. Do not add missing sticks or overpaint gaps to manufacture that grouping. No candidate/API.'}
}
for q,d in proofs.items():
    e=eligibility(q);assert e['eligible'],e['reasons']
    save(f'{q}/eligibility_before_assessment.json',e)
    rec=e['formal_record'];scene=read(PROJECT/'PlaneGeometry'/rec['scene'])
    save(f'{q}/source_scene_snapshot.json',scene)
    save(f'{q}/mathematical_audit.json',{'question_id':q,'checked_at':now(),'independent_of_assignment':True,'native_formal_and_source_jpg_viewed':True,**d})

# Two exact mathematical cross-checks rather than rounded visual assumptions.
verts=[(q,r) for q in range(-2,3) for r in range(-2,3) if max(abs(q),abs(r),abs(q+r))<=2]
edges=[(p,(p[0]+dq,p[1]+dr)) for p in verts for dq,dr in [(1,0),(0,1),(1,-1)] if (p[0]+dq,p[1]+dr) in verts]
assert len(verts)==19 and len(edges)==42
save('Plane351/lattice_enumeration.json',{'vertices':verts,'edges':edges,'edge_count':42,'already_present':6,'additional':36})
assert F(5,2)*F(9,2)/F(1,2)==F(45,2)

config=load_config();adapter=RendererAdapter(config)
def style(ctx,target,start=None,end=None,color='#DC2626',width=1.5):
    a={'type':'set_object_style','target':target,'color':color,'linewidth_pt':width}
    if start is not None:
        p=next(t for t in ctx['canvas']['targets'] if t['id']==target)['partial_paths'][0]
        a['interval']={'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}
    return a

specs={
'Plane251':('r54_triangle_scale_unit_transfer','5.625',
    'Open two-edge V correspondences match one actual smallest triangle outside the gray target and one side2 triangle within it. Transfer area1 by similar shape while overlooking scale2/area4.',
    'Old Plane251 had no candidate/API; related Plane405 had no saved candidate/API and specifically rejected numeric choices inconsistent with a unit swap. This is a newly constructed numeric-unit transfer for Plane251, not a recolored failed405 PNG or old output relabel. Open V geometry, precise new numeric error and six actual grid-edge IDs are frozen before calls.'),
'Plane291':('r54_half_height_full_side_binding','D',
    'Pair the full left vertical side with the half-height divider in red; pair the genuinely equal upper-right/lower-right horizontal spans in blue. Transfer the former full height1 to the latter half-height1/2 in the small gray triangle.',
    'Oldv01 highlighted both entire gray contours red and one full diagonal blue; expectedD observedA/B. Oldv02 contrasted entire gray contours red/blue; expectedA observedB/D. This design retains black gray sloping boundaries and diagonals and marks ONLY four measured axis-aligned spans. New mechanism is a specific base/height whole-to-half substitution, not counting two gray pieces or ignoring one gray part. PresetD is derived before new calls, not harvested from oldv02 observedD.'),
'Plane345':('r54_nine_long_edge_perimeter_sum','E',
    'One exact10cm long-edge exemplar from each of9 congruent rectangles, across horizontal and vertical orientations; count those unit features as the perimeter instead of excluding seams and including short outer spans.',
    'Old Plane345 and related Plane395 were prescreen-only, no old candidate/API. This selects9 systematic one-per-rectangle long edges,4 of them genuine interior seams; no arbitrary outer contour salience and no false long=short equality. The new error9*10=90 is fully specified.'),
'Plane346':('r54_interior_line_interval_binding','C',
    'Two orientation families mark all5 internal verticals and3 internal horizontals, binding line counts to dimension counts while retaining the black outerframe. Misread5x3 scaffold lines as6x4 cell intervals, at correct side4.',
    'Old Plane346 considered only arc/area cancellation and saved no candidate/API. New target is grid line-versus-interval correspondence; dove contour and all arcs/fill remain untouched. This is a distinct count-to-length mechanism with actual5/3 source lines and exact wrong dimensions20x12, not whole-dove salience or an arc recolor.')
}
for q,(name,wrong,mechanism,difference) in specs.items():
    root=OWN/q/name;root.mkdir(parents=True,exist_ok=True)
    ctx=adapter.inspect_question(q)
    assert ctx==read(OWN/q/'context.json'),'Context drift'
    save(root/'context.json',ctx)
    actions=[];roles=[]
    if q=='Plane251':
        for target in ['grid16','grid25','grid35','grid44','grid70','grid76']:
            actions.append(style(ctx,target));roles.append({'target':target,'role':('Side2 internal triangle open V, area4 unit triangles.' if target not in ['grid70','grid76'] else 'Side1 actual smallest triangle open V, the formal area1 exemplar.'),'source_geometry':next(o['geometry'] for o in ctx['objects'] if o['id']==target)})
    elif q=='Plane291':
        for target,start,end,col,role in [('gray0',0,1/3,'#DC2626','Actual full left side length1, source for height transfer.'),('half_divider',None,None,'#DC2626','Actual center-bottom height1/2, target of full-side transfer.'),('rectangle',.5,.625,'#2563EB','Upper-right half of long side, length1; horizontal base comparator.'),('gray1',0,1/3,'#2563EB','Small gray triangle bottom base, actual length1; genuinely equal to blue upper span.')]:
            actions.append(style(ctx,target,start,end,col));roles.append({'target':target,'role':role})
    elif q=='Plane345':
        for i in range(9):
            idx=0 if i<2 else 2 if i<4 else 1
            actions.append(style(ctx,'rectangle'+str(i),idx/4,(idx+1)/4))
            roles.append({'target':'rectangle'+str(i),'edge_index':idx,'role':f'Exactly one long10cm side of congruent small rectangle{i}; '+('outer boundary exemplar.' if i<4 or i==8 else 'interior seam exemplar, deliberately not a true outer perimeter contribution.')})
    else:
        for typ,ns,col in [('v',range(1,6),'#DC2626'),('h',range(1,4),'#2563EB')]:
            for i in ns:
                target=typ+str(i);actions.append(style(ctx,target,color=col))
                roles.append({'target':target,'role':f'Interior {"vertical" if typ=="v" else "horizontal"} grid line {i}; one count member of actual {5 if typ=="v" else 3}-line family, distinct from the {6 if typ=="v" else 4} cell intervals.'})
    audit={'question_id':q,'variant_id':name,'created_at':now(),'material_difference':difference,'mechanism':mechanism,'old_history_manifest':str(OWN/'old_history_manifest.json'),'expected_wrong_answer_derived_before_calls':wrong,'no_cosmetic_retry':True,'not_a_claim_of_observed_mechanism':True}
    save(root/'design_difference_audit.json',audit)
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':'Finite material refinement; research only.','params':{'actions':actions}}
    renderer=PluginRenderer(config,adapter,{q:ctx})
    plugin=renderer.normalize(plugin)
    normalized,data,pix=renderer.render(plugin,frozen=True)
    normalized2,data2,pix2=renderer.render(plugin,frozen=True)
    assert normalized==normalized2==plugin and data==data2 and pix==pix2
    save(root/'plugin.json',plugin)
    (root/'candidate.png').write_bytes(data)
    (root/'repeat.png').write_bytes(data2)
    save(root/'render_check.json',{'checked_at':now(),'schema_default_normalization':True,'fresh_context_matches':True,'noop_formal_pixel_equal':True,'two_byte_identical_renders':True,'png_sha256':sha(root/'candidate.png'),'pixel_sha256':pix,'repeat_sha256':sha(root/'repeat.png'),'normalized_plugin_sha256':sha(root/'plugin.json')})
    save(root/'path_fingerprints.json',{t['id']:t['partial_paths'] for t in ctx['canvas']['targets'] if t['id'] in {a['target'] for a in actions}})
    design={'question_id':q,'variant_id':name,'created_at':now(),'expected_wrong_answer':wrong,'formal_correct_answer':proofs[q]['answer'],'mechanism':mechanism,'primary_math_proof':proofs[q],'marker_roles':roles,'image_path':str(root/'candidate.png'),'plugin_path':str(root/'plugin.json'),'image_sha256':sha(root/'candidate.png'),'pixel_sha256':pix,'plugin_sha256':sha(root/'plugin.json'),'difference_audit_sha256':sha(root/'design_difference_audit.json'),'source_context_sha256':sha(root/'context.json'),'approval_status':'UNREVIEWED; parent NEW independent second review required; no Pass/Collect'}
    save(root/'design.json',design)
    print(q,name,len(actions),'actions; rendered twice',flush=True)

# Runtime-only copy of the EXISTING helper. Only location bootstrap is adapted;
# payload, profile, run loop, error handling and response limits remain exact.
source=(BASE/'harness/quicktest3_isolated.py').read_text(encoding='utf-8')
old='PROJECT = Path(__file__).resolve().parents[3]'
new='sys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nimport env54\nPROJECT = env54.PROJECT'
assert source.count(old)==1
destination=OWN/'harness/quicktest3_isolated.py';destination.parent.mkdir(exist_ok=True)
destination.write_text(source.replace(old,new),encoding='utf-8')
save('harness_routing_audit.json',{'existing_helper':str(BASE/'harness/quicktest3_isolated.py'),'existing_sha256':sha(BASE/'harness/quicktest3_isolated.py'),'own_helper':str(destination),'own_sha256':sha(destination),'only_replacement':{'old':old,'new':new},'request_profile_system_prompt_loop_error_handling_unchanged':True,'strict_write_guard_before_project_imports':True})
