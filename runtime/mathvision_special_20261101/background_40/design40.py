from tools40 import *
import numpy as np
from partial_style import object_paths
from fractions import Fraction
from itertools import product
RED='#DC2626';BLUE='#2563EB'
def objects(q):return read(TASK/q/'context.json')['objects']
def native(q):
    p=next(x for x in AD.records[q]['runtime_dependencies'] if x.endswith('/scene.json'))
    return read(AD.branch/p)
def edge(q,ends):
    out=[o['id'] for o in objects(q) if o.get('styleable') and o['geometry']['type']=='segment' and (np.array_equal(o['geometry']['points'],ends) or np.array_equal(o['geometry']['points'],ends[::-1]))]
    assert len(out)==1,(ends,out)
    return out[0]
def paths(q,targets):
    s=AD.scene(q)
    try:
        s.fig.canvas.draw()
        return {t:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'controls':[s['control'].tolist() for s in p['segments']]} for p in object_paths(s,t)] for t in targets}
    finally:s.close()
def style(t,c=RED,interval=None):
    a={'type':'set_object_style','target':t,'color':c,'linewidth_pt':2}
    if interval:a['interval']=interval
    return a
def interval(q,t,a,b):
    p=paths(q,[t])[t][0]
    return {'path_id':p['id'],'path_sha256':p['sha256'],'start':a,'end':b,'wrap':False}
def frozen_artist_snapshot(s):
    return {'fills':[{'path':p.get_path().vertices.tolist(),'codes':None if p.get_path().codes is None else p.get_path().codes.tolist(),'color':list(p.get_facecolor()),'transform':p.get_transform().get_matrix().tolist()} for p in s.ax.patches if p.get_fill()],
            'texts':[{'text':t.get_text(),'position':list(t.get_position()),'font':t.get_fontsize(),'transform':t.get_transform().get_matrix().tolist()} for t in s.ax.texts],
            'view':[list(s.ax.get_xlim()),list(s.ax.get_ylim()),s.ax.get_aspect(),s.fig.get_size_inches().tolist()]}
def save(q,v,expected,actions,roles,mechanism,math,difference):
    d=TASK/q/v;d.mkdir(exist_ok=False)
    check=eligibility(q);assert check['eligible']
    write(d/'eligibility_before_design.json',check)
    write(d/'design_difference_audit.json',{'question_id':q,'variant_id':v,'created_at':now(),'old_history_sha256':file_hash(TASK/q/'history_audit.json'),'substantive_new_difference':difference,'new_mechanism':mechanism,'not_recolor_or_relabel':True,'old_evidence_immutable':True,'old_controls_reused_without_new_calls':[]})
    ctx=AD.inspect_question(q);write(d/'context.json',ctx)
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism[:999],'intent':mechanism[:999],'params':{'actions':actions}}
    pr=PluginRenderer(CONFIG,AD,{q:ctx});normalized=pr.normalize(plugin)
    write(d/'plugin.json',normalized)
    bound=paths(q,sorted(set(a['target'] for a in actions)))
    write(d/'marker_path_bindings.json',bound)
    frozen_before=frozen(q)
    p1,png1,pix1=pr.render(normalized);p2,png2,pix2=pr.render(normalized)
    assert png1==png2 and pix1==pix2 and p1==p2
    (d/'candidate.png').write_bytes(png1)
    s=AD.scene(q)
    try:
        s.fig.canvas.draw();before=frozen_artist_snapshot(s)
        pr.apply_actions(s,normalized);s.fig.canvas.draw();after=frozen_artist_snapshot(s)
        assert before==after,'fill/text/view changed'
    finally:s.close()
    assert frozen(q)==frozen_before
    om={o['id']:o for o in ctx['objects']}
    write(d/'render_check.json',{'question_id':q,'schema_valid':True,'normalization_idempotent':pr.normalize(normalized)==normalized,'no_op_pixel_equals_formal':True,'two_draws_byte_equal':True,'png_sha256':file_hash(d/'candidate.png'),'pixel_sha256':pix1,'frozen_inputs':frozen_before,'original_filled_paths_text_and_view_exactly_equal_after_apply':True,'frozen_artist_snapshot_sha256':canonical_hash(before),'appearance_changes':pr.appearance_changes(normalized),'isolation':ISOLATION})
    write(d/'design.json',{'question_id':q,'variant_id':v,'created_at':now(),'expected_wrong_answer':str(expected),'formal_correct_answer':AD.records[q]['answer'],'mechanism':mechanism,'primary_math_proof':math,'marker_roles':[{'index':i,'action':a,'role':role,'source_object':om[a['target']]} for i,(a,role) in enumerate(zip(normalized['params']['actions'],roles))],'candidate_png_sha256':file_hash(d/'candidate.png'),'plugin_sha256':file_hash(d/'plugin.json'),'exact_path_bindings_sha256':file_hash(d/'marker_path_bindings.json'),'difference_audit_sha256':file_hash(d/'design_difference_audit.json'),'status':'FROZEN_BEFORE_CALLS; native visual primary review still required; not independently reviewed','limitations':['No causal gain or human performance claim.','No new original control calls.','Parent must create a NEW independent review for any possible candidate.']})
    print(q,v,'preset',expected,'marks',len(actions),'sha',file_hash(d/'candidate.png'),flush=True)

if __name__=='__main__':
    q=sys.argv[1]
    if q=='Solid106':
        acts=[style('route_arc0_0'),style('route_arc0_1'),style('route_arc2_0'),style('route_arc2_1',RED,interval(q,'route_arc2_1',0,.5)),style('route_arc2_1',BLUE,interval(q,'route_arc2_1',.5,1))]
        roles=['First passage through the rear angular sector80..180 at height3.75; red100 degrees.','First passage through front sector180..240 at height3.75; red60 degrees.','Second passage through same rear sector80..180 at height11.25; red100 degrees.','Second passage through same front sector180..240 at height11.25; red60 degrees.','Remaining front sector240..300 at height11.25 belongs to complementary200-degree angular class.']
        for t in ['route_arc1_0','route_arc1_1','route_arc3_0','route_arc3_1']:
            acts.append(style(t,BLUE));g=next(o['geometry'] for o in objects(q) if o['id']==t);roles.append('Actual complementary angular-class fragment '+str(g['domain_deg'])+' at height'+str(g['center'][2])+'. Together blue appears twice over240..360 plus0..80; not an extra route.')
        math={'derivation':'Read the continuous route A to B in descending unwrapped angles240,80,-60,-280,-480, with four upward rises summing15cm. Horizontal directed progress160+140+220+200=720degrees, so length60cm. Total75cm, unique E.','angular_class_counts':{'red_80_to_240':{'per_traversal_degrees':160,'multiplicity':2},'blue_240_to_440':{'per_traversal_degrees':200,'multiplicity':2}},'wrong_derivation':'Treat each matched angular class as one reusable geometric unit rather than two visits: (160+200)/360*30+15=45cm, option A. This is a traversal-versus-angular-union mistake, not a proposed new length given.','human_uniqueness':'All route arcs, rises, front solid/back dash visibility and A/B survive. Actual route passes through both heights even where angular projections agree. No path omitted, added or moved.'}
        save(q,'r40_angular_class_revisit_binding','A',acts,roles,'Group repeated160-degree and complementary200-degree angular footprints across distinct heights, targeting counting angular union once instead of cumulative route traversal.',math,'Old initial prescreen considered same-color whole arcs but rejected because160,140,220,200 extents differ. This new construction cuts only the existing220-degree arc at its actual240-degree angular boundary, creating exact repeated160/200-degree footprint groups; no old PNG or preset was tested. Each path interval is bound before calls.')
    elif q=='Solid152':
        acts=[style('netedge3'),style('netedge4',RED,interval(q,'netedge4',7/15,1))]
        roles=['Left side spans y0..10: it contains strip height2 plus flap extension8, and shares the actual10cm measurement endpoints.','Right side of upper flap spans y2..10 only: match it visually to composite10cm side, testing transfer of total span to panel extension. The strip fold at y2 remains black and clear.']
        math={'derivation':'Let alternating band widths a,b and band height h. Full horizontal range2a+2b=26; left total a+h=10; right total b+h=7. Hence a+b=13,h=(10+7-13)/2=2,a=8,b=5. Volume8*5*2=80, unique C.','wrong_derivation':'After retaining narrow strip2 and short side5, incorrectly transfer10cm composite side to the8cm panel dimension because both red edges terminate at the flap top. Compute10*5*2=100, option D. This local endpoint/scope transfer is inconsistent with the still-readable total ranges and must be rejected by a careful human.','human_uniqueness':'Two appearance-only existing vertical sides; original folds at0 and2, outer26/10/7 measurements, six rectangular faces and every endpoint stay unchanged. Color is not an equality symbol. This is a numeric net-volume question, not a color-preserving picture transformation.'}
        save(q,'r40_composite_span_to_flap_side','D',acts,roles,'Pair a composite10cm side with only the8cm flap extension on its opposite side, targeting local measurement-scope transfer and volume100.',math,'Old prescreen proposed multiplying all three total ranges26*10*7=1820 and rejected the unstructured triple cue. This uses one explicit shared-top/local-fold correspondence and target100; it neither colors all ranges nor uses the old global product hypothesis. No prior PNG/API was saved for this question.')
    elif q=='Solid155':
        acts=[];roles=[]
        for axis,segments in [('width',[[[i,0,0],[i+1,0,0]] for i in range(5)]),('depth',[[[5,i,0],[5,i+1,0]] for i in range(3)]),('height',[[[5,3,i],[5,3,i+1]] for i in range(4)])]:
            for e in segments:acts.append(style(edge(q,e),BLUE));roles.append('Actual visible '+axis+' unit on the connected boundary walk Q->(5,0,0)->(5,3,0)->P; contributes one of5+3+4 boundary intervals, a misleading surrogate for body-diagonal cells.')
        times=sorted(set([Fraction(i,5) for i in range(1,5)]+[Fraction(i,3) for i in range(1,3)]+[Fraction(i,4) for i in range(1,4)]))
        math={'derivation':'The actual diagonal is (5t,3t,4t),0<=t<=1. Interior coordinate planes are crossed at'+str([str(t) for t in times])+'. All9 are distinct (pairwise coprime dimensions), none is an internal edge/vertex crossing. Starting cell plus9 transitions gives10.','wrong_derivation':'Count highlighted boundary-unit walk5+3+4=12 as the cells passed by the diagonal. It matches P/Q and all three dimension families but substitutes a three-segment boundary walk for the straight interior diagonal.','human_uniqueness':'Body diagonal is explicitly named in the unchanged question. Highlighted polyline visibly bends twice and is not another diagonal. No inside grid, space intersection point, diagonal or fill is added. Human can still identify the unique10 result.'}
        save(q,'r40_boundary_walk_unit_substitution','12',acts,roles,'Bind all three dimension chains into a connected P-Q boundary walk and test substituting its12 unit-edge intervals for body-diagonal cube visits.',math,'Old failed design added only the blue straight projected P-Q diagonal to induce11 projected intervals; both raw finals10. This design adds no diagonal and instead groups existing three-dimensional boundary-unit chains into a connected different walk with12 units. Geometric object, grouping and predicted count differ substantively; not a new preset on old line.')
    elif q=='Solid178':
        corners=[[[1,2,4],[2,2,4]],[[2,2,4],[2,3,4]],[[2,1,4],[2,2,4]],[[2,2,4],[3,2,4]]]
        acts=[style(edge(q,e),RED if i<2 else BLUE) for i,e in enumerate(corners)]
        roles=['True gray-cell top front boundary ending at shared vertex(2,2,4).','True gray-cell right boundary: paired red open corner identifies gray side of an actual edge-only contact.','True diagonal white-cell left boundary at the same vertex, below the gray cell in depth.','True diagonal white-cell back boundary: paired blue open corner touches gray red corner only at the top vertex. In3D the two cubes share a vertical edge, not a face.']
        cubes=list(product(range(4),repeat=3));start=(1,2,3)
        near=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))==1
        edge_near=lambda a,b:max(abs(x-y) for x,y in zip(a,b))==1 and sum(abs(x-y) for x,y in zip(a,b))<=2
        def grow(rule):
            sets=[{start}]
            for _ in range(2):sets.append(sets[-1]|{a for a in cubes for b in sets[-1] if rule(a,b)})
            return [sorted(s) for s in sets]
        true=grow(near);wrong=grow(edge_near);assert len(true[2])==17
        math={'derivation':'Source gray top face spansx1..2,y2..3,z4, so start cube lower corner(1,2,3). Synchronous face-neighbor expansion for2 days equals Manhattan distance<=2 restricted to64cubes.','face_rule_days_0_1_2':true,'correct_day2':len(true[2]),'wrong_rule':'Allow edge contacts as well as face contacts: displacement components<=1 and L1<=2 per day; corner-only contacts are still excluded.','wrong_rule_days_0_1_2':wrong,'wrong_day2':len(wrong[2]),'wrong_derivation':'Transfer the visible top-corner contact between gray and diagonal white cube into the problem neighbor relation, then consistently apply edge-or-face adjacency for two days.','human_uniqueness':'No fill or cube count changes; all four marks coincide with genuine existing grid edges and draw no connecting fake adjacency. Explicit face-only definition excludes the highlighted edge-only contact. Colors encode comparison, not changed gray state or new givens.'}
        save(q,'r40_edge_contact_to_face_neighbour',str(len(wrong[2])),acts,roles,'Pair the actual touching top corners of gray and diagonal white cubes, targeting edge-contact being counted as face-neighbour propagation.',math,'Old failed design paired two parallel x-directed edges at different depths to move the start to a front boundary, expected13, finals19/11. This keeps start fixed, uses a true shared vertical-edge contact between diagonally positioned cubes, and tests a different adjacency rule through independently enumerated two-day expansion. No old observed final is relabeled.')
