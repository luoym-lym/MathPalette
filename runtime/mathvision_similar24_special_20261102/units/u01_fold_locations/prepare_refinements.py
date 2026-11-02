import prepare_candidates as p
rt=p.rt
import sys,copy

original_definition=p.definition
def interval(meta,oid,start,end):
    target=next(t for t in meta['canvas']['targets'] if t['id']==oid)
    path=target['partial_paths'][0]
    return {'path_id':path['id'],'path_sha256':path['sha256'],'start':start,'end':end,'wrap':False}

def refined(qid,meta):
    old,_=original_definition(qid,meta)
    if qid=='Plane202':
        variant='u01_paper_frame_vs_animal_symmetry'
        actions=[p.style('o0',p.RED),p.style('o1603',p.RED),p.style('o1604',p.RED)]
        old.update(variant_id=variant,expected_wrong_answer='4',expected_wrong_value='4 fold lines',
            primary_math_proof='The four displayed lines exhaust x=0,y=0,y=x,y=-x. Independent comparison of all1600 frozen animal segments as multisets gives1600 preserved segments under each horizontal/vertical reflection. A snout endpoint(-.93,.35) reflects under the two diagonals to(.35,-.93) and(-.35,.93); each is at least.033 display units from the entire unchanged animal segment set, so either diagonal fails. Full calculation is in proof_calculation.json. Only2 lines work. This plugin adds NO animal marks: all animals remain entirely unchanged black strokes. The only red physical boundary is the uniform existing square frame, which preserves both correct reflections even under intrinsic colored-edging interpretation. Red diagonal comparison guides do not change kangaroo silhouettes. Thus the exact same unique answer2 holds without assuming humans ignore colored animal ink.',
            mechanism='Pair the actual square paper outline with BOTH diagonal candidate folds in one color. Each diagonal really IS a symmetry of the square paper frame, so the comparison conveys a true partial fact. Predict4 by substituting this carrier-paper symmetry for the question-required kangaroo silhouette symmetry, adding the two highlighted diagonals to the two already valid midlines. The animals carry no new marks at all.',
            marker_roles=[{'action_index':0,'source':'actual enclosing square paper boundary o0','target':'both diagonal candidate axes o1603/o1604',
                'purpose':'Identify the carrier object whose true square symmetry is being compared; it is an existing physical boundary, not a new frame or a choice box.'},
                {'action_index':1,'source':'square paper outline','target':'existing rising diagonal o1603','purpose':'Compare an actual symmetry of the carrier square with the stronger requirement of animal overlap; tempting but insufficient partial information.'},
                {'action_index':2,'source':'square paper outline','target':'existing falling diagonal o1604','purpose':'Second true square symmetry that fails the head silhouettes; comparison distinguishes carrier symmetry from printed-animal symmetry.'}],
            human_semantics='Native kangaroos, every ear, snout, eye and neck are entirely black and unchanged. The red square frame is uniformly colored, so even intrinsic colored edging preserves both correct folds (and all square symmetries). Diagonal guide appearance is not a new animal condition. Thus no alternative material reading removes either real kangaroo fold. Only three real original objects are styled, and all three belong to the specific carrier-symmetry comparison.',
            substantive_difference_from_all_prior_designs='All old/current ear-tip designs compare features ON the animals and overgeneralize partial animal symmetry. This design removes every animal mark and changes the source entity to the carrier PAPER FRAME. The new mistake is substituting square-paper symmetry for the requested printed-animal symmetry, a distinct quantifier/object error with a true partial fact. No palette/width-only retry; new pixels and correspondence.',
            limits_of_previous_evidence='Earlier current ear-type candidate finals2,2 did not hit4; old opposite-corner ear candidate0,1 did not hit4. Neither frozen image is reused, and their wrong narratives are not counted as hits.')
    elif qid=='Plane238':
        variant='u01_punch_half_to_staggered_layer_numbers'
        actions=[p.style('o135',p.RED,1.5,interval(meta,'o135',0,.5)),
                 p.style('o135',p.BLUE,1.5,interval(meta,'o135',.5,1))]
        roles=[{'action_index':0,'source':'existing punched-hole UPPER semicircle (same single physical hole)','target':'original row3 open-L cell markers at14,16',
                'purpose':'Split the one hole contour into two directional source parts; red proposes the upper half as the top-layer cell pair.'},
               {'action_index':1,'source':'existing punched-hole LOWER semicircle (same single physical hole)','target':'original row4 open-L cell markers at21,23',
                'purpose':'Blue proposes lower half as the lower-layer pair; the intended error is a one-column stagger between layers instead of one fixed reflection orbit.'}]
        for r,c,color in [(3,2,p.RED),(3,4,p.RED),(4,3,p.BLUE),(4,5,p.BLUE)]:
            left='o'+str(c-1);top='o'+str(7+(7-r))
            for target,a,b,side in [(left,(6-r)/6,(7-r)/6,'left'),(top,(c-1)/6,c/6,'top')]:
                actions.append(p.style(target,color,1.5,interval(meta,target,a,b)))
                roles.append({'action_index':len(actions)-1,'source':'actual punched-hole '+('upper red' if color==p.RED else 'lower blue')+' half',
                    'target':f'original cell {6*(r-1)+c}, row{r} column{c}, existing {side} edge {target}',
                    'purpose':'One leg of an open L identifies the numbered existing cell without covering its numeral or adding a hole/cut. Two legs together give a concrete cell location; red/blue pairs are staggered across the two row layers.'})
        old.update(variant_id=variant,expected_wrong_answer='B',expected_wrong_value='14,16,21,23',
            mechanism='Pair the upper and lower halves of the EXISTING single punched-hole contour with two differently staggered numbered-cell pairs: red14/16 in row3, blue21/23 in row4. Predict B by incorrectly treating two source contour halves as independently shifted layer correspondences. B is invariant under a half-turn but fails the two separate mirror maps; the design targets that orientation/layer substitution. All physical cells and the one hole retain their exact positions.',
            marker_roles=roles,
            human_semantics='The two semicircle intervals partition the boundary of one unchanged filled black punch, not its interior and not two physical holes. Four open-L marks restyle existing cell grid edges; all36 numbers remain black and exposed, all fold axes/arrows unchanged. Even literal colored ink on numbered paper does not alter the set of numbered cells physically pierced. The wording asks pierced numbers, not a color-preserving picture. C remains the unique actual orbit.',
            substantive_difference_from_all_prior_designs='Old D candidates paired the full punch outline to one adjacent COLUMN cell (originalcell15 or intermediatecolumn4). Current A design compared whole ROW bands and predicted a uniform rows2/5 offset. New B design has two real punch-contour source parts, four explicit numbered receivers and a layer-dependent COLUMN stagger in rows3/4. It preserves only half-turn pairing in the false receiver set, rather than a wrong rectangular mirror orbit. The new B preset comes from these predeclared cells, not the earlier E output.',
            limits_of_previous_evidence='Current row-band candidate complete finals C,E both miss its frozenA; old originalcell candidate has an eight-number no-option answer and D, while intermediatecell candidate has one aborted request. All old/current tested PNGs are excluded.')
    else:raise ValueError(qid)
    return old,actions

p.definition=refined
if __name__=='__main__':p.prepare(sys.argv[1:] or ['Plane202','Plane238'])
