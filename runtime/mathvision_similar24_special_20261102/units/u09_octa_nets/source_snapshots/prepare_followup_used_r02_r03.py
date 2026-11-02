from own_bootstrap import *
from unit_tools import eligibility
import copy

variant=sys.argv[1]
kind=sys.argv[2]
assert kind in ('four','two','four_blue_true_seam')
receiver={'four':('4','netedge2'),'two':('2','netedge9'),'four_blue_true_seam':('4','netedge2')}[kind]
preset,target=receiver
directory=OWN/'Solid166'/variant
directory.mkdir(parents=True,exist_ok=False)
elig=eligibility('Solid166')
save(directory/'eligibility_before_design.json',elig,exclusive=True)
plugin={'plugin_schema_version':'1.0.0','question_id':'Solid166','category':'C','operation':'C_manual',
  'description':'Compare target x with existing edge'+preset+' as a specific candidate closure boundary.',
  'intent':'Follow the two indicated original net boundaries without changing fold geometry.',
  'params':{'actions':[{'type':'set_object_style','target':'netedge15','color':'#DC2626'},
                       {'type':'set_object_style','target':target,'color':'#DC2626'}]}}
roles=[{'action_index':0,'source':'queried edge x','target':'netedge15','use':'Identifies the boundary whose second endpoint must be tracked through folds.'},
       {'action_index':1,'source':'shared-red comparison from x','target':target,'use':
          'Compare the opposite open end of the central strip (label4) with the target terminal flap; a proposed long-range end closure, not an asserted color-matching rule.' if preset=='4' else
          'Compare the top free strip boundary2 with the target lower terminal flap. This tests the across-strip boundary alignment, different from either opposite flap3 or adjacent sloping boundary1.'}]
if kind=='four_blue_true_seam':
    plugin['params']['actions'] += [{'type':'set_object_style','target':'netedge13','color':'#2563EB'},
                                   {'type':'set_object_style','target':'netedge9','color':'#2563EB'}]
    roles += [{'action_index':2,'source':'actual folded endpoints of edge3, {+e1,-e3}','target':'netedge13','use':'Provides an independently verified true seam source, helping orient how the top flap closes.'},
              {'action_index':3,'source':'edge3 actual folded seam','target':'netedge9','use':'Receives the true blue seam correspondence3–2, so the proposed red opposite-end closure is compared alongside a valid closure.'}]
save(directory/'plugin.json',plugin,exclusive=True)
transfer=load(OWN/'Solid166/r01_terminal_x_three/reference_transfer.json')
transfer['migration']='Use the current Solid203 two-original-edge comparison method on a different receiver in Solid166: target x versus boundary'+preset+'. This tests '+('opposite open strip ends' if preset=='4' else 'top strip boundary against bottom terminal flap')+'.'
if kind=='four_blue_true_seam':
    transfer['migration']+=' Add one blue, mathematically true seam3–2 as a reference for folding the red pair; this is an additional substantive information correspondence, not a width/color restyling of the failed red pair.'
transfer['roles']=roles
transfer['minimality']=str(len(roles))+' actions on distinct original edges, one per information source or recipient, no overwritten attributes.'
save(directory/'reference_transfer.json',transfer,exclusive=True)
history=[]
for q in load(OWN/'history_selected.json'):
    if q['question_id']=='Solid166':
        for d in q['designs']:
            history.append({'origin':'old','path':d['design_path'],'variant':d['variant_id'],'preset':d['predeclared_wrong_answer'],
               'png_sha256':d['frozen_candidate_png_sha256'],'calls':d['unique_started_call_count_from_saved_records']})
for p in (OWN/'Solid166').glob('*/design.json'):
    if p.parent==directory:continue
    old=load(p)
    bindings=[load(b) for b in p.parent.rglob('binding.json')]
    history.append({'origin':'this unit','path':str(p),'variant':old['variant_id'],'preset':old['expected_wrong_answer'],
        'plugin':load(p.parent/'plugin.json')['params']['actions'],'bindings':[{'image_sha256':b['image_sha256'],'requested_runs':b['requested_runs']} for b in bindings]})
newdiff=('New red receiver4 is a different original paper boundary from old receiver1 and r01 receiver3. Although folded seam4 shares its endpoints with seam1, its flat source identity, location and propagation route differ; the hypothesis is closure of opposite open strip ends rather than adjacent right-hand flaps.' if preset=='4' else
         'New receiver2 is the top strip free edge, whereas r01 receiver3 is the upper-left flap and old receiver1 is the right sloping strip edge. Although2 and3 meet in the correct folding, this compares a different flat boundary to the target lower flap and tests a different shortcut across the strip.')
if kind=='four_blue_true_seam':newdiff+=' The red4 pair alone has already been tested and is never repeated: new blue3–2 correspondence supplies valid folding orientation information and changes the hypothesis about how seam comparison is read.'
audit={'question_id':'Solid166','known_old_and_current_designs':history,'new_material_difference':newdiff,
       'not_width_color_filename_only':True,'all_prior_failures_preserved':True,'old_raw_fully_read':True,'new_png_collision_audit_required_before_call':True}
save(directory/'history_difference.json',audit,exclusive=True)
math=load(OWN/'Solid166/primary_math.json')
endpoints=math['exhaustive_numbered_edge_test'][preset]['folded_endpoints']
assert not math['exhaustive_numbered_edge_test'][preset]['coincides_with_x']
design={'question_id':'Solid166','branch':'SolidGeometry','variant_id':variant,'created_at':now(),
 'status_at_freeze':'PRESET_FROZEN_BEFORE_ANY_NEW_CALL','correct_answer':'5','answer_type':'number','expected_wrong_answer':preset,
 'preset_semantics':{'letter':None,'value':preset,'meaning':'Edge bearing printed identifier'+preset},
 'information_hypothesis':('The two red boundaries at the open far ends of the strip may be prematurely treated as a single closure seam, selecting4.' if preset=='4' else
       'The red upper strip boundary and red lower flap boundary may be aligned as the closing pair across the strip, selecting2.')+
       (' The blue true3–2 seam provides a concrete accurate neighboring closure against which the red end closure can be judged.' if kind=='four_blue_true_seam' else ''),
 'independent_mathematics':{'derived_correct':'5','x_endpoints':math['target_x']['world'],'receiver_endpoints':endpoints,'different_endpoint_sets':True},
 'primary_math_path':str(OWN/'Solid166/primary_math.json'),'primary_math_sha256':sha(OWN/'Solid166/primary_math.json'),
 'primary_unique_correctness':'All five labels exhaustively tested using the eight distinct convex octahedral faces. All global orientations preserve seam equality; only5 meetsx.',
 'plugin_sha256':sha(directory/'plugin.json'),'reference_transfer_path':str(directory/'reference_transfer.json'),
 'reference_transfer_sha256':sha(directory/'reference_transfer.json'),'history_difference_path':str(directory/'history_difference.json'),
 'history_difference_sha256':sha(directory/'history_difference.json'),'eligibility_sha256':sha(directory/'eligibility_before_design.json'),
 'human_semantics_and_mark_roles':roles,
 'paper_edge_reading':'Ink on existing boundaries does not change which edges coincide; no direction to match ink, no result-picture options, new cuts or partitions. Literal colored-paper reading still has answer5.',
 'two_run_rule':'Exactly two complete final values must equal the frozen preset. No third call, relabel, retest, retry, output selection or hidden extra control.',
 'scope':'PRIMARY research only; no independent second review, user approval, Pass, Collect or delivery.'}
save(directory/'design.json',design,exclusive=True)
print('Frozen',variant,'preset',preset,'actions',len(roles))
