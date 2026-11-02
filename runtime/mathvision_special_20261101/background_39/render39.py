from tools39 import *
import math
from collections import defaultdict
RED='#DC2626';BLUE='#2563EB'
def key(edge):return tuple(sorted(tuple(round(v,10) for v in xy) for xy in edge))
def render(q):
    cfg,ad=adapter();e=eligibility(q);assert e['eligible'];m=ad.inspect_question(q);before=inputs(ad,q)
    sc=ad.scene(q)
    try:
        sc.fig.canvas.draw();paths={o['id']:object_paths(sc,o['id']) for o in m['objects']}
    finally:sc.close()
    actions=[];roles=[]
    def part(o,a,b,col,role):
        p=paths[o][0];n=len(p['segments']);assert 0<=a<b<=n
        ac={'type':'set_object_style','target':o,'color':col,'linewidth_pt':1.5,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':a/n,'end':b/n,'wrap':False}}
        actions.append(ac);roles.append({'action_index':len(actions)-1,'action':ac,'role':role,'source_object':next(x for x in m['objects'] if x['id']==o),'path_id':p['id'],'path_sha256':p['sha256'],'full_precision_native_controls':[s['control'].tolist() for s in p['segments']],'selected_segment_range':[a,b]})
    def point(xy,role):
        snap=next((p for p in m['snap_points'] if tuple(p['xy'])==tuple(xy)),None);assert snap,xy
        ac={'type':'add_point','id':'r39_node_'+str(len(actions)),'xy':snap['xy'],'color':RED}
        actions.append(ac);roles.append({'action_index':len(actions)-1,'action':ac,'role':role,'exact_snap_point':snap})
    numeric={}
    if q=='Plane276':
        v='r39_split_exterior_unit_to_contact';wrong='E';wrongvalue='72 cm'
        part('o0',3,4,RED,'The original full left exterior side is12cm. The actual horizontal cut divides this marked material edge into two6cm halves.')
        part('o4',3,4,RED,'One migrated lower6cm half becomes the new left exterior short edge; false transfer treats this individual half as the full original12cm unit.')
        part('o5',0,1,RED,'The other migrated upper6cm half lies at the actual internal contact seam; its original dashed status is retained. This is the second half of the original12cm material edge, not a new exterior side.')
        diff='Old exposed_cut_edge_migration selected the horizontal12cm CUT and its two exposed12cm copies and targeted adding24 without removing12; presetE, actualD60/D60 remains MISS. New design removes ALL those marks and selects a different original feature: the UNCUT left exterior12cm side, now split between a6cm outer end and a6cm hidden contact. The distinct misconception transfers the full original unit12 to EACH half, giving rectangle width12 and length24, hence72=E. No old observed error is reused (old outputs were60). New source-to-result ownership and scale mapping is substantive despite the same target letter.'
        proof='The square side is48/4=12. The actual horizontal midpoint cut gives two12x6 congruent rectangles. In the shown end-to-end assembly the long side is24 and short side6, so perimeter2(24+6)=60, D uniquely. Boundary accounting independently gives48+2*12-2*6=60. For an intrinsic-ink interpretation, translate the lower source half by(7.5,1) and upper half by(11.5,-1) in display coordinates. Source left lower edge [0,0]..[0,2] maps to x7.5,y1..3 exterior, and upper edge [0,2]..[0,4] maps to x11.5,y1..3 seam. Both red halves are conserved consistently; red does not require them each to be12. The source cut itself and new exposed cut edges are black. Dashed seam remains interior under either material or comparison reading.'
        semantics='This is physical cutting and rearrangement but a numerical perimeter question. Unlike Plane242, the exact selected ink has a consistent rigid-piece migration shown explicitly in the proof; no colored feature disappears from an exposed boundary or creates a second feasible rectangle. The contact remains dashed. Same color is no equality glyph; 12 versus6 follows the visible cut.'
        numeric={'source_side':12,'piece_sides':[12,6],'result_sides':[24,6],'correct_perimeter':60,'false_individual_half_length':12,'wrong_perimeter':72}
    elif q=='Plane280':
        v='r39_path_vertex_interval_alias';wrong='C';wrongvalue='20 cm'
        obs={o['id']:o for o in m['objects']};seq=[];counts=[]
        for k in range(7):
            a,b=obs['thick'+str(k)]['geometry']['points'];length=math.dist(a,b);n=round(length);assert abs(n-length)<1e-12
            if not seq:seq.append(a)
            else:assert math.dist(seq[-1],a)<1e-12
            for j in range(1,n+1):
                xy=[a[i]+(b[i]-a[i])*j/n for i in range(2)]
                # Use the existing frozen visible grid vertex, never a rounded generated midpoint.
                snap=min(m['snap_points'],key=lambda p:math.dist(p['xy'],xy));assert math.dist(snap['xy'],xy)<1e-12;seq.append(snap['xy'])
            counts.append(n)
        assert counts==[2,1,1,2,1,1,1] and len(seq)==10
        for k,xy in enumerate(seq):point(xy,'Ordered path unit-boundary node '+str(k+1)+' of10: '+('first endpoint; interval0 starts here' if k==0 else 'last endpoint; interval8 ends here' if k==9 else 'joins consecutive true unit intervals'+str(k-1)+' and'+str(k))+'. The marker is exactly at an already visible frozen grid vertex on the unchanged black target.')
        diff='Old unit_to_double_span colored one non-target thin grid edge and thick3 red, presetA16, rejected before API because actual native widths were both1pt and black/gray path membership was lost. This new design colors NO edge and adds no non-target mark. It marks all10 existing ordered unit-boundary nodes ON the original black9-unit route. The different hypothesis is counting vertices as intervals (10*2=20,C), not treating a two-unit span as one (16,A). The old untested image is not repeated and its membership objection is explicitly resolved.'
        proof='In source traversal order the seven original black segments have lengths2,1,1,2,1,1,1 square sides. Their sum is9. A square area4cm2 means side2cm, hence18cm=B uniquely. Splitting the two length2 runs at existing visible grid vertices yields9 intervals and10 nodes. Nodes are boundaries of intervals, not lengths; counting10 nodes as10 intervals would yield20=C. All seven target segments retain their actual black1pt strokes and all gray non-target strokes remain gray. The original executed1pt width differs from semantic2.5 metadata; this candidate never claims or changes that physical width. No extra branch, line or square is introduced.'
        semantics='Pure numerical line-length question. Ten colored dots are external vertex markers on the same existing black target, which remains an unbroken distinguishable path. They do not add graph edges or change the requested quantity to a dot count. Native inspection must verify continuity and all node spacing; no color-preservation condition is added.'
        numeric={'segment_unit_counts':counts,'unit_interval_count':9,'ordered_node_count':10,'ordered_full_precision_snap_coordinates':seq,'correct_length':18,'false_node_times_unit_length':20,'actual_target_width_pt':1,'semantic_metadata_width_pt':2.5}
    elif q=='Plane283':
        v='r39_full_height_to_short_end_units';wrong='B';wrongvalue='30 cm'
        part('rectangle3',1,2,RED,'Actual whole outer height10cm, adjacent to the unchanged10cm dashed dimension: source of the real long-side unit.')
        part('rectangle0',2,3,RED,'Top short side of the left upright small rectangle, actual5cm; recipient of the false10cm long-to-short transfer.')
        part('rectangle3',2,3,RED,'Top short side of the right upright small rectangle, also5cm; repeated recipient, making the false three-column sum10+10+10=30 concrete.')
        diff='Prior Plane283 was screened with zero saved designs/calls because whole contour emphasis added no meaningful correspondence. New three open existing edges explicitly bind the dimensioned full height to the two short end widths, leaving the actual middle10cm width and horizontal split visible. This is a long-versus-short unit transfer, not whole-outline salience or a color rename.'
        proof='Let small rectangle long side L and short side s. The two central horizontal rectangles are stacked across the whole height, so L=2s. The outer height is the long side L=10cm, hence s=5. Outer length is s+L+s=5+10+5=20cm, C uniquely. Falsely giving the two short red receivers the same numeric10 as the full-height red source makes10+10+10=30cm=B. Coloring carries no equality tick or condition and cannot override congruent rectangles and the explicit full-height dimension.'
        semantics='Numerical lengths of four congruent rectangles. Open edge color does not redefine the10cm dimension, which still spans the full outer height with unchanged dashed line and connectors. All four rectangle boundaries remain visible; no physical artwork transformation or new equality is requested.'
        numeric={'L':10,'s':5,'outer_length':20,'wrong_column_sum':30}
    elif q=='Plane323':
        v='r39_gray_unit_to_white_base_unit';wrong='24';wrongvalue='24'
        part('hatched_square0',0,1,RED,'The full bottom horizontal edge of one genuinely hatched gray8cm square: numeric unit source.')
        part('small_white0',0,1,RED,'The full bottom horizontal edge of the left white base square, actual6cm: representative receiving unit for the three equal white base squares. Other two boundaries remain black and countable.')
        diff='Old Plane323 was screened without saved design/API. New two open horizontal edge portions match a genuine8cm gray-square source to a6cm white-base receiver. This supplies a concrete incorrect unit migration into the repeated3-square base, unlike outlining the large white square or arbitrary distractor salience. No hatch line, fill or whole contour is recolored.'
        proof='The rectangle has height3*8=24 from its three stacked gray squares. Let large white side x. The bottom row consists of three white squares of equal height s, so all have side s and3s=x. Height also equals x+s. Thus x+x/3=24, x=18 and s=6 uniquely. False unit transfer8 to s gives x=3*8=24. The7 squares and all original gray hatching remain unchanged; equal color is no equal-length assertion.'
        semantics='This numerical diagram asks for a side length. Gray semantic membership is supplied by the unchanged diagonal hatching; a thin red existing boundary does not recolor a square interior or introduce a new gray square. It supplies no additional premise that red sides are equal.'
        numeric={'total_height':24,'base_small_side':6,'large_white_side':18,'wrong_transferred_base_unit':8,'wrong_large_side':24}
    elif q=='Plane428':
        v='r39_growth_flanks_and_consumed_contacts';wrong='4026';wrongvalue='4026 cm'
        edges={}
        for k in range(6):
            p=paths['square'+str(k)][0];assert len(p['segments'])==4
            edges[k]=[s['control'].tolist() for s in p['segments']]
        es={k:{key(x) for x in xs} for k,xs in edges.items()}
        adjacent=[(i,j) for i in range(6) for j in range(i+1,6) if es[i]&es[j]];assert adjacent==[(0,1),(1,2),(2,3),(3,4),(4,5)],adjacent
        for k in [2,4]:
            inc=es[k]&es[k-1];out=es[k]&es[k+1];assert len(inc)==len(out)==1
            for j,ed in enumerate(edges[k]):
                ek=key(ed)
                if ek in inc:part('square'+str(k),j,j+1,BLUE,'Actual incoming contact of added square'+str(k)+'. This original exterior edge of the previous partial chain is consumed as a shared seam; one boundary unit is removed, not exposed.')
                elif ek not in out:part('square'+str(k),j,j+1,RED,'Persistent exterior flank of added square'+str(k)+'. Along with its other red flank this gives the two-unit net growth after consuming the blue contact and replacing the forward cap. It is a real outer unit edge.')
        diff='Old Plane428 screened with no saved design/calls: styling seams alone would not specify a false recurrence. New two concrete middle-square examples each link one consumed incoming contact (blue) to two persistent exterior flanks (red). This models true net growth+2 while tempting multiplication by n without the initial+2 cap constant. No endpoint is hidden, weakened or recolored, and the given six-square perimeter14 is unchanged.'
        proof='All6 squares form a path of5 edge adjacencies, verified from exact native shared-edge sets; no other positive-length contacts exist. P6=4*6-2*5=14, matching the text. Extending the same zigzag adds one square sharing exactly one full side, hence deltaP=4-2=2. P2013=14+2*(2013-6)=4028, equivalently Pn=2n+2. The false answer4026 counts only2n persistent flank units and omits the two unchanged terminal cap units. The two colored examples are squares2 and4, with predecessor/successor shown; each blue incoming contact is internal in the final figure, each red flank external. Both endcaps remain full black.'
        semantics='Numerical perimeter under continuation. Existing open edge styles are growth examples, not extra squares, cuts or altered boundary ownership. Blue shared contacts remain physically internal with two cells incident; the black complete silhouette and given14 make the target unambiguous.'
        numeric={'square_adjacencies':adjacent,'shared_count':5,'sample_perimeter':14,'n':2013,'correct_perimeter':4028,'false_growth_only_perimeter':4026}
    elif q=='Plane433':
        v='r39_shared_contact_single_deduction';wrong='29';wrongvalue='29 cm'
        contacts=defaultdict(list)
        for o in m['objects']:
            p=paths[o['id']][0];assert len(p['segments'])==4
            for j,s in enumerate(p['segments']):contacts[key(s['control'].tolist())].append((o['id'],j,s['control'].tolist(),p))
        shared=[(k,a) for k,a in contacts.items() if len(a)==2];outer=[(k,a) for k,a in contacts.items() if len(a)==1]
        assert len(shared)==11 and len(outer)==18 and all(len(a)<=2 for a in contacts.values())
        # Numeric native object IDs are not valid schema targets. Use permitted
        # fixed1pt add_line overlays on EXACT existing controls, without ID edits.
        def overlay(item,role):
            k,a=item;oid,j,control,p=a[0];assert len(control)==2
            ac={'type':'add_line','id':'r39_contact_'+str(len(actions)),'endpoints':control,'color':RED,'linestyle':'solid'}
            actions.append(ac);roles.append({'action_index':len(actions)-1,'action':ac,'role':role,'native_owners':[{'object_id':x[0],'segment_index':x[1],'path_sha256':x[3]['sha256'],'path_id':x[3]['id'],'full_precision_controls':x[2]} for x in a],'coincides_exactly_with_existing_line':True,'schema_target_constraint':'Native numeric object IDs cannot be set_object_style targets; permitted fixed1pt existing-edge overlay used; no schema/helper change.'})
        source=min(outer,key=lambda x:x[0]);overlay(source,'One true exterior unit side is the1cm side-length exemplar, paired with the same-length internal contacts. It remains an exterior side, not a subtraction record.')
        for k,item in enumerate(sorted(shared,key=lambda x:x[0])):overlay(item,'Shared contact record '+str(k+1)+' of11: exactly two adjacent original squares own this one unit segment. False arithmetic deducts it once from40; correct perimeter excludes BOTH incident side copies. No contact is drawn outside or renamed as perimeter.')
        diff='Old Plane433 was screened without a saved candidate/API because a subset of seams alone gave no unit counterpart and could cue an arbitrary omission. New design records all11 actual contacts once each and pairs them with one real outer1cm side. The specific representation error is one geometric contact record versus TWO incident side occurrences in4*10. Wrong40-11=29 is derived before tests. No original edge is moved or erased, no new closed cell is drawn, and no inner seam is claimed exterior.'
        proof='Exact native polygon-edge incidence yields10 squares,11 edges with two owners and18 exterior edges with one owner. Summing all40 side occurrences, each shared contact has contributed twice, so P=40-2*11=18cm. This is unique and can also be checked by traversing the complete outer silhouette. A single contact record is a physical one-unit segment but corresponds to two cell-side occurrences; subtracting once gives29. All red contact lines lie exactly on existing seams, and the one exterior exemplar is separately identified by its one-owner topology, not a new mathematical condition.'
        semantics='Numerical perimeter of the same ten-square union. Thin fixed1pt red overlays coincide exactly with existing grid edges; they add no cells or cuts and retain the entire black exterior outline except the one actual exterior unit counterpart. Cells remain joined. Red contact lines are internal under the same incidence topology; color does not redefine the perimeter target.'
        numeric={'cells':10,'shared_contacts':11,'exterior_units':18,'all_side_occurrences':40,'wrong_single_deduction':29,'outer_exemplar':source[0],'contact_records':[x[0] for x in sorted(shared,key=lambda x:x[0])]}
    else:raise ValueError(q)
    out=HERE/q/v;out.mkdir(exist_ok=False)
    write(out/'eligibility_before_design.json',e)
    write(out/'design_difference_audit.json',{'question_id':q,'variant_id':v,'created_at':now(),'stage':'material_refinement','before_any_API_call':True,'material_difference':diff,'not_cosmetic_or_posthoc_or_unchanged_retest':True,'prior_history_path':str(HERE/'history_read_audit.json'),'expected_wrong_answer':wrong,'independently_derived_wrong_value':wrongvalue,'primary_unique_math_proof':proof,'actual_semantics':semantics,'proposed_actions':actions})
    p={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':diff[:1000],'intent':'','params':{'actions':actions}}
    pr=PluginRenderer(cfg,ad,{q:m});norm,png,pix=pr.render(p);norm2,png2,pix2=pr.render(norm,frozen=True)
    assert norm==norm2 and png==png2 and pix==pix2 and before==inputs(ad,q)
    (out/'candidate.png').write_bytes(png);write(out/'plugin.json',norm);write(out/'context.json',m)
    write(out/'marker_geometry_audit.json',{'question_id':q,'variant_id':v,'roles':roles,'independent_numeric_audit':numeric,'all_source_geometry_text_fill_counts_unchanged':True,'native_path_binding':{o:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'controls':[s['control'].tolist() for s in p['segments']]} for p in paths[o]] for o in sorted({a['target'] for a in actions if 'target' in a})}})
    write(out/'design.json',{'question_id':q,'variant_id':v,'stage':'material_refinement','created_at':now(),'expected_wrong_answer':wrong,'expected_wrong_value':wrongvalue,'correct_answer':ad.records[q]['answer'],'formal_question':ad.records[q]['question'],'material_difference':diff,'primary_unique_math_proof':proof,'human_semantics':semantics,'marker_roles':roles,'numeric_audit':numeric,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pix,'plugin_sha256':file_hash(out/'plugin.json'),'design_difference_sha256':file_hash(out/'design_difference_audit.json'),'approval_status':'UNREVIEWED PRIMARY ONLY; parent NEW independent second review required before delivery'})
    write(out/'render_check.json',{'no_op_formal_pixel_equal':True,'schema_default_normalized':True,'twice_byte_identical_render':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pix,'design_sha256':file_hash(out/'design.json'),'frozen_inputs':before,'isolation':ISOLATION,'strict_own_root_guard_before_project_imports':True})
    print(q,v,'rendered',len(actions),'actions',flush=True)
if __name__=='__main__':
    for q in sys.argv[1:]:render(q)
