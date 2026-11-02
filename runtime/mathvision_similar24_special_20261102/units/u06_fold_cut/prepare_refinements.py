from local_env import *
from api_gate import check_eligibility
import json

def interval(qid,target,first,end,color):
    p=read_json(OWN/qid/'raw_paths.json')[target][0];n=len(p['segments'])
    return {'type':'set_object_style','target':target,'color':color,
      'interval':{'path_id':p['id'],'path_sha256':p['sha256'],'start':first/n,'end':end/n,'wrap':False}}

manifest=[]
qid='Solid239';vid='endpoint_to_four_border_orbits'
actions=[interval(qid,'line148',0,.5,'#DC2626'),interval(qid,'line148',.5,1,'#2563EB')]
for first,color in [(1,'#DC2626'),(9,'#DC2626'),(5,'#2563EB'),(13,'#2563EB')]:
    actions.append(interval(qid,'line150',first,first+2,color))
roles=[
 {'action_index':0,'source':'Bottom-crease endpoint half of the one original dashed cut','receiver':'A upper/lower V pairs (actions 2,3)','information':'Red distinguishes which part of the existing cut is anchored at the bottom crease. It does not add a second cut or change the straight dashed line.','necessity':'First distinct source endpoint class.'},
 {'action_index':1,'source':'Right-crease endpoint half of the same dashed cut','receiver':'A left/right V pairs (actions 4,5)','information':'Blue distinguishes the other original crease endpoint. Red and blue meet on the same collinear cutting instruction.','necessity':'Second distinct endpoint class; no overlap or dead action.'}]
for i,(location,color) in enumerate([('bottom','red'),('top','red'),('right','blue'),('left','blue')],2):
    roles.append({'action_index':i,'source':'The corresponding colored endpoint class of the original cutting instruction',
                  'receiver':f'A {location} complete V notch, two original connected slants',
                  'information':f'{color} groups the opposite {location} border notch with its partner as if the two cut endpoints generated two independent boundary-notch orbits.',
                  'necessity':'One complete V counterpart, retaining its exact geometry and all uncut edge portions.'})
manifest.append((qid,vid,'A',actions,roles,
 'The current references use two concrete cut-origin groups and opposite hole pairs. This refinement distinguishes the two ENDPOINT halves of one specified cut and pairs them to two different opposite-border orbits. The source remains one continuous collinear dashed instruction, not two newly given cuts.',
 'Old D stopped one unfolding and inherited a crease as a hole base; old C substituted crease directions for cut directions. The new first B attempt compared one cut slope with two border Vs. This refinement introduces a different two-channel endpoint/crease relation and four border notches: bottom-crease endpoint -> top/bottom pair, right-crease endpoint -> left/right pair. It is not a palette swap or B-to-A substitution of the same four slants; it changes both the source feature partition and receiver orbit structure. Preset A is derived from this endpoint-as-independent-notch hypothesis, not from the previous C/E outputs.',
 'Only the already explicit dashed cutting instruction and A invalid boundary notches are colored. Instruction color is not a paper ink condition. The bands, layer order, folds and correct uncolored E are untouched; E remains the internal diamond under either instruction/annotation reading or an intrinsic color reading of the impossible A option.'))

qid='Plane220';vid='near_tangent_fold_contact_alias'
actions=[{'type':'set_object_style','target':'o6','color':'#2563EB'},
         interval(qid,'o7',19,30,'#2563EB'),interval(qid,'o8',19,30,'#2563EB'),
         interval(qid,'o7',50,56,'#DC2626'),interval(qid,'o8',50,56,'#DC2626')]
roles=[
 {'action_index':0,'source':'B existing dotted global fold line','receiver':'The two blue facing circular arcs (actions 1,2)','information':'Anchors the actual shown reflection axis to the apparent contact of the two loops. This is an existing instruction line, no new seam is drawn.','necessity':'Defines the particular contact location being compared.'},
 {'action_index':1,'source':'B left rounded boundary immediately facing the fold','receiver':'B right rounded boundary (action 2)','information':'Blue compares the near-tangent curved contact, inviting a zero-width boundary contact to be mistaken for the positive-width join of a single hole. Native polygon gap and curve shape remain exact.','necessity':'Left member of the contact comparison; color only, original 1pt kept.'},
 {'action_index':2,'source':'B right rounded boundary immediately facing the fold','receiver':'Action 1 and existing dotted fold','information':'Second near-tangent contact member. This is not a whole arc or a source cut-profile copy.','necessity':'Completes the contact comparison; no new bridge or fill.'},
 {'action_index':3,'source':'B left outward zigzag','receiver':'B right outward zigzag (action 4)','information':'Red pairs the outer reflected star tips, matching the direction a correct one-fold reflection must duplicate, while blue misleadingly supplies the apparent central join.','necessity':'Left member of a concrete outward-tip pair, not whole-option highlighting.'},
 {'action_index':4,'source':'B right outward zigzag','receiver':'Action 3','information':'Completes outer-tip correspondence. Rounded outer arcs and source paper stay black.','necessity':'Right member of the outward mirror pair.'}]
manifest.append((qid,vid,'B',actions,roles,
 'Transfer red/blue concrete cut-edge comparison from current Solid142/Solid167, with current Solid176 within-option pair comparison. Red marks the two outward reflected zigzags, blue the contact neighborhood and pre-existing global fold. Source remains untouched to avoid printed-edge ambiguity.',
 'Old C copied a single whole arc/star; old A colored full arcs and star tips as two disconnected raw copies. Initial new E compared inner/outer zigzags of two locally complete holes. This B hypothesis instead compares near-tangent circular boundaries to the already shown global fold and distinguishes contact from positive-width connectivity. No source contour is colored, no new seam/bridge is drawn, and no whole circular arc is colored. Prior B outward-tip substitution alone was rejected as immaterial; the new source/receiver relation is specifically the existing fold-to-local-contact relation, not that substitution. A prior B final on the E image is preserved as failure and supplies zero calls for this new image/preset.',
 'Source and correct D remain entirely unchanged. All new color lies on B existing instruction/invalid output contours. On a literal output-ink reading B is still invalid by disconnected interiors and D remains the only exact uncolored reflected cut. Blue line is the original dotted fold, not a new cut. Color-only 1pt styling retains the small native gap and does not fill or thicken it.'))

out=[]
for qid,vid,wrong,actions,roles,transfer,difference,semantics in manifest:
    ev=check_eligibility(qid,'before_material_refinement_design')
    assert ev['eligible'],ev['reasons']
    candidate=OWN/qid/vid
    save(candidate/'eligibility_before_design.json',ev,True)
    source=next(x for x in read_json(OWN/'primary_design_manifest.json') if x['question_id']==qid)
    old=Path(source['candidate_directory'])
    save(candidate/'plugin.json',{'plugin_schema_version':'1.0.0','question_id':qid,'category':'C','operation':'C_manual',
      'description':vid,'intent':'Compare specified cut endpoints or existing fold contact; preserve the unique original solution.',
      'params':{'actions':actions}},True)
    save(candidate/'mathematics.json',read_json(old/'mathematics.json'),True)
    save(candidate/'reference_transfer.json',{'current_nine_read_inventory':str(OWN/'reference_read_inventory.json'),
      'current_nine_PNGs_actually_viewed':True,'primary_current_refs':['Solid142','Solid167'],'migration':transfer,'old18_not_authority':True},True)
    save(candidate/'history_difference_audit.json',{'question_id':qid,'difference':difference,
      'old_full_read_inventory':str(OWN/qid/'history_files_read.json'),
      'previous_new_candidate_full_review':str(old/'manual_full_final_review.json'),'previous_frozen_preset_not_changed':True,
      'new_hypothesis_not_postoutput_relabel':True},True)
    save(candidate/'premodel_primary_reasoning.json',{'created_at':now(),'question_id':qid,'variant_id':vid,
      'expected_wrong_answer':wrong,'expected_wrong_value':wrong,'formal_correct_answer':source['correct_answer'],
      'each_action_role':roles,'human_semantics_both_readings':semantics,
      'conciseness':'One disjoint action per actual source class or counterpart. No points, auxiliary lines, labels, fills or fold/cut additions; no thickness changes.',
      'primary_only':True,'new_candidate_calls_at_creation':0,
      'prior_unit_requests':len(list(OWN.glob('*/*/actual_call_*_payload_gate.json'))),
      'native_candidate_visual_review_pending':True},True)
    out.append({'question_id':qid,'variant_id':vid,'expected_wrong_answer':wrong,'correct_answer':source['correct_answer'],'candidate_directory':str(candidate)})
save(OWN/'supplementary_design_manifest.json',out,True)
print(json.dumps(out,ensure_ascii=False,indent=2))
