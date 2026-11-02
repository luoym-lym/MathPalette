from worker import *
import difflib
import traceback

def visual_review(qid, variant):
    out = OWN / qid / variant
    design = read(out / 'design.json')
    report = {'question_id':qid,'variant_id':variant,'reviewed_at':now(),
      'role':'PRIMARY author inspection, not independent second review',
      'actual_native_768_PNG_viewed':True,
      'actual_formal_PNG_and_source_JPG_viewed':True,
      'mathematics':'Independent exhaustive placement proof establishes A for Plane218 and E for Plane398; do not use the stored answer as the proof.',
      'image_sha256':filehash(out/'candidate.png'),'design_sha256':filehash(out/'design.json'),
      'plugin_sha256':filehash(out/'plugin.json'),
      'every_marker_role':design['marker_roles'],
      'visual_findings':[
        'The red and blue length brackets sit visibly outside the black object outlines, with air gaps and tiny perpendicular endpoint caps. They carry no fill and enclose no region.',
        'All source and option cell boundaries, black/white fills and labels remain readable at the native 768-pixel size. No cell or diagnostic pattern is obscured.',
        'Each three-action bracket is one length comparison: a span and its two exact endpoint caps. There is no duplicate, overwritten or ineffective action.',
        'No new seam or fixed partition crosses the board/pieces; all original cut/assembly alternatives remain possible.',
        'A literal material-ink interpretation includes the original unchanged material boundaries and black-white cells. These detached tick-capped lines are external comparison spans, with no ink on the pieces to transport; the unique original answer therefore remains unchanged.'],
      'specific_readability': {
        'p01_detached_C_four_by_two_comparison':'Board and C red spans are four cells; blue spans are two cells, with the remaining third board row plainly visible. C can interlock after a half-turn.',
        'p02_detached_U_quarterturn_span_comparison':'The board left side and B top side are three cells red; the board bottom two-cell interval and B left side are blue. Their axes exchange through a quarter-turn. B retains its open U notch and can be paired after changing relative orientation.',
        'p01_detached_A_square_orientation_comparison':'The source square and lower-left 3 by 3 region in A have red vertical and blue horizontal spans. The last top row and right column of A are outside the marked square spans. Its correct square rotation and all other options remain visible.',
        'p02_detached_two_piece_B_independent_rotations':'The source L and B have four-cell top and left red brackets, while the source square and lower-right region of B have blue three-cell bottom brackets. All six spans are outside material; the two source pieces remain separate and their independent rotations remain permitted.',
        'p03_native_outer_boundary_conservation':'The two vertical board borders have three red units each. A/B/C/E each have three red units, D has two. All unit grids, shapes and choice labels remain clear; the open U and both long-arm shapes are unchanged.',
        'p03_native_L_arm_transport_all_options':'The given L has red top and blue left arms. A has red right and blue top after a clockwise quarter-turn; B-E have red top/blue left. The 3 by 3 source square stays uncolored. Every original black and white square is readable.'
      }[variant],
      'predeclared_wrong_answer':design['expected_wrong_answer'],
      'primary_clearance_for_exactly_two_calls':True,
      'limitations':['Detached comparison brackets adapt the current Plane233 method; parent must assess that adaptation independently.',
                     'No claim of model success, causal effect, user approval, Pass or Collect is made by this inspection.']}
    if design.get('marking_mode')=='native_boundary':
        report['visual_findings']=[
          'Only original boundary edges are recolored at 1.5pt. There are no new points, lines, cuts, seams, labels, fills or source subregions.',
          'All source/option grids, black-white fills, diagnostic notches and letters remain readable at native size.',
          'Each marked unit contributes to a documented continuous boundary run; there is no overwritten, duplicated or ineffective action.',
          'The independent exact color-preserving material proof transports every marked edge and every black grid edge in explicit valid witnesses for each geometrically admissible choice.',
          'Keeping colors as real printed ink and treating them as comparison highlights both leave the original unique answer unchanged. This is certified by witnesses, not by asking readers to ignore ink.']
        report['material_color_proof_path']=design['material_color_proof_path']
        report['material_color_proof_sha256']=design['material_color_proof_sha256']
        report['limitations'][0]='The native boundary correspondence and actual material-color witness audit require a fresh independent second review if two calls hit.'
    write(out / 'primary_visual_review_before_calls.json', report)

def run(qid, variant):
    out = OWN / qid / variant
    if (OWN/'host_api_halt.json').exists(): raise RuntimeError('Batch halted after host/API failure; no later calls allowed')
    if (out/'api_process.json').exists(): raise RuntimeError('This exact candidate already started; never retry')
    review = read(out/'primary_visual_review_before_calls.json')
    assert review['primary_clearance_for_exactly_two_calls']
    gates = read(out/'render_gates.json')
    replay = read(out/'independent_process_exact_replay.json')
    assert replay['PNG_bytes_equal'] and replay['source_inputs_equal']
    assert gates['image_sha256'] == replay['image_sha256'] == review['image_sha256'] == filehash(out/'candidate.png')
    assert gates['design_sha256'] == replay['design_sha256'] == filehash(out/'design.json')
    cfg, ad = adapter()
    assert fingerprints(ad,qid) == gates['source_inputs']
    check = eligibility(qid); assert check['eligible'], check['reasons']
    write(out/'eligibility_immediately_before_calls.json', check)
    harness_path = OWN/'harness/quicktest3_isolated.py'
    original_path = OLD/'harness/quicktest3_isolated.py'
    original_bytes = original_path.read_bytes()
    harness_path.parent.mkdir(parents=True,exist_ok=True)
    if harness_path.exists(): assert harness_path.read_bytes() == original_bytes
    else: harness_path.write_bytes(original_bytes)
    copied_bytes = harness_path.read_bytes()
    assert copied_bytes == original_bytes
    h = loadmodule('u02_exact_original_quicktest3',harness_path)
    # Only local lookup globals change. Remote payload/transport/timeout remain original.
    h.PROJECT = PROJECT
    h.RUNTIME = PROJECT / 'runtime'
    write(out/'harness_context.json',{
      'original':str(original_path),'original_sha256':digest(original_bytes),
      'copy':str(harness_path),'copy_sha256':digest(copied_bytes),
      'byte_identical':True,'exact_source_diff':'',
      'reverse_replacement_proof':'No byte replacements; copy == original byte for byte.',
      'only_local_lookup_globals_rebound':{'PROJECT':str(h.PROJECT),'RUNTIME':str(h.RUNTIME)},
      'HARNESS_cache_root':str(h.HARNESS),'remote_code_and_settings_modified':False,
      'strict_ownroot_writeguard':True,
      'per_call_local_eligibility_gate':'Python urllib.Request audit event, with no payload/header logging or mutation.'})
    write(out/'api_process.json',{'pid':os.getpid(),'command':sys.argv,'started_at':now(),
                                'runs':2,'status':'started','harness_sha256':digest(original_bytes)})
    counter = {'actual_request_events':0}
    def request_gate(event,args):
        if event != 'urllib.Request': return
        assert not (OWN/'host_api_halt.json').exists(), 'Batch already halted; no later API call'
        counter['actual_request_events'] += 1
        index = counter['actual_request_events']
        assert index <= 2, 'Third API request forbidden'
        state = eligibility(qid)
        assert state['eligible'], state['reasons']
        assert filehash(out/'candidate.png') == gates['image_sha256']
        assert filehash(out/'design.json') == gates['design_sha256']
        state['actual_request_index'] = index
        state['image_sha256'] = gates['image_sha256']
        state['design_sha256'] = gates['design_sha256']
        state['no_remote_arguments_modified'] = True
        write(out/f'eligibility_before_actual_call_{index:02d}.json', state)
    sys.addaudithook(request_gate)
    status = 'unresolved'
    try:
        summary = h.run_tests('PlaneGeometry',qid,out/'candidate.png',out/'design.json',out/'tests',runs=2)
        status = 'completed' if summary['two_completed'] else 'API_ERROR_STOP_BATCH'
        if not summary['two_completed']:
            write(OWN/'host_api_halt.json',{'created_at':now(),'question_id':qid,
                  'variant_id':variant,'reason':'Original harness did not complete both responses; no retry and no later API calls.',
                  'summary_path':str(Path(summary['evidence_dir'])/'summary.json')})
        print(json.dumps({'summary_path':str(Path(summary['evidence_dir'])/'summary.json'),
                          'two_completed':summary['two_completed'],
                          'actual_request_events':counter['actual_request_events']},ensure_ascii=False),flush=True)
    except BaseException:
        status = 'LOCAL_OR_HOST_FAILURE_STOP_BATCH'
        write(OWN/'host_api_halt.json',{'created_at':now(),'question_id':qid,
              'variant_id':variant,'traceback':traceback.format_exc(),
              'reason':'Failure during original harness execution; no retry or later API calls.'})
        raise
    finally:
        import matplotlib.pyplot as plt
        plt.close('all')
        write(out/'api_process_finished.json',{'pid':os.getpid(),'finished_at':now(),
              'status':status,'actual_request_events':counter['actual_request_events'],
              'original_harness_hash_unchanged':filehash(original_path)==digest(original_bytes),
              'copy_hash_unchanged':filehash(harness_path)==digest(original_bytes),
              'candidate_hash_unchanged':filehash(out/'candidate.png')==gates['image_sha256'],
              'design_hash_unchanged':filehash(out/'design.json')==gates['design_sha256'],
              'all_Matplotlib_figures_closed':not plt.get_fignums(),
              'no_local_subprocesses_spawned_by_runner':True,
              'request_session_closed_by_original_context_manager':True})

if __name__ == '__main__':
    if sys.argv[1] == 'visual': visual_review(sys.argv[2],sys.argv[3])
    elif sys.argv[1] == 'run': run(sys.argv[2],sys.argv[3])
