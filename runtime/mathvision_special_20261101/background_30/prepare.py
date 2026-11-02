import tools_local as t
import math
from itertools import combinations
R='#DC2626';B='#2563EB'
def read(p):return t.json.loads(p.read_text(encoding='utf-8-sig'))
def ctx(q):return read(t.HERE/q/'context.json')
def old(q):return [a for a in read(t.BASE/'exploration_report.json')['attempts'] if a['question_id']==q]
def part(q,o,a,b,c,width=1.5):
    path=read(t.HERE/q/'paths_public.json')[o][0]
    return {'type':'set_object_style','target':o,'color':c,'linewidth_pt':width,'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':a,'end':b,'wrap':False}}
def edge(q,o,c):return part(q,o,0,1,c)
def make(q,n,acts,preset,hyp,roles,proof,diff,repair):
    audit={'stage':'material_refinement','question_id':q,'variant_id':n,'created_at':t.now(),'previous_attempts':old(q),'substantive_old_new_difference':diff,'semantic_repair':repair,'new_geometric_rationale_for_preset':hyp,'expected_wrong_answer_predeclared':preset,'cosmetic_only':False,'unchanged_failed_or_aborted_repeat':False,'old_observed_answer_relabel':False,'new_information_targets':[{'action':a,'role':r} for a,r in zip(acts,roles)],'primary_only':True,'new_independent_parent_review_required':True}
    assert len(acts)==len(roles)
    t.write(t.HERE/q/(n+'_difference_preparation.json'),audit)
    t.render(q,n,acts,preset,hyp,roles,proof)
    out=t.HERE/q/n;t.write(out/'design_difference_audit.json',audit)
    objects={o['id']:o for o in ctx(q)['objects']}
    paths=read(t.HERE/q/'paths_public.json')
    t.write(out/'per_marker_geometry_audit.json',[{'index':i+1,'normalized_action':a,'role':roles[i],'source_object':objects.get(a.get('target')),'source_paths':paths.get(a.get('target')),'endpoint_proof':a.get('xy'),'appearance_only':True,'no_new_givens_or_cut':True} for i,a in enumerate(read(out/'plugin.json')['params']['actions'])])
    return out

def plane171():
    q='Plane171';areas={}
    for o in ctx(q)['objects']:
        if not o['id'].startswith('lawn'):continue
        pts=o['geometry']['points'];p=[(round(2*x),round(y/(math.sqrt(3)/2))) for x,y in pts]
        area2=abs(sum(x*p[(i+1)%len(p)][1]-y*p[(i+1)%len(p)][0] for i,(x,y) in enumerate(p)))
        areas[o['id']]=area2/2
    # Physical unit-triangle area is sqrt(3)/4; this transformed shoelace area equals its count.
    proof={'method':'Fresh integer triangular-lattice shoelace, X=2x,Y=y/(sqrt(3)/2). Each unit triangle has transformed area1.','unit_triangle_areas':areas,'unique_minimum':'lawn0 = A','targeted_error':'C has two opposing V notches; counting notches without comparing different hull/truncation areas falsely gives C.'}
    t.write(t.HERE/q/'primary_math_audit.json',proof)
    acts=[part(q,'lawn0',1/8,3/8,R),part(q,'lawn2',2/10,4/10,R),part(q,'lawn2',7/10,9/10,R)]
    make(q,'r30_opposed_notch_unit_binding',acts,'C','Match the actual inward V of A with the two opposing inward Vs of C. Predict C from counting two congruent missing unit triangles while overlooking A larger northeast truncation, rather than comparing complete areas.', ['A two-edge inward top V is the reference missing unit triangle.','C top inward V is one congruent notch, matched to A.','C bottom inward V is a second congruent notch, inviting an invalid notch-count-only comparison.'],proof,'Old v01 outlined only E and predicted E (actual A/B). New selects congruent local notch chains in A and C, compares two separated missing unit triangles, and predicts C before any new output. No old E contour is retained.','All dots and the larger A truncation remain visible; three open edge intervals, no new region or relation glyph.')

def plane206():
    q='Plane206';objects=ctx(q)['objects']
    def cells(prefix):
        seg={tuple(sorted(tuple(p) for p in o['geometry']['points'])) for o in objects if o['id'].startswith(prefix)}
        vs={p for e in seg for p in e};result=set()
        for x in range(min(p[0] for p in vs),max(p[0] for p in vs)):
            for y in range(min(p[1] for p in vs),max(p[1] for p in vs)):
                edges=[((x,y),(x+1,y)),((x,y+1),(x+1,y+1)),((x,y),(x,y+1)),((x+1,y),(x+1,y+1))]
                if all(tuple(sorted(e)) in seg for e in edges):result.add((x,y))
        return result
    source=cells('source_');orients=[]
    for r in range(4):
        p=set(source)
        for _ in range(r):p={(-y,x) for x,y in p}
        mx=min(x for x,y in p);my=min(y for x,y in p);orients.append({(x-mx,y-my) for x,y in p})
    results=[]
    for k in range(4):
        target=cells('option'+str(k)+'_');placements=[]
        for orient in orients:
            for x,y in target:
                for u,v in orient:
                    p={(a+x-u,b+y-v) for a,b in orient}
                    if p<=target and p not in placements:placements.append(p)
        covers=[[sorted(p),sorted(target-p)] for p in placements if target-p in placements]
        assert covers
        results.append({'target':sorted(target),'witness':covers[0]})
    wrong={(18,0),(18,1),(18,2),(19,0)};res=cells('option3_')-wrong
    proof={'method':'Fresh extraction of four boundary edges per cell and all four rotations of source L; exact two-copy cover for every target.','source':sorted(source),'covers':results,'unique_count':4,'greedy_wrong_first_placement':sorted(wrong),'its_nontileable_residue':sorted(res),'residue_not_L':all({(x-min(a for a,b in res),y-min(b for a,b in res)) for x,y in res}!=o for o in orients)}
    t.write(t.HERE/q/'primary_math_audit.json',proof)
    acts=[];roles=[]
    for oid in ['source_1','source_4','source_7']:
        acts.append(edge(q,oid,R));roles.append('One unit of source outer 3-unit rail, matched to a genuine three-unit exterior span at the fourth target bottom-left.')
    for oid in ['source_11','source_12']:
        acts.append(edge(q,oid,B));roles.append('One unit of source outer 2-unit foot-side span, orthogonal to the red rail; fixes a greedy corner anchor without drawing a cut.')
    for oid in ['option3_0','option3_2','option3_4']:
        acts.append(edge(q,oid,R));roles.append('Fourth target exterior lower three-unit rail; a rotated source can occupy this span, but the corresponding greedy placement leaves disconnected residue.')
    for oid in ['option3_1','option3_10']:
        acts.append(edge(q,oid,B));roles.append('Fourth target exterior bottom two-unit span corresponding to source blue side; together with red, tempts committing to the wrong initial L placement.')
    make(q,'r30_greedy_corner_residue',acts,'3','Bind both orthogonal 3-unit and 2-unit source exterior spans to the lower-left corner of the fourth target. A locally valid greedy L placement there leaves a non-L disconnected residue; incorrectly treating this first placement as forced rejects exactly this otherwise formable shape, giving 3.',roles,proof,'Old source3 rail matched a mismatching third-pattern4 rail (finals4/1 preset3). New uses an exact two-feature rotated local fit in target4, and tests failure to backtrack from a greedy anchor. The targeted error is placement/residue, not whole-span length.','All styles lie on actual exterior edges. No internal rail is colored and no closed colored contour prescribes a cut; original eight-cell grid and alternative placement remain clear.')

def plane278():
    q='Plane278';proof={'convex_concave_counts':{'A':[0,2],'B':[1,1],'C':[2,0],'D':[1,0],'E':[0,1]},'necessity':'All curved boundaries must be interior paired convex/concave seams. Omitting A/B/C/D/E leaves imbalance +2/0/-2/-1/+1, respectively. Only B can be omitted.','construction':{'lower_left':'C original','lower_right':'E half-turn','upper_left':'A clockwise90','upper_right':'D counterclockwise90'},'actual_seams':['C top with A bottom','C right with E left','D left with A right','D bottom with E top'],'unique_answer':'B','target_error':'B and E share the same lower-left straight L frame and right concavity; treating this three-side match as complete substitutability ignores B convex top.'}
    t.write(t.HERE/q/'primary_math_audit.json',proof)
    acts=[];roles=[]
    for o in ['piece1','piece4']:
        for a,b,c,role in [(0,.25,R,'Lower straight side of the B/E common square-corner frame.'),(.75,1,R,'Left straight side of the B/E common square-corner frame.'),(.25,.5,B,'Actual concave right arc shared by B and E, a third matching side.')]:
            acts.append(part(q,o,a,b,c));roles.append(o+': '+role)
    make(q,'r30_three_side_surrogate',acts,'E','Pair B and E lower-left straight L frames and concave right sides, inducing B-for-E substitution and falsely discarding E as redundant while retaining B; this ignores the mismatching convex versus straight top.',roles,proof,'Old convex B/D tops plus B/E concavity tested presetD and returned C/C, which remains a miss. New removes all D marks and every colored top arc, binds two straight external sides plus the right concavity of B/E, and predicts E from a three-side substitution error, not old observed C.','Neither B nor E is fully encircled; their different top edges remain black and fully visible. No matching-color rule is a new puzzle requirement.')

def plane286():
    q='Plane286';c=ctx(q);objs={o['id']:o['geometry']['points'] for o in c['objects'] if o.get('styleable')};p=objs['option2']
    proof={'unique_answer':'A','necessity_for_A':'Side length is2 from the given squares. The base interval[0,2] at y=0 requires one contained square to have its entire horizontal side there, hence the upright base square. The apex(1,3), outside that square, must be the other square corner. Its two adjacent exposed roof slopes +/-1 require side endpoints x=1+/-sqrt(2), outside the allowed width[0,2]; impossible.','other_constructions':{'B':'Two side2 squares at center(5,sqrt2), relative rotation45deg.','C':'Side2 diamond vertices(10,0),(10+sqrt2,sqrt2),(10,2sqrt2),(10-sqrt2,sqrt2), united with upright [9,11]x[sqrt2,2+sqrt2].','D':'Two side2 upright squares shifted(1,1).','E':'Two side2 upright squares shifted(1,0).'},'new_span_comparison':{'given_side_width':2,'C_upright_width':2,'C_diamond_width':2*math.sqrt(2),'same_true_square_side':2},'target_error':'Diagonal bounding width of rotated square compared to side bounding width of upright square; false unequal-size inference.'}
    t.write(t.HERE/q/'primary_math_audit.json',proof)
    marks=[(objs['given0'][3],R,'First reference square upper-left endpoint of a side.'),(objs['given0'][2],R,'First reference square upper-right endpoint of the same side.'),(objs['given1'][3],B,'Second equal reference square upper-left side endpoint.'),(objs['given1'][2],B,'Second equal reference square upper-right side endpoint.'),(p[5],R,'C rotated-square left extremum; red span is a diagonal, not a side.'),(p[3],R,'C rotated-square right extremum; completes the falsely matched diagonal span.'),(p[0],B,'C upright square top-left side endpoint.'),(p[1],B,'C upright square top-right side endpoint; blue span remains a side.')]
    acts=[{'type':'add_point','id':'r30_span_'+str(i),'xy':xy,'color':color} for i,(xy,color,role) in enumerate(marks)]
    make(q,'r30_diagonal_side_span',acts,'C','Pair one reference side endpoint pair with the wide lateral extrema of the rotated square inside C, and the second reference side pair with C upright top side. Predict C from falsely comparing a diagonal width2sqrt2 with side width2 as unequal square sizes.',[role for xy,color,role in marks],proof,'Old targeted B exposed short steps versus a full side, presetB and finalsD/A. New targets C and compares whole diagonal versus side through two endpoint-pair correspondences using both reference squares. No B marks or old exposed-step intervals are reused.','Only eight existing visible vertices receive point markers. No connecting span, cut, equality symbol or region is added. Underlying equal side2 construction and C arrowhead outline remain intact; native check must verify points do not obscure corners/labels.')

def plane289():
    q='Plane289';proof={'source_unit_triangle_count':7,'minimum_container':'Unique downward side4 triangle with vertices(-.5,sqrt3/2),(3.5,sqrt3/2),(1.5,-3sqrt3/2).','lower_bound':'For downward containers with top horizontal y=b, left constraint x-y/sqrt3>=a-b/sqrt3 and right x+y/sqrt3<=a+b/sqrt3. Source extremes require top b>=sqrt3/2 and minimum horizontal span4 at that top. Upright containers require side>=5; enumeration of lattice-parallel integer-side containers for sides1..3 yields none.','minimum_added':4**2-7,'old_exact_enumeration_reference':str(t.BASE/'background_12/Plane289/completion_math_audit.json'),'new_grouping':'Triangles3,4,5,6 already form a downward side2 compound triangle; triangle1 is one downward unit triangle.','wrong_count_rationale':'Counting the compound four-unit triangle as one identical piece makes the displayed inventory4 instead of7, so16-4=12. Interior seams remain black and disprove this for a human.'}
    t.write(t.HERE/q/'primary_math_audit.json',proof)
    acts=[];roles=[]
    # Side2 outer contour: triangle3 edges0 and2; triangle5 edges0 and1; triangle6 edges1 and2.
    for o,indices in [('triangle3',[0,2]),('triangle5',[0,1]),('triangle6',[1,2])]:
        for i in indices:
            acts.append(part(q,o,i/3,(i+1)/3,R,1));roles.append('One existing outer unit edge of the side2 four-triangle downward compound group; no interior seam is recolored.')
    acts.append(part(q,'triangle1',0,1,R,1));roles.append('Existing perimeter of a single downward unit triangle; paired by orientation/shape with the side2 compound group, tempting unit-scale conflation.')
    make(q,'r30_compound_unit_inventory',acts,'12','Match a downward side2 compound triangle already present in the lower cluster with one downward unit triangle above it. Predict inventory4 by treating the four-unit compound as one piece, hence16-4=12 additions rather than16-7=9.',roles,proof,'Old side5 enclosing dashed triangle was rejected outside frozen viewport before API; preset18 remains untested. New stays entirely on existing visible edges and tests unit inventory/grouping at two scales, preset12. No old guide endpoints or proposed sides are reused.','No enclosing guide, new boundary or extra piece is added. All seven original unit triangles and the three internal lower-group seams remain visible; 1pt styles preserve small scale distinctions.')

def plane307():
    q='Plane307';source={(2,4),(2,5),(1,5)}
    def orbit(p,diag=True):
        x,y=p;result={(x,y),(5-x,y),(x,5-y),(5-x,5-y)}
        return result|{(b,a) for a,b in result} if diag else result
    all_orbits=[orbit(p) for p in sorted(source)];closure=set().union(*all_orbits);hv=set().union(*(orbit(p,False) for p in source))
    assert len(closure)==24 and len(hv)==12
    proof={'method':'Fresh exact six-by-six cell action: H(x,y)=(x,5-y), V(x,y)=(5-x,y), diagonal(x,y)=(y,x). The square grid admits exactly H,V and its two diagonals as four reflection axes.','initial_cells':sorted(source),'D4_orbits':[sorted(o) for o in all_orbits],'D4_orbits_disjoint':all(not a&b for a,b in combinations(all_orbits,2)),'minimum_completion_cells':sorted(closure),'minimum_added':21,'HV_only_closure':sorted(hv),'targeted_wrong_added':9,'styled_grid_symmetry':'v3 and h3 are both identical blue1.5pt, exchanged by diagonal reflection and quarterturn; the rest of the grid remains identically black. Thus grid appearance itself preserves all four reflection axes, unlike arbitrary colored cell borders.'}
    t.write(t.HERE/q/'primary_math_audit.json',proof)
    acts=[edge(q,'v3',B),edge(q,'h3',B)]
    make(q,'r30_invariant_cross_axis_confusion',acts,'9','Group the two actual central perpendicular grid lines with identical blue styling. Predict completion using only horizontal/vertical cell mirrors, confusing the four quadrants of this cross with four axes, yielding12-3=9 rather than completing diagonal orbits.', ['Existing central vertical grid line: one member of the H/V axis cue.','Existing central horizontal grid line: second H/V cue; identical styling ensures the entire marked grid remains invariant under both diagonal reflections as well.'],proof,'Old first-pass saved no candidate because asymmetric colored cell borders would alter the design INCLUDING THE GRID. New resolves that precise objection with an identical centered cross invariant under the full D4 group and tests an axis-count/orbit error.','Exact color/width invariance under all four grid axes is checked algebraically; only existing lines styled, no new diagonal cell cut, fill or shaded cell. Three semantic gray cells remain unmodified.')

if __name__=='__main__':
    for q in t.sys.argv[1:]:globals()[q.lower()]()
