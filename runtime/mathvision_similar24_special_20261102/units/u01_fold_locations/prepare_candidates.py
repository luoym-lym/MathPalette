import research_core as core
rt=core.rt
import sys,json,hashlib,math
from pathlib import Path
from collections import Counter
from partial_style import object_paths

RED='#DC2626';BLUE='#2563EB'
def style(target,color,width=1.5,interval=None):
    d={'type':'set_object_style','target':target,'color':color,'linewidth_pt':width}
    if interval is not None:d['interval']=interval
    return d

def definition(qid,meta):
    byid={o['id']:o for o in meta['objects']}
    if qid=='Plane202':
        variant='u01_homologous_two_ear_types_diagonal_comparison'
        actions=[];roles=[]
        for group,x,color in [('outer',.96,RED),('inner',.34,BLUE)]:
            for sx,sy,corner in [(-1,1,'TL'),(1,1,'TR'),(-1,-1,'BL'),(1,-1,'BR')]:
                xy=[sx*x,sy*.98]
                actual=next(p for p in meta['snap_points'] if p['xy']==xy)
                actions.append({'type':'add_point','id':'ear_'+group+'_'+corner,'xy':actual['xy'],'color':color})
                roles.append({'action_index':len(actions)-1,'source':actual,'target':'o1603 / o1604 directional candidate axes',
                    'purpose':group+' ear-tip member of one four-way homologous feature group; compare feature locations with the two diagonal axes, without implying that the entire head reflects.'})
        for target,color in [('o1603',RED),('o1604',BLUE)]:
            actions.append(style(target,color));roles.append({'action_index':len(actions)-1,'source':'two distinct ear feature families','target':target,
                'purpose':'One candidate diagonal is paired with each feature-family color; tempting partial-feature direction match cannot establish full-outline overlap.'})
        preset='4';value='4 fold lines'
        mechanism='Compare all four homologous outer ear tips (red) and all four inner ear tips (blue) with the two diagonal candidate axes. Predict an overgeneralization from repeated ear-feature organization to both diagonal symmetries, adding the two diagonals to the two actual midline symmetries, hence 4. Unlike old diagonal-corner tip grouping, color groups here are anatomical feature types and each group is itself invariant under both true reflections.'
        proof='There are exactly four displayed candidate lines: x=0, y=0, y=x, y=-x. Each of the 400 upper-left head segments is copied with independent sign changes to produce all four heads. Thus reflecting the entire segment set in x=0 or y=0 preserves it. The eye point (-0.69,0.55), for example, and snout/ear geometry do not map to the same anatomical set under diagonal exchange. More decisive exhaustive segment-set comparison and an explicit positive-distance witness against each diagonal are saved in proof_calculation.json. Every segment is considered, not just the four tips. Both diagonal failures and both valid midlines exhaust the candidates. The added red tip set is {(+-0.96,+-0.98)} and blue tip set {(+-0.34,+-0.98)}; each is invariant under x and y reflection. Consequently even if these endpoint marks are intrinsic ink, both true symmetries still work. Added ink cannot repair a geometric nonoverlap; positive-distance witnesses remain outside marked tips. Unique answer remains 2.'
        semantics='All four copies of each homologous ear type receive the same color and fixed-size mark. This is essential: unlike old opposite-corner coloring, intrinsic ink is also preserved by each valid fold. Candidate fold-line colors are on the preexisting comparison guides, not a requirement to match a different animal. Full snouts, inner ears, eyes and necks remain exposed; native PNG review required.'
        difference='Old design grouped only four outer ear endpoints by opposite corners with two colors. New design introduces a second real anatomical feature family, groups each family across ALL FOUR heads, and preserves horizontal/vertical colored symmetry. This changes correspondence membership and the human material-color calculation, beyond a palette or linewidth change.'
    elif qid=='Plane238':
        variant='u01_punched_row_band_to_outer_reflection_band'
        pairs=[('o32',RED),('o31',BLUE),('o12',RED),('o8',RED),('o11',BLUE),('o9',BLUE)]
        actions=[style(t,c) for t,c in pairs]
        roles=[{'action_index':0,'source':'final grid top edge y=3','target':'original y=5 and y=1 red boundaries','purpose':'Propose the outside boundary of the punched top row as outer boundary of original row2/row5 pair; it is actually the first-fold crease and corresponds to original y=3.'},
               {'action_index':1,'source':'final grid y=2, lower edge of punched top row','target':'original y=4 and y=2 blue boundaries','purpose':'Opposite edge of the same one-cell row band; makes the wrong distance-from-fold pair concrete.'}]
        for i,(t,c) in enumerate(pairs[2:],2):
            roles.append({'action_index':i,'source':'final punched-row '+('top red' if c==RED else 'bottom blue')+' border','target':t,
                'purpose':'Existing horizontal grid edge of original row2 or row5; two open parallel boundary pairs compare reflected row-band location, with all numbers and actual fold axes intact.'})
        preset='A';value='8,11,26,29'
        mechanism='Red/blue identify the two borders of the actual punched top row in the final 3x3 packet, and pair them to the original row2/row5 bands. This targets the first-fold distance error (rows2/5 instead of3/4), while retaining the true middle-column reflection pair2/5. The resulting wrong orbit is 8,11,26,29 = A. No punch boundary, original numbered cell or intermediate cell is boxed.'
        proof='Use original coordinates x,y in [0,6], with row r from top having y in (6-r,7-r). First top-to-bottom fold is y -> 6-y; the stationary stack occupies y in [0,3]. Second left-to-right fold is x -> 6-x; stationary half occupies x in [3,6]. Final packet is translated from this to [16,19]x[0,3]. Its hole is centered (17.5,2.5), so original stationary coordinate is (4.5,2.5). The four preimages are (1.5,2.5),(4.5,2.5),(1.5,3.5),(4.5,3.5), giving rows3/4 and columns2/5, i.e. 14,17,20,23, only C. Exhaustive per-cell folding enumeration is saved. A uses rows2/5 with columns2/5; B,D,E each fail the exact orbit as enumerated. Colored existing grid edges cannot change which cells have a physical hole; even if intrinsic colored ink, the question asks only numbered cells pierced, so C remains uniquely correct.'
        semantics='Only six existing horizontal grid edges are recolored. No new grid subdivision, printed numeral change, closed cell box, physical hole, punch fill change or fold-arrow change. Existing first fold at y=3 and second fold at intermediate x=11 remain fully visible and unchanged. The colors identify two open row bands; they do not assert a new crease or cut.'
        difference='Both old designs predicted D by changing COLUMN localization (original cell15 or intermediate column4) and coloring the punch outline plus a closed cell. New design leaves punch and intermediate grid black, compares two-colored ROW BOUNDARIES, and predicts A through an independently specified rows2/5 distance-from-first-fold error. Different geometry, correspondence and preset, not a retry of either old PNG.'
    else:
        variant='u01_symbol_X_diagonals_to_central_hole_pairs'
        pairs=[('o14',RED),('o15',BLUE),('o40',BLUE),('o41',RED),('o42',RED),('o43',BLUE)]
        actions=[style(t,c) for t,c in pairs]
        roles=[]
        for i,(t,c) in enumerate(pairs):
            roles.append({'action_index':i,'source':('existing rising X stroke' if c==RED else 'existing falling X stroke'),
                'target':t,'purpose':('Color one of the TWO original symbolic X diagonals at the punch location; it is not a second hole or unfolding hinge.' if i<2 else 'One existing D hole belongs to the opposite-position pair lying on the corresponding diagonal through D center. Pair direction resembles X, but loses the actual punch distance from the free top edge.')})
        preset='D';value='D central four-hole cluster'
        mechanism='Use the two actual strokes of the source location symbol X as red/blue diagonal directions and pair them with the two opposite-position hole pairs in D. Predict D by substituting the visual X-shaped four-hole arrangement for the correct free-edge distance tracking. Source circle, paper sides, creases and all fold arrows remain black and unaltered. This directly transfers the current Plane217 two-direction/two-hole-pair comparison, with source and target roles reversed.'
        proof='Normalize the original rectangle to [0,4]x[0,2]. Bottom-to-top folding reflects y about1 and retains y in[1,2]; left-to-right reflects x about2 and retains x in[2,4]. The final packet, at drawing [12,14]x[4.7,5.7], has punch(12.25,5.45), hence normalized(2.25,1.75). Undo folds independently: x in{1.75,2.25}, y in{0.25,1.75}. B has exactly that set. A fails both reflection symmetry; C has x in{.25,3.75}; D has y in{.75,1.25}; E has both wrong x and wrong y. Thus exactly B works. All option centers/radii and symmetry mismatches are independently enumerated in proof_calculation.json. Wording expressly says hole punched AT X: X is a location symbol, not printed artwork to reproduce. Coloring its strokes cannot add physical marks to be unfolded; colored existing hole outlines identify absent-paper boundaries. The punch X and circle remain discernible and unchanged in count/position. Unique answer remains B.'
        semantics='Unlike physical colored kangaroo or paper-piece boundaries, X is explicitly a punch-location symbol in this wording. Red/blue restyles only its two existing strokes. Four original circular hole boundaries in D are colored by opposite-pair direction; their white interiors, four-hole count, centers and radii stay fixed. No physical artwork is introduced. Diagram still clearly has one punch at X and four choices of reflection orbit.'
        difference='Old C colored source punch circle and C corner holes; old D paired final free/hinge packet EDGES to D dashed axes. New design changes neither packet edges nor any axis nor punch circle. It compares the two X direction strokes with two opposite HOLE-PAIR directions. Its error is symbol-direction substitution for punch offset, rather than free edge versus hinge identification. All old PNGs remain excluded.'
    return {'question_id':qid,'variant_id':variant,'expected_wrong_answer':preset,'expected_wrong_value':value,
        'correct_answer':{'Plane202':'2','Plane238':'C','Plane461':'B'}[qid],
        'mechanism':mechanism,'primary_math_proof':proof,'marker_roles':roles,'human_semantics':semantics,
        'substantive_difference_from_all_prior_designs':difference,'created_at':rt.now(),
        'reference':'current frozen Plane217 C01; all nine current references actually viewed',
        'scope':'PRIMARY AUTHOR ONLY; new independent parent second review still required',
        'limitations':['Two observations only; no causal or general success-rate assertion.','Native original figure size and layout retained.','Not user approval or Pass/Collect.']},actions

def calculate(qid,meta):
    obs={o['id']:o['geometry'] for o in meta['objects']}
    if qid=='Plane202':
        segs=[obs['o'+str(i)]['points'] for i in range(1,1601)]
        canonical=lambda s:tuple(sorted(tuple(p) for p in s))
        original=Counter(map(canonical,segs))
        transforms={'vertical':lambda x,y:(-x,y),'horizontal':lambda x,y:(x,-y),'rising_diagonal':lambda x,y:(y,x),'falling_diagonal':lambda x,y:(-y,-x)}
        results={}
        def dist_to_segment(p,s):
            a,b=s;dx=b[0]-a[0];dy=b[1]-a[1]
            t=max(0,min(1,((p[0]-a[0])*dx+(p[1]-a[1])*dy)/(dx*dx+dy*dy)))
            return math.hypot(p[0]-a[0]-t*dx,p[1]-a[1]-t*dy)
        for name,f in transforms.items():
            mapped=Counter(canonical([f(*p) for p in s]) for s in segs)
            equal=mapped==original
            detail={'all_1600_segments_equal_as_multiset':equal,'equal_segment_count':sum((mapped&original).values())}
            if not equal:
                witness=f(-.93,.35)
                dist=min(dist_to_segment(witness,s) for s in segs)
                assert dist>.001
                detail.update(original_snout_endpoint=[-.93,.35],reflected_witness=witness,minimum_distance_to_entire_head_segment_set=dist)
            results[name]=detail
        assert results['vertical']['all_1600_segments_equal_as_multiset'] and results['horizontal']['all_1600_segments_equal_as_multiset']
        return {'all_four_displayed_lines_exhausted':True,'results':results,'unique_answer':2,
                'tip_material_color_symmetry':'both red and blue sets invariant under independent signs; original head witness near snout is away from all ear marks'}
    if qid=='Plane238':
        holes=[];cells=[]
        for r in range(1,7):
            for c in range(1,7):
                x=c-.5;y=6.5-r
                final=(max(x,6-x),min(y,6-y))
                pierced=final==(4.5,2.5)
                cell={'row':r,'column':c,'number':6*(r-1)+c,'folded_center':final,'pierced':pierced}
                cells.append(cell)
                if pierced:holes.append(cell['number'])
        assert holes==[14,17,20,23]
        choices=core.eligibility(qid)['formal_record']['choices']
        return {'all_36_cells':cells,'pierced_numbers':holes,'choices_exactly_matching':{'A':False,'B':False,'C':True,'D':False,'E':False},'unique_answer':'C'}
    correct={(x,y) for x in (1.75,2.25) for y in (.25,1.75)}
    results={}
    for letter,start,offset in [('A',19,0),('B',26,6),('C',33,12),('D',40,18),('E',47,24)]:
        centers={tuple([obs['o'+str(i)]['center'][0]-offset,obs['o'+str(i)]['center'][1]]) for i in range(start,start+4)}
        results[letter]={'centers':sorted(centers),'matches':centers==correct,'radii':[obs['o'+str(i)]['radius'] for i in range(start,start+4)]}
    assert [k for k,v in results.items() if v['matches']]==['B']
    return {'normalized_punch':[2.25,1.75],'independent_reflections':[sorted(correct)],'all_options':results,'unique_answer':'B'}

def prepare(qids):
    cfg,ad=core.adapter()
    for qid in qids:
        e=core.eligibility(qid)
        assert e['eligible'],e['reasons']
        meta=ad.inspect_question(qid)
        assert json.loads(json.dumps(meta))==rt.read(rt.OWN/qid/'context.json')
        design,actions=definition(qid,meta)
        d=rt.OWN/qid/design['variant_id']
        assert not (d/'design.json').exists(), 'Never overwrite an immutable design'
        assert not list((d/'tests').glob('quicktest3_*')), 'Never rerender a tested candidate'
        d.mkdir(parents=True,exist_ok=True)
        rt.save(d/'eligibility_before_design.json',e)
        rt.save(d/'context.json',meta)
        rt.save(d/'proof_calculation.json',calculate(qid,meta))
        plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':'Two-colour comparison of existing directional/positional information.','intent':'User-authorized current C01 style transfer.','params':{'actions':actions}}
        renderer=core.PluginRenderer(cfg,ad,{qid:meta})
        normalized=renderer.normalize(plugin)
        core.check_schema(normalized,rt.read(BRANCH/'workbench/plugin.schema.json'),rt.read(BRANCH/'workbench/plugin.schema.json'))
        rt.save(d/'plugin.json',normalized)
        n1,b1,p1=renderer.render(normalized,frozen=True)
        n2,b2,p2=renderer.render(normalized,frozen=True)
        assert n1==n2==normalized and b1==b2 and p1==p2
        (d/'candidate.png').write_bytes(b1)
        (d/'repeat.png').write_bytes(b2)
        # Save the actual paths, including full-precision interval fingerprints.
        scene=ad.scene(qid)
        try:
            scene.fig.canvas.draw()
            paths={a['target']:[{k:p[k] for k in ('id','sha256','closed')} for p in object_paths(scene,a['target'])] for a in actions if a['type']=='set_object_style'}
            rt.save(d/'path_fingerprints.json',paths)
        finally:scene.close()
        history=rt.read(rt.OWN/'history_read_audit.json')['questions'][qid]['index']
        old_hashes={g['image_sha256'] for g in history['all_saved_transport_groups_for_question']}
        h=hashlib.sha256(b1).hexdigest()
        assert h not in old_hashes,'OLD ACTUAL IMAGE MUST NOT BE RETESTED'
        rt.save(d/'history_difference_audit.json',{'all_old_designs_read':history['designs'],
            'all_old_transport_images_excluded':sorted(old_hashes),'new_candidate_sha256':h,
            'substantive_difference':design['substantive_difference_from_all_prior_designs'],
            'complete_history_read_audit':str(rt.OWN/'history_read_audit.json')})
        design.update({'image_sha256':h,'plugin_sha256':rt.sha(d/'plugin.json'),'context_sha256':rt.sha(d/'context.json'),
            'proof_calculation_sha256':rt.sha(d/'proof_calculation.json'),'frozen_before_calls':True})
        rt.save(d/'design.json',design)
        rt.save(d/'reference_transfer.json',{'current_reference':'Plane217','source_png_sha256':'dd0ec0b6f718da69f70f66b469f62ce9226c16eb25c41419b93d0fd48772a0c4',
            'source_actions_sha256':'8bee734c5a13265edba080d4e4d082a50a5babc663ff0d1ee3d3d2bca8d8f76f',
            'actual_native_source_viewed':True,'all_nine_references_viewed':True,'new_question':qid,'mechanism':design['mechanism'],
            'not_inheriting_source_option_A':True,'independent_formal_stem':e['formal_record']['question']})
        rt.save(d/'render_gates.json',{'fresh_schema':True,'default_normalization':True,'noop_pixel_equal':True,
            'same_candidate_two_byte_identical_renders':True,'image_sha256':h,'pixel_sha256':p1,'design_sha256':rt.sha(d/'design.json'),
            'fresh_context_exact_json_normalized':True,'new_independent_process_exact_replay':'PENDING','native_visual_gate':'PENDING'})
        print(qid,design['variant_id'],'preset',design['expected_wrong_answer'],'actions',len(actions),'sha',h,flush=True)

BRANCH=core.BRANCH
if __name__=='__main__':prepare(sys.argv[1:] or ['Plane202','Plane238','Plane461'])
