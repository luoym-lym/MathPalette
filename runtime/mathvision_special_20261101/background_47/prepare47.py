from env47 import *
import json
import itertools
from fractions import Fraction as F
from datetime import datetime, timezone
from inspect47 import IDS, BRANCH, eligibility

sys.path.insert(0,str(BRANCH/'workbench'))
from workbench_io import load_config, pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from dataset_tools.mathvision_workbench import png_bytes
from partial_style import object_paths, portion
import numpy as np
from PIL import Image
import io

def area(points):
    return abs(sum(F(str(a[0]))*F(str(b[1]))-F(str(a[1]))*F(str(b[0])) for a,b in zip(points,points[1:]+points[:1])))/2

def proof(qid):
    s=json.loads((OWN/qid/'formal_scene_snapshot.json').read_text(encoding='utf-8'))
    pp=s['points']; oo={o['id']:o for o in s['objects']}
    def pts(oid):return [pp[k] for k in oo[oid]['points']]
    if qid=='Plane452':
        dims=[(1,6),(2,4),(5,6),(2,7),(2,3)]
        solutions=[]
        for perm in itertools.permutations(range(5)):
            for turns in itertools.product([0,1],repeat=4):
                top,right,bottom,left=[dims[i][::(-1 if t else 1)] for i,t in zip(perm[:4],turns)]
                if top[0]+right[0]!=8 or top[1]+left[1]!=8 or right[1]+bottom[1]!=8 or bottom[0]+left[0]!=8:continue
                center=(8-left[0]-right[0],8-top[1]-bottom[1])
                if min(center)>0 and sorted(center)==sorted(dims[perm[4]]):
                    solutions.append({'permutation_top_right_bottom_left_center':list(perm),'oriented_dimensions':[list(v) for v in [top,right,bottom,left,center]],'center_letter':'ABCDE'[perm[4]]})
        assert solutions and {v['center_letter'] for v in solutions}=={'B'}
        return {'answer':'B','derivation':'Total rectangle area 6+8+30+14+6=64, hence square side8. For the actual pinwheel topology write top(wt,ht),right(wr,hr),bottom(wb,hb),left(wl,hl). Boundary equations wt+wr=ht+hl=hr+hb=wb+wl=8; center is (8-wl-wr,8-ht-hb). Enumerate all120 assignments and16 orientations; only center2x4 survives. This uses list dimensions and topology, never screenshot lengths.','solutions':solutions,'unique_source_assignment':False,'limitation':'Outer assignments rotate through the four roles. In particular the narrow-looking right block is not uniquely D from the stated dimensions/topology; not drawn to scale forbids resolving this by its pixel aspect.'}
    if qid=='Plane456':
        vals={oid:str(area(pts(oid))) for oid in ['grayIbottom','grayItop','grayII','leftdiamond','rightdiamond']}
        return {'answer':'A','shaded_component_areas_for_outer_side2':vals,'outer_area':4,'derivation':'With outer side2, I diagonal meets the vertical midline at(1,1); its two shaded right triangles each have legs1 and1 and area1/2. II shaded quarter square has area1. In III the midpoint diamond and two main diagonals intersect at(6.5,1.5),(6.5,.5),(7.5,1.5),(7.5,.5). Each shaded diamond has perpendicular diagonals1 and1, area1/2. All three sums1, i.e.1/4 of each large square. A is the only choice asserting all equal.','semantic_target':'Only pre-existing gray interiors count; colored outlines do not add shaded pieces.'}
    if qid=='Plane457':
        return {'answer':'50','derivation':'Outer area100^2=10000. Disjoint four congruent L regions consume4*(3/16)*10000=7500. Center square area2500; its positive side sqrt2500=50. This determines the unique answer without measuring the picture.','margin_qualification':'The frozen symmetric layout has outer side4, center side2 and each radial connector length1. Under the correct100:4 scale these are100,50,25. The margin25 is a derived corroboration in the displayed symmetric layout, not an additional printed dimension or an independent given; the area proof needs no margin assumption.'}
    if qid=='Plane458':
        return {'answer':'B','vertices':pts('triangle'),'shoelace_area':str(area(pts('triangle'))),'derivation':'20 original dots form a5-column4-row unit grid. A=(0,0),B=(3,2),C=(4,3), not B=(4,2) or C=(5,3). |3*3-2*4|/2=1/2. For the auxiliary comparison cell D=(4,2), BC=sqrt2; A and D are on opposite sides of x-y=1 at distance1/sqrt2. Thus ABC and DBC each have area1/2, whereas the full one-by-one cell has area1. Only B gives1/2.','target_identity':'ABC stays the single labeled original triangle; D is only an existing unlabeled grid dot. No new point is drawn.'}
    if qid=='Plane460':
        import math
        p=pts('boundary')
        b=sum(math.gcd(abs(a[0]-v[0]),abs(a[1]-v[1])) for a,v in zip(p,p[1:]+p[:1]))
        assert area(p)==6 and b==12
        return {'answer':'6','vertices':p,'shoelace_area':'6','boundary_lattice_points':b,'interior_lattice_points':[[1,1]],'pick_area':'1+12/2-1=6','derivation':'Relative to the3-by2 rectangle [0,3]x[0,2], add the upper half-unit triangle(1,2),(2,2),(2,3) and remove the lower half-unit triangle(1,0),(2,0),(2,1). They cancel, leaving area6. Direct exact shoelace and Pick agree. The left/right long vertical sides each span two adjacent intervals, not one.'}
    if qid=='Plane462':
        return {'answer':'E','I_vertices':pts('I'),'II_vertices':pts('II'),'areas':[str(area(pts(o))) for o in ['I','II']],'perimeters':['2+2sqrt2','1+2sqrt2+sqrt5'],'difference_II_minus_I':'sqrt5-1>0','derivation':'I is a parallelogram with unit vertical base and unit horizontal separation, area1. II ordered(2,1),(4,2),(3,1),(3,0) has shoelace area1. I side lengths sqrt2,1,sqrt2,1. II side lengths sqrt5,sqrt2,1,sqrt2. Thus equal area and smaller perimeter I, uniquely E. In particular the red II side has Δx2,Δy1 and lengthsqrt5 even though it spans one vertical row.'}
    if qid=='Plane463':
        return {'answer':'21','vertices':pts('kite'),'point_count':56,'shoelace_area':str(area(pts('kite'))),'derivation':'Only one kite is pictured: top(3,7),right(6,5),bottom(3,0),left(0,5). Seven columns and eight rows give six horizontal intervals and seven vertical intervals. Perpendicular diagonals are6in and7in, hence area6*7/2=21sq in. The large kite is described in text, not drawn. Tripling both dimensions would give189 for a different unasked kite.','large_kite_receiver_exists':False}
    if qid=='Plane465':
        motif=pts('gray0')
        assert area(motif)==16
        return {'answer':'B','complete_motif_vertices':motif,'exact_motif_area':'16','period_block':{'x':[0,6],'y':[5,11],'area':36},'dark_cell_decomposition':{'full_cells':12,'half_cells':8,'dark_area':'12+8/2=16'},'derivation':'The actually repeated grid motif has horizontal and vertical period6. In the complete upper-left6-by6 block the dark cross is twelve whole unit cells plus eight half cells, total16. Its top apex and left apex are three units from the corner; successive actual apices along either border are six units apart. For the opposite corners to have the same shown corner alignment, floor width and height must each be6 times a positive integer: the final apex is3 units from the other corner. Thus the finite rectangular floor is a union of complete6-by6 blocks and the global dark-area fraction is16/36=4/9, uniquely B. No infinite-area limit or crop-edge-as-floor-boundary assumption is used.','crop_qualification':'The ragged lower-right end is the illustration truncation, not an additional wall. Only top and left solid borders define the displayed corner. The period6 and half cells are verified in the fully displayed upper-left motif and its shown right/below repetitions.'}

DEFS={
 'Plane456':('r47_rotated_square_unit_transfer','B','Match two adjacent sides of the unit gray square II to two adjacent sides of EACH gray diamond III. The proposed error treats square shape/orientation matching as equal area, ignoring the scale1/sqrt2: it keeps I=II=1 but counts III as2, selecting B.', 'Old initial assessment saved no plugin or call: it feared fill changes/new dissection. New design uses only two existing open sides per already shaded square, never recolors fills or creates partitions.'),
 'Plane457':('r47_margin_unit_to_center_side','25','Bind the actual short radial margin connector to one full side of the center square, with the outer100-inch side as scale source. Proposed error copies the margin linear quarter-scale25 to the center side, confusing margin versus remaining square side.', 'Old assessment saved no design: center or arm salience lacked a receiver. New three-edge calibration binds an outer scale, one actual margin and one actual center side; no extra partition is drawn.'),
 'Plane458':('r47_unit_cell_to_shared_diagonal_triangle','D','Pair a true unit horizontal/vertical L in the empty grid with the unit L adjacent to BC. Proposed error assigns the full1x1 cell area1 to triangle ABC via its shared diagonal BC, forgetting that the equivalent adjacent half-cell triangle has area1/2.', 'Old v01 colored the entire ABC contour red, presetD, finalsB/D. New design leaves all original triangle edges black and draws four1pt unit projection spans between EXISTING dots; it supplies an actual one-cell area source and receiver instead of whole-triangle salience. PresetD is retained prospectively for the new full-cell/half-triangle rule, not a relabel of the old one-hit.'),
 'Plane460':('r47_unit_span_to_two_interval_run','3','Pair the true one-unit bottom-left horizontal boundary edge with the full two-unit left and right vertical boundary runs. Proposed error treats each colored straight run as one length unit rather than counting the intermediate original dots; the balanced bump/notch cancel around width3 by mistaken height1, yielding3.', 'Old assessment rejected matching the two true half-triangle edges because that would aid correct cancellation. This new metric source/receiver is a true unit edge versus two longer unbroken straight edges, not the old cancellation pair or a new bounding contour.'),
 'Plane462':('r47_vertical_rise_to_slant_length','C','Match I left vertical unit edge to II long oblique edge by their one-row rise, and pair the other genuine vertical unit edges. Proposed error ignores II Δx2 and copies length1 to its sqrt5 edge. The two unchanged sqrt2 sides then give identical perimeter as well as equal area, C.', 'Old v01 colored both whole quadrilateral contours red; presetC, finalsE/E. New four selective existing-edge marks encode a specific one-row-rise-versus-Euclidean-length error with a true unit pair as calibration; diagonal families remain black. This is a structural grouping change, not mere palette/width replacement.'),
 'Plane465':('r47_full_cell_to_half_cell_count','D','Pair a fully gray unit cell open L with the catheti of all eight boundary half cells of one complete dark motif. Proposed error counts each half cell as the same whole unit as the source, producing(12+8)/36=5/9, choiceD.', 'Old assessment feared a highlighted complete6x6 contour would look like a new tile boundary or use the crop. This design marks only existing dashed unit-grid portions, in four open T groups at the real motif tips and one two-edge full-cell exemplar. No new6x6 frame, fill, boundary, tile or crop assumption is introduced.')
}

def make(qid,adapter,config):
    variant,preset,hypothesis,difference=DEFS[qid]
    root=OWN/qid/variant
    root.mkdir(parents=True,exist_ok=False)
    audit=eligibility(qid);assert audit['eligible']
    dump(root/'eligibility_before_design.json',audit)
    # Freeze difference and mathematical error BEFORE making any solver request.
    dump(root/'design_difference_audit.json',{'created_at':datetime.now(timezone.utc).isoformat(),'question_id':qid,'variant_id':variant,'substantive_new_difference':difference,'new_hypothesis_and_wrong_rule':hypothesis,'predeclared_wrong_answer':preset,'old_evidence_readonly':True,'old_manifest':str(OWN/qid/'old_file_manifest.json'),'not_just_color_width_crop_name':True,'no_posthoc_relabel':True})
    metadata=adapter.inspect_question(qid)
    scene=adapter.scene(qid)
    actions=[]; roles=[]; paths={}
    try:
        scene.fig.canvas.draw()
        def style_edge(target,index,color,role,width=2):
            path=object_paths(scene,target)[0]
            n=len(path['segments']);assert 0<=index<n
            control=path['segments'][index]['control'].tolist()
            a={'type':'set_object_style','target':target,'color':color,'linewidth_pt':width,'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':index/n,'end':(index+1)/n,'wrap':False}}
            actions.append(a);roles.append({'action_index':len(actions)-1,'role':role,'actual_selected_controls':[control],'actual_selected_length':float(np.linalg.norm(np.diff(control,axis=0),axis=1).sum())})
            paths[target]=[{k:p[k] for k in ['id','sha256','closed']}|{'controls':[x['control'].tolist() for x in p['segments']]} for p in object_paths(scene,target)]
        def whole(target,color,role,width=2):
            path=object_paths(scene,target)[0]
            actions.append({'type':'set_object_style','target':target,'color':color,'linewidth_pt':width})
            roles.append({'action_index':len(actions)-1,'role':role,'actual_selected_controls':[x['control'].tolist() for x in path['segments']]})
            paths[target]=[{k:p[k] for k in ['id','sha256','closed']}|{'controls':[x['control'].tolist() for x in p['segments']]} for p in object_paths(scene,target)]
        def grid_interval(target,startxy,endxy,color,role):
            path=object_paths(scene,target)[0];assert len(path['segments'])==1
            control=path['segments'][0]['control'];assert len(control)==2
            delta=control[1]-control[0]
            ts=[float(np.dot(np.array(v)-control[0],delta)/np.dot(delta,delta)) for v in [startxy,endxy]]
            for t,v in zip(ts,[startxy,endxy]):assert np.allclose(control[0]+t*delta,v,rtol=0,atol=1e-12)
            lo,hi=sorted(ts);lo=max(0.,lo);hi=min(1.,hi)
            actions.append({'type':'set_object_style','target':target,'color':color,'linewidth_pt':2,'interval':{'path_id':path['id'],'path_sha256':path['sha256'],'start':lo,'end':hi,'wrap':False}})
            selected=portion(control,lo,hi).tolist()
            roles.append({'action_index':len(actions)-1,'role':role,'actual_selected_controls':[selected],'intended_endpoints':[startxy,endxy],'original_dashes_preserved':True})
            paths[target]=[{k:p[k] for k in ['id','sha256','closed']}|{'controls':[x['control'].tolist() for x in p['segments']]} for p in object_paths(scene,target)]
        red='#DC2626';blue='#2563EB'
        if qid=='Plane456':
            for target,name in [('grayII','unit square II source'),('leftdiamond','left gray diamond III receiver'),('rightdiamond','right gray diamond III receiver')]:
                style_edge(target,0,red,name+': first complete original side, matches source square role despite its different actual length.')
                style_edge(target,1,blue,name+': adjacent perpendicular complete side; second orientation feature, same square-shape grouping without an equality mark.')
        elif qid=='Plane457':
            style_edge('outer',0,blue,'Outer bottom side: actual100-inch scale reference; no new numeric label.')
            whole('top',red,'Actual top radial connector, one frozen display unit long: margin source for the proposed quarter-scale length copy.')
            style_edge('inner',0,red,'Complete bottom side of center square, two display units long: receiver of the erroneous margin-length copy.')
        elif qid=='Plane458':
            snaps={p['id']:p['xy'] for p in metadata['snap_points']}
            for name,aa,bb,col,role in [('unitHorizontal','p03','p13',red,'One genuine horizontal grid interval source.'),('unitVertical','p02','p03',blue,'One genuine vertical grid interval source; paired with horizontal source supplies unit-cell scale.'),('receiverHorizontal','p32','p42',red,'B to existing right-neighbor dot: one horizontal cathetus of the BC cell receiver.'),('receiverVertical','p42','p43',blue,'Existing right-neighbor dot to C: one vertical cathetus of the BC cell receiver; does not represent ABC altitude.')]:
                assert aa in snaps and bb in snaps
                actions.append({'type':'add_line','id':name,'endpoints':[snaps[aa],snaps[bb]],'color':col,'linestyle':'solid'})
                roles.append({'action_index':len(actions)-1,'role':role,'source_snap_ids':[aa,bb],'full_precision_endpoints':[snaps[aa],snaps[bb]]})
        elif qid=='Plane460':
            style_edge('boundary',0,red,'True one-unit bottom-left boundary interval: source unit.')
            style_edge('boundary',4,red,'Full right two-unit vertical run: receiver wrongly counted as one unit; original intermediate p31 stays visible.')
            style_edge('boundary',9,red,'Full left two-unit vertical run: second receiver wrongly counted as one unit; original p01 stays visible.')
        elif qid=='Plane462':
            style_edge('I',3,red,'I left actual vertical unit edge: one-row-rise unit source.')
            style_edge('II',0,red,'II long oblique edge with Δx2,Δy1,lengthsqrt5: receiver of false rise-to-length correspondence.')
            style_edge('I',1,blue,'I right actual vertical unit edge: genuine calibration-pair source.')
            style_edge('II',2,blue,'II actual vertical unit edge: true unit counterpart; remaining two sqrt2 sides in each figure stay black.')
        elif qid=='Plane465':
            for target,a,b,col,role in [
                ('grid1_8',[2,8],[3,8],red,'Full gray unit cell(2..3,8..9) exemplar bottom side: whole-area source.'),
                ('grid0_2',[2,8],[2,9],blue,'Same fully gray unit cell exemplar left side: second scale direction.'),
                ('grid1_10',[2,10],[4,10],red,'Top-tip pair of half cells: two adjacent unit horizontal catheti, original midpoint grid intersection retained.'),
                ('grid0_3',[3,10],[3,11],blue,'Top-tip shared vertical unit cathetus: serves both half-cell receivers, no duplicate action.'),
                ('grid1_6',[2,6],[4,6],red,'Bottom-tip pair of half cells: two unit horizontal catheti.'),
                ('grid0_3',[3,5],[3,6],blue,'Bottom-tip shared vertical unit cathetus.'),
                ('grid1_8',[0,8],[1,8],red,'Left-tip shared horizontal unit cathetus.'),
                ('grid0_1',[1,7],[1,9],blue,'Left-tip pair: two adjacent unit vertical catheti.'),
                ('grid1_8',[5,8],[6,8],red,'Right-tip shared horizontal unit cathetus.'),
                ('grid0_5',[5,7],[5,9],blue,'Right-tip pair: two adjacent unit vertical catheti.')]:
                grid_interval(target,a,b,col,role)
        original_bytes=png_bytes(scene)
        assert pixel_hash(original_bytes)==pixel_hash(BRANCH/audit['record']['image'])
    finally:scene.close()
    plugin={'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual','description':hypothesis,'intent':hypothesis,'params':{'actions':actions}}
    renderer=PluginRenderer(config,adapter,{qid:metadata})
    plugin=renderer.normalize(plugin)
    normalized,one,pixel=renderer.render(plugin,frozen=True)
    normalized2,two,pixel2=renderer.render(plugin,frozen=True)
    assert plugin==normalized==normalized2 and one==two and pixel==pixel2
    assert sha(OWN/qid/'noop.png') or True
    (root/'candidate.png').write_bytes(one);(root/'repeat.png').write_bytes(two)
    dump(root/'plugin.json',plugin);dump(root/'context.json',metadata);dump(root/'path_fingerprints.json',paths)
    proofval=json.loads((OWN/qid/'math_proof.json').read_text(encoding='utf-8'))
    dump(root/'design.json',{'question_id':qid,'variant_id':variant,'created_at':datetime.now(timezone.utc).isoformat(),'expected_wrong_answer':preset,'formal_correct_answer':audit['record']['answer'],'geometric_error_rule':hypothesis,'material_difference':difference,'primary_math_proof':proofval,'per_marker_roles':roles,'plugin_path':str(root/'plugin.json'),'plugin_sha256':sha(root/'plugin.json'),'image_path':str(root/'candidate.png'),'image_sha256':sha(root/'candidate.png'),'pixel_sha256':pixel,'context_sha256':sha(root/'context.json'),'path_fingerprints_sha256':sha(root/'path_fingerprints.json'),'original_approval_content_sha256':audit['current_content_sha256'],'human_semantics':'Numerical metric/area comparison. Colors on existing edges or allowed auxiliary lines do not become explicit equality, length, fill or count conditions. Actual target outlines, all gray/white interiors, vertices/dots and labels remain. Task does not require carrying printed colors to another picture. Primary native visual review still required before calls.','approval_status':'UNREVIEWED research; no Pass/Collect or independent second review'})
    im=np.array(Image.open(io.BytesIO(one)).convert('RGBA')); orig=np.array(Image.open(io.BytesIO(original_bytes)).convert('RGBA'))
    diff=np.any(im!=orig,axis=2)
    dump(root/'render_check.json',{'adapter':'unchanged PlaneGeometry/workbench/mathvision_adapter.py RendererAdapter','renderer':'unchanged mathvision_plugins.PluginRenderer','baseline_pixel_equal':pixel_hash(original_bytes)==metadata['original_pixel_sha256'],'schema_and_normalization_pass':normalized==plugin,'two_consecutive_offline_PNG_bytes_equal':one==two,'png_sha256':sha(root/'candidate.png'),'repeat_sha256':sha(root/'repeat.png'),'pixel_sha256':pixel,'changed_pixels':int(diff.sum()),'native_visual_review_done':False,'all_actions':plugin['params']['actions'],'per_marker_roles':roles,'strict_own_directory_guard':True})
    print(json.dumps({'qid':qid,'variant':variant,'preset':preset,'actions':len(actions),'bytes_equal':one==two,'png':str(root/'candidate.png')},ensure_ascii=False),flush=True)

def main():
    for qid in IDS:
        dump(OWN/qid/'math_proof.json',proof(qid))
    for qid,reason in [('Plane452','Although centerB is proved by complete dimension/topology enumeration, the outer blocks can rotate through roles. A proposed right-block2x7-to-center transfer has no unique anchored2x7 source; using the apparent long narrow block would rely on a not-drawn-to-scale visual assignment. Other complete-span annotations either aid correct constraints or repeat old whole-center salience. No clean materially distinct numeric source/receiver selected.'),('Plane463','Real JPEG and PNG show only the small kite. No large-kite receiver exists for a3x/9x correspondence; adding one is forbidden. Unit/dot-count alternatives would require invented point grouping or merely make the correct6-by7 diagonal count more salient. Old189 preset missed with18/24, neither is relabeled. No concise distinct target-bound mechanism selected.')]:
        dump(OWN/qid/'primary_prescreen.json',{'question_id':qid,'status':'screened_no_design','reason':reason,'math_proof_path':str(OWN/qid/'math_proof.json'),'source_jpg_and_native_formal_png_viewed':True,'fresh_context_and_noop_pass':True,'calls':0,'arbitrary_action_cap':False})
    config=load_config();config['runtime_dir']=str(OWN/'wb_runtime_unused');config['output_dir']=str(OWN/'wb_output_unused')
    adapter=RendererAdapter(config)
    for qid in DEFS:make(qid,adapter,config)
    # Only bootstrap/path routing differ; actual solver payload and loop remain untouched.
    shared=ROOT/'harness/quicktest3_isolated.py'
    src=shared.read_text(encoding='utf-8')
    new=src.replace('PROJECT = Path(__file__).resolve().parents[3]','PROJECT = Path(__file__).resolve().parents[4]')
    marker='from __future__ import annotations\n'
    insertion="\nimport sys\nfrom pathlib import Path\nsys.path.insert(0, str(Path(__file__).resolve().parent.parent))\nfrom env47 import ISOLATION\n"
    new=new.replace(marker,marker+insertion,1)
    h=OWN/'harness';h.mkdir(exist_ok=False)
    (h/'quicktest3_isolated.py').write_text(new,encoding='utf-8',newline='\n')
    import ast
    oldtree=ast.parse(src);newtree=ast.parse(new)
    funcs=lambda t:{n.name:ast.dump(n) for n in t.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
    assert funcs(oldtree)==funcs(newtree)
    dump(OWN/'harness_isolation_audit.json',{'shared_path':str(shared),'shared_sha256':sha(shared),'own_path':str(h/'quicktest3_isolated.py'),'own_sha256':sha(h/'quicktest3_isolated.py'),'changes':['PROJECT parent3 to parent4 for one additional own directory','env47 strict guard bootstrap before project imports'],'all_function_ASTs_identical':True,'profile_timeout_token_limit_payload_loop_unchanged':True})

if __name__=='__main__':main()
