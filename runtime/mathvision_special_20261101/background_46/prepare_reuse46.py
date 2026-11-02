from tools46 import *
from fractions import Fraction
from itertools import product
scan=read(OWN/'full_task_api_reuse_scan_followup.json');assert scan['reuse_zero_prior_calls_supported']
oldhash={str(p):sha(p) for p in (TASK/'background_40').rglob('*') if p.is_file()}
save(OWN/'old40_readonly_baseline.json',oldhash)
for entry in ASSIGN['questions'][:2]:
    q=entry['question_id'];reuse=entry['reuse_input'];src=Path(reuse['source_directory']);dst=OWN/q/reuse['variant_id'];dst.mkdir(parents=True,exist_ok=False)
    copied=[]
    for p in sorted(src.rglob('*')):
        if not p.is_file():continue
        assert not any(x.startswith('tests') for x in p.relative_to(src).parts),'Unexpected existing test evidence'
        target=dst/p.relative_to(src);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(p.read_bytes())
        assert p.read_bytes()==target.read_bytes()
        copied.append({'source':str(p),'destination':str(target),'source_sha256':sha(p),'copy_sha256':sha(target),'byte_identical':True})
    assert all(sha(dst/name)==h for name,h in reuse['files_sha256'].items())
    e=eligibility(q);save(dst/'current_eligibility_46.json',e);assert e['eligible'],e
    before=inputs(q);save(dst/'current_source_inputs_46.json',before)
    ctx=AD.inspect_question(q);save(dst/'current_context_46.json',ctx)
    assert ctx==read(dst/'context.json'),'frozen context changed'
    plugin=read(dst/'plugin.json');pr=PluginRenderer(CONFIG,AD,{q:ctx});assert pr.normalize(plugin)==plugin
    s=AD.scene(q)
    try:
        noop,pix=scene_png(s);(dst/'noop_46.png').write_bytes(noop);assert pix==pixel_hash(AD.original_paths[q])
        s.fig.canvas.draw();sa=artist_snapshot(s);pr.apply_actions(s,plugin);s.fig.canvas.draw();sb=artist_snapshot(s);assert sa==sb
    finally:s.close()
    binds=paths(q,[a['target'] for a in plugin['params']['actions']]);assert binds==read(dst/'marker_path_bindings.json')
    replays=[]
    for i in [1,2]:
        _,b,ph=pr.render(plugin);p=dst/f'replay_46_{i}.png';p.write_bytes(b);assert b==(dst/'candidate.png').read_bytes();replays.append({'path':str(p),'png_sha256':sha(p),'pixel_sha256':ph,'byte_identical_to_frozen':True})
    design=read(dst/'design.json');om={o['id']:o for o in ctx['objects']}
    mark=[]
    for i,(a,m) in enumerate(zip(plugin['params']['actions'],design['marker_roles'])):
        assert a==m['action'] and om[a['target']]==m['source_object']
        g=om[a['target']]['geometry'];assert g['visibility']=='visible'
        mark.append({'index':i,'action':a,'actual_source_geometry':g,'source_path_binding':binds[a['target']],'specific_information_role':m['role'],'frozen_source_matches_exactly':True})
    if q=='Solid155':
        ts=sorted(set(Fraction(i,n) for n in [5,3,4] for i in range(1,n)));assert len(ts)+1==10
        ends=[m['actual_source_geometry']['points'] for m in mark]
        assert all(ends[i][1]==ends[i+1][0] for i in range(11))
        assert ends[0][0]==[0,0,0] and ends[-1][1]==[5,3,4]
        proof={'diagonal':'(5t,3t,4t), t in [0,1]','crossing_times':[str(t) for t in ts],'crossings':9,'unique_correct_answer':'10','boundary_unit_intervals':len(ends),'wrong_surrogate':'12 = 5+3+4 counts a two-bend Q-P boundary walk; it is not the requested body diagonal.','human_uniqueness':'The bends and P/Q are clear. The question explicitly says diagonal, so numeric conditions determine10 even with highlighted boundary chains.'}
    else:
        cubes=list(product(range(4),repeat=3));start=(1,2,3)
        def grow(edge):
            hist=[{start}]
            for day in range(2):
                nxt=set(hist[-1])
                for c in cubes:
                    for g in hist[-1]:
                        delta=[abs(a-b) for a,b in zip(c,g)]
                        if (max(delta)<=1 and 0<sum(delta)<=2) if edge else sum(delta)==1:nxt.add(c)
                hist.append(nxt)
            return [sorted(x) for x in hist]
        face=grow(False);edge=grow(True);assert [len(x) for x in face]==[1,6,17] and [len(x) for x in edge]==[1,14,42]
        assert face==[list(map(tuple,x)) for x in design['primary_math_proof']['face_rule_days_0_1_2']]
        proof={'seed_lower_corner':start,'gray_top_face':'x1..2,y2..3,z4, unique unchanged source fill','face_days':face,'edge_or_face_days':edge,'correct_answer':'17','wrong_preset':'42','human_uniqueness':'The two colored top-face open corners touch at(2,2,4); the cubes share vertical edge x2,y2,z3..4, no face. Face-neighbour definition excludes this contact. Neither gray seed nor any fill is changed.'}
    save(dst/'primary_pretest_revalidation_46.json',{'question_id':q,'role':'new primary revalidation; not independent second review','source_noop_pixel_matches':True,'schema_valid':True,'same_frozen_context':True,'all_actual_path_bindings_equal':True,'two_offline_replays':replays,'original_fills_text_view_equal':True,'frozen_3D_projection_visibility_inputs_unchanged':before==inputs(q),'mark_checks':mark,'independently_recomputed_math':proof,'native_image_viewing_pending_record':True,'old_primary_is_historical_only':True})
    save(dst/'reuse_provenance.json',{'question_id':q,'reuse_kind':'FIRST TEST of never-called frozen r40 input; no new design, no retry','variant_id':design['variant_id'],'frozen_created_at':design['created_at'],'expected_wrong_answer':design['expected_wrong_answer'],'copied_files':copied,'full_task_zero_prior_call_scan':str(OWN/'full_task_api_reuse_scan.json'),'scan_sha256':sha(OWN/'full_task_api_reuse_scan.json'),'noncall_parse_error_disposition':str(OWN/'full_task_api_reuse_scan_followup.json'),'scan_limitations':scan['limitations'],'prior_calls_found':0,'current_eligibility':e,'original_frozen_history_preserved':True,'source_r40_unchanged':True,'design_internal_old_paths_preserved':True,'new_test_records_will_be_separate':True})
    print(q,'exact copy/noop/schema/real paths/two byte-identical replays/math verified',flush=True)
save(OWN/'initial_source_baseline.json',{q:inputs(q) for q in IDS})
