from design_tools import *
q='Solid187';vid='r25_two_halves_counted_as_two_holes'
# Independently run the same exact faceframe algorithm on this question's current
# native material rectangles. Only the proof prefix is executed, no old render/call.
source=(TASK/'design170.py').read_text(encoding='utf-8')
proof_source=source[:source.index('\naudit=')].replace("q='Solid170';vid='r25_bent_opening_to_planar_window'", "q='Solid187';vid='r25_two_halves_counted_as_two_holes'")
exec(compile(proof_source,str(TASK/'design187.py'),'exec'),globals())
audit={'question_id':q,'variant_id':vid,'stage':'material_refinement','saved_before_any_calls':True,'prior_variants':['false_cap_notch_partner','paired_but_adjacent_edge_holes'],'old_presets':['B','D'],'old_complete_finals':[['D','C'],['D','C']],'old_mechanisms':'B design mispaired outercaps as onehole; D design correctlypaired bothphysicalholes but ignoredadjacent/oppositerelation.','new_feature_correspondence':'Differentcolors distinguish TOPandLEFT HALFcontours of justoneactualupperphysicalopening. Eachhalf maps toonecompleteA seamopening: redhalf toleftAopening, bluehalf torightAopening. The secondactualsourceopening staysblack.','new_misconception':'Treat thetwofacehalves of onephysicaledgeopening as two separateholes, substituting componentcount for physicalhole identity. Newpart-to-whole counting error is prior to globalplacement and closure.','material_difference':'Oldsourcecolorclasses eachrepresented onewholephysicalhole; newred/blue classes represent differentfaces of SAMEhole. NewAreceivers areeachcompleteholes, notBoutercaps orDgloballywrongpairs. This is neither recoloringthesamecorrespondence nor changinganoldobservedpreset.','expected_wrong_answer_frozen':'A','not_cosmetic_or_old_observed_answer_relabel':True,'human_semantics':'No newcut closure, fill, markpoint or removedsourcehole. The entireotherhole remains visibleblack, originalhiddendashes remain. A carefulhuman can countphysicalopenings and applyfoldproofC.','prior_evidence':str((TASK/'all_prior_same_question_evidence.json').relative_to(ROOT)),'no_independent_hold_or_reject_report_found':True}
write(TASK/q/'design_difference_audit.json',audit)
actions=[];roles=[]
for half,color,bounds in [(0,RED,(.7,1.3)),(1,BLUE,(1.7,2.3))]:
    for side in range(3):
        t=f'hole{half}_{side}';actions.append(style(t,color,1));roles.append(f'Actualupperphysicalhole half{half}, originalUcontour side{side}. Redtophalf andbluelefthalf arethetwofacecomponents of ONEopening. Originalvisibility/dashstyle retained. Bothhalfidentifiers feeddifferentAwholehole receivers.')
    lo,hi=bounds
    matches=[]
    for o in source_objects(q):
        if not o['id'].startswith('Aboundary') or not o.get('styleable'):continue
        pts=o['geometry'].get('points',[])
        if len(pts)!=2:continue
        a,b=np.array(pts[0]),np.array(pts[1])
        if min(a[0],b[0])<lo-1e-9 or max(a[0],b[0])>hi+1e-9:continue
        if min(a[2],b[2])<.35-1e-9 or max(a[2],b[2])>.65+1e-9:continue
        matches.append(o['id'])
    assert len(matches)==6,matches
    for t in matches:
        actions.append(style(t,color,1));roles.append(f'Acomplete seamopening atx{(lo+hi)/2:g}, actualcontour side{t}. Sixexistingsegments identifythefulltwofacehole intheflatnet. Itscolorbinds ittoONLYonefacehalf oftheupperphysicalsourcehole, encodingthespecificpart-to-whole mismatch.')
f=save_candidate(q,vid,'A',actions,roles,audit['new_misconception'],proof,TASK/q/'primary_math_proof.json');write(f/'design_difference_audit.json',audit);print(f)
