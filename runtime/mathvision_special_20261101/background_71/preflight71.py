from env71 import *
import base64
import gc
import difflib

prepared=read(OWN/'prepared_candidates.json')[0]
dest=Path(prepared['path'])
try:
    assert not (OWN/'local_failure.json').exists()
    assert sha(dest/'candidate.png')==prepared['image_sha256']
    assert sha(dest/'design.json')==prepared['design_sha256']
    eligibility_now=eligibility('Solid120')
    assert eligibility_now['eligible']
    save(dest/'eligibility_preflight.json',eligibility_now)
    old_hash_checks=[]
    for item in read(OWN/'old_evidence_full_byte_read.json'):
        actual=sha(PROJECT/item['path'])
        old_hash_checks.append({'path':item['path'],'expected':item['sha256'],'actual':actual,'unchanged':actual==item['sha256']})
    assert all(x['unchanged'] for x in old_hash_checks)
    save('old_evidence_preservation_preflight.json',old_hash_checks)
    # All request files are decoded one at a time; no image/base64 is retained.
    request_audit=[]
    matches=[]
    for path in sorted(BASE.rglob('request.json')):
        if path.is_relative_to(OWN): continue
        raw=path.read_bytes()
        item={'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw)}
        try:
            value=json.loads(raw.decode('utf-8-sig'))
            hashes=[]
            for message in value.get('messages',[]):
                content=message.get('content')
                if not isinstance(content,list): continue
                for part in content:
                    url=part.get('image_url',{}).get('url','')
                    if url.startswith('data:image/'):
                        data=base64.b64decode(url.split(',',1)[1],validate=True)
                        hashes.append(hashlib.sha256(data).hexdigest())
                        del data
            item['embedded_image_sha256']=hashes
            if prepared['image_sha256'] in hashes: matches.append(str(path))
            del value,hashes
        except (ValueError,UnicodeError,AttributeError,TypeError) as exc:
            item['read_limitation']=str(exc)
        request_audit.append(item)
        del raw
        gc.collect()
    image_audit=[]
    for path in sorted(BASE.rglob('*.png')):
        if path.is_relative_to(OWN): continue
        digest=sha(path)
        if digest==prepared['image_sha256']: matches.append(str(path))
        image_audit.append({'path':str(path),'sha256':digest})
    save('new_image_prior_call_hash_audit.json',{'at':now(),'candidate_sha256':prepared['image_sha256'],'prior_requests':request_audit,'prior_PNGs':image_audit,'exact_matches':matches,'no_exact_prior_image_or_embedded_request_found':not matches,'limitations':'Full existing runtime filesystem scan at this timestamp; no claim about undisclosed external calls or future parallel writes. Malformed/unknown requests are disclosed in per-file records.'})
    assert not matches
    install_render()
    from delivery_bridge_adapter import RendererAdapter
    from render_plugins import PluginRenderer
    from workbench_io import load_config,pixel_hash
    config=load_config()
    adapter=RendererAdapter(config)
    fresh=adapter.inspect_question('Solid120')
    plugin=read(dest/'plugin.json')
    renderer=PluginRenderer(config,adapter,{'Solid120':fresh})
    assert renderer.normalize(plugin)==plugin
    _,png,px=renderer.render(plugin,frozen=True)
    assert png==(dest/'candidate.png').read_bytes()
    (dest/'fresh_offline_replay.png').write_bytes(png)
    save(dest/'offline_replay_check.json',{'at':now(),'fresh_process':True,'fresh_native_context':True,'fresh_noop_formal_pixels_equal':True,'normalized_plugin_idempotent':True,'replay_byte_exact':True,'replay_sha256':sha(dest/'fresh_offline_replay.png'),'pixel_sha256':px,'API_calls_before':0})
    del png,fresh,renderer,adapter
    gc.collect()
    save(dest/'primary_native_review.json',{'at':now(),'review_role':'PRIMARY designer only','actual_new_PNG_individually_viewed_at768x768':True,'original_JPG_formal_PNG_and8old_scoped_PNGs_viewed':True,'every_marker':'All11 original lower-row ticks are visibly red, including the near-silhouette end ticks; the12th style is the separate existing bottom semicircle. They are the source count set and geometric receiver. No upper/middle tick is selected. No mark covers a printed number or creates a new counted tick.','legibility':'All1..11 and22..32 values and? remain black/readable. Tick placement/length and tape boundaries unchanged. The bottom arc is an existing boundary, not a new cut or route.','human_semantics':'Fixed measuring-tape numerical task. Keeping red as physical ink still preserves every printed value and the true21-unit revolution, so48 remains unique. Color is not a length-equality sign.','information_targeting':'Selected count-to-half-turn unit correspondence, with an explicit eleven-objects-versus-length error. Primary plausibility only; no claim of causal sufficiency or empirical per-mark necessity.','independent_review_required_if_doublehit':True,'candidate_sha256':prepared['image_sha256'],'design_sha256':prepared['design_sha256'],'false_relation_symbols_new_partition_new_paint_new_counted_objects':False})
    original=(BASE/'harness/quicktest3_isolated.py').read_bytes()
    old=b'PROJECT = Path(__file__).resolve().parents[3]'
    new=b'sys.path.insert(0, str(Path(__file__).resolve().parents[1]))\nimport env71\nPROJECT = env71.PROJECT'
    assert original.count(old)==1
    patched=original.replace(old,new)
    target=OWN/'harness/quicktest3_isolated.py'
    target.parent.mkdir(parents=True,exist_ok=True)
    assert not target.exists()
    target.write_bytes(patched)
    assert target.read_bytes().replace(new,old)==original
    diff=''.join(difflib.unified_diff(original.decode('utf-8').splitlines(True),patched.decode('utf-8').splitlines(True),fromfile='original isolated harness',tofile='background_71 local path relocation'))
    (OWN/'harness_local_path_only.diff').write_text(diff,encoding='utf-8')
    save('harness_isolation_audit.json',{'reference_path':str(BASE/'harness/quicktest3_isolated.py'),'reference_sha256':hashlib.sha256(original).hexdigest(),'own_sha256':sha(target),'exact_byte_roundtrip':True,'only_change':{'old':old.decode(),'new':new.decode()},'remote_payload_model_thinking_system_profile_API_credentials_tokens_timeout_logic':'byte-identical outside local PROJECT bootstrap; no overrides','diff':str(OWN/'harness_local_path_only.diff')})
    save('preflight_ready.json',{'at':now(),'candidate':prepared,'API_calls_so_far':0,'exact_prior_PNG_matches':0,'prior_request_files_scanned':len(request_audit),'prior_PNG_files_scanned':len(image_audit),'fresh_replay_exact':True,'old_frozen_evidence_unchanged':True,'ready_for_exact_runs2':True})
    print('Preflight PASS:',len(request_audit),'old requests,',len(image_audit),'PNGs; no exact candidate match; fresh replay byte-exact.',flush=True)
except BaseException as exc:
    save('local_failure.json',{'at':now(),'stage':'offline_preflight','error_type':type(exc).__name__,'error':str(exc),'stop_subsequent_calls':True,'API_calls':0})
    raise
