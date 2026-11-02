from review_env import *
import io, copy, math
import numpy as np
from PIL import Image
from dataset_tools.catalog import rows, digest
from dataset_tools import mathvision_workbench as bridge
BRANCH=ROOT/'SolidGeometry'; BASE=ROOT/'runtime/mathvision_special_20261101'
CAND=BASE/'background_37/Solid126/r37_local_area_replacement'
sys.path.insert(0,str(BRANCH/'workbench'))
from renderer_adapter import scene_png
from render_plugins import PluginRenderer
from partial_style import object_paths
from workbench_io import pixel_hash, environment_versions
row=next(r for r in rows(BRANCH/'dataset.jsonl') if r['id']=='Solid126')
frozen=read(BRANCH/row['scene']);plugin=read(CAND/'plugin.json');design=read(CAND/'design.json')
context=read(CAND/'context.json');parentcontext=read(BASE/'background_37/Solid126/context.json')
scene=bridge.build_scene(BRANCH,row)
markers=[]
def lineinfo(line):
    return {'xy':line.get_xydata().tolist(),'gid':line.get_gid(),'color':line.get_color(),'linewidth_pt':line.get_linewidth(),'linestyle':line.get_linestyle(),'unscaled_dash_pattern':getattr(line,'_unscaled_dash_pattern',None),'zorder':line.get_zorder()}
def textinfo(text):
    return {'text':text.get_text(),'position':text.get_position(),'fontsize':text.get_fontsize(),'color':text.get_color(),'ha':text.get_ha(),'va':text.get_va(),'rotation':text.get_rotation()}
try:
    baseline_bytes,baseline_pixels=scene_png(scene)
    (OUT/'baseline_reproduced.png').write_bytes(baseline_bytes)
    scene.fig.canvas.draw()
    transform=np.array([[1,0,0],[0,-1,768],[0,0,1]])@scene.ax.transData.get_affine().get_matrix()
    metadata={'objects':copy.deepcopy(scene.objects),'xlim':list(scene.ax.get_xlim()),'ylim':list(scene.ax.get_ylim()),'original_pixel_sha256':baseline_pixels}
    class Adapter:
        def scene(self,qid):
            assert qid=='Solid126'
            return bridge.build_scene(BRANCH,row)
    config=read(BRANCH/'workbench/config.json')
    renderer=PluginRenderer(config,Adapter(),{'Solid126':metadata})
    normalized=renderer.normalize(plugin)
    before=[lineinfo(x) for x in scene.ax.lines];text_before=[textinfo(t) for t in scene.ax.texts]
    for index,action in enumerate(plugin['params']['actions']):
        target=action['target'];obj=next(o for o in scene.objects if o['id']==target)
        world=np.array(obj['geometry']['points'],dtype=float)
        M=np.array(frozen['projection']['matrix']);origin=np.array(frozen['projection']['origin']);offset=np.array(frozen['projection']['offset'])
        xy=(world-origin)@M.T+offset
        projected=scene.artists[target][0].get_xydata()
        paths=object_paths(scene,target)
        markers.append({'action_index':index,'target':target,'action':action,'world_endpoints':world.tolist(),'exact_projected_endpoints':xy.tolist(),'native_pixel_endpoints':(np.c_[xy,np.ones(len(xy))]@transform.T)[:,:2].tolist(),'world_length':float(np.linalg.norm(world[1]-world[0])),'source_role':obj['role'],'frozen_visibility':obj['frozen_visibility'],'source_linestyle':obj['geometry'].get('linestyle','solid'),'actual_artist_linestyle_before':scene.artists[target][0].get_linestyle(),'geometry_sha256':digest(obj['geometry']),'geometry_matches_design':digest(obj['geometry'])==design['pretest_marker_roles'][index]['source_object_geometry_sha256'],'endpoints_match_design':np.array_equal(world,np.array(design['pretest_marker_roles'][index]['world_endpoints'])),'projected_path_matches_geometry':bool(np.array_equal(xy,projected)),'styleable':obj['styleable'],'artist_count':len(scene.artists[target]),'paths':[{'id':p['id'],'sha256':p['sha256'],'closed':p['closed'],'exact_controls':[s['control'].tolist() for s in p['segments']]} for p in paths]})
    renderer.apply_actions(scene,normalized)
    same_scene_bytes,same_scene_pixels=scene_png(scene)
    after=[lineinfo(x) for x in scene.ax.lines];text_after=[textinfo(t) for t in scene.ax.texts]
    for m in markers:
        artist=scene.artists[m['target']][0]
        m['actual_artist_linestyle_after']=artist.get_linestyle();m['actual_artist_linewidth_after']=artist.get_linewidth();m['actual_artist_color_after']=artist.get_color()
    altered=[{'index':i,'before':a,'after':b} for i,(a,b) in enumerate(zip(before,after)) if a!=b]
    appearances=renderer.appearance_changes(normalized)
    preserved={'line_count':len(before)==len(after),'line_geometry_all':all(a['xy']==b['xy'] for a,b in zip(before,after)),'line_gid_all':all(a['gid']==b['gid'] for a,b in zip(before,after)),'linestyle_all':all(a['linestyle']==b['linestyle'] for a,b in zip(before,after)),'unscaled_dash_pattern_all':all(a['unscaled_dash_pattern']==b['unscaled_dash_pattern'] for a,b in zip(before,after)),'text_and_dimension_artists_all':text_before==text_after,'no_patch_or_fill_added':len(scene.ax.patches)==0,'exact_six_changed_original_artists':len(altered)==6 and {x['after']['gid'] for x in altered}=={a['target'] for a in plugin['params']['actions']},'only_color_and_linewidth_changed':all({k:v for k,v in a.items() if k not in ('color','linewidth_pt')}=={k:v for k,v in b.items() if k not in ('color','linewidth_pt')} for a,b in zip(before,after))}
finally:scene.close()
normal1,data1,pix1=renderer.render(plugin);normal2,data2,pix2=renderer.render(plugin)
(OUT/'candidate_reproduced_01.png').write_bytes(data1);(OUT/'candidate_reproduced_02.png').write_bytes(data2)
with Image.open(BRANCH/row['image']) as im:formal=np.array(im.convert('RGBA'))
with Image.open(CAND/'candidate.png') as im:candidate=np.array(im.convert('RGBA'))
with Image.open(io.BytesIO(baseline_bytes)) as im:baseline=np.array(im.convert('RGBA'))
diff=np.any(formal!=candidate,axis=2);ys,xs=np.where(diff)
points=np.c_[xs+.5,ys+.5]
def distances(points,a,b):
    a=np.array(a);b=np.array(b);v=b-a;t=np.clip(((points-a)@v)/(v@v),0,1)
    return np.linalg.norm(points-a-t[:,None]*v,axis=1)
dists=np.stack([distances(points,*m['native_pixel_endpoints']) for m in markers])
footprint={'changed_pixel_count':int(diff.sum()),'difference_bbox_xyxy':[int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())],'max_distance_of_any_changed_pixel_from_six_original_segments_px':float(dists.min(axis=0).max()),'all_changed_pixels_within_3px_of_original_paths':bool(np.all(dists.min(axis=0)<3))}
grid_y,grid_x=np.mgrid[0:768,0:768];allpoints=np.c_[grid_x.ravel()+.5,grid_y.ravel()+.5]
for m in markers:
    color=tuple(int(m['action']['color'][i:i+2],16) for i in (1,3,5))
    exact=np.all(candidate[:,:,:3]==color,axis=2).ravel()
    nearby=distances(allpoints,*m['native_pixel_endpoints'])<2.5
    m['exact_color_pixels_within_2_5px_of_own_path']=int(np.count_nonzero(exact & nearby))
    m['changed_pixels_within_3px_of_own_path']=int(np.count_nonzero((distances(points,*m['native_pixel_endpoints'])<3)))
# Independent integer-cell boundary count, with no shared area helper.
original={(x,y,z) for x in range(12) for y in range(6) for z in range(8)}
removed={(x,y,z) for x in range(9) for y in range(6) for z in range(5,8)}
remaining=original-removed
directions=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def exterior(cells):
    return {str(d):sum(tuple(c[i]+d[i] for i in range(3)) not in cells for c in cells) for d in directions}
oareas=exterior(original);nareas=exterior(remaining)
cross=[(0,0),(12,0),(12,8),(9,8),(9,5),(0,5)]
area2=abs(sum(cross[i][0]*cross[(i+1)%6][1]-cross[(i+1)%6][0]*cross[i][1] for i in range(6)))
perimeter=sum(abs(cross[i][0]-cross[(i+1)%6][0])+abs(cross[i][1]-cross[(i+1)%6][1]) for i in range(6))
mathaudit={'method':'Independent integer unit-cell six-neighbor external boundary enumeration; independent shoelace area and edge-length perimeter. No shared box/ground-exclusion helper imported.','source_dimensions':{'width':12,'height':8,'depth':6,'remaining_left_height':5,'remaining_right_width':3},'removed_dimensions':{'width':12-3,'height':8-5,'depth':6},'original_cell_count':len(original),'removed_cell_count':len(removed),'remaining_cell_count':len(remaining),'original_exterior_faces_by_direction':oareas,'remaining_exterior_faces_by_direction':nareas,'original_area':sum(oareas.values()),'remaining_area':sum(nareas.values()),'loss':sum(oareas.values())-sum(nareas.values()),'loss_fraction':'1/8','loss_percent':12.5,'cross_section_vertices_xz':cross,'cross_section_area_shoelace':area2/2,'cross_section_perimeter':perimeter,'remaining_prism_area':2*(area2/2)+perimeter*6,'correct_choice':'B','ground_bottom_included':True}
audit={'checked_at':stamp(),'pid':os.getpid(),'isolation':ISOLATION,'environment':environment_versions(),'baseline_formal_pixel_match':np.array_equal(baseline,formal),'baseline_formal_byte_match':baseline_bytes==(BRANCH/row['image']).read_bytes(),'baseline_sha256':hashlib.sha256(baseline_bytes).hexdigest(),'baseline_pixel_sha256':baseline_pixels,'normalized_plugin_equals_frozen':normalized==plugin,'candidate_exact_bytes_reproduced_twice':data1==data2==(CAND/'candidate.png').read_bytes(),'candidate_direct_apply_exact_bytes':same_scene_bytes==data1,'candidate_pixel_hashes':[pix1,pix2],'candidate_sha256':hashlib.sha256(data1).hexdigest(),'candidate_size':[768,768],'opaque':bool(np.all(candidate[:,:,3]==255)),'original_objects_match_both_saved_contexts':metadata['objects']==context['objects']==parentcontext['objects'],'canvas_data_to_pixel':transform.tolist(),'frozen_fields':{'projection':frozen['projection'],'view':frozen['view'],'visibility':frozen['visibility'],'dimensions':frozen['dimensions'],'labels':frozen['labels'],'fill_object_count':sum(x['type']=='face' for x in frozen['objects'])},'preservation_checks':preserved,'appearance_changes':appearances,'markers':markers,'changed_artists':altered,'pixel_difference_footprint':footprint,'independent_math':mathaudit,'blocked':BLOCKED,'all_own_figures_closed':True}
save('render_and_geometry_audit.json',audit)
print(json.dumps({k:v for k,v in audit.items() if k not in ('frozen_fields','changed_artists','markers','canvas_data_to_pixel')},ensure_ascii=False,indent=2))
print('MARKERS',json.dumps(markers,ensure_ascii=False,indent=2))
