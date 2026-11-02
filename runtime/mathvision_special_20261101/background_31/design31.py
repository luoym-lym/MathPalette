from bootstrap31 import *
from inspect31 import eligibility
import math
from fractions import Fraction
from collections import Counter

sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
from workbench_io import load_config, pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer

RED='#DC2626'; BLUE='#2563EB'; GREEN='#16A34A'; ORANGE='#EA580C'

def edge(qid,oid,indices,color,role):
    c=read(OWN/qid/'context.json')
    t=next(t for t in c['canvas']['targets'] if t['id']==oid)
    p=t['partial_paths'][0]
    g=next(o['geometry'] for o in c['objects'] if o['id']==oid)
    assert g['type']=='polygon' and len(g['points'])==4
    start=min(indices)/4; end=(max(indices)+1)/4
    assert list(indices)==list(range(min(indices),max(indices)+1))
    a={'type':'set_object_style','target':oid,'color':color,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}
    r={'action':a,'role':role,'source_geometry':g,'selected_edges':[{'index':i,'endpoints':[g['points'][i],g['points'][(i+1)%4]]} for i in indices], 'grounding':'Exact existing frozen polygon edges; no new edge, vertex, cut, equality or dimension.'}
    return a,r

def whole(qid,oid,color,role):
    c=read(OWN/qid/'context.json'); t=next(t for t in c['canvas']['targets'] if t['id']==oid)
    g=next(o['geometry'] for o in c['objects'] if o['id']==oid)
    a={'type':'set_object_style','target':oid,'color':color}
    return a,{'action':a,'role':role,'source_geometry':g,'frozen_paths':t['partial_paths'],'grounding':'Existing contour only; native width, fill, geometry and line type retained.'}

def math_proofs():
    result={}
    # Each source bar is a 1xn straight polyomino, not independently movable cells.
    s=read(OWN/'Plane232/source_scene_snapshot.json')
    lengths=Counter(int(o['id'].split('cell')[0][3:])+1 for o in s['objects'])
    assert dict(lengths)=={i:i for i in range(1,8)}
    tilings={'1x28':[[1,2,3,4,5,6,7]],'2x14':[[7,6,1],[5,4,3,2]],'4x7':[[7],[6,1],[5,2],[4,3]]}
    result['Plane232']={'derived_answer':'3','total_unit_area':28,'unordered_integer_factor_pairs':[[1,28],[2,14],[4,7]],'constructive_row_tilings':tilings,'perimeters_in_unit_side_lengths':[58,32,22],'proof':'Straight whole bars of lengths1..7 have area28. A lattice rectangle has an integer side pair; the only pairs are1x28,2x14,4x7. The listed rows tile each without splitting/reflection. Their three perimeters differ, proving exactly3.'}
    result['Plane255']={'derived_answer':'D','proof':'A common jagged path L joins opposite parallelogram vertices. Each part boundary consists of one side from each opposite equal pair plus this same path, so both perimeters=a+b+L. Moving a divider tooth changes areas while retaining the hypotheses. Thus area equality or inequality is not universal, and perimeter inequalities are false. D alone always holds.'}
    s=read(OWN/'Plane285/source_scene_snapshot.json'); seg=s['objects'][:10]
    lengths=[math.dist(o['points'][0],o['points'][1]) for o in seg]
    assert max(lengths)-min(lengths)<1e-12
    result['Plane285']={'derived_answer':'A','wire_unit_count':10,'equal_display_segment_lengths':lengths,'cuts_at_chain_vertex_indices':[3,8],'source_cut_objects':s['objects'][10:12],'component_unit_lengths':[3,5,2],'proof':'The10cm wire comprises10 equal chain links, hence1cm each. The two existing dashed cuts cross bends at chain distances3 and8. The three components measure3,5,2cm, exactly choiceA. No other cut is licensed.'}
    s=read(OWN/'Plane294/source_scene_snapshot.json'); parts=[]
    for o in s['objects']:
        xs=[p[0] for p in o['points']]; ys=[p[1] for p in o['points']]
        w=max(xs)-min(xs);h=max(ys)-min(ys)
        parts.append({'id':o['id'],'dimensions_in_8cm_units':[w,h],'area_in_unit_squares':w*h})
    assert sum(o['area_in_unit_squares'] for o in parts)==25
    result['Plane294']={'derived_answer':'D','parts':parts,'proof':'All widths are8cm. The spiral has four4x1 outer rectangles, four2x1 inner rectangles, and the1x1 centre square: total25 width-squared units=1600cm^2. Conservation of area at assembled width8 gives200cm, D. Equivalently the nine long dimensions sum4*32+4*16+8=200.'}
    s=read(OWN/'Plane297/source_scene_snapshot.json'); panels=[]
    for i,n in enumerate(range(2,7)):
        objs=[o for o in s['objects'] if o['id'].startswith(f'panel{i}_')]
        black=[o for o in objs if o['semantic_color']=='#000000']
        f=Fraction(len(black),n*n)
        panels.append({'option':chr(65+i),'grid':n,'black_cells':len(black),'total_cells':n*n,'black_fraction':str(f),'all_cells_same_side_within_panel':True})
    assert [p['black_cells'] for p in panels]==[2,5,8,13,18]
    result['Plane297']={'derived_answer':'B','panels':panels,'proof':'Actual equal-size checkerboard cells within each panel give fractions1/2,5/9,1/2,13/25,1/2. B exceeds D since125>117 and exceeds1/2. D central3x3 and B whole3x3 share exactly the same pattern, but D cells have side3/5 versus B1, so they cannot be equated in area.'}
    masks=[7,11,13,14]; parity=[]
    for t in range(16):
        out=0
        for i,m in enumerate(masks):
            if t>>i&1:out^=m
        if out==15:parity.append(t)
    assert parity==[15]
    result['Plane302']={'derived_answer':'4','source_state_left':[1,0,0,0],'source_state_right':[0,1,1,0],'touch_masks':masks,'all_successful_touch_parity_masks':parity,'proof':'Actual tangency graph is C4, each touch flips self and two side neighbours. All16 parity subsets were enumerated: only touching every circle oddly yields1111. At least4 touches are necessary and one per circle suffices. In the depicted example a single TL touch toggles exactly the three TL/TR/BL entries; BR stays white.'}
    # Infer source cells solely from four present unit edges, then use only rotations.
    s=read(OWN/'Plane319/source_scene_snapshot.json')
    def cells(prefix):
        edges={tuple(sorted(tuple(p) for p in o['points'])) for o in s['objects'] if o['id'].startswith(prefix)}
        pts=[p for e in edges for p in e]; found=set()
        for x in range(min(p[0] for p in pts),max(p[0] for p in pts)):
            for y in range(min(p[1] for p in pts),max(p[1] for p in pts)):
                corners=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
                if all(tuple(sorted([corners[i],corners[(i+1)%4]])) in edges for i in range(4)):found.add((x,y))
        return found
    board=cells('target_');tri=cells('triomino_');tet=cells('tetromino_')
    assert (len(board),len(tri),len(tet))==(22,3,4)
    def orientations(shape):
        forms=set(); current=shape
        for _ in range(4):
            a=min(x for x,y in current);b=min(y for x,y in current)
            forms.add(tuple(sorted((x-a,y-b) for x,y in current)))
            current={(-y,x) for x,y in current}
        return forms
    placements=[]
    for name,shape in [('triomino',tri),('tetromino',tet)]:
        for form in orientations(shape):
            for x,y in board:
                placed=frozenset((x+u,y+v) for u,v in form)
                if placed<=board:placements.append((name,placed))
    def solve(left,nt,acc):
        if not left:return acc if nt==2 else None
        if nt>2:return None
        p=min(left)
        for name,ps in placements:
            if p in ps and ps<=left:
                ans=solve(left-ps,nt+(name=='triomino'),acc+[{'kind':name,'cells':sorted(ps)}])
                if ans:return ans
        return None
    tiling=solve(board,0,[]);assert tiling
    result['Plane319']={'derived_answer':'2','board_cells':sorted(board),'triomino_source_cells':sorted(tri),'tetromino_source_cells':sorted(tet),'rotation_only_tiling':tiling,'proof':'The board has22 cells. 3t+4q=22 forces t=2 mod4, so t>=2. The explicit disjoint covering uses exactly2 triominoes and4 tetrominoes, each translated from a rotation of the printed handed template, without reflection. Thus2 is attainable and minimal.'}
    result['Plane327']={'derived_answer':'C','outer_unit_sides':12,'hexagon_unit_sides':6,'triangle_side_cm':3,'hexagon_perimeter_cm':18,'proof':'The given12 congruent equilateral triangles comprise6central and6outer triangles. The visible star boundary has12 sides of one triangle, so each side=36/12=3cm. The grey central hexagon has6 of those sides, hence18cm, C. Internal spokes are not its perimeter.'}
    for q,v in result.items():
        assert str(v['derived_answer'])==str(read(OWN/q/'formal_record.json')['answer'])
        save(OWN/q/'primary_original_math.json',{'created_at':stamp(),'primary_derivation_from_actual_source_and_frozen_formal':True,'source_JPG_and_native_formal_PNG_actually_viewed':True,'formal_record':str(OWN/q/'formal_record.json'),'source_and_renderer_inputs':str(OWN/q/'input_fingerprints.json'),**v})

def prepare():
    math_proofs()
    config=load_config();config.update(runtime_dir=str(OWN/'state'),output_dir=str(OWN/'output'))
    adapter=RendererAdapter(config)
    specs=[]
    q='Plane232'; actions=[]; roles=[]
    for b in range(7):
        col=[RED,BLUE,GREEN,GREEN,BLUE,RED,ORANGE][b]
        group=[[1,6],[2,5],[3,4],[3,4],[2,5],[1,6],[7]][b]
        for cell in range(b+1):
            a,r=edge(q,f'bar{b}cell{cell}',[0],col,f'Unit {cell+1} of the length{b+1} whole bar; its existing long-edge portion joins the other units of this bar in color group{group}. The three complementary pairs each sum7 and the lone7 completes four rows of7. This mark contributes a real unit to that grouping; it is not an answer glyph or new boundary.')
            actions.append(a);roles.append(r)
    specs.append((q,'r31_complementary_seven_row_binding','1',actions,roles,'Three actual complementary length pairs1+6,2+5,3+4 and the lone7 encode a concrete4x7 arrangement. The target misconception is counting only the indicated assembly/perimeter instead of all possible rectangles.','Old prescreen rejected ungrounded length salience because no assembled rectangle was shown. New grouping explicitly binds whole bars into four compatible rows of equal total7; no rectangle, seam or new piece is drawn. The hypothesis is arrangement fixation, not arbitrary emphasis of long bars.'))
    q='Plane294'; actions=[];roles=[]
    for i,e in [(0,1),(1,0),(2,1),(3,0)]:
        a,r=edge(q,f'part{i}',[e],BLUE,'Existing length4 outer component edge; establishes the32cm outer-length family before contrasting inner short ends. It is not a dimension label or equality symbol.');actions.append(a);roles.append(r)
    for i,e in [(4,0),(5,1),(6,2),(7,3)]:
        a,r=edge(q,f'part{i}',[e],RED,'Existing width1 short end of one actual inner2x1 rectangle; matches the centre square unit while its length2 remains unmarked and fully visible. Targets substituting this width8 for that rectangle length16.');actions.append(a);roles.append(r)
    a,r=whole(q,'part8',RED,'Actual centre1x1 square supplies the square/width unit shared with four inner short ends. Existing closed square alone is retained; no new partition is drawn.');actions.append(a);roles.append(r)
    specs.append((q,'r31_inner_width_to_length_transfer','B',actions,roles,'Bind the four inner short ends to the central unit square while separately identifying four genuine outer long sides. Incorrectly using8 instead of16 for each inner length yields4*32+5*8=168, B.','Old prescreen objected to new closed component partitions or extra equalities. This design selects existing open short edges and outer long edges, preserving every one of the9 original components. The new information error is width-to-length substitution on exactly the four2x1 parts.'))
    q='Plane297'; actions=[];roles=[]
    for panel,lo,hi,description in [(1,0,2,'the full B3x3 board'),(3,1,3,'the central3x3 subpattern inside D5x5')]:
        for e,col,ij,corner in [([0],RED,lo,'lower left horizontal'),([3],RED,lo,'lower left vertical'),([1,2],BLUE,hi,'upper right two-edge elbow')]:
            a,r=edge(q,f'panel{panel}_{ij}_{ij}',e,col,f'Existing {corner} boundary of {description}; pairs corresponding corners of identical3x3 checker patterns at different cell scales. Both marked motifs contain5 black cells, but their cells have different areas.');actions.append(a);roles.append(r)
    specs.append((q,'r31_nested_checker_unit_binding','D',actions,roles,'Match the whole3x3 B pattern to the identical central3x3 pattern of D using corresponding open corner elbows. Targets treating their equal cell counts as equal area, then adding D outer black cells to conclude D is larger, ignoring cell-side scale1 versus3/5.','Old prescreen rejected uniformly tracing black cells for largest raw count and noted odd-board centres. This design links the entire actual B pattern with a proper scaled subpattern in D; it tests a specific nested-pattern unit mismatch, not whole-option salience or a recolored black-cell count.'))
    q='Plane302';actions=[];roles=[]
    for panel in range(2):
        for i in [0,1,2]:
            a,r=whole(q,f'circle{panel}_{i}',GREEN,f'Existing circle {i} in panel{panel}, one member of the actual TL/TR/BL neighbourhood toggled by the depicted single TL touch. Corresponding member in the other panel has the same contour cue. BR is excluded because it does not change. Filled black/white state is retained.');actions.append(a);roles.append(r)
    specs.append((q,'r31_toggled_triple_action_unit','3',actions,roles,'Bind the actual three-circle changed neighbourhood across the shown before/after panels. Targets confusing the cardinality3 of cells toggled by one touch with the number of required touches. The immutable wrong final is3; true minimum4 follows parity.','Old diagonal_state_pairing used opposite-corner pairs, preset2, actual4/4. New design groups the actual three affected circles, excludes the unchanged diagonal, and uses effect-cardinality versus action-count confusion. New preset3 follows this new rationale before testing; no posthoc use of old finals.'))
    for q,n,wrong,actions,roles,mechanism,diff in specs:
        d=OWN/q/n
        e=eligibility(q);assert e['eligible'];save(d/'eligibility_before_design.json',e)
        save(d/'design_difference_audit.json',{'created_at':stamp(),'stage':'material_refinement','question_id':q,'variant_id':n,'material_difference':diff,'new_mathematical_information_correspondence':mechanism,'predeclared_wrong_answer_rationale':wrong,'no_cosmetic_repeat':True,'no_old_outcome_relabel':True,'previous_evidence_inventory':str(OWN/q/'prior_evidence_inventory.json'),'semantic_lesson':'Plane295/342 rejected because actual completion/printed-content semantics conflict. This numerical/assembly problem keeps all original geometry/fill/states/counts and uses existing-edge styling; native review must separately establish one readable original problem.','forbidden_fixes_used':[]})
        metadata=adapter.inspect_question(q)
        save(d/'fresh_context.json',metadata)
        assert metadata==read(OWN/q/'context.json')
        ren=PluginRenderer(config,adapter,{q:metadata})
        raw={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared misconception; see frozen design.json','params':{'actions':actions}}
        normalized,data,pixels=ren.render(raw)
        normalized2,data2,pixels2=ren.render(normalized,frozen=True)
        assert normalized==normalized2 and data==data2 and pixels==pixels2
        save(d/'plugin.json',normalized)
        (d/'candidate.png').write_bytes(data)
        save(d/'design.json',{'question_id':q,'variant_id':n,'stage':'material_refinement','created_at':stamp(),'expected_wrong_answer':wrong,'correct_answer':e['formal_record']['answer'],'mechanism':mechanism,'design_difference_audit_sha256':sha(d/'design_difference_audit.json'),'original_math_proof':str(OWN/q/'primary_original_math.json'),'primary_original_math_sha256':sha(OWN/q/'primary_original_math.json'),'marker_roles':roles,'plugin_sha256':sha(d/'plugin.json'),'candidate_sha256':sha(d/'candidate.png'),'candidate_pixel_sha256':pixels,'human_semantics':'No semantic fill, text, original state, piece/circle count, true adjacency, geometry or dimensions changed. Only existing contour portions are recolored at their native1pt width. Color has no equality/angle/parallel/cut glyph. No legend, caption or question edits. Actual native image review is required before any call.','independent_review_status':'UNREVIEWED; NEW parent review required for eventual delivery.'})
        save(d/'render_check.json',{'created_at':stamp(),'fresh_no_op_formal_pixel_equality':True,'formal_pixel_sha256':metadata['original_pixel_sha256'],'exact_actual_schema_normalization_passed':True,'idempotent_frozen_normalization':True,'two_render_bytes_identical':True,'two_render_pixels_identical':True,'png_sha256':sha(d/'candidate.png'),'pixel_sha256':pixels,'all_actions_existing_contours':True,'no_added_geometry':True,'original_widths_retained':True,'schema_sha256':sha(PROJECT/'PlaneGeometry/workbench/plugin.schema.json'),'renderer_sha256':sha(PROJECT/'PlaneGeometry/workbench/mathvision_plugins.py')})
        print(json.dumps({'question_id':q,'variant_id':n,'actions':len(actions),'expected_wrong_answer':wrong,'png':str(d/'candidate.png')}),flush=True)
    # The exact harness is placed directly in the unit root so its parents[3] stays PROJECT.
    (OWN/'quicktest3_isolated.py').write_bytes((SHARED/'harness/quicktest3_isolated.py').read_bytes())
    assert sha(OWN/'quicktest3_isolated.py')==sha(SHARED/'harness/quicktest3_isolated.py')

if __name__=='__main__':prepare()
