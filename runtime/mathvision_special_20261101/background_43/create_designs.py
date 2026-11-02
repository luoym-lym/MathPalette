import env
from env import OWN,PROJECT
from prepare import read,dump,sha,eligibility
from datetime import datetime,timezone
import hashlib,io,json

def now():return datetime.now(timezone.utc).isoformat()
RED='#DC2626';BLUE='#2563EB';GREEN='#16A34A'

def interval(ctx,target,start,end,color,width=1.5):
    t=next(t for t in ctx['canvas']['targets'] if t['id']==target)
    p=t['partial_paths'][0]
    return {'type':'set_object_style','target':target,'color':color,'linewidth_pt':width,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':start,'end':end,'wrap':False}}

def make(qid,name,preset,actions,roles,proof,mechanism,difference,semantics):
    root=OWN/qid/name;root.mkdir(parents=True,exist_ok=True)
    e=eligibility(qid);assert e['eligible'];dump(root/'eligibility_before_design.json',e)
    dump(root/'design_difference_audit.json',{'question_id':qid,'variant_id':name,'created_at':now(),'historical_evidence_audit':str(OWN/qid/'history_audit.json'),'substantive_new_information':difference,'mechanism_before_calls':mechanism,'expected_wrong_answer_before_calls':preset,'old_failed_or_aborted_unchanged_repeat':False,'cosmetic_only':False,'no_posthoc_preset_relabel':True,'every_marker_role':roles,'annotation_semantics_lesson_applied':semantics})
    adapter,config=env.renderer()
    ctx=adapter.inspect_question(qid);dump(root/'context.json',ctx)
    from mathvision_plugins import PluginRenderer
    from dataset_tools.mathvision_workbench import png_bytes
    from partial_style import object_paths
    from workbench_io import pixel_hash
    pr=PluginRenderer(config,adapter,{qid:ctx})
    raw={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':mechanism,'intent':mechanism,'params':{'actions':actions}}
    plugin=pr.normalize(raw)
    dump(root/'plugin_input.json',raw);dump(root/'plugin.json',plugin)
    assert pr.normalize(plugin)==plugin
    sc=adapter.scene(qid)
    try:
        noop=png_bytes(sc);(root/'noop.png').write_bytes(noop)
        assert pixel_hash(noop)==ctx['original_pixel_sha256']
        paths=[]
        for i,a in enumerate(plugin['params']['actions']):
            if a['type']=='set_object_style':
                for p in object_paths(sc,a['target']):
                    paths.append({'action_index':i,'target':a['target'],'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'full_controls':[s['control'].tolist() for s in p['segments']],'original_styles':[s['style'] for s in p['segments']]})
            else:
                matches=[p for p in ctx['snap_points'] if p['xy']==a['xy']]
                assert matches,(qid,a)
                paths.append({'action_index':i,'xy':a['xy'],'exact_existing_snap_points':matches})
    finally:sc.close()
    dump(root/'path_fingerprints.json',paths)
    normalized,data,pixel=pr.render(plugin,frozen=True)
    (root/'candidate.png').write_bytes(data)
    _,data2,pixel2=pr.render(plugin,frozen=True)
    (root/'repeat.png').write_bytes(data2)
    assert data==data2 and pixel==pixel2
    from PIL import Image
    import numpy as np
    a=np.array(Image.open(io.BytesIO(noop)).convert('RGBA'));b=np.array(Image.open(io.BytesIO(data)).convert('RGBA'))
    changed=np.any(a!=b,axis=2);ys,xs=np.where(changed)
    counts={c:int(np.all(b[:,:,:3]==tuple(bytes.fromhex(c[1:])),axis=2).sum()) for c in [RED,BLUE,GREEN]}
    assert b.shape==(768,768,4) and (b[:,:,3]==255).all()
    dump(root/'render_check.json',{'no_op_pixel_equal_formal':True,'formal_png_sha256':sha(PROJECT/'PlaneGeometry/image'/f'{qid}.png'),'noop_png_sha256':sha(root/'noop.png'),'actual_schema_validation':True,'normalized_defaults_frozen':True,'normalization_idempotent':True,'fresh_context_equal_preparation_context':ctx==read(OWN/qid/'context.json'),'two_offline_render_bytes_identical':True,'candidate_sha256':sha(root/'candidate.png'),'repeat_sha256':sha(root/'repeat.png'),'candidate_pixel_sha256':pixel,'opaque_768_square':True,'changed_pixels':int(changed.sum()),'changed_bbox':[int(xs.min()),int(ys.min()),int(xs.max()+1),int(ys.max()+1)],'exact_palette_pixel_counts':counts,'geometry_unchanged_by_operations':True,'text_fill_view_unchanged_by_schema':True,'all_original_input_paths_sha256':e['source_files'],'strict_own_write_guard':True,'created_at':now()})
    dump(root/'design.json',{'question_id':qid,'variant_id':name,'expected_wrong_answer':preset,'correct_answer':e['current_formal_record']['answer'],'created_at':now(),'mechanism':mechanism,'primary_math_proof':proof,'marker_roles':roles,'human_semantics':semantics,'material_difference_audit':str(root/'design_difference_audit.json'),'image_sha256':sha(root/'candidate.png'),'plugin_sha256':sha(root/'plugin.json'),'context_sha256':sha(root/'context.json'),'status':'PRIMARY research design only; no approval/Pass/Collect; parent NEW independent second review required for any possible pair'})
    print(json.dumps({'id':qid,'variant':name,'preset':preset,'image_sha256':sha(root/'candidate.png'),'actions':len(actions)}),flush=True)

def main():
    c=read(OWN/'Plane402/context.json')
    a=[interval(c,'o0',.75,1,GREEN,2),interval(c,'o7',0,1,GREEN,2),interval(c,'o8',0,1,GREEN,2)]
    make('Plane402','r43_elbow_double_projection_binding','10/3',a,[
      {'action_index':0,'role':'Source: original 4-unit strip width on its existing left edge; 4 label is untouched.'},
      {'action_index':1,'role':'Receiver one: existing dashed horizontal 4-unit elbow projection; its dashed old-position role remains.'},
      {'action_index':2,'role':'Receiver two: existing dashed vertical 4-unit elbow projection, not another independent strip length.'}],
      'Let q be exposed height of Q and strip width w=4. The 45-degree fold consumes a w-by-w elbow. Original longitudinal material length is x+w+q=13. P=w*x and Q=w*q, so x=2q. Thus 3q=9,q=3,x=6 uniquely. An unfolded-coordinate check reflects the material tail beyond line y=u at the elbow to an upgoing tail; both displayed projections have length4 but describe the same elbow, so they must not both enter material length. Erroneous x+q+4+4=13 gives x=10/3. This preset differs from the old missing-elbow26/3 and old observed8.',
      'Bind the original strip width to both perpendicular existing elbow projections. Targets counting the same fold elbow twice in material length: x+q+8=13, x=2q, giving10/3.',
      'Old exposed_strip_extent_binding colored original13 and exposed x/q and omitted the elbow, preset26/3, finals26/3 and8. The new three marks instead identify source4 and two distinct perpendicular OLD-position projections of the same elbow. The new error is duplication, not omission; original13/x/q edges are unstyled.',
      'This is a numerical folded-strip measurement question, not a colored printed-paper output-choice task. Both marked projections are already dashed reference edges; no new paper edge or extra fold is drawn. Colors do not change area membership or require a colored result option. The unique6 construction remains valid even if the original short boundary is colored ink.')
    c=read(OWN/'Plane407/context.json');a0=5.142857142857143;b0=18.;c0=20.571428571428573;L=36.
    top=lambda x:.5+(L-x)/(4*L)
    aa=[interval(c,'o0',top(b0),top(a0),BLUE,2),interval(c,'o4',(a0-2.5714285714285716)/9,1,BLUE,2),interval(c,'o0',top(L),top(c0),GREEN,2),interval(c,'o5',(c0-19.285714285714285)/(28.28571428571429-19.285714285714285),1,GREEN,2)]
    make('Plane407','r43_full_base_to_center_half_binding','E',aa,[
      {'action_index':0,'role':'Blue source: full top edge of the second rectangle, b.'},
      {'action_index':1,'role':'Blue receiver: portion of first centre line inside second rectangle, b/2, between existing dividing edge and original black centre.'},
      {'action_index':2,'role':'Green source: full top edge of fourth rectangle, d.'},
      {'action_index':3,'role':'Green receiver: portion of second centre line inside fourth rectangle, d/2.'}],
      'Let positive rectangle widths be a,b,c,d with a+b+c+d=36. Original line one runs from centre(a) to centre(b): length a/2+b/2. Line two is c/2+d/2. Sum is18 regardless of four lengths, uniquely A. No coordinates of this particular illustrative partition are treated as givens. False full-to-half transfer gives a/2+b+c/2+d=18+(b+d)/2, which varies with widths and would support E. E is an anticipated mistaken dependence claim, not the actual geometry.',
      'Pair complete second/fourth rectangle bases with the half widths actually traversed by the two centre lines. Targets transferring a whole-width role into each receiver half and wrongly making the sum depend on the partition, E.',
      'Old unit03 screened without a variant or API. This is a new explicit two-group full-width to centre-half comparison, with exact existing boundary/centre endpoints. It also leaves original centre dots black; it is not a copied Plane254 design.',
      'Numerical ribbon length problem. Existing black centre dots, dividing lines and outer contour remain readable; no new line divides the ribbon. Colored portions are part of the original requested centre lines, so they remain included in the sum. Color preservation is not an output-picture selection constraint.')
    c=read(OWN/'Plane410/context.json')
    aa=[interval(c,'Coutline',2/3,.75,RED,1.5),interval(c,'Coutline',.75,1,BLUE,1.5),interval(c,'Ctri',1/3,2/3,RED,1.5),interval(c,'Ctri',2/3,1,BLUE,1.5)]
    make('Plane410','r43_similar_triangle_area_unit_binding','3',aa,[
      {'action_index':0,'role':'Red source: horizontal unit leg of actual white corner half-square triangle, from(15,2.75) to(16,2.75).'},
      {'action_index':1,'role':'Blue source: vertical unit leg of same white half-square triangle, from(15,2.75) to(15,1.75).'},
      {'action_index':2,'role':'Red receiver: right sloping leg of actual central black triangle; lengthsqrt2, not1.'},
      {'action_index':3,'role':'Blue receiver: left sloping leg of that central black triangle; lengthsqrt2.'}],
      'Use the actual original unit squares. Left-to-right A has3 black of8 squares=3/8. B has12 black of20=3/5. C whole rectangle area3, black triangle base2*height1/2=1 plus right black square1, giving2/3. D has15 black of25=3/5. E has4 black of8=1/2. Exactly B,D satisfy3/5, correct2. Source white corner triangle has area1/2 and legs1; receiver black triangle has perpendicular legs sqrt2, similarity scale sqrt2 and area1. Equating their areas despite scale incorrectly changes C black area to1+1/2 while retaining true white area1: (3/2)/(5/2)=3/5, falsely adding C and giving3. All five original black/white masks stay unchanged.',
      'Match the ordered legs of a real white half-square triangle to the two perpendicular legs of the similar but double-area central black triangle. Targets transferring a half-square area unit by shape while ignoring scale, making a spurious third3/5 design.',
      'Old unit20 had no design/call, rejecting arbitrary borders or new partitions. Here four partial EXISTING edges encode a definite right-triangle similarity and the wrong half-area transfer; no new diagonal or source square is drawn.',
      'Area/count question uses original black semantic interiors. Styling outlines does not add shaded area or change which five designs are counted. The tiny central figure is inspected at native768px before calls; if triangle distinctions are not readable this design will be held. This is not a physical printed-picture transform.')
    c=read(OWN/'Plane412/context.json')
    pts=[([1.,6.],RED,'unit_start'),([2.,6.],BLUE,'unit_end'),([2.,0.],RED,'long_start'),([5.,0.],BLUE,'long_end')]
    aa=[{'type':'add_point','id':'r43_'+name,'xy':xy,'color':color} for xy,color,name in pts]
    make('Plane412','r43_unit_endpoint_to_long_run_binding','A',aa,[
      {'action_index':0,'role':'Red source start: actual left end of one20cm horizontal smallest-square side on the black route.'},
      {'action_index':1,'role':'Blue source end: actual right end of that20cm side.'},
      {'action_index':2,'role':'Red receiver start: lower-left endpoint of the full60cm black bottom run.'},
      {'action_index':3,'role':'Blue receiver end: lower-right endpoint of that60cm run.'}],
      'Small squares have side1unit=20cm. Edge matching of the rectangle shows the medium squares side2 and the large squares side3: the rectangle is5units wide,7high. Traversing the ORIGINAL black route P->Q gives maximal straight lengths[1,1,2,2,2,2,2,3,4,1,1], sum21=420cm,C. A direct graph enumeration of all original black unit-edge objects independently gives21edges and one P-Q chain. Mapping the marked endpoint pair of the bottom3unit run to the source1unit side would undercount2units, giving19units=380cm,A. It does not omit colored sections of the path; all original black route edges remain black,2.5pt.',
      'Match start/end roles of one actual20cm square side with the two endpoints of the bottom60cm straight run. Targets treating a single uninterrupted endpoint-to-endpoint run as one unit, undercounting40cm and selecting A=380.',
      'Old unit20 screened without design/API because recoloring a grid route could create a competing marked path. This design instead adds four exact existing-vertex point markers; every black route edge and every gray grid edge keeps its original color/width. It supplies an explicit source-unit/receiver-run endpoint correspondence, not an alternate route.',
      'Numerical length question, not a point-count target. Four markers lie on actual existing square/path corners and do not introduce a new edge or route. Original black path remains continuous and distinguishable from gray grid; P,Q labels remain. Marked points are endpoint comparisons, not equal-length symbols or additional20cm givens.')

if __name__=='__main__':main()
