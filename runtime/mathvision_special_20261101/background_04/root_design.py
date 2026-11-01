from research import *
from copy import deepcopy
RED='#DC2626'
PROOFS={
'Plane224':('77','Each of the three bottom unit squares has side1. Their combined width3 is the side of the next square. Its top is height4, so the next square has side4. The upper square spans width3+4=7, making the rectangle7 by11 and area77. All dimensions are forced by square incidences.','prescreen_only','No clean concise legal measurement-binding trap was found: all three unit-area1 labels are already clear. Making a larger square look like the area1 unit would just impose a misleading scale association with little informational need.'),
'Plane280':('B','The thick path contains consecutive square-side counts2+1+1+2+1+1+1=9. Every small square has area4, hence side2cm; its total length is18cm and unique optionB. The two colored overlays do not change any stroke width, path endpoint, grid or target membership.','prepared_for_test','False unit-span correspondence: color one true unit grid side and the long two-unit thick route segment identically. The proposed wrongA=16 occurs if that long span is treated as a single2cm unit instead of4cm. Only actual existing geometry is colored.'),
'Solid206':('288','Put base square vertices at(0,0,0),(s,0,0),(s,s,0),(0,s,0). The ridge endpoints are(-s/2,s/2,h),(3s/2,s/2,h), forced by the four equal side edges and ridge length2s. Equal edges give h=s/sqrt2=6. At relative heightt a horizontal section is s(1+t) bys(1-t). Thus V=s^2*h*integral_0^1(1-t^2)dt=(2/3)*72*6=288. Reflection/rigid motion leaves this unique.','prescreen_only','No concrete concise appearance mechanism yields a stable numerical misread: outlining congruent triangular end faces may suggest a prism, but supplies no definite perpendicular prism length and would add many weakly useful edges. Skip instead of broad face salience.'),
'Solid247':('224sqrt(3)/3','The parallel base planes cut the same section plane in parallel linesQP andMN. With raysCQ parallelDM andCP parallelDN, trianglesCQP andDMN are similar. CQ/DM=8/4=2, soCP=4. The two triangular areas are8sqrt3 and2sqrt3, separated by height16. The solid is a triangular frustum: V=16/3*(8sqrt3+2sqrt3+sqrt(48))=224sqrt3/3. All chosen edge distances are explicit and solve uniquely.','prescreen_only','A falseQ/M orP/N color pairing either reproduces the true correspondence or conflicts with explicit distances and the12-unit edge. Prism-like outline emphasis supplies no targeted legal binding error without weak extra marks. No candidate saved or API calls.')}
def prescreens():
    for qid,(answer,proof,status,reason) in PROOFS.items():
        folder=HERE/qid;branch='PlaneGeometry' if qid.startswith('Plane') else 'SolidGeometry'
        write(folder/'primary_prescreen.json',{'question_id':qid,'branch':branch,'status':status,'correct_answer':answer,'unique_mathematical_solution':proof,'design_or_rejection_reason':reason,'original_png_actually_viewed':True,'eligibility_rechecked':eligible(branch,qid),'context_path':str(folder/'context.json'),'frozen_inputs_path':str(folder/'frozen_inputs.json'),'independent_second_review':False})
def render():
    qid='Plane280';branch='PlaneGeometry';check=eligible(branch,qid);assert check['eligible']
    cfg,ad,PR=adapter(branch);record=ad.records[qid];before=inputs(branch,record);context=ad.inspect_question(qid)
    from partial_style import object_paths
    capture=ad.scene(qid)
    try:
        capture.fig.canvas.draw()
        paths={target:[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'segments':[{'control':s['control'].tolist(),'style':s['style']} for s in p['segments']]} for p in object_paths(capture,target)] for target in ['grid0','thick3']}
    finally:capture.close()
    actions=[{'type':'set_object_style','target':target,'color':RED} for target in ['grid0','thick3']]
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':'Color a genuine unit grid side and a two-unit path span identically; retain all original widths and the target path.','intent':'Test a one-versus-two unit correspondence misread.','params':{'actions':actions}}
    renderer=PR(cfg,ad,{qid:context});normal,data,pixels=renderer.render(plugin);normal2,data2,pixels2=renderer.render(normal,frozen=True)
    assert normal==normal2 and data==data2 and pixels==pixels2
    assert inputs(branch,record)==before
    folder=HERE/qid/'unit_to_double_span';folder.mkdir(parents=True,exist_ok=True)
    if (folder/'candidate.png').exists():
        assert (folder/'candidate.png').read_bytes()==data
        assert json.loads((folder/'plugin.json').read_text(encoding='utf-8'))==normal
        assert json.loads((folder/'context.json').read_text(encoding='utf-8'))==context
        suffix=1
        while (folder/f'target_paths.failed_partial_{suffix}.json').exists():suffix+=1
        (folder/'target_paths.json').rename(folder/f'target_paths.failed_partial_{suffix}.json')
        write(folder/f'render_serialization_error_{suffix}.json',{'status':'metadata_serialization_corrected_before_any_API','errors':['TypeError: Object of type ndarray is not JSON serializable','AttributeError: Line2D has no attribute tolist'],'preserved_partial':f'target_paths.failed_partial_{suffix}.json','candidate_plugin_context_preserved_byte_identical':True,'correction':'Serialize native path controls and frozen styles only; omit live artist handles. Render operations unchanged.'})
    else:
        (folder/'candidate.png').write_bytes(data);write(folder/'plugin.json',normal);write(folder/'context.json',context)
    write(folder/'target_paths.json',paths)
    write(folder/'eligibility_before_design.json',check)
    write(folder/'design.json',{'question_id':qid,'variant_id':'unit_to_double_span','expected_wrong_answer':'A','expected_wrong_value':'16 cm','correct_answer':record['answer'],'mechanism':PROOFS[qid][3],'mathematical_solution':PROOFS[qid][1],'marker_roles':[
        {'target':'grid0','role':'A real one-unit thin grid side gives the visual source of the false unit correspondence. Its original1pt width is preserved.'},
        {'target':'thick3','role':'The actual two-unit portion of the thick target path receives the same color, providing the destination of the one-to-two span confusion. Its original2.5pt width and both constituent grid steps remain visible.'}],
        'human_readability':'All original geometry, thin/thick membership, square areas, labels and quantity asked are unchanged. Color does not declare equal length. Nine side units remain countable; no added point or mathematical condition.','created_at':datetime.now(timezone.utc).isoformat(),'review_status':'PRIMARY_ONLY_REQUIRES_NEW_INDEPENDENT_SECOND_REVIEW'})
    write(folder/'render_check.json',{'question_id':qid,'baseline_pixel_matches_formal':True,'original_pixel_sha256':context['original_pixel_sha256'],'schema_default_normalization':True,'two_redraws_byte_identical':True,'candidate_png_sha256':digest(folder/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':digest(folder/'plugin.json'),'design_sha256':digest(folder/'design.json'),'frozen_inputs':before,'unchanged_after_render':True,'isolation':ISOLATION})
    print(str(folder),flush=True)
if __name__=='__main__':
    if sys.argv[1]=='prescreens':prescreens()
    else:render()
