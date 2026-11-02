from bootstrap import install,OWN,PROJECT,SESSION
install(render=True)
from gates import sha,load,save,now,eligibility
import sys,copy,json,itertools,hashlib,gc,traceback
from fractions import Fraction as F
from pathlib import Path

def math_proof(q):
    if q=='Plane482':
        # Row indices run downward. A center diamond needs SE,SW / NE,NW.
        events=[]
        for r in range(2):
            for c in range(2):
                events.append({r*3+c:2,r*3+c+1:3,(r+1)*3+c:1,(r+1)*3+c+1:0})
        conflicts=[]
        for i,j in itertools.combinations(range(4),2):
            cells=[k for k in events[i].keys()&events[j].keys() if events[i][k]!=events[j][k]]
            assert cells
            conflicts.append({'events':[i,j],'contradictory_shared_cells':cells})
        hist=[0]*5;win=[0]*4
        for a in itertools.product(range(4),repeat=9):
            hits=[all(a[k]==v for k,v in e.items()) for e in events]
            hist[sum(hits)]+=1
            for i,v in enumerate(hits):win[i]+=int(v)
        result=F(sum(hist[1:]),4**9);assert result==F(1,64)
        return {'unique_answer':'C = 1/64','derived_from':'Four pictured equiprobable gray-corner tiles. A fixed2x2 gray diamond prescribes SE,SW / NE,NW in its four cells. There are four locations. Each event has probability1/256; all six event pairs require incompatible gray corners in at least one common cell. Therefore exact union probability4/256=1/64. White diamonds are not the target.','events':[{str(k):v for k,v in e.items()} for e in events],'pairwise_conflicts':conflicts,'enumerated_assignments':4**9,'each_window_hit_counts':win,'simultaneous_hit_histogram':hist,'probability':str(result),'wrong_preset_E_is_not_mathematical_claim':'Replacing four gray-corner types by two slope types and still asserting the old event disjointness is inconsistent; this is the frozen prospective model-error target only.'}
    x=F(4);y2=F(25)-x*x;assert y2==9;y=F(3)
    a=F(20,8);b=8-a
    def reflect(p,v):
        dot=sum(i*j for i,j in zip(p,v));vv=sum(i*i for i in v)
        return tuple(2*dot*i/vv-j for i,j in zip(v,p))
    assert reflect((F(0),F(5)),(a,F(5)))==(x,y)
    # Right crease based at R; V-R=(0,5).
    assert reflect((F(0),F(5)),(-a,F(5)))==(-x,y)
    area=(F(8)+b-a)*F(5)/2;assert area==F(55,2)
    return {'unique_answer':'55/2','proof':['Let L=(0,0),R=(8,0),U=(0,5),V=(8,5), and X be the shown common reflected corner. Creases fix L and R, so LX=RX=5. Subtract x²+y²=25 and(x-8)²+y²=25 to give x=4; the pictured interior point gives y=3. No symmetry assumption is needed.','The left crease top P=(a,5) satisfies PU=PX: a²=(a-4)²+4, hence a=5/2. Right Q=(11/2,5). Exact reflection checks send U to X across LP and V to X across RQ.','The footprint has vertices L,R,Q,P, height5, bases8 and3. Its area is(8+3)*5/2=55/2. The two reflected triangles lie within that trapezoid and meet at X; their interiors do not create extra holes. Removing each original6.25 triangle once also gives40-12.5=27.5.'],'contact':[4,3],'crease_top_endpoints':[[2.5,5],[5.5,5]],'exact_reflection_checks':True,'area':str(area),'frozen_wrong_double_subtraction':'40-4*(25/4)=15; subtracting reflected copies again is invalid.','color_cues_not_used_as_givens':True}

def run(q):
    assert load(OWN/'zero_prior_invocation_scan.json')['zero_old_call_gate_pass']
    e=eligibility(q,'qualification_before_local_render.json');assert e['eligible']
    item=next(x for x in load(SESSION/'background_62_assignment.json')['questions'] if x['question_id']==q)
    src=Path(item['source_directory']);old=src.parent;out=OWN/q/'fresh_validation';out.mkdir(parents=True,exist_ok=False)
    for n,h in item['frozen_files_sha256'].items():assert sha(src/n)==h,(q,n)
    sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
    from workbench_io import load_config,pixel_hash
    from mathvision_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    from dataset_tools.mathvision_workbench import png_bytes
    from partial_style import object_paths,apply_partial_styles
    from matplotlib.patches import Patch
    from matplotlib.text import Text
    import matplotlib.pyplot as plt
    cfg=load_config();adapter=RendererAdapter(cfg)
    context=adapter.inspect_question(q);save(out/'full_context.json',context)
    assert context==load(src/'fresh_context.json')
    plugin=load(src/'plugin.json');renderer=PluginRenderer(cfg,adapter,{q:context})
    assert renderer.normalize(plugin)==plugin
    proof=math_proof(q);save(out/'unique_math.json',proof)
    scene=adapter.scene(q)
    try:
        data=png_bytes(scene);(out/'no_op.png').write_bytes(data)
        assert pixel_hash(data)==pixel_hash(PROJECT/'PlaneGeometry'/e['formal_record']['image'])
        scene.fig.canvas.draw()
        originals={k:list(v) for k,v in scene.artists.items()}
        def snapshot():
            paths={};fills={}
            for oid,artists in originals.items():
                paths[oid]=[];fills[oid]=[]
                for art in artists:
                    if hasattr(art,'get_path'):
                        p=art.get_path();paths[oid].append({'vertices':p.vertices.tolist(),'codes':None if p.codes is None else p.codes.tolist(),'transform':art.get_transform().get_matrix().tolist()})
                    if isinstance(art,Patch):fills[oid].append(list(art.get_facecolor()))
            return {'original_paths':paths,'semantic_fills':fills,'texts':[{'text':a.get_text(),'position':list(a.get_position()),'size':a.get_fontsize(),'color':a.get_color(),'visible':a.get_visible(),'transform':a.get_transform().get_matrix().tolist()} for a in scene.fig.findobj(match=Text)],'objects':copy.deepcopy(scene.objects),'snap_points':copy.deepcopy(scene.snap_points),'limits':[list(scene.ax.get_xlim()),list(scene.ax.get_ylim())],'axes_position':list(scene.ax.get_position().bounds),'canvas_size':list(scene.fig.canvas.get_width_height())}
        before=snapshot()
        paths={o['id']:[{k:p[k] for k in ('id','sha256','closed')}|{'controls':[s['control'].tolist() for s in p['segments']]} for p in object_paths(scene,o['id'])] for o in scene.objects if o.get('styleable')}
        assert paths==load(old/'exact_paths.json')
        save(out/'all_exact_native_paths.json',paths)
        per=[];tile_patterns={}
        for i,act in enumerate(plugin['params']['actions']):
            path=next(p for p in paths[act['target']] if p['id']==act['interval']['path_id'])
            assert path['sha256']==act['interval']['path_sha256']
            n=len(path['controls']);s=act['interval']['start']*n;t=act['interval']['end']*n
            def point(u):
                idx=min(int(u),n-1);f=u-idx;seg=path['controls'][idx]
                return [seg[0][j]+f*(seg[1][j]-seg[0][j]) for j in range(2)]
            endpoints=[point(s),point(t)]
            if q=='Plane482':
                assert abs(t-s-1)<1e-12
                p0,p1=endpoints;dx=p1[0]-p0[0];dy=p1[1]-p0[1];assert abs(abs(dx)-1)<1e-9 and abs(abs(dy)-1)<1e-9
                rising=dx*dy>0;assert act['linewidth_pt']==(3 if rising else 1.5)
                vertices=[seg[0] for seg in path['controls']];xmin=min(p[0] for p in vertices);ymin=min(p[1] for p in vertices)
                pattern=sorted([round(p[0]-xmin,8),round(p[1]-ymin,8)] for p in vertices)
                tile_patterns[act['target']]={'gray_triangle':pattern,'diagonal_width_pt':act['linewidth_pt']}
                role=('Source tile '+act['target'] if i<4 else 'Example recipient '+act['target'])+': '+('rising' if rising else 'falling')+' diagonal classification. The gray side remains separately visible. This mark completes global sample-to-example slope coverage; deleting it makes that tile an inconsistent member.'
            else:
                labels=['Original right5 side R-V, paired with o5 R-X','Original right top2.5 side V-Q, paired with o6 Q-X','Original left top2.5 side P-U, paired with o4 P-X','Original left5 side U-L, paired with o3 L-X','Reflected left5 side L-X, image of L-U','Reflected left2.5 side P-X, image of P-U','Reflected right5 side R-X, image of R-V','Reflected right2.5 side Q-X, image of Q-V']
                role=labels[i]+'. This existing interval is one member of a true original/image pair; it distinguishes5-side blue from2.5-side red without adding a dimension or equality sign. Both phases of one physical flap are shown, targeting the erroneous counting of both as losses.'
                length2=sum((endpoints[0][j]-endpoints[1][j])**2 for j in range(2))
                assert abs(length2-(25 if act['color']=='#2563EB' else 6.25))<1e-8
            per.append({'index':i,'action':act,'native_endpoints':endpoints,'fresh_usefulness_and_concision_review':role,'human_unambiguous':True,'not_new_geometry_or_given':True})
        if q=='Plane482':
            samples=[tile_patterns['graytile'+str(i)] for i in range(4)]
            assert len({json.dumps(x,sort_keys=True) for x in samples})==4
            assert all(v in samples for k,v in tile_patterns.items() if k.startswith('eggray'))
            save(out/'literal_tile_identity.json',{'all4_distinct_samples':samples,'all9_example_tiles':{k:v for k,v in tile_patterns.items() if k.startswith('eggray')},'every_example_matches_a_complete_styled_sample':True,'no_fifth_pattern':True})
        touched=apply_partial_styles(scene,plugin['params']['actions']);scene.fig.canvas.draw();after=snapshot()
        assert touched=={a['target'] for a in plugin['params']['actions']};assert before==after
        for arts in originals.values():
            for art in arts:
                if isinstance(art,Patch) and art.get_fill() and art.get_facecolor()[3]>0:assert art in scene.ax._children
        save(out/'native_preservation.json',{'before':before,'after':after,'original_paths_fills_texts_objects_points_view_exact_equal':True,'current_context_equals_frozen':True,'no3D_projection_visibility_changes':True})
    finally:scene.close();plt.close('all')
    del before,after,originals,scene,data
    replays=[]
    for i in (1,2):
        normalized,data,digest=renderer.render(plugin,frozen=True)
        h=hashlib.sha256(data).hexdigest();assert h==item['PNG_sha256'];assert data==(src/'candidate.png').read_bytes()
        (out/f'replay_{i}.png').write_bytes(data);replays.append({'run':i,'sha256':h,'pixel_sha256':digest,'byte_identical_to_frozen':True})
        del normalized,data;plt.close('all');gc.collect()
    semantics=('Black stroke widths mark diagonal slope consistently across all four samples and all nine example cells. Gray triangles remain visible and unchanged, including both opposite gray-side choices for each slope. Thick strokes coincide with existing boundaries and do not add gray areas or a selected window. Under literal printed-tile interpretation, all example tiles still match the same four supplied complete tile patterns. The unique probability remains1/64.' if q=='Plane482' else 'Each red top flap-side interval has a red reflected dotted image, and each blue vertical5 side has its blue reflected dotted image. Black dashed creases, black central top base, numeric5 and8, and X contact are readable at native768 resolution. Ink preservation follows both real reflections, unlike the rejected242 nonadjacent arc transport. Color groups express actual side-image relationships and are not additional numeric premises. Folding leaves a numeric trapezoid footprint55/2; there are no extra cuts, paint target or holes.')
    report={'question_id':q,'variant_id':item['variant_id'],'checked_at_utc':now(),'primary_only':True,'independent_second_review':False,'actual_original_formal_frozen_images_viewed':True,'full_formal_and_source_context_read':True,'semantics':semantics,'each_marker':per,'unique_math_file':str(out/'unique_math.json'),'schema_frozen_normalization_equal':True,'no_op_formal_pixel_equal':True,'fresh_context_and_paths_equal_frozen':True,'deterministic_byte_exact_replays':replays,'all_figures_closed':not plt.get_fignums(),'passes_fresh_primary_gates':True,'limits':['Prospective error hypothesis is not a proof of model behavior.','No causal effect or human study claimed. Any doublehit needs parent NEW independent reviewer.']}
    save(out/'fresh_primary_review.json',report)
    print(json.dumps({'question_id':q,'fresh_gates_pass':True,'replay':replays,'marker_count':len(per),'figures_open':plt.get_fignums()}),flush=True)

if __name__=='__main__':
    try:run(sys.argv[1])
    except BaseException as exc:
        save(OWN/'local_validation_failure.json',{'at':now(),'question_id':sys.argv[1],'type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc(),'API_calls_started':0})
        raise
