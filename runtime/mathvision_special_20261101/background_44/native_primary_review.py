import task_env
from task_env import OWN, PROJECT
from inspect_sources import read,save,sha
from pathlib import Path
import sys,io,math
import numpy as np
from PIL import Image
from datetime import datetime,timezone
sys.path.insert(0,str(PROJECT/'PlaneGeometry/workbench'))
from workbench_io import load_config
from mathvision_adapter import RendererAdapter
from partial_style import object_paths,portion

cfg=load_config();cfg['runtime_dir']=str(OWN/'adapter_runtime');cfg['output_dir']=str(OWN/'adapter_output')
adapter=RendererAdapter(cfg)
notes={
'Plane415':{'variant':'r44_exposed_radius_to_contact_seam',
 'native_findings':'Both selected red radii are clearly visible at768px. On the left the line borders white exterior on its left and a quarter piece on its right. On the right both sides of the red line belong to the upper cap, so it is visibly an internal seam. Other arcs, exposed straight radii, central rectangles and contacts stay black and legible.',
 'group_review':[{'group':'two red actual10cm material radii','targeting':'Specific same-piece radial-edge translation from external boundary to contact seam.','mathematical_validity':'Congruent lengths and actual correspondence true; perimeter ownership transfer is false. Correct difference remains20.','conciseness':'Exactly one source radius and its one receiving seam; neither is an option/answer highlight.','effectiveness_before_calls':'Plausible primary hypothesis only; no causal performance assertion.','human_unambiguity':'Numerical perimeter question: either comparison annotations or literal colored edges leave geometric perimeter20. No false equality/angle symbol, new piece, added cut or missing output picture.'}]},
'Plane421':{'variant':'r44_unequal_triangle_count_transfer',
 'native_findings':'At768px the two hexagons each show6 clearly separated blue radial triangles. Each gray pentagon has3 blue fan cells of visibly different shape and area. Original black border, shared hexagon side, all gray/white membership and all outer corners remain readable. The thin blue lines are uniform auxiliary decomposition lines, without point disks or equality symbols.',
 'group_review':[{'group':'12 source spokes,6 per hexagon','targeting':'Explicit equal-triangle area units for both actual regular hexagons.','mathematical_validity':'Source centers are means of opposite frozen vertices; each source cell has area t. The spokes do not move vertices or alter semantic fills.','conciseness':'Each radial boundary supplies one necessary edge of the complete6-cell count; no unrelated decoration or invisible mark.','effectiveness_before_calls':'Supplies the specific unit to be over-transferred, not merely white-region salience.','human_unambiguity':'Static numerical shaded-area problem; ordinary auxiliary triangulation does not introduce new cut instructions.'},
 {'group':'4 receiver diagonals,2 per gray pentagon','targeting':'Make3 receiving triangles per gray region for a prospective count6/(6+12)=1/3 error.','mathematical_validity':'Every diagonal joins existing frozen vertices and stays inside its original gray pentagon. Their actual areas3t,t,2t are distinct; original total6t per pentagon is unchanged.','conciseness':'Two diagonals are needed to triangulate a5-vertex concave polygon. Both gray regions need the same complete count for the global fraction.','effectiveness_before_calls':'Concrete count-versus-area mismatch; whether a solver follows it remains unobserved.','human_unambiguity':'Gray remains the same filled region. Blue1pt lines have no area-fill meaning and cannot alter the numerical answer1/2. No picture transformation or printed-content matching is requested.'}]},
'Plane441':{'variant':'r44_total_rise_to_horizontal_run_overlay',
 'native_findings':'The original AD height is a thin red coincident overlay; all3 original step segments are red and clearly visible. A,B,C,D and y are unobstructed. No rearranged square, endpoint, extra cut or puzzle piece was drawn. The source AD, the two vertical returns and the horizontal receiving run can all be distinguished at native size.',
 'group_review':[{'group':'AD and the two vertical returns','targeting':'True source decomposition8=4+4 from full outer height to the two actual stepped half-heights.','mathematical_validity':'Only actual source edges are traced. Endpoint coordinates remain exact; AD overlay coincides with the existing edge.','conciseness':'Whole8 source plus both4-unit members are needed for the stated aggregate-rise mechanism.','effectiveness_before_calls':'A primary source grouping; no empirical effect yet.','human_unambiguity':'Printed red outlines also leave the original numerical length data and area unchanged.'},
 {'group':'horizontal y-run','targeting':'Receiving run for the false substitution of total rise8 into one transverse run, predicting8.','mathematical_validity':'This is a deliberately false inference, not a supplied equal-length condition; no conventional equality tick is added. Original construction still uniquely gives y6.','conciseness':'One actual target run. No answer choice or fake target square is highlighted.','effectiveness_before_calls':'Information-targeting is less direct than Plane415 and is explicitly left for NEW independent judgment if it hits.','human_unambiguity':'A shared outline hue alone is not a conventional equality condition; original perpendicular geometry and y label remain legible. No output picture whose colored content would be missing is requested.'}]}
}
for qid,note in notes.items():
    folder=OWN/qid/note['variant'];design=read(folder/'design.json');plugin=read(folder/'plugin.json')
    scene=adapter.scene(qid)
    try:
        scene.fig.canvas.draw()
        image=np.array(Image.open(folder/'candidate.png').convert('RGB'))
        yy,xx=np.indices(image.shape[:2]);per=[]
        for idx,action in enumerate(plugin['params']['actions']):
            if action['type']=='add_line':
                segs=[np.array(action['endpoints'])]
            else:
                paths=object_paths(scene,action['target'])
                selected=action.get('interval')
                segs=[]
                for p in paths:
                    count=len(p['segments'])
                    for j,s in enumerate(p['segments']):
                        if selected is None:segs.append(s['control'])
                        elif p['id']==selected['path_id'] and selected['start'] < (j+.5)/count < selected['end']:
                            segs.append(s['control'])
            color=tuple(int(action['color'][i:i+2],16) for i in (1,3,5))
            palette=np.all(image==color,axis=2);mask=np.zeros(image.shape[:2],dtype=bool);length=0
            controls=[]
            for seg in segs:
                controls.append(seg.tolist());pix=scene.ax.transData.transform(seg);pix[:,1]=768-pix[:,1]
                assert len(pix)==2,'Only straight candidate marks are used'
                a,b=pix;v=b-a;den=float(v@v);length+=math.sqrt(den)
                if den==0:continue
                t=np.clip(((xx-a[0])*v[0]+(yy-a[1])*v[1])/den,0,1)
                d2=(xx-(a[0]+t*v[0]))**2+(yy-(a[1]+t*v[1]))**2
                mask |= d2<=16
            actual=int(np.count_nonzero(palette&mask))
            assert actual>0,(qid,idx)
            per.append({'action_index':idx,'normalized_action':action,'full_precision_selected_controls':controls,
                        'length_pixels':length,'exact_palette_pixels_within4px':actual,
                        'role':design['marker_roles'][idx],'native_visibility_confirmed':True,
                        'primary_targeting_validity_conciseness_semantics':'See role and group review; no independent or causal claim.'})
    finally:scene.close()
    review={'question_id':qid,'variant_id':note['variant'],'reviewed_at_utc':datetime.now(timezone.utc).isoformat(),
            'actual_source_JPG_formal_PNG_old_candidates_and_new_PNG_opened':True,'native_dimensions':[768,768],
            **note,'per_marker':per,'math_proof_path':str(OWN/qid/'primary_math_audit.json'),
            'schema_and_two_draw_check':str(folder/'render_check.json'),'design_sha256':sha(folder/'design.json'),
            'png_sha256':sha(folder/'candidate.png'),'plugin_sha256':sha(folder/'plugin.json'),
            'proceed_to_exactly_two_real_calls':True,'primary_only':True,'approved':False,'Pass_Collect_publication':False,
            'independent_review':'Must be a NEW parent-launched independent task; primary worker does not second-review itself.'}
    save(folder/'primary_review_before_calls.json',review)
    print(qid,'all',len(per),'marks natively visible; primary review saved')

save(OWN/'Plane441/r44_total_rise_to_horizontal_run/offline_error.json',{
    'status':'offline render failed before a PNG or design.json or request existed','error_code':'object_changed',
    'error':'outer partial path hash differs between post-canvas-draw capture/normalization and pre-draw rendering',
    'no_API_call':True,'old_draft_bytes_retained':True,'not_external_API_failure':True,
    'resolution':'Same geometric hypothesis prepared as r44_total_rise_to_horizontal_run_overlay using an exact existing-side1pt add_line overlay; no adapter change.'})
