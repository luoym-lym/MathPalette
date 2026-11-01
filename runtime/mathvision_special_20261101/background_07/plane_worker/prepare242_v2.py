from tools_local import *
import math
q='Plane242';vid='semicircle_and_ordered_sector_rays';out=HERE/q/vid
check=eligibility(q);assert check['eligible'],check
cfg,ad=adapter();before=inputs(ad,q);m=ad.inspect_question(q);objs={o['id']:o for o in m['objects']};scene=ad.scene(q)
try:
    scene.fig.canvas.draw();paths={o['id']:object_paths(scene,o['id']) for o in m['objects']}
finally:scene.close()
actions=[];roles=[];bindings=[]
def add(oid,p,start,end,color,role,extra=None):
    interval={'path_id':p['id'],'path_sha256':p['sha256'],'start':start/len(p['segments']),'end':end/len(p['segments']),'wrap':False}
    actions.append({'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2,'interval':interval});roles.append({'action_index':len(actions)-1,'target':oid,'role':role,'segment_start':start,'segment_end':end,**(extra or {})})
for oid,part in [('image1_quarter','sourcewhite'),('option1_2','Bwhite'),('image1_semicircle','sourcegray'),('option1_0','Bgray')]:
    g=objs[oid]['geometry'];center=g['center'];p=paths[oid][0]
    if 'gray' in part:
        curves=[j for j,s in enumerate(p['segments']) if len(s['control'])>2];assert curves==list(range(len(curves))) and curves
        add(oid,p,0,len(curves),'#16A34A',part+': the actual curved180degree semicircleboundary, sourceandB are truly congruent equalradius halfarcs. This is visibleanddistinctfromthewhitepiece red/blue rays.')
    else:
        radials=[]
        for j,s in enumerate(p['segments']):
            c=s['control'].tolist()
            if len(c)!=2:continue
            if math.dist(c[0],center)<1e-8:endpoint=c[1]
            elif math.dist(c[1],center)<1e-8:endpoint=c[0]
            else:continue
            if abs(math.dist(endpoint,center)-g['radius'])>1e-8:continue
            angle=math.degrees(math.atan2(endpoint[1]-center[1],endpoint[0]-center[0]))%360;is_start=abs((angle-g['start_deg']+180)%360-180)<1e-7;radials.append(j)
            add(oid,p,j,j+1,'#DC2626' if is_start else '#2563EB',part+': '+('ordered start(red)' if is_start else 'ordered end(blue)')+' boundaryray; sourceopening90degrees versus B45degrees remainexplicitlydifferent. Orderalonecannotestablishcongruence.',{'angle_deg':angle,'exact_path_control':c})
        assert len(radials)==2
    bindings.append({'target':oid,'path_id':p['id'],'path_sha256':p['sha256'],'closed':p['closed'],'segment_count':len(p['segments']),'segments':[s['control'].tolist() for s in p['segments']]})
previous=json.loads((HERE/q/'diameter_and_ordered_sector_rays/design.json').read_text());math=previous['mathematical_solution']
mechanism='Green pairs the actual180degree curvedboundary of the sourcegraysemicircle with the congruentgraysemicircle in B. Red/blue pair the orderedboundaryrays of the sourcewhitequarter with the orderedrays ofBwhite45degreewedge. Targets accepting a truegrayhalfarc match plus sameorderedwhiteedge identities without verifying the whitepiece90degreeopening. The actual90versus45degreeangleandareas remain clearlyvisible.'
plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared wrong answer B','params':{'actions':actions}}
pr=PluginRenderer(cfg,ad,{q:m});normalized,png,pixels=pr.render(plugin);n2,png2,pixels2=pr.render(normalized,frozen=True)
assert normalized==n2 and png==png2 and pixels==pixels2 and before==inputs(ad,q)
out.mkdir(parents=True,exist_ok=False)
write(out/'eligibility_before_design.json',check);write(out/'context.json',m);write(out/'path_fingerprints.json',bindings);write(out/'plugin.json',normalized);(out/'candidate.png').write_bytes(png)
write(out/'design.json',{'question_id':q,'variant_id':vid,'created_at':now(),'expected_wrong_answer':'B','correct_answer':'E','mechanism':mechanism,'mathematical_solution':math,'marker_roles':roles,'human_semantics':'Allsixmarks recolorexistingsectoredges: two fullcurvedsemicirclearcsandfour straightwhiteboundaryrays. No text,angleequalitysymbol,cut,point,fillorregion isadded. Sourcewhite90degreequarterandBwhite45degreewedge stay visiblynoncongruent. Thegreenarcs reallyarecongruent. Localorderedrays do not assertangleequality.','review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'})
write(out/'render_check.json',{'question_id':q,'baseline_pixel_match':True,'baseline_pixel_sha256':m['original_pixel_sha256'],'schema_default_normalized':True,'two_byte_identical_redraws':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'geometry_fill_labels_unchanged':True})
print(json.dumps({'qid':q,'variant':vid,'actions':len(actions),'png_sha256':file_hash(out/'candidate.png')}))
