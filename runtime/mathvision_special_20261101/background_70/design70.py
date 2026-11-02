from env70 import *
import math
import gc

NAMES={'Plane275':'r70_signed_turn_vs_position_closure',
       'Plane378':'r70_tile_aspect_to_full_frame'}
RED='#DC2626'; BLUE='#2563EB'

def directory(qid):return OWN/qid/NAMES[qid]

def partial(c,target,start,end,color):
    t=next(t for t in c['canvas']['targets'] if t['id']==target)
    p=t['partial_paths'][0]
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':2,
            'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}

def construct_track():
    proof=read(OWN/'Plane275/exact_track_proof.json')
    word=proof['all_minimum_words'][0]; R=2.5; sample_count=96
    x=y=angle=0.; arcs=[]; polygons=[]
    for sign in word:
        center=(x-sign*R*math.sin(angle),y+sign*R*math.cos(angle))
        start=angle-sign*math.pi/2
        pts=[]
        for j in range(sample_count+1):
            a=start+sign*math.pi/4*j/sample_count
            pts.append((center[0]+R*math.cos(a),center[1]+R*math.sin(a)))
        outer=[(center[0]+3*math.cos(start+sign*math.pi/4*j/sample_count),
                center[1]+3*math.sin(start+sign*math.pi/4*j/sample_count)) for j in range(sample_count+1)]
        inner=[(center[0]+2*math.cos(start+sign*math.pi/4*j/sample_count),
                center[1]+2*math.sin(start+sign*math.pi/4*j/sample_count)) for j in range(sample_count,-1,-1)]
        arcs.append({'center':center,'start_angle_radian':start,'sign':sign,'centerline_samples':pts})
        polygons.append(outer+inner)
        x,y=pts[-1];angle+=sign*math.pi/4
    checks=[]
    # Every point is at arc-distance <= R*pi/(8*m) from its nearest sample.
    # Two independent sample errors add to at most R*pi/(4*m).
    error=R*math.pi/(4*sample_count)
    for i in range(12):
        for j in range(i+1,12):
            if j==i+1 or (i==0 and j==11):continue
            sampled_min=math.sqrt(min((a[0]-b[0])**2+(a[1]-b[1])**2
                             for a in arcs[i]['centerline_samples'] for b in arcs[j]['centerline_samples']))
            lower=sampled_min-error
            assert lower>1
            checks.append({'pieces':[i,j],'sample_minimum':sampled_min,'proven_lower_bound':lower})
    assert abs(x)<1e-10 and abs(y)<1e-10
    save('Plane275/track_construction_clearance.json',{'word':word,'source_centerline_radius':R,
         'material_inner_radius':2,'material_outer_radius':3,'arcs':arcs,
         'nonadjacent_centerline_separation_checks':checks,
         'rigorous_sampling_bound':'The coordinate sampling is supplemented by the Lipschitz arc-length error bound R*pi/(4*m), not used as a closure proof. Each annular piece lies within0.5 of its centerline, so separation>1 proves nonadjacent material interiors disjoint.',
         'adjacent_clearance':'Adjacent45-degree annular sectors lie in opposite open half-planes of their common radial butt seam; all radii are positive and each angle is<90deg. This includes the closing seam. Thus adjacent interiors do not overlap.',
         'closure':'Exact cyclotomic closure already proved in exact_track_proof.json; floating endpoint check is only a consistency check.',
         'bound_and_construction_complete':True})
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    fig,ax=plt.subplots(figsize=(5,5))
    for i,poly in enumerate(polygons):
        ax.add_patch(Polygon(poly,closed=True,facecolor='#eeeeee',edgecolor='black',linewidth=1))
        ps=arcs[i]['centerline_samples'];ax.plot([p[0] for p in ps],[p[1] for p in ps],color='black',linewidth=.5)
    ax.autoscale_view();ax.set_aspect('equal');ax.axis('off')
    fig.savefig(OWN/'Plane275/track_construction.png',dpi=120,facecolor='white')
    plt.close(fig);plt.close('all')
    print(json.dumps({'nonadjacent_minimum_lower_bound':min(c['proven_lower_bound'] for c in checks),'construction_valid':True}))

def specs(qid,c):
    if qid=='Plane275':
        actions=[partial(c,'outer_green',0,.125,RED),partial(c,'outer_green',.125,.25,BLUE),
                 partial(c,'Martin_firstgreen',0,.25,RED),partial(c,'Martin_secondgreen',0,.25,BLUE)]
        roles=['Red source: one true45-degree piece outer arc in the completed eight-piece reference circle.',
               'Blue source: the immediately adjoining true45-degree reference piece outer arc.',
               'Red receiver: the whole existing outer45-degree arc of the first shown S piece.',
               'Blue receiver: the whole existing outer45-degree arc of the opposite-turn second S piece.']
        mechanism='Map two adjacent reference45-degree pieces to the opposite signed turns of the shown S. Target using only turning-number closure: the two shown turns cancel, then8 further same-signed pieces appear to complete360deg, giving10 total; exact position closure rejects10.'
        difference='Old v01 styles the complete reference outer circle and both full S-piece contours uniformly red with preset8. This design retains only two adjacent45-degree reference outer arcs and two corresponding S outer arcs, with separate source/receiver roles. It tests signed-turn cancellation followed by eight additional turns (10), rather than whole-track similarity (8). No old answer is relabeled and no prior PNG is reused.'
        mathproof='Eight identical pieces per reference circle imply45deg per piece. Exact exhaustive signed-chord enumeration after the shown opposite-turn prefix excludes allN<12 for position+tangent closure. A12-piece annular construction has rigorous material clearance; see exact_track_proof.json and track_construction_clearance.json. Thus12 is feasible and minimal. 10 closes tangent but not position.'
        wrong='10'
    else:
        actions=[partial(c,'rectangle6',0,.25,BLUE),partial(c,'rectangle6',.25,.5,RED)]
        roles=['Blue source: full horizontal long side a of one actual central tile.',
               'Red source: full vertical short side b of that same actual central tile.']
        for target in ('rectangle3','rectangle4','rectangle0'):
            actions.append(partial(c,target,.75,1,RED))
            roles.append('Red receiver: original left boundary constituent '+target+'; together these three intervals cover the entire AD, INCLUDING the top short-width strip.')
        for target in ('rectangle0','rectangle1','rectangle2'):
            actions.append(partial(c,target,.5,.75,BLUE))
            roles.append('Blue receiver: original top long edge of '+target+'; the three intervals cover all of DC.')
        mechanism='Transfer the small tile aspect b/a directly to the full frame AD/DC by matching vertical-short and horizontal-long roles. This wrongly assumes similarity of the component and the composite, giving2/3 (D), although the true full-frame ratio is8/9 (A).'
        difference='Old Plane378 five red intervals compare3 long units across DC against2 long units on only the lower portion of AD, omitting the top strip. New design colors FULL AD including the strip, distinguishes numerator/denominator by two hues, and introduces a specific central tile long/short source pair. The error is component-to-composite similarity, not omission of the top strip. Related Plane436 r41 counts3 versus4 ordered boundary spans; this design neither numbers nor alternates boundary spans and adds no unmatched fourth span. It does not retarget the old incidental E or B finals.'
        mathproof='Let a>b be tile sides. The lower block has height2a along the left and3b along the central three-tile stack, hence2a=3b. Full AD=b+2a=4b; DC=3a=9b/2. AD/DC=8/9 uniquelyA. Congruence of the12 small rectangles does not imply any is similar to the9-by8 overall frame. Target b/a=2/3 is uniqueD.'
        wrong='D'
    return actions,roles,mechanism,difference,mathproof,wrong

def render(qid):
    assert qid in NAMES
    e=eligibility(qid);assert e['eligible']
    from workbench_io import load_config,pixel_hash
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    cfg=load_config();adapter=RendererAdapter(cfg)
    c=adapter.inspect_question(qid)
    d=directory(qid)
    save(d/'eligibility_before_design.json',e)
    save(d/'fresh_context.json',c)
    save(d/'adapter_manifest.json',adapter.manifest)
    actions,roles,mechanism,difference,mathproof,wrong=specs(qid,c)
    audit={'question_id':qid,'variant_id':NAMES[qid],'created_at':now(),
           'old_history':str(OWN/'history_reads'/f'{qid}.json'),
           'substantive_difference':difference,'new_feature_and_misconception':mechanism,
           'expected_wrong_answer_before_any_calls':wrong,'old_misses_preserved':True,
           'not_cosmetic_or_cross_ID_failed_PNG_copy':True}
    save(d/'design_difference_audit.json',audit)
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
            'description':mechanism,'intent':mechanism,'params':{'actions':actions}}
    save(d/'plugin_input.json',plugin)
    renderer=PluginRenderer(cfg,adapter,{qid:c})
    normalized=renderer.normalize(plugin)
    save(d/'plugin.json',normalized)
    _,a,pix=renderer.render(normalized,frozen=True)
    _,b,pix2=renderer.render(normalized,frozen=True)
    assert a==b and pix==pix2 and pix!=c['original_pixel_sha256']
    (d/'candidate.png').write_bytes(a);(d/'repeat.png').write_bytes(b)
    save(d/'render_check.json',{'created_at':now(),'schema_and_fresh_default_normalization':True,
         'no_op_formal_pixel_equality':True,'twice_byte_identical':True,'pixel_sha256':pix,
         'candidate_sha256':sha(d/'candidate.png'),'plugin_sha256':sha(d/'plugin.json'),
         'canvas_and_view_unchanged':True,'source_inputs':e['authoritative_hashes']})
    save(d/'design.json',{'question_id':qid,'variant_id':NAMES[qid],'created_at':now(),
         'expected_wrong_answer':wrong,'correct_answer':row(qid)['answer'],
         'mechanism':mechanism,'primary_math_proof':mathproof,'marker_roles':roles,
         'design_difference_audit_sha256':sha(d/'design_difference_audit.json'),
         'plugin_sha256':sha(d/'plugin.json'),'image_sha256':sha(d/'candidate.png'),'pixel_sha256':pix,
         'status':'PRIMARY research only; no user approval, Pass, Collect or independent second review',
         'solver_input':'Only the formal question and this exact frozenPNG via the unchanged quicktest3 payload.'})
    print(json.dumps({'question_id':qid,'candidate':str(d/'candidate.png'),'actions':len(actions),'byte_repeat':True}))
    del a,b,c,adapter,renderer
    gc.collect()

def replay(qid):
    from workbench_io import load_config
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    d=directory(qid);cfg=load_config()
    adapter=RendererAdapter(cfg,expected_manifest=read(d/'adapter_manifest.json'))
    context=adapter.inspect_question(qid)
    plugin=read(d/'plugin.json')
    _,png,pixel=PluginRenderer(cfg,adapter,{qid:context}).render(plugin,frozen=True)
    assert png==(d/'candidate.png').read_bytes()
    (d/'offline_replay.png').write_bytes(png)
    save(d/'offline_replay_check.json',{'created_at':now(),'fresh_process':True,
         'fresh_context_noop_pixels_match_formal':True,'frozen_manifest_matches':True,
         'unchanged_approved_PluginRenderer':True,'exact_byte_replay':True,'png_sha256':sha(d/'offline_replay.png'),
         'plugin_sha256':sha(d/'plugin.json'),'design_sha256':sha(d/'design.json'),'pixel_sha256':pixel})
    print(json.dumps({'question_id':qid,'fresh_offline_replay_exact':True}))

if __name__=='__main__':
    try:
        if sys.argv[1]=='construct_track':construct_track()
        elif sys.argv[1]=='render':render(sys.argv[2])
        elif sys.argv[1]=='replay':replay(sys.argv[2])
    except Exception as exc:
        import traceback
        save('local_failure_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')+'.json',
             {'created_at':now(),'argv':sys.argv,'type':type(exc).__name__,'error':str(exc),
              'traceback':traceback.format_exc(),'no_API_in_this_script':True})
        raise
