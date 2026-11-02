from research import *
from prepare_designs import PROOFS

VARIANTS={'Solid238':'r53_whole_span_to_hypotenuse','Solid241':'r53_cross_plane_angle_difference','Solid242':'r53_arc_width_to_cut_diameter','Solid243':'r53_face_base_angle_subtraction'}
NATIVE={
'Solid238': 'At native768px the complete GH red span visibly passes through the unchanged black J dot; the black right-angle glyph at J remains distinct. BG is red dashed, while BJ is black dashed. AH/EF and all A..J labels are readable. The two red paths identify different actual source/receiver objects and do not enclose an invented face. Human uses the original rectangular prism net to get192; there is no color-count or transported-print answer requirement.',
'Solid241': 'Native768px shows all8 original letters, all12 original box edges and the original3 hidden rear edges. AF and EC are thin red dashed true diagonals; AH and EG are thin blue dashed true diagonals. The AF/EC projected crossing has no new dot and is not claimed to be a spatial intersection. Green AB and AD remain separate perpendicular box directions; AD remains dashed. E target rays are identifiable. No false arcs, angle labels, equality signs, material faces or plane conditions appear. A careful human can use the unchanged30/60 givens and3D rectangular box to get sqrt130/13.',
'Solid242': 'Native768px shows a solid half cylinder with a full visible top semicircle and its black diameter, visible cut rectangle and originally dashed lower semicircular rim. Red upper semicircular rim and red lower straight diameter are each visible and each has a different dimensional role. Both straight cut-side boundaries remain black and solid. No new rim, opening, radial line, paint region or numerical label was introduced. The ordinary numerical total-surface-area task still means all boundary faces, so actual96pi+120 is unique; red does not designate a new target subset.',
'Solid243': 'Native768px retains A at apex, B/C/D/E at distinct base positions, all8 original edges including3 hidden black dashed rear edges. Red BA, green BC and the new thin blue dashed BD share B but remain distinguishable. BD crosses original AC without a dot; it is a base diagonal auxiliary, not a ninth original edge or an equal-edge glyph. Nothing hides C/E or joins a false physical face. Colors distinguish angular roles, so an ordinary human retains the square-base and8-equal-edge interpretation and gets45deg.'}

def freeze(qid):
    folder=OWN/qid/VARIANTS[qid]
    draft=folder/'draft_candidate.png'
    report=read(folder/'render_check.json')
    assert sha(draft)==report['png_sha256']==sha(folder/'repeat.png')
    assert all(report[k] for k in ['schema_valid_and_defaults_normalized','normalization_idempotent','no_op_pixel_equals_formal','two_sequential_draws_byte_identical','fresh_context_matches_initial'])
    assert eligibility(qid)['eligible']
    design=read(folder/'pending_design.json')
    design.update(status='FROZEN_BEFORE_BOTH_CALLS',frozen_at_utc=now(),candidate_png_sha256=sha(draft),plugin_sha256=sha(folder/'plugin.json'),difference_audit_sha256=sha(folder/'design_difference_audit.json'),path_bindings_sha256=sha(folder/'path_bindings.json'),native_review=NATIVE[qid],primary_only=True,second_review_required='Parent must start a NEW independent review before delivery. No self second review, Pass, Collect or formal approval.')
    with (folder/'design.json').open('x',encoding='utf-8',newline='\n') as f:
        json.dump(design,f,ensure_ascii=False,indent=2,allow_nan=False);f.write('\n')
    with (folder/'candidate.png').open('xb') as f:f.write(draft.read_bytes())
    dump(folder/'primary_prescreen.json',{'question_id':qid,'variant_id':VARIANTS[qid],'reviewed_at':now(),'actual_source_JPG_formal_PNG_old_PNGs_and_new_native_PNG_viewed':True,'primary_math_proof':PROOFS[qid],'per_mark_information_roles':design['marker_roles'],'actual_native_findings':NATIVE[qid],'meaningful_difference':design['design_difference'],'human_unique_solution_and_semantics_primary_pass':True,'each_mark_useful_primary_pass':True,'concise_primary_pass':True,'not_equating_color_with_new_length_or_coplanarity':True,'no_new_motion_premise':True,'no_geometry_projection_visibility_dimension_label_fill_dot_count_changes':True,'correct_answer_used_as_premise':False,'candidate_sha256':sha(folder/'candidate.png'),'design_sha256':sha(folder/'design.json'),'plugin_sha256':sha(folder/'plugin.json'),'status':'PRIMARY_ONLY_PRECALL','limitations':['An intended mistaken correspondence is a hypothesis, not a demonstrated solver mechanism.','No causal benefit, human prevalence or per-mark ablation is established.','No additional original-control call is required or made; historical controls are reused if any.']})
    print(qid,'frozen',sha(folder/'design.json'),sha(folder/'candidate.png'))

if __name__=='__main__':
    for q in VARIANTS:freeze(q)

