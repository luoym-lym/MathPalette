from tools_local import *
import math
q='Plane242';vid='diameter_and_ordered_sector_rays';out=HERE/q/vid
check=eligibility(q);assert check['eligible'],check
cfg,ad=adapter();before=inputs(ad,q);m=ad.inspect_question(q);objs={o['id']:o for o in m['objects']};scene=ad.scene(q)
try:
    scene.fig.canvas.draw();paths={o['id']:object_paths(scene,o['id']) for o in m['objects']}
finally:scene.close()
actions=[];roles=[];bindings=[]
for oid,part in [('image1_quarter','sourcewhite'),('option1_2','Bwhite'),('image1_semicircle','sourcegray'),('option1_0','Bgray')]:
    g=objs[oid]['geometry'];center=g['center'];p=paths[oid][0];radials=[]
    for j,s in enumerate(p['segments']):
        c=s['control'].tolist()
        if len(c)!=2:continue
        if math.dist(c[0],center)<1e-8:endpoint=c[1]
        elif math.dist(c[1],center)<1e-8:endpoint=c[0]
        else:continue
        if abs(math.dist(endpoint,center)-g['radius'])>1e-8:continue
        angle=math.degrees(math.atan2(endpoint[1]-center[1],endpoint[0]-center[0]))%360
        is_start=abs((angle-g['start_deg']+180)%360-180)<1e-7
        radials.append((j,angle,is_start,c))
    assert len(radials)==2,(oid,radials)
    for j,angle,is_start,c in radials:
        col='#16A34A' if 'gray' in part else ('#DC2626' if is_start else '#2563EB')
        interval={'path_id':p['id'],'path_sha256':p['sha256'],'start':j/len(p['segments']),'end':(j+1)/len(p['segments']),'wrap':False}
        actions.append({'type':'set_object_style','target':oid,'color':col,'linewidth_pt':2,'interval':interval})
        role=('One half of the actualgraysemicircle straightdiameter; sourceandB bothtruly have180degreegrayhalfdisks.' if 'gray' in part else ('Orderedstart(red)' if is_start else 'Orderedend(blue)')+' radialedge ofthewhitepiece; sourcequarter has90degrees andBwhitewedge45degrees, so this orderedraymatchisdeliberately insufficient for congruence.')
        roles.append({'action_index':len(actions)-1,'target':oid,'role':part+': '+role,'segment_index':j,'angle_deg':angle,'exact_path_control':c,'is_start_ray':is_start})
    bindings.append({'target':oid,'path_id':p['id'],'path_sha256':p['sha256'],'closed':p['closed'],'segment_count':len(p['segments']),'segments':[s['control'].tolist() for s in p['segments']]})
mechanism='Green matches the actualdiameters of the sourcegraysemicircle and Bgraysemicircle, a truecongruentfeature. Red/blue pair the orderedboundaryrays of the sourcewhitequartercircle with the orderedrays ofBwhite45degreewedge. Targets accepting the matchingdiameter plus correspondingrayorder instead of checking the whitepiece90degreeopening. The originalsource angle and Bsmallwedgearea remain fullyvisible.'
math='The source uncutgraysemicircle has180degrees andwhitequartercircle90degrees, same unitradius as theblackdisk. Withoutoverlap theircoveredregions must retain theseareasandcontiguity; remainingblackarea is90degrees. B correctly hasone180degreegraysector but whiteonly45degrees. Cgray135degrees; AandD splitgray into separatedsectors. Egray125to305 is180degreesandwhite350to440is90degrees, withtwo45degreeblacksectors. Thus E alone is possible. Thecolors neitherassertangleequality norchangetheactualshape.'
plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared wrong answer B','params':{'actions':actions}}
pr=PluginRenderer(cfg,ad,{q:m});normalized,png,pixels=pr.render(plugin);n2,png2,pixels2=pr.render(normalized,frozen=True)
assert normalized==n2 and png==png2 and pixels==pixels2 and before==inputs(ad,q)
out.mkdir(parents=True,exist_ok=False)
write(out/'eligibility_before_design.json',check);write(out/'context.json',m);write(out/'path_fingerprints.json',bindings);write(out/'plugin.json',normalized);(out/'candidate.png').write_bytes(png)
write(out/'design.json',{'question_id':q,'variant_id':vid,'created_at':now(),'expected_wrong_answer':'B','correct_answer':'E','mechanism':mechanism,'mathematical_solution':math,'marker_roles':roles,'human_semantics':'All8marks recolorexistingstraightsectoredges; nofilledregion,cut,radius,anglelabelorpointisadded. Inputgreenstraightdiameter and red/bluequarterrays preserve the exactsourcepieces. Bwhite45degreeopening remains visiblysmallerthan the90degreeinputquarter and canberejected byahuman. Orderedraysarefeatureidentitiesonly,notanexplicitangleequalitymark.','review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'})
write(out/'render_check.json',{'question_id':q,'baseline_pixel_match':True,'baseline_pixel_sha256':m['original_pixel_sha256'],'schema_default_normalized':True,'two_byte_identical_redraws':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'geometry_fill_labels_unchanged':True})
print(json.dumps({'qid':q,'variant':vid,'actions':len(actions),'png_sha256':file_hash(out/'candidate.png')}))
