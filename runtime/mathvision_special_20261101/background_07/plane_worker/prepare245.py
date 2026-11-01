from tools_local import *
q='Plane245';vid='cut_vs_ghost_corner_edge_binding';out=HERE/q/vid
check=eligibility(q);assert check['eligible'],check
cfg,ad=adapter();before=inputs(ad,q);m=ad.inspect_question(q);scene=ad.scene(q)
try:
    scene.fig.canvas.draw();paths={o['id']:object_paths(scene,o['id']) for o in m['objects']}
finally:scene.close()
actions=[];roles=[];bindings=[]
def mark(oid,color,role,start=None,end=None):
    p=paths[oid][0];a={'type':'set_object_style','target':oid,'color':color,'linewidth_pt':2}
    if start is not None:a['interval']={'path_id':p['id'],'path_sha256':p['sha256'],'start':start/len(p['segments']),'end':end/len(p['segments']),'wrap':False}
    actions.append(a);roles.append({'action_index':len(actions)-1,'target':oid,'role':role,'segment_start':start,'segment_end':end})
    bindings.append({'target':oid,'path_id':p['id'],'path_sha256':p['sha256'],'closed':p['closed'],'segment_count':len(p['segments']),'segments':[s['control'].tolist() for s in p['segments']]})
assert len(paths['o104'][0]['segments'])==5
mark('o104','#DC2626','Actual slanted cut boundary of the folded paper. Red supplies the source feature falsely copied as the horizontal pair of A hole edges.',4,5)
mark('o105','#2563EB','Actual dashed vertical ghost leg of the removed corner. Blue distinguishes this fold/corner trace from the actual red cut; the lure falsely transfers its role into the vertical pair of A hole edges. Original dash style is preserved.')
for i in range(4):
    mark('o114','#DC2626' if i%2==0 else '#2563EB','A inner square hole edge '+str(i)+': '+('one of the two horizontal red counterparts proposed for the true slanted cut' if i%2==0 else 'one of the two vertical blue counterparts proposed for the ghost corner/fold trace')+'. This is a deliberately wrong role correspondence, not a true reflection image.',i,i+1)
mechanism='Separate the actual folded-paper diagonal cut (red) from one discarded-corner vertical ghost trace (blue), then pair these with alternating horizontalred and verticalblue edges of A inner square. Targets constructing a square hole partly from cut edges and partly from folded-corner/crease traces instead of reflecting the actual diagonalcut through both folds. The source diagonal remains slanted and the blue source remains dashed; those visible distinctions reject the false edge roles.'
math='The horizontal then vertical half-fold leaves one quarter of the original square, and its clipped lower-left corner is the original sheet centre. In coordinates where the centre is(0,0), the removed triangle is{x>=0,y>=0,x+y<0.75}. Reflection across both axes produces{|x|+|y|<0.75}, one centraldiamond opening, with the original square outerboundary untouched. B alone has that outerboundary and diamondhole. A squarehole sides are horizontal/vertical and cannot arise by those axis-reflections of the true45degreecut; C has no centralhole, D no centralhole plus outercornercuts, E adds outercornercuts. Thus B is unique. The ghost trace is not an extra cut and must not be included in the opened hole.'
plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared wrong answer A','params':{'actions':actions}}
pr=PluginRenderer(cfg,ad,{q:m});normalized,png,pixels=pr.render(plugin);n2,png2,pixels2=pr.render(normalized,frozen=True)
assert normalized==n2 and png==png2 and pixels==pixels2 and before==inputs(ad,q)
out.mkdir(parents=True,exist_ok=False)
write(out/'eligibility_before_design.json',check);write(out/'context.json',m);write(out/'path_fingerprints.json',bindings);write(out/'plugin.json',normalized);(out/'candidate.png').write_bytes(png)
write(out/'design.json',{'question_id':q,'variant_id':vid,'created_at':now(),'expected_wrong_answer':'A','correct_answer':'B','mechanism':mechanism,'mathematical_solution':math,'marker_roles':roles,'human_semantics':'Only two existing source edges and four existing A hole edges are recolored. The colored source edges form an open V; no new closed cut contour or fixed partition is drawn. Source blue stays dashed, red stays solid, fills and foldingarrows stay unchanged. The intended false transfer of sourceghost trace into an aperture must not be described as a real cut.','review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'})
write(out/'render_check.json',{'question_id':q,'baseline_pixel_match':True,'baseline_pixel_sha256':m['original_pixel_sha256'],'schema_default_normalized':True,'two_byte_identical_redraws':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'geometry_fill_labels_unchanged':True})
print(json.dumps({'qid':q,'variant':vid,'actions':len(actions),'png_sha256':file_hash(out/'candidate.png')}))
