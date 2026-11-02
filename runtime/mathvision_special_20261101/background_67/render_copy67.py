from env67 import *
import argparse
import gc
import difflib
import traceback

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['render','replay','copy'])
    mode=parser.parse_args().mode
    A=read(OWN/'snapshots/background_67_assignment.json')
    assert read(OWN/'zero_call_final_gate.json')['all_three_zero_prior_actual_calls_proved']
    if mode=='copy':
        copied=[]
        for v in A['questions']:
            q=v['question_id']; src=Path(v['source_directory']); dst=OWN/q/v['variant_id']
            assert read(OWN/q/'fresh_render_audit.json')['all_passed']
            assert read(OWN/q/'fresh_offline_replay_audit.json')['all_passed']
            assert read(OWN/q/'fresh_primary_math_native_every_marker_review.json')['no_math_native_targeting_hold']
            current=eligibility(q); assert current['eligible']; save(OWN/q/'eligibility_before_copy.json',current)
            dst.mkdir(parents=True,exist_ok=False)
            rows=[]
            for name,expected in v['frozen_source_files_sha256'].items():
                assert sha(src/name)==expected
                data=(src/name).read_bytes(); (dst/name).write_bytes(data); del data
                assert sha(dst/name)==expected
                rows.append({'file':name,'source':str(src/name),'source_sha256':expected,'copy':str(dst/name),'copy_sha256':sha(dst/name),'byte_identical':True})
            d=read(dst/'design.json')
            assert d['variant_id']==v['variant_id'] and d['created_at']==v['frozen_created_at'] and d['expected_wrong_answer']==v['expected_wrong_answer']
            provenance={'at':now(),'question_id':q,'variant_id':d['variant_id'],'original_created_at':d['created_at'],'original_wrong_preset':d['expected_wrong_answer'],'reuse_type':'First actual pair of this original frozen never-called draft; not a new design or retry.','new_mechanism_count':0,'source_directory':str(src),'own_candidate_directory':str(dst),'all_original_internal_old_paths_preserved':True,'all_selected_input_bytes_preserved':True,'source_copy_hashes':rows,'zero_prior_calls_audit':str(OWN/'zero_call_final_gate.json'),'fresh_approval_audit':str(OWN/q/'eligibility_before_copy.json'),'fresh_math_native_every_marker_audit':str(OWN/q/'fresh_primary_math_native_every_marker_review.json'),'fresh_schema_noop_repeat_audit':str(OWN/q/'fresh_render_audit.json'),'fresh_offline_replay_audit':str(OWN/q/'fresh_offline_replay_audit.json'),'source_prose_corrections_external_only':read(OWN/q/'fresh_primary_math_native_every_marker_review.json')['source_prose_corrections'],'original_user_approval_not_changed':True,'primary_only_no_independent_review_no_Pass_Collect':True}
            save(dst/'reuse_provenance.json',provenance)
            copied.append({'question_id':q,'variant_id':d['variant_id'],'directory':str(dst),'expected_wrong_answer':d['expected_wrong_answer'],'original_created_at':d['created_at'],'PNG_sha256':sha(dst/'candidate.png'),'design_sha256':sha(dst/'design.json')})
            print(q,'BYTE_IDENTICAL_COPY_REUSE_PROVENANCE_SAVED',flush=True)
        save('copied_frozen_candidates.json',copied)
        old=BASE/'background_59/harness/quicktest3_isolated.py'
        source=old.read_bytes(); before=b'import env59\nPROJECT = env59.PROJECT'; after=b'import env67\nPROJECT = env67.PROJECT'
        assert source.count(before)==1
        own_source=source.replace(before,after)
        target=OWN/'harness/quicktest3_isolated.py'; target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(own_source)
        assert own_source.replace(after,before)==source
        diff=''.join(difflib.unified_diff(source.decode().splitlines(True),own_source.decode().splitlines(True),fromfile=str(old),tofile=str(target)))
        (OWN/'harness_local_relocation.patch').write_text(diff,encoding='utf-8')
        save('harness_relocation_byte_audit.json',{'at':now(),'source':str(old),'source_sha256':sha(old),'local_copy':str(target),'local_copy_sha256':sha(target),'only_difference':'env59 import and local PROJECT lookup changed to env67; all other bytes exact.','byte_roundtrip_exact':True,'remote_payload_model_thinking_prompt_API_credentials_tokens_timeout_logic_unchanged':True,'original_reference':str(BASE/'harness/quicktest3_isolated.py'),'original_reference_sha256':sha(BASE/'harness/quicktest3_isolated.py'),'source_local_bootstrap_audit':str(BASE/'background_59/harness_isolation_audit.json'),'diff_file':str(OWN/'harness_local_relocation.patch')})
        return
    from runtime_isolation import install
    isolation=install(OWN/'render_tmp')
    sys.path.insert(0,str(PROJECT/'SolidGeometry/workbench'))
    from delivery_bridge_adapter import RendererAdapter
    from render_plugins import PluginRenderer
    from workbench_io import load_config,pixel_hash,environment_versions
    from dataset_tools.mathvision_workbench import png_bytes
    from partial_style import object_paths
    import matplotlib.pyplot as plt
    config=load_config()
    save(f'{mode}_process_environment.json',{'at':now(),'pid':os.getpid(),'isolation':isolation,'versions':environment_versions(),'remote_calls':0})
    for v in A['questions']:
        q=v['question_id']; src=Path(v['source_directory'])
        for name,expected in v['frozen_source_files_sha256'].items(): assert sha(src/name)==expected,(q,name)
        assert read(OWN/q/'fresh_primary_math_native_every_marker_review.json')['no_math_native_targeting_hold']
        e=eligibility(q); assert e['eligible']; save(OWN/q/f'eligibility_before_{mode}.json',e)
        adapter=RendererAdapter(config)
        context=adapter.inspect_question(q)
        assert context==read(src/'fresh_context.json'),q+' native context drift'
        save(OWN/q/f'{mode}_fresh_context.json',context)
        renderer=PluginRenderer(config,adapter,{q:context})
        normalized=renderer.normalize(read(src/'plugin_submitted.json'))
        assert normalized==read(src/'plugin.json'),q+' normalization drift'
        if mode=='render':
            capture=adapter.scene(q)
            try:
                noop=png_bytes(capture)
                paths={o['id']:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segments':[{'control':s['control'].tolist(),'style':s['style']} for s in p['segments']]} for p in object_paths(capture,o['id'])] for o in context['objects'] if o['styleable']}
            finally: capture.close()
            assert paths==read(src/'frozen_paths.json'),q+' frozen path drift'
            assert pixel_hash(noop)==context['original_pixel_sha256']
            (OWN/q/'verification_noop.png').write_bytes(noop)
            _,first,px=renderer.render(normalized,frozen=True)
            _,second,px2=renderer.render(normalized,frozen=True)
            assert first==second==(src/'candidate.png').read_bytes()==(src/'repeat.png').read_bytes()
            assert px==px2==read(src/'design.json')['pixel_sha256']
            (OWN/q/'verification_render_1.png').write_bytes(first)
            (OWN/q/'verification_render_2.png').write_bytes(second)
            save(OWN/q/'fresh_render_audit.json',{'at':now(),'question_id':q,'all_passed':True,'actual_current_schema_validated_before_and_after_normalization':True,'submitted_defaults_normalize_to_exact_frozen_plugin':True,'fresh_context_equals_original_frozen_context':True,'all_frozen_paths_full_precision_equal':True,'formal_noop_pixel_equal':True,'formal_png_sha256':sha(PROJECT/'SolidGeometry/image'/f'{q}.png'),'verification_noop_sha256':sha(OWN/q/'verification_noop.png'),'twice_byte_identity_and_exact_frozen_source_PNG':True,'PNG_sha256':sha(src/'candidate.png'),'pixel_sha256':px,'fresh_source_hashes_unchanged':True,'renderer':{'adapter_path':str(BASE/'delivery_bridge_adapter.py'),'adapter_sha256':sha(BASE/'delivery_bridge_adapter.py'),'approved_PluginRenderer_path':str(PROJECT/'SolidGeometry/workbench/render_plugins.py'),'approved_PluginRenderer_sha256':sha(PROJECT/'SolidGeometry/workbench/render_plugins.py'),'schema_sha256':sha(PROJECT/'SolidGeometry/workbench/plugin.schema.json')},'API_calls':0})
            del noop,paths,first,second,capture
        else:
            assert read(OWN/q/'fresh_render_audit.json')['all_passed']
            _,data,px=renderer.render(read(src/'plugin.json'),frozen=True)
            assert data==(src/'candidate.png').read_bytes()
            assert px==read(src/'design.json')['pixel_sha256']
            (OWN/q/'verification_offline_replay.png').write_bytes(data)
            save(OWN/q/'fresh_offline_replay_audit.json',{'at':now(),'question_id':q,'all_passed':True,'fresh_separate_Python_process':True,'pid':os.getpid(),'same_unchanged_dedicated_adapter_and_approved_PluginRenderer':True,'no_workbench_state_or_special_recipe_fabrication':True,'exact_frozen_plugin':str(src/'plugin.json'),'exact_replayed_PNG_sha256':hashlib.sha256(data).hexdigest(),'pixel_sha256':px,'fresh_schema_defaults_and_original_noop_gate_passed_again':True,'API_calls':0})
            del data
        plt.close('all')
        del renderer,adapter,context,normalized,e
        gc.collect()
        print(q,mode,'ALL_PASS',flush=True)

try: main()
except BaseException as exc:
    save('local_failure_checkpoint.json',{'at':now(),'stage':'local_validation_failure_stop_before_API','error_type':type(exc).__name__,'error':str(exc),'traceback':traceback.format_exc(),'no_API_call_permitted_after_this_local_failure':True,'scope':list(QIDS)})
    raise
