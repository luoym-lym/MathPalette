from env50 import *
from inspect50 import IDS,BRANCH,eligibility
from dataset_tools.catalog import read
from datetime import datetime,timezone
from fractions import Fraction as F
sys.path.insert(0,str(BRANCH/'workbench'))
from workbench_io import load_config,pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from partial_style import object_paths,portion
from dataset_tools.mathvision_workbench import png_bytes
import numpy as np
PROOFS={
'Plane170':{'answer_in_formal':'12','independent_unique_answer_proved':False,'finding':'Actual source JPEG and formal PNG show ONLY one2-by1 rectangular stone and its dimensions. No small-square path arrangements or target square are present. If5 means inner side of a one-unit-wide square border, area(7^2-5^2)/2=12 stones; if5 means outer side, area(5^2-3^2)/2=8. These conventions cannot be resolved from the displayed arrangement. Do not manufacture a layout or call a conditional12 derivation a unique proof. Formal source/approval left unchanged.'},
'Plane176':{'unique_answer':'16','proof':'Nine original gray cells occupy exactly five rows y2..6 and five columns x2..6. Direct shared-edge counting gives perimeter4*9-2*8=20. For any finite union of unit cells, if r rows and c columns are occupied then perimeter>=2(r+c), and area<=rc<=((r+c)/2)^2. At perimeter<=20 area<=25. The bounding5x5 square has area25 and perimeter20 and contains all nine cells, so16 is achievable and is the unique maximum. At area25 equality forces the same5 rows and5 columns, hence the complete original bounding5x5 block. This is the standard maximal reading of how many more; without maximal intent smaller additions are possible.','gray_cells':[[2,2],[3,2],[3,3],[4,3],[4,4],[5,4],[5,5],[6,5],[6,6]],'new_wrong_rule':'Treat initial two-gray-neighbor test as a one-time independent exhaustive test. Initially exactly7 blank cells have two gray edge neighbors. Each is locally ΔP=4-2*2=0, but newly gray cells enable further cells, giving16 overall.','initial_two_neighbor_cells':[[2,3],[3,4],[4,2],[4,5],[5,3],[5,6],[6,4]]},
'Plane177':{'unique_answer':'C','proof':'Use the actual8-by6 equal-square board with outgoing ray at(0,2),velocity(1,1). Specular wall hits in order(4,6),(8,2),(6,0),(0,6). In unfolded coordinates a corner needs t=8k and2+t=6m. Least positive solution k2,m3 gives t16 and folded coordinate(0,6)=C, with no earlier corner. Original incoming/outgoing ray,45-degree arc and pockets untouched.','skip':'No drawn later billiard trajectory or second true45-degree traveling segment exists. Coloring grid/table sides to suggest an alternative pocket has no specific wrong ray-to-ray receiver; adding a false continuation or rebound point would violate target identity. No new marks/calls.'},
'Plane180':{'unique_answer':'C','value_degrees':120,'proof':'Choose the original first crease horizontal. Original longitudinal ray has angle alpha=70 degrees. After the first reflection the two downward arm rays are L=180+alpha=250 and R=360-alpha=290; the small central isosceles triangle apex is180-2alpha=40. In the shown next folds each downward arm is reflected about the other original side of that central triangle. Reflection formula theta_new=2phi-theta gives left output2L-R=3alpha=210 and right output2R-L=540-3alpha=330. Their shown lower opening is330-210=540-6alpha=120, three times40; only C. The fold axes are the existing two sides of the central triangle, not invented right angles or an angle measured from pixels.','wrong_rule':'Copy the supplementary angle adjacent to alpha,180-70=110, onto beta, forgetting the two subsequent reflections.'},
'Plane181':{'unique_answer':'C','area_cm2':32,'proof':'A=(0,4),B=(0,0),C=(16,0),D=(16,4). The fold is perpendicular bisector AC:4x-y=30, so N=(7.5,0),M=(8.5,4). Quadrilateral NC DM is a trapezoid with parallel lengths NC=8.5,MD=7.5 and height4, area(8.5+7.5)*4/2=32. Reflection C->A,D->Dprime preserves area and sends it exactly to ANMDprime. Independent central symmetry through rectangle center also exchanges the two material halves.','triangle_check':'AM=8.5,MDprime=MD=7.5,ADprime=AB=4. Triangle ANM area17 and triangle AMDprime area15, sum32.','wrong_rule':'Transfer actual source MDprime length7.5 to receiver AM length8.5, using equal true width references ADprime=AB=4; then incorrectly assign both triangles area15 and output30(B). No equality marks are added.'},
'Plane182':{'unique_answer':'B','path_length':'28*pi/3','proof':'Triangle side=unit square side1. To roll from one attached square side to the next around a convex square corner, the triangle pivots through360-90-60=210 degrees=7pi/6. Four such corner pivots restore the unlabeled triangle footprint after one lap but rotate vertex identities by840 mod360=120 degrees, a3-cycle. Both the marked vertex and triangle first return after3laps=12pivots. Each of the three vertices is the fixed pivot4times; the marked vertex is stationary4times and moves on a radius1 arc8times. Thus8*7pi/6=28pi/3 uniquely B. Intermediate gray triangles are motion illustrations, not extra copies. The three trailing dots are an ellipsis, not count targets.','skip':'A source moving radius1 edge and a receiver edge attached to the marked stationary pivot are visible, but the receiver is not the marked point radius. Equal-looking side styles would require changing vertex ownership or misidentifying the original mark to claim an arc. The period error alone yields a first-lap marked path7pi/2 for this starting vertex, not any option;14pi/3(D) additionally counts the stationary pivot as a moving radius1 arc. No simple marker pairing was found to encode both errors without point/path ambiguity; no new motion depiction, point or call.'},
'Plane183':{'unique_answer':'10','proof':'A regular pentagon interior angle is108. At each shown inner ring junction two pentagon angles meet, leaving inner-hole angle360-2*108=144. Following the actual ring inner boundary turns180-144=36 degrees per plate. A complete simple ring turns360, hence360/36=10 plates. Translation/rotation repeats the same gluing role; no extra plate or radial seam is assumed.','wrong_rule':'Copy the single pentagon exterior turn180-108=72 to the inner ring boundary advance36, obtaining360/72=5.'},
'Plane197':{'unique_answer':'C','length_dm':46,'proof':'Centers of successive10 stones make9 original black segments. In the natural unrotated tile axes their vectors alternate(6,0) five times and(0,-4) four times. Rotations preserve length, so5*6+4*4=46dm uniquely C. Endpoints are centers, not outer tile ends.','skip':'Keeping every original black path segment black and identical excludes styling the actual source/receiver route. The drawn tile boundaries carry whole4/6 lengths but no separate drawn half-center spans. Matching outer L-corners would highlight a different boundary walk or count5 complete(6+4) motifs=50 without an actual center-distance receiver. Added half-span connectors would extend/branch the explicit black target and create the prohibited alternative route. Pure tile/endpoint salience is insufficient. No design/call.'}
}
DEFS={
'Plane176':('r50_initial_contact_to_global_fill','7','Two opposed open L contact frames pair a real initial two-gray-neighbor blank with another on the opposite side of the staircase. Proposed error transfers the local zero-perimeter-addition rule to a single simultaneous pass over the unchanged starting picture, counts7, and omits newly enabled cells.','Old initial assessment saved no design or calls and rejected a selected closed ten-cell completion patch. New4existing-edge styles show only two local concave contact frames, no new region or prescribed completion boundary.'),
'Plane180':('r50_supplementary_angle_role_transfer','D','Pair the original110-degree supplementary ray frame adjacent to alpha with the final beta boundary rays. Proposed error copies180-alpha=110 to beta rather than tracking three reflections.','Old initial assessment saved no design or calls and found no specific wrong angle. New design explicitly identifies the original adjacent supplementary rays and final angle rays; no whole-strip coloring or equal-angle symbol.'),
'Plane181':('r50_folded_leg_to_horizontal_base','B','Pair actual folded long leg MDprime=7.5 with horizontal AM=8.5, calibrated by actual equal widths ADprime=AB=4. Proposed error copies the former base into triangle ANM, counting15+15=30 instead of15+17=32.','Old initial assessment saved no design/calls and rejected gray-area or whole-region emphasis. Four selective existing segments encode a particular unequal-base transfer, with semantic gray and fold arrow unchanged.'),
'Plane183':('r50_plate_turn_to_ring_turn','5','Pair a two-edge outer vertex of the last displayed pentagon (interior108/exterior72) with the two inner-boundary edges at a shared junction (hole144/turn36). Proposed error uses72 per ring step and returns5.','Old initial assessment saved no design/calls: whole successive-side color lacked a selective correspondence and extra radii risked fake seams. New two separated open angle frames use4existing boundary-edge intervals, without whole contour or any added radius/center/seam.')
}
def make(q,config,adapter):
    variant,preset,hyp,diff=DEFS[q];d=OWN/q/variant;d.mkdir(exist_ok=False)
    e=eligibility(q);assert e['eligible'];dump(d/'eligibility_before_design.json',e)
    dump(d/'design_difference_audit.json',{'created_at':datetime.now(timezone.utc).isoformat(),'question_id':q,'variant_id':variant,'old_history_audit':str(OWN/'history_read_audit.json'),'difference':diff,'new_information_and_error':hyp,'expected_wrong_answer':preset,'not_cosmetic_or_old_retry':True})
    meta=adapter.inspect_question(q);s=adapter.scene(q);actions=[];roles=[];paths={}
    try:
        s.fig.canvas.draw()
        def edge(oid,k,col,role,t0=0.,t1=1.):
            pp=object_paths(s,oid);p=pp[0];n=len(p['segments']);c=p['segments'][k]['control'];assert len(c)==2
            a={'type':'set_object_style','target':oid,'color':col,'linewidth_pt':2,'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':(k+t0)/n,'end':(k+t1)/n,'wrap':False}}
            actions.append(a);selected=portion(c,t0,t1).tolist()
            roles.append({'action_index':len(actions)-1,'role':role,'selected_control_full_precision':selected,'original_selected_segment':c.tolist(),'segment_index':k,'segment_count':n,'length_display_units':float(np.linalg.norm(np.diff(np.array(selected),axis=0),axis=1).sum()),'no_new_geometry_or_relation_symbol':True})
            paths[oid]=[{kk:p2[kk] for kk in ['id','sha256','closed']}|{'controls':[seg['control'].tolist() for seg in p2['segments']]} for p2 in pp]
        red='#DC2626';blue='#2563EB'
        if q=='Plane176':
            edge('cell2_3',0,red,'SOURCE blank(2,3) lower contact edge to original gray(2,2): first of two replaced perimeter edges.')
            edge('cell2_3',1,red,'SOURCE same blank right contact edge to gray(3,3): establishes local k2,DeltaP0.')
            edge('cell4_2',2,red,'RECEIVER blank(4,2) upper contact edge to gray(4,3): opposite-side same local rule.')
            edge('cell4_2',3,red,'RECEIVER same blank left contact edge to gray(3,2): completes second local k2 frame; no cell filled.')
        elif q=='Plane180':
            edge('o1',0,red,'SOURCE horizontal crease ray from original alpha vertex to the right; original dashed style preserved.')
            p=object_paths(s,'o0')[0];c=p['segments'][3]['control'];av=np.array(read(OWN/q/'formal_scene_snapshot.json')['points']['aV']);delta=c[1]-c[0];t=float(np.dot(av-c[0],delta)/np.dot(delta,delta));assert np.allclose(c[0]+t*delta,av,rtol=0,atol=1e-12)
            edge('o0',3,red,'SOURCE opposite longitudinal ray below alpha vertex, forming supplementary110 with original horizontal crease; alpha70 arc stays untouched.',t,1.)
            edge('o10',2,red,'RECEIVER left lower arm ray bounding beta, actual orientation210; not a new fold.')
            edge('o11',1,red,'RECEIVER right lower arm ray bounding beta, actual orientation330; beta arc remains the original120 opening.')
        elif q=='Plane181':
            edge('o6',0,red,'SOURCE folded MDprime: actual former MD7.5; long leg of right triangle AMDprime.')
            edge('o3',0,red,'RECEIVER AM: actual8.5, horizontal base of triangle ANM; proposed false copy of7.5.')
            edge('o7',0,blue,'SOURCE true short width ADprime4, perpendicular to MDprime.')
            edge('o1',0,blue,'RECEIVER calibration AB4, the genuine vertical separation of N and AM; not a new altitude line.')
        elif q=='Plane183':
            edge('pentagon3',3,red,'SOURCE first edge at bottom outer pentagon vertex; with next edge gives intrinsic108 angle/exterior72.')
            edge('pentagon3',4,red,'SOURCE second edge of same last displayed pentagon, completes open intrinsic-angle frame.')
            edge('pentagon0',2,red,'RECEIVER upper inner-hole boundary edge terminating at the shared junction; not the glued seam.')
            edge('pentagon1',2,red,'RECEIVER lower inner-hole boundary edge leaving that junction, together hole144/turn36; not a radial line.')
        baseline=png_bytes(s);assert pixel_hash(baseline)==pixel_hash(BRANCH/e['record']['image'])
    finally:s.close()
    plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':hyp,'intent':hyp,'params':{'actions':actions}}
    r=PluginRenderer(config,adapter,{q:meta});plugin=r.normalize(plugin)
    np1,b1,h1=r.render(plugin,frozen=True);np2,b2,h2=r.render(plugin,frozen=True)
    assert plugin==np1==np2 and b1==b2 and h1==h2
    (d/'candidate.png').write_bytes(b1);(d/'repeat.png').write_bytes(b2)
    dump(d/'plugin.json',plugin);dump(d/'context.json',meta);dump(d/'path_fingerprints.json',paths)
    dump(d/'design.json',{'question_id':q,'variant_id':variant,'created_at':datetime.now(timezone.utc).isoformat(),'expected_wrong_answer':preset,'formal_correct_answer':e['record']['answer'],'hypothesis':hyp,'difference':diff,'primary_math_proof':PROOFS[q],'per_marker_roles':roles,'plugin_path':str(d/'plugin.json'),'plugin_sha256':sha(d/'plugin.json'),'image_path':str(d/'candidate.png'),'image_sha256':sha(d/'candidate.png'),'pixel_sha256':h1,'context_sha256':sha(d/'context.json'),'path_fingerprints_sha256':sha(d/'path_fingerprints.json'),'approval_content_sha256':e['current_content_sha256'],'human_semantics':'This asks for a numerical count, angle or area, not color-preserving picture completion. Existing-edge color does not add equality, angle, length, fill or cut conditions. Source/fold geometry and targets remain. A physical colored edge may remain ink without changing the requested numerical quantity; no matching colored-result option is required. Native review is a separate required pre-call step.','approval_status':'UNREVIEWED primary research only; parent must commission NEW independent second review.'})
    dump(d/'render_check.json',{'schema_normalization_idempotent':True,'no_op_pixel_equal_formal':True,'two_consecutive_offline_byte_equal':True,'image_sha256':sha(d/'candidate.png'),'repeat_sha256':sha(d/'repeat.png'),'pixel_sha256':h1,'native_png_viewed':False,'adapter_unchanged':True,'PluginRenderer_unchanged':True,'all_mark_roles':roles})
    print(q,variant,sha(d/'candidate.png'),flush=True)
def main():
    for q in IDS:
        e=eligibility(q);assert e['eligible'];dump(OWN/q/'eligibility_before_math.json',e);dump(OWN/q/'math_proof.json',PROOFS[q])
    gray={tuple(p) for p in PROOFS['Plane176']['gray_cells']};initial=sorted((x,y) for x in range(8) for y in range(8) if (x,y) not in gray and sum((x+dx,y+dy) in gray for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])>=2)
    assert initial==[tuple(p) for p in PROOFS['Plane176']['initial_two_neighbor_cells']]
    config=load_config();config['runtime_dir']=str(OWN/'unused_state');config['output_dir']=str(OWN/'unused_output');adapter=RendererAdapter(config)
    for q in DEFS:make(q,config,adapter)
if __name__=='__main__':main()
