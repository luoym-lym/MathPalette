from tools_local import *
import math
q='Plane239';vid='ordered_four_segment_prefix_binding';out=HERE/q/vid
check=eligibility(q);assert check['eligible'],check
cfg,ad=adapter();before=inputs(ad,q);m=ad.inspect_question(q);objects={o['id']:o for o in m['objects']}
scene=ad.scene(q)
try:
    scene.fig.canvas.draw();paths={o['id']:object_paths(scene,o['id']) for o in m['objects']}
finally:scene.close()
source=['o7','o6','o5','o4'];target=['o28','o30','o31','o35'];colors=['#DC2626','#2563EB','#16A34A','#EA580C']
actions=[];roles=[];bindings=[];centers={}
for oid in source+target:
    pts=objects[oid]['geometry']['points'];centers[oid]=[(min(p[i] for p in pts)+max(p[i] for p in pts))/2 for i in range(2)]
for i,(s,t,col) in enumerate(zip(source,target,colors)):
    assert objects[s]['geometry']['fill_color']==objects[t]['geometry']['fill_color']
    for oid,role in [(s,'Actual source segment '+str(i+1)+' from the head: '+['marked head','first black body segment','first white body segment','second black body segment'][i]),(t,'Concrete C counterpart in the same head-black-white-black local contact order: prefix position'+str(i+1))]:
        actions.append({'type':'set_object_style','target':oid,'color':col,'linewidth_pt':2})
        roles.append({'action_index':len(actions)-1,'target':oid,'role':role,'head_to_tail_prefix_position':i+1,'exact_center_from_context_bbox':centers[oid],'source_geometry':objects[oid]['geometry']})
        p=paths[oid][0];bindings.append({'target':oid,'path_id':p['id'],'path_sha256':p['sha256'],'closed':p['closed'],'segments':[s['control'].tolist() for s in p['segments']]})
for sequence in [source,target]:assert all(abs(math.dist(centers[a],centers[b])-1)<1e-10 for a,b in zip(sequence,sequence[1:]))
mechanism='Four color pairs link the first four consecutive source segments from its marked head to a genuinely touching head-black-white-black prefix in C. Targets accepting a correct local four-segment order as evidence for the entire curled caterpillar, while overlooking that C has no contact path preserving the remaining four alternating segments. Each outline identifies one concrete ordered source body segment and its proposed C counterpart; no connecting line is added.'
math='The source order from the marked head is H,B,W,B,W,B,W,B. A curled representation needs a path visiting all eight touching body disks once in that order. Enumerating every head-started Hamiltonian path on the exact tangent-contact graph yields2 valid paths for A and0 each for B,C,D,E. For example A route o9,o14,o15,o11,o16,o12,o13,o17 is valid. The colored four-disk prefix in C (o28,o30,o31,o35) is genuinely valid locally, but cannot extend through the other four disks in the alternating order. Thus A remains unique. Incidental contacts between non-consecutive disks are allowed in the search; only consecutive body segments must touch.'
plugin={'plugin_schema_version':'1.0.0','question_id':q,'category':'C','operation':'C_manual','description':mechanism,'intent':'Predeclared wrong answer C','params':{'actions':actions}}
pr=PluginRenderer(cfg,ad,{q:m});normalized,png,pixels=pr.render(plugin);n2,png2,pixels2=pr.render(normalized,frozen=True)
assert normalized==n2 and png==png2 and pixels==pixels2 and before==inputs(ad,q)
out.mkdir(parents=True,exist_ok=False)
write(out/'eligibility_before_design.json',check);write(out/'context.json',m);write(out/'path_fingerprints.json',bindings);write(out/'plugin.json',normalized);(out/'candidate.png').write_bytes(png)
write(out/'design.json',{'question_id':q,'variant_id':vid,'created_at':now(),'expected_wrong_answer':'C','correct_answer':'A','mechanism':mechanism,'mathematical_solution':math,'marker_roles':roles,'exact_prefix_bindings':{'source':source,'targetC':target,'centers':centers,'all_local_consecutive_distances_equal_to_one':True},'human_semantics':'Colors are appearance correspondences on existing circles. Original black/white fills, head ring and eye, all eight body disks in each option, contacts and question letters remain unchanged. No new body segment, joint, path edge or directed arrow is added. The local colored prefix is mathematically genuine and does not claim a new fullchain as a condition.','review_status':'PRIMARY_ONLY_REQUIRES_NEW_PARENT_INDEPENDENT_REVIEW'})
write(out/'render_check.json',{'question_id':q,'baseline_pixel_match':True,'baseline_pixel_sha256':m['original_pixel_sha256'],'schema_default_normalized':True,'two_byte_identical_redraws':True,'png_sha256':file_hash(out/'candidate.png'),'pixel_sha256':pixels,'plugin_sha256':file_hash(out/'plugin.json'),'design_sha256':file_hash(out/'design.json'),'input_fingerprints':before,'isolation':ISOLATION,'geometry_fill_labels_unchanged':True})
print(json.dumps({'qid':q,'variant':vid,'actions':len(actions),'png_sha256':file_hash(out/'candidate.png')}))
