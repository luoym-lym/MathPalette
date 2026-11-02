from bootstrap import HERE, PROJECT, TASK, renderer_setup
from research import read,save,sha,eligible,record
import json,copy,hashlib,sys
from datetime import datetime,timezone

SPECS={
'Solid134':{
 'variant_id':'r61_front_height_to_plan_depth', 'expected_wrong_answer':'E',
 'mechanism':'Bind the three equal complete front-view heights to the three equal plan depths in E. The false inference is that equal front elevations force equal horizontal base depths/capacities, ignoring water-volume divided by water-height. This is not the old I/III water-level identity swap.',
 'proof':'Let common front width be w, water heights hII>hI>hIII and base depths dI,dII,dIII. V=w*d*h. Equal volumes VI=VIII=4 imply dIII>dI; VII=3<4 with hII>hI implies dII<dI. Thus dIII>dI>dII, and only A satisfies this. B/C put I first; D puts II first; E makes all equal. No exact pixel-height ratios are used.',
 'difference':'Old uses three PARTIAL water-height spans with swapped I/III identities to B and preset B (final A/B). New uses COMPLETE exterior vessel heights and E plan-depth sides with identity preserved, preset E. The geometric error is cross-view dimension/capacity inference rather than swapping water-level identities.',
 'styles':[(f'front{i}edge3','#DC2626',None,f'Source vase {i+1} full exterior front height; equal elevation is the supplied invariant whose horizontal-depth inference is false.') for i in range(3)]+[(f'option4vase{i}edge1','#DC2626',None,f'Receiver E vase {i+1} plan depth; cross-view role differs from the source vertical height.') for i in range(3)]},
'Solid165':{
 'variant_id':'r61_local_right_angle_transfer','expected_wrong_answer':'D',
 'mechanism':'Pair the actual face-right-angle rays at R with short portions of the two face diagonals meeting at P. The source right angle is 90; P is a spatial 60-degree angle. Transferring the local orthogonal-ray role to P gives four right angles and 360. No colored closed quadrilateral is made.',
 'proof':'Use P=(0,0,0),Q=(0,1,1),R=(1,1,1),S=(1,1,0). At P, PQ dot PS=1 and both squared norms2, hence60 degrees. At Q, QP dot QR=0; at R, RQ dot RS=0; at S, SR dot SP=0. Three right angles plus60 give330=B. Original arcs select these nonreflex angles.',
 'difference':'Old colors all four complete sides into one closed projection loop, arguing planar quadrilateral sum360; final180/C missed D. New selects two LOCAL ray pairs only, one true face right angle and one noncoplanar-face diagonal angle; most of every side remains black and no full red loop exists. Same wrong value has a newly specified local misconception.',
 'styles':[('cube011_cube111','#2563EB',(0.75,1),'Source RQ ray near R, one side of actual square-face right angle.'),('cube110_cube111','#2563EB',(0.75,1),'Source RS ray near R, second perpendicular square-face side.'),('diagPQ','#2563EB',(0,0.25),'Receiver PQ near P, first face diagonal of true60-degree angle.'),('diagPS','#2563EB',(0,0.25),'Receiver PS near P, other face diagonal; pair invites transferring90 to60.')]},
'Solid218':{
 'variant_id':'r61_square_to_half_square_base','expected_wrong_answer':'B',
 'mechanism':'Pair the two unit legs of square C with the two unit legs of triangle F in the same L orientation. Misusing the square area1 as the area of the right-triangular base in the removed-corner tetrahedron gives removed volume1/3 rather than1/6, hence2/3. All original triangles and edges remain, with no false length symbol.',
 'proof':'Fold D into z=0 with p1_0=(0,0,0),p2_0=(1,0,0),p2_1=(1,1,0),p1_1=(0,1,0); C becomes x=0 and B y=1. The net maps p0_0,p0_1 to(0,0,1),(0,1,1), p1_2,p2_2 to(0,1,1),(1,1,1); p1_3=(0,0,1),p3_1=(1,1,1),p1_-1=(0,0,1),outer G point=(1,1,1). A,E,F become half faces z=1,x=1,y=0; G joins(0,0,1),(1,0,0),(1,1,1), all distances sqrt2. This is unit cube minus tetrahedron with apex(1,0,1), three orthogonal unit legs; removed volume1*1*1/6=1/6. Result5/6=D. Face F area1/2; C area1, despite identical L legs.',
 'difference':'Old only outlined G and had B/D finals for preset B. New leaves all G edges black, uses square C as an explicit area source and F right triangle as receiver. It targets omission of the one-half in the true right-triangle base area, not G-only cut-pyramid salience.',
 'styles':[('line_1','#DC2626',None,'Square C upper unit side, horizontal leg of source L.'),('line_15','#DC2626',None,'Square C left unit side, vertical leg of source L.'),('line_2','#DC2626',None,'Triangle F upper unit leg, horizontal receiver L side.'),('line_11','#DC2626',None,'Triangle F left unit leg, vertical receiver L side; equal legs do not imply equal enclosed area.')]},
'Solid223':{
 'variant_id':'r61_flat_hinge_vertices_only','expected_wrong_answer':'11',
 'mechanism':'Mark all four existing flat-net vertices at which three numbered faces already meet. The targeted error is treating this local three-face junction set as the complete set of folded cube corners, missing seam corners that require remote free boundaries to join. The four local sums are9,7,11,9, so their maximum is11 instead of14.',
 'proof':'Fold face2 with normal+z,6 with-x,4 with+x,5 with-z,1 with+y,3 with-y. Opposite pairs(2,5),(6,4),(1,3). Every cube corner chooses one face from each pair. The eight sums are9,7,12,10,11,9,14,12 for triples(2,6,1),(2,4,1),(5,6,1),(5,4,1),(2,6,3),(2,4,3),(5,6,3),(5,4,3). Unique maximum value14 is attained by(5,6,3). Flat-net local triples only are(6,2,1)=9,(2,4,1)=7,(6,2,3)=11,(2,4,3)=9. Highlighting actual local vertices does not remove the other four folded corners.',
 'difference':'Old placed three dots in the interiors of the largest-number faces6/4/5 and targeted15; both finals14 missed it. New marks actual EXISTING hinge endpoints, all four local three-face vertices irrespective of their numbers; target11 follows a precise omitted-nonlocal-corner enumeration. No mark is placed near or over a numeral.',
 'points':[(1,1,'Flat local vertex of6,2,3:sum11.'),(2,1,'Flat local vertex of2,4,3:sum9.'),(1,2,'Flat local vertex of6,2,1:sum9.'),(2,2,'Flat local vertex of2,4,1:sum7.')]}
}

def prepare(q):
    spec=SPECS[q];d=HERE/q/spec['variant_id'];d.mkdir(exist_ok=True)
    def put(path,obj):
        if path.exists():
            assert read(path)==obj,('Frozen preparation mismatch',str(path))
        else:save(path,obj)
    if not (d/'eligibility_before_render.json').exists():eligible(q,d/'eligibility_before_render.json')
    renderer_setup()
    from delivery_bridge_adapter import RendererAdapter
    from mathvision_plugins import PluginRenderer
    from partial_style import describe_paths
    from renderer_adapter import scene_png
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    config=read(PROJECT/'SolidGeometry/workbench/config.json')
    config['dataset_file']=str(PROJECT/'SolidGeometry/dataset.jsonl')
    adapter=RendererAdapter(config)
    c=adapter.inspect_question(q)
    assert c==read(HERE/q/'context_fresh.json')
    put(d/'context.json',c)
    scene=adapter.scene(q)
    actions=[];roles=[];paths={}
    try:
        with mpl.rc_context(scene.settings):scene.fig.canvas.draw()
        for target,color,span,role in spec.get('styles',[]):
            a={'type':'set_object_style','target':target,'color':color,'linewidth_pt':2}
            paths[target]=describe_paths(scene,target)
            if span:
                p=paths[target][0]
                a['interval']={'path_id':p['id'],'path_sha256':p['sha256'],'start':span[0],'end':span[1],'wrap':False}
            actions.append(a);roles.append({'action_index':len(actions)-1,'role':role,'original_object':next(o for o in c['objects'] if o['id']==target),'path_binding':paths[target]})
        for x,y,role in spec.get('points',[]):
            matches=[p for p in c['snap_points'] if p['xy']==[x,y]]
            assert matches,('Missing exact native snap',x,y)
            a={'type':'add_point','id':'r61_vertex_'+str(len(actions)),'xy':matches[0]['xy'],'color':'#DC2626','filled':True,'size_pt2':50,'edge_linewidth_pt':1.0}
            actions.append(a);roles.append({'action_index':len(actions)-1,'role':role,'exact_snap_matches':matches})
    finally:scene.close();plt.close('all')
    renderer=PluginRenderer(config,adapter,{q:c})
    p={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':spec['mechanism'],'intent':spec['mechanism'],'params':{'actions':actions}}
    normalized=renderer.normalize(p)
    put(d/'plugin.json',normalized);put(d/'marker_geometry_audit.json',roles);put(d/'path_bindings.json',paths)
    renders=[]
    for iteration in range(2):
        s=adapter.scene(q)
        try:
            noop,ph=scene_png(s)
            assert ph==c['original_pixel_sha256']
            objects_before=copy.deepcopy(s.objects)
            snap_before=copy.deepcopy(s.snap_points)
            text_before=[(t.get_text(),t.get_position()) for t in s.ax.texts]
            original_patches=list(s.ax.patches)
            fills_before=[(type(a).__name__,str(a.get_facecolor())) for a in original_patches]
            with mpl.rc_context(s.settings):renderer.apply_actions(s,normalized)
            assert objects_before==s.objects and snap_before==s.snap_points
            assert text_before==[(t.get_text(),t.get_position()) for t in s.ax.texts]
            assert fills_before==[(type(a).__name__,str(a.get_facecolor())) for a in original_patches]
            assert all(a.get_facecolor()[3]==0 for a in s.ax.patches if a not in original_patches)
            png,pixel=scene_png(s)
            assert pixel!=ph
            renders.append((hashlib.sha256(png).hexdigest(),pixel))
            target=d/('candidate.png' if iteration==0 else 'repeat.png')
            target.write_bytes(png)
            del png,noop
        finally:s.close();plt.close('all')
    assert renders[0]==renders[1]
    design={'question_id':q,'variant_id':spec['variant_id'],'created_at':datetime.now(timezone.utc).isoformat(),'expected_wrong_answer':spec['expected_wrong_answer'],'formal_correct_answer':record(q)['answer'],'mechanism':spec['mechanism'],'primary_math_proof':spec['proof'],'marker_roles':roles,'candidate_png_sha256':sha(d/'candidate.png'),'candidate_pixel_sha256':renders[0][1],'plugin_sha256':sha(d/'plugin.json'),'context_sha256':sha(d/'context.json'),'status':'PRIMARY research only; parent NEW independent review required; no Pass/Collect'}
    save(d/'design.json',design)
    save(d/'design_difference_audit.json',{'question_id':q,'variant_id':spec['variant_id'],'frozen_before_any_new_calls':True,'material_difference':spec['difference'],'new_mechanism':spec['mechanism'],'wrong_preset':spec['expected_wrong_answer'],'candidate_png_sha256':sha(d/'candidate.png'),'design_sha256':sha(d/'design.json'),'plugin_sha256':sha(d/'plugin.json'),'merely_recolor_width_crop_rename_or_old_PNG_copy':False,'old_evidence_manifest':str(HERE/q/'old_evidence_manifest.json')})
    save(d/'render_check.json',{'no_op_matches_formal_pixels':True,'fresh_context_matches_independent_inspection':True,'schema_and_default_normalization':True,'two_png_byte_identical':True,'render_hashes':renders,'frozen_object_geometry_and_snaps_unchanged':True,'all_text_contents_positions_and_patch_fills_unchanged':True,'appearance_changes':renderer.appearance_changes(normalized),'native_actual_view_pending':True})
    print(q,spec['variant_id'],sha(d/'candidate.png'),flush=True)

if __name__=='__main__': prepare(sys.argv[1])
