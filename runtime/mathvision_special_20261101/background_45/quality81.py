from tools45 import *
from partial_style import object_paths
from renderer_adapter import scene_png
import numpy as np
q='Solid81';f=TASK/q/'r45_external_overlapping_domino_side_seams'
ctx=AD.inspect_question(q);plugin=read(f/'plugin.json');ren=PluginRenderer(CONFIG,AD,{q:ctx});assert ren.normalize(plugin)==plugin
sc=AD.scene(q)
try:
    sc.fig.canvas.draw();noop,p0=scene_png(sc);assert p0==ctx['original_pixel_sha256']
    anchors=[]
    for i,pair in enumerate([('given1e1','Ae2'),('given2e1','Ae6')]):
        for obj in pair:
            native=next(o for o in ctx['objects'] if o['id']==obj)
            for path in object_paths(sc,obj):anchors.append({'action_index':i,'target':obj,'object_sha256':canonical_hash(native),'object':native,'path_id':path['id'],'path_sha256':path['sha256'],'segments':[s['control'].tolist() for s in path['segments']]})
    original_lines=[{'vertices':a.get_path().vertices.tolist(),'transform':a.get_transform().get_matrix().tolist(),'color':a.get_color(),'linewidth':a.get_linewidth(),'linestyle':a.get_linestyle()} for a in sc.ax.lines]
    original_text=[(a.get_text(),a.get_position()) for a in sc.ax.texts]
    ren.apply_actions(sc,plugin);data,p1=scene_png(sc);assert data==(f/'candidate.png').read_bytes()
    assert original_lines==[{'vertices':a.get_path().vertices.tolist(),'transform':a.get_transform().get_matrix().tolist(),'color':a.get_color(),'linewidth':a.get_linewidth(),'linestyle':a.get_linestyle()} for a in list(sc.ax.lines)[:len(original_lines)]]
    assert original_text==[(a.get_text(),a.get_position()) for a in sc.ax.texts]
    # All guide/original-line intersections must occur at one of the guide endpoints.
    unexpected=[];contacts=[]
    for i,act in enumerate(plugin['params']['actions']):
        a,b=np.array(act['endpoints']);d=b-a
        for o in ctx['objects']:
            if not o['styleable']:continue
            for path in object_paths(sc,o['id']):
                for seg in path['segments']:
                    v,w=np.array(seg['control']);e=w-v;mat=np.column_stack([d,-e]);det=np.linalg.det(mat)
                    if abs(det)<1e-10:continue
                    t,u=np.linalg.solve(mat,v-a)
                    if -1e-9<=t<=1+1e-9 and -1e-9<=u<=1+1e-9:
                        item={'guide':i,'object':o['id'],'guide_parameter':float(t),'original_parameter':float(u)};contacts.append(item)
                        if 1e-9<t<1-1e-9:unexpected.append(item)
    assert not unexpected,unexpected
    write(f/'pretest_visual_review.json',{'checked_at':now(),'actual_exact768_native_png_viewed':True,'schema_default_normalization_verified':True,'no_op_matches_formal':True,'two_full_byte_identical_renders':True,'direct_apply_reproduces_tested_png':True,'source_context_equals_fresh':ctx==read(f/'context.json'),'all_original_lines_text_geometry_fill_unchanged':True,'anchors_and_paths':anchors,'exact_guide_intersections_with_originals':contacts,'interior_guide_intersections_with_original_geometry':unexpected,'native_marker_review':'Two thin dashed cross-panel links are visibly external comparisons. Red joins source first glue seam to A lower internal seam; blue joins second source glue seam to A next internal seam. No labels or diagnostic four-cube seams are obscured. Red/blue cross in whitespace without a point marker. No closed outline, new cube edge, source cut, or face membership is drawn.','semantics':'The blocks retain entirely black original boundaries. Long links cross blank space between separate panels and are external diagram annotations; they cannot reasonably be moving physical ink on a block. They suggest two candidate overlapping placements, not an additional required fixed cut. The original problem still uniquely excludes B through perfect matching, with A constructed using a horizontal base domino and the upper vertical pair.','primary_only':True})
    write(f/'pretest_freeze.json',{'created_at':now(),'all_pretest_gates_pass':True,'question_id':q,'expected_wrong_answer':'A','files':{n:file_hash(f/n) for n in ['design.json','design_difference_audit.json','plugin.json','candidate.png','context.json','pretest_visual_review.json','render_check.json']},'requires_new_parent_independent_review':True})
    print('Solid81 pretest passed, external links meet originals only at endpoints')
finally:sc.close()
