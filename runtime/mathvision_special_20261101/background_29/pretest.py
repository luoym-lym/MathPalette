import bootstrap
from bootstrap import OWN,ROOT,HISTORY
from make_candidates import eligible,save
import json,sys,hashlib
from workbench_io import file_hash
findings={
'Solid175':'Six colored boundaries are precisely the six actual shared edges crossed in E,E,N,E,N,E order. Four red hinges include the perpendicular 3->4 crossing; the last two are blue. All seven labels and square boundaries remain clear. Original six-face tracking still uniquely gives1/6(B).',
'Solid191':'Upper panel contains five red east hinges and two blue south hinges. Initial east hinge is one line represented twice in scene IDs, not two steps. Both original pip panels, all Start/End labels and every grid cell remain clear. Lower panel remains the given one-east-roll intermediate state.',
'Solid91':'Twelve contact hinges, in chronological groups of4red/4blue/4green, are visible as original grid boundaries. Four colors never used; no added pips, text or arrows. Original12cells and die1/2/3pips remain readable. Duplicate footprint edges at beginning/end overlap the same original line and do not add a crossing.',
'Solid150':'Six actual arms are paired by red x,blue y,green z open two-edge motifs. Rear positive-y arm remains partial, with its existing clipped vertical edge; lower negative-z arm remains partially occluded. No hidden segment extended. All original blank faces, central occlusion and seven-cube cross remain unchanged. Marked motifs are actual outer face rim fragments, not new glue interfaces.',
'Solid147':'Red source L borders the front/left of the upper white face, blue borders the bottom/far side of the lower-right rear white face. A has paired red upper and blue opposite lower terminal motifs. Source white/lightgray/darkgray areas, lower hidden row constraints and labelsA-E remain distinguishable at768. The panel is small at its original scale; no claim of human performance validation.',
'Solid198':'Red/blue front rims and green shared receding seam actually border the two source white top faces. Exactly corresponding original edges appear on B top cap. Green is the original common seam, not an added partition. Source dark/gray/black/white distinctions and all five option3D/planarity differences remain visible, with the original small-panel readability limit.'}
if sys.argv[1]=='all':
    for q,text in findings.items():
        p=next((OWN/q).glob('r29_*/design.json'));d=json.loads(p.read_text(encoding='utf-8'));base=p.parent
        report=json.loads((base/'frozen/render_check.json').read_text(encoding='utf-8'));plugin=json.loads((base/'frozen/plugin.json').read_text(encoding='utf-8'))
        audit={'stage':'material_refinement','question_id':q,'variant_id':d['variant_id'],'native_actual_png_viewed':True,'image_sha256':file_hash(base/'frozen/candidate.png'),'viewing_method':'functions.view_image original768x768 PNG, individually displayed before any API calls','actual_visual_findings':text,'every_marker_roles':d['marker_roles'],'fresh_path_hashes':str(base/'fresh_target_paths.json'),'all_endpoints_original_and_visibility_frozen':all(a['type']=='set_object_style' and a.keys()<= {'type','target','color','linewidth_pt'} for a in plugin['params']['actions']),'schema_and_defaults_normalized':True,'original_noop_pixel_agreement':report['baseline_matches_formal'],'twice_byte_identical_PNG':report['deterministic'],'mathematics':str(base/'primary_math_audit.json'),'all_original_labels_material_fills_geometry_projection_visibility_preserved':True,'no_false_extra_cuts_regions_equalities_labels_fills_or_geometry':True,'no_arbitrary_mark_count_cap':True,'no_control_calls':'No new controls; existing original-control evidence is not repeated.','primary_only':True,'independent_review_required_before_delivery':True}
        save(base/'pretest_native_visual_and_marker_audit.json',audit)
        save(base/'eligibility_immediately_before_calls.json',eligible(q))
        assert audit['image_sha256']==d['candidate_sha256']
    save(OWN/'Solid150/r29_opposed_arm_single_interface_count/pretest_math_clarification.json',{'before_any_solver_call':True,'clarification':'The correct proof uses the sum of all six central faces21 and matching six arm glue faces21; no individual opposite-face sum7 is needed or added as a given. The immutable draft paragraph mentioning ordinary opposite-pair convention is unnecessary and is superseded by this statement. The wrong count126 is147-21, subtracting only one side of each of six interfaces. Opposite arm color pairs indicate geometry only.','correct_total':105,'preset_remains':126})
    print('Six native PNG inspections and eligibility audits saved; ready for exact pairs.')
else:
    for q in ['Solid91','Solid118','Solid124','Solid147','Solid150','Solid175','Solid191','Solid198']:
        manifest=json.loads((OWN/q/'old_evidence_manifest.json').read_text(encoding='utf-8'));byhash={}
        for e in manifest:
            if e['path'].endswith('.png'):byhash.setdefault(e['sha256'],[]).append(e['path'])
        print(q,json.dumps(byhash,ensure_ascii=False))
