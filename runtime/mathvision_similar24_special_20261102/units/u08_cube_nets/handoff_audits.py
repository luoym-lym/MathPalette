from worker import *

def references():
    observations={
        'Plane217':'Four source holes alternate red/blue on diagonals; A dashed falling diagonal red and rising diagonal blue. Original outlines and other choices black.',
        'Plane233':'Open left four-cell border red and bottom two-cell border blue on source and option C. No interior partition added; existing full grid black.',
        'Plane308':'Odd source numerals1,3,5 red points and even2,4,6 blue. A triangle pair red/blue. Numerals remain legible; not contiguous old1/2/3 grouping.',
        'Plane427':'Two real ST and TV sides red, original dotted SV base blue. Original70-degree arc and S/T labels intact.',
        'Solid126':'Removal/new ledge comparison red; depth connections blue. Saved removed2 is finally blue after override, not both colors. Gray-free face geometry stays intact.',
        'Solid142':'Left folded cut red, upper cut blue. A left/right vertical diamonds red; top/bottom vertical diamonds blue. Existing filled gray paper retained.',
        'Solid167':'Two folds original text visible; left cut red and top cut blue. A corresponding vertical diamonds red left/right and blue top/bottom. Not oldD horizontal mapping.',
        'Solid176':'Four true flap slants in D red: flap310a,flap311a,flap300b,flap301b. Dashed folds remain. This is a real flap-orientation and closure comparison, not an entire option highlight.',
        'Solid203':'Original x edge and C-labeled edge red; all other net/solid edges and labels unchanged. Not oldA correspondence.'
    }
    save(OWN/'reference_visual_audit.json',{'created_at':now(),'actually_viewed_all9_current_C01_PNG':True,'all_C01_plugins_read':True,'all_recipes_and_reference_JSON_parsed_completely_one_file_at_a_time':True,'source_read_hash_ledger':str(OWN/'reference_read_ledger.json'),'observations':observations,'primary_reference':'Solid176','claims':'Methods and current pixels only; reference pass status is not approval of this research.'})

def unresolved187():
    save(OWN/'Solid187/remaining_semantic_assessment.json',{'created_at':now(),'status':'UNRESOLVED_NO_PRIMARY_CANDIDATE','not_an_impossibility_claim':True,'original_unique_correct':'C, two openings on centrally opposite parallel cube edges affecting four faces','new_tests':[
        {'variant':'C01_opposite_face_window_substitution','preset':'E','finals':['E','D'],'hit_count':1},
        {'variant':'C02_shared_face_notch_ownership','preset':'A','finals':['D','D'],'hit_count':0},
        {'variant':'C03_opposite_face_axes_true_and_false','preset':'D','finals':['E','C'],'hit_count':0}],
        'earlier_history':'All three old tested A/B/D designs and six complete raw responses read, hashes preserved and never tested again.',
        'remaining_directions_examined':[
            {'idea':'Top/bottom cap notch partners in B','reason_not_called':'Exact false-cap closure relation already tested in old B; mere more edges or stronger ink is not a new correspondence.'},
            {'idea':'Full same-hole contours on D or target','reason_not_called':'Old D already binds both local closed hole pairs to target while ignoring opposite-edge placement. Recolor/width or a subset of its same full-hole mapping is not a fresh hypothesis.'},
            {'idea':'Count target two half-notches as separate holes','reason_not_called':'Old A did exactly this. C02 instead tested genuine face ownership, now failed; no relabel/retry.'},
            {'idea':'Opposite interior windows in E','reason_not_called':'New C01 tested this genuine opposite-face relation and failed. No color/linewidth repeat.'},
            {'idea':'New bridges or diagonals across a notch, stronger hidden-edge style changes','reason_not_called':'Would risk adding tunnel walls, extra cut boundaries, convex tabs, or removing the decisive open-shell/hidden contour interpretation. No reliable new useful mark without ambiguity.'},
            {'idea':'Only trace C correct closure invariant','reason_not_called':'Useful for ordinary explanation, but supplies no credible wrong-preset prediction for this objective.'}
        ],'why_unfinished':'All current defensible fresh mappings have failed their frozen two-call tests. No further independently justified distinct informative design remains in this assessment; future solutions are not ruled out. The three new designs are not a stopping quota: each covers a distinct relation absent from old attempts, and remaining directions have explicit semantic/history objections.','actual_new_calls':6,'errors_or_aborts':0,'formal_actions':0,'independent_second_review':False})
    cp=read(OWN/'checkpoint.json');cp['questions']['Solid187']={'status':'unresolved_no_primary','actual_new_api_calls':6,'reason_path':str(OWN/'Solid187/remaining_semantic_assessment.json')};checkpoint(questions=cp['questions'])

if __name__=='__main__':references();unresolved187()
