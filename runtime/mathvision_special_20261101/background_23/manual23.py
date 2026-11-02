from common23 import *
from datetime import datetime,timezone
manual={
'Plane192':(['A','A'],['Run1 explicitly ends A:A after discussing the red segments, badly miscounting grid units, and preferring fewer oscillations. The final A is unambiguous; its purported metric argument is false.','Run2 explicitly ends A:A. It calls A a single direct line, although A visibly has two diagonal segments. The final is a hit; this does not establish faithful reading of the proposed run-unit mapping.']),
'Plane233':(['D','B'],['Run1 finally chooses D after incompatible shape classifications and unsuccessful invented tilings; mentions of C and B are not counted as finals. Misses presetB.','Run2 explicitly ends B, with incorrect A/D cell counts and a local U placement generalized to a complete partition. Hits presetB; mixed D/B pair fails.']),
'Solid220':(['A','E'],['Run1 correctly derives X oppositeY, then explicitly changes the question to V and ends A:Z. Final A is consistent with choiceZ but not with the actual question. Counted as one final hit, not as evidence of sound folding or mechanism.','Run2 correctly uses both U-V-W and V-X-Z strips and ends E:Y. Misses presetA; pair fails.']),
'Plane263':(['5','5'],['Run1 explicitly rejects two pieces by area and ends5, confusing area compatibility with tileability. Preset2 misses.','Run2 ends5 and asserts without a witness that five L pentominoes form5x5. Preset2 misses. Old/new observed5/5 cannot be relabeled as new preset success.'])}
for qid in sys.argv[1:]:
    ds=[p.parent for p in (OUT/qid).glob('r23_*/design.json')]
    for d in ds:
        if not (d/'api_process_finished.json').exists():continue
        if (d/'manual_final_review.json').exists():continue
        inv=Path(read(d/'api_process_finished.json')['evidence_dir']);b=read(inv/'binding.json');sm=read(inv/'summary.json')
        finals,notes=manual[qid]
        if d.name=='r23_four_cell_corner_spine':
            finals=['C','C'];notes=['Run1 explicitly ends C after calling it a vertical T and inventing incompatible/overlapping regions. FinalC is unambiguous; the tiling narration is false and does not prove the intended boundary-matching mechanism.','Run2 explicitly ends C, accurately describes C as four-cell column plus one foot, but miscounts A/B/D as4 and incorrectly treats local fit as sufficient. FinalC hits; no complete congruent tiling is given.']
        rs=[]
        for i in [1,2]:
            raw=read(inv/f'run_{i:02d}_response.json');job=read(inv/f'run_{i:02d}.json');c=raw['choices'][0]
            assert job['status']=='completed' and c['finish_reason']=='stop'
            rs.append({'run_index':i,'full_final_manually_read':True,'full_final':c['message']['content'],'explicit_final':finals[i-1],'hits_frozen_preset':finals[i-1]==str(b['expected_wrong_answer']),'manual_notes':notes[i-1],'raw_response_path':str((inv/f'run_{i:02d}_response.json').relative_to(ROOT)),'raw_response_sha256':sha(inv/f'run_{i:02d}_response.json'),'run_id':job['run_id']})
        hit=all(r['hits_frozen_preset'] for r in rs)
        write(d/'manual_final_review.json',{'stage':'material_refinement','review_type':'Primary manual FULL final reading only','reviewed_at':datetime.now(timezone.utc).isoformat(),'expected_wrong_answer_unchanged':b['expected_wrong_answer'],'complete_runs':2,'manual_finals':finals,'results':rs,'paired_target_hit':hit,'status':'PRIMARY_POSSIBILITY_REQUIRES_PARENT_NEW_INDEPENDENT_REVIEW' if hit else 'FAILED_FROZEN_PRESET_PAIR','old_controls_reused':str(OUT/'old_control_reuse.json'),'limits':'Original controls also wrong for Plane192 (A/A), Plane233(C/C), Plane263(5); Solid220 had one correctE. No causal improvement or population rate is established. Narratives need not match, but their errors and mechanism limits are disclosed.'})
        print(json.dumps({'qid':qid,'variant':d.name,'finals':finals,'paired_hit':hit}))
