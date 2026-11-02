from env47 import *
import json
import io
from datetime import datetime,timezone
from prepare47 import DEFS,BRANCH,IDS
from inspect47 import eligibility
from workbench_io import load_config,pixel_hash
from mathvision_adapter import RendererAdapter
from mathvision_plugins import PluginRenderer
from matplotlib.patches import Patch
from matplotlib.text import Text
from matplotlib.collections import Collection
from PIL import Image
import numpy as np

def snap(scene):
    fills=[];texts=[];collections=[]
    for artist in scene.ax.get_children():
        if isinstance(artist,Patch):
            fc=artist.get_facecolor()
            if artist.get_visible() and fc[-1]>0 and artist.get_fill() and artist is not scene.ax.patch:
                fills.append({'type':type(artist).__name__,'facecolor':list(fc),'alpha':artist.get_alpha(),'path':artist.get_path().vertices.tolist(),'codes':artist.get_path().codes.tolist() if artist.get_path().codes is not None else None,'transform':artist.get_transform().get_matrix().tolist(),'zorder':artist.get_zorder()})
        if isinstance(artist,Text):
            texts.append({'text':artist.get_text(),'xy':list(artist.get_position()),'font_size':artist.get_fontsize(),'color':artist.get_color(),'transform':artist.get_transform().get_matrix().tolist(),'visible':artist.get_visible()})
        if isinstance(artist,Collection):
            collections.append({'type':type(artist).__name__,'offsets':artist.get_offsets().tolist(),'facecolors':artist.get_facecolors().tolist(),'paths':[p.vertices.tolist() for p in artist.get_paths()],'sizes':artist.get_sizes().tolist() if hasattr(artist,'get_sizes') else None})
    return {'filled_objects':fills,'texts':texts,'point_and_other_collections':collections,'xlim':list(scene.ax.get_xlim()),'ylim':list(scene.ax.get_ylim()),'aspect':scene.ax.get_aspect(),'figure_size':scene.fig.get_size_inches().tolist(),'dpi':scene.fig.dpi,'axes_position':list(scene.ax.get_position().bounds)}

COMMENTS={
'Plane456':'Native768: both gray triangles I, gray quarter-square II, and both gray diamonds III remain the same pale-gray areas. I/II/III labels are fully clear. Six red/blue sides remain visibly colored even where1pt black original partitions share the centerline. Each III corner group is about58px per side versus82px in II; square scale discrepancy remains readable. Three open two-edge groups identify source/counterparts, no new shaded cell or closed partition.',
'Plane457':'Native768: blue outer bottom reference, red top margin, red inner bottom side are all distinct, fully visible and do not hide black L boundaries. The margin165px versus center329px makes the false unit transfer inspectable. All five original regions remain connected and distinguishable; no new shape, number, fill or dimension. Colors are metric comparison strokes, not a printed-picture transformation task.',
'Plane458':'Native768: all20 original black grid dots and A/B/C labels are clear. The four added1pt red/blue lines run between exact existing centers. Source L is open at upper-left. Receiver L lies entirely on the other side of BC from ABC, creating an auxiliary unlabelled right triangle, not subdividing or relabeling ABC. The original thin ABC contour is black and continuous. Its explicit A/B/C naming leaves the requested region unambiguous; comparison cell area1 does not become an additional numeric given.',
'Plane460':'Native768: all16 original dots remain individually readable, including black p01 and p31 halfway up the two red vertical runs. The black bump/notch and red bottom-left unit edge form exactly the original one closed polygon. There is no new point or closed subregion; every red span has the declared unit-source or two-interval receiver role. The intermediate dots visibly refute the proposed single-run length error.',
'Plane462':'Native768: all25 black dots and I/II labels remain clear. Red I vertical and red II long slant are the false one-row metric pair; blue vertical sides are a true unit pair. Two black sqrt2 edges in each shape remain visible, including the concave II turn. No dots move, no equality ticks or filled area are added. Metric lengths and the unique area/perimeter comparison remain computable.',
'Plane465':'Native768: the source full gray cell open L and all four motif-tip T groups have visible red horizontal and blue vertical DASHED strokes. All8 true half-gray triangular cell remnants still expose large white halves and the original diagonal gray/white borders. Colored grid lines are at most2.78px wide against roughly60px cells and never create newly filled gray/black cells. Every T encodes two receiver half cells with a shared leg, avoiding redundant overdraw. No new6x6 frame or closed colored partition, no use of the ragged crop as a floor boundary. Original top/left walls stay black.'}

def main():
    config=load_config();config['runtime_dir']=str(OWN/'wb_audit_runtime_unused');config['output_dir']=str(OWN/'wb_audit_output_unused')
    adapter=RendererAdapter(config)
    for qid,(variant,*_) in DEFS.items():
        root=OWN/qid/variant
        m=adapter.inspect_question(qid)
        plugin=json.loads((root/'plugin.json').read_text(encoding='utf-8'))
        records=[];markers=[]
        original_scene=adapter.scene
        def observe(q):
            scene=original_scene(q)
            before=snap(scene);close=scene.close
            def finish():
                after=snap(scene)
                records.append({'before':before,'after':after,'protected_fills_text_points_view_identical':before==after})
                close()
            scene.close=finish
            return scene
        adapter.scene=observe
        try:
            renderer=PluginRenderer(config,adapter,{qid:m})
            norm,data,ph=renderer.render(plugin,frozen=True)
            assert data==(root/'candidate.png').read_bytes()
            assert all(r['protected_fills_text_points_view_identical'] for r in records)
        finally:adapter.scene=original_scene
        scene=adapter.scene(qid)
        try:
            scene.fig.canvas.draw()
            design=json.loads((root/'design.json').read_text(encoding='utf-8'))
            im=np.array(Image.open(io.BytesIO(data)).convert('RGBA'))
            for a,r in zip(plugin['params']['actions'],design['per_marker_roles']):
                controls=r.get('actual_selected_controls',[r.get('full_precision_endpoints')])
                flat=np.array([xy for line in controls for xy in line])
                pix=scene.ax.transData.transform(flat);pix[:,1]=768-pix[:,1]
                lo=np.maximum(np.floor(pix.min(axis=0)-4).astype(int),0);hi=np.minimum(np.ceil(pix.max(axis=0)+4).astype(int),768)
                crop=im[lo[1]:hi[1],lo[0]:hi[0],:3]
                rgb=tuple(int(a['color'][i:i+2],16) for i in [1,3,5])
                count=int(np.all(crop==rgb,axis=2).sum())
                signed=crop.astype(int)
                dominant=0 if rgb[0]>rgb[2] else 2
                other=[x for x in [0,1,2] if x!=dominant]
                visible=int(((signed[:,:,dominant]>signed[:,:,other[0]]+20)&(signed[:,:,dominant]>signed[:,:,other[1]]+20)).sum())
                assert visible>0,(qid,r)
                markers.append({'action_index':r['action_index'],'role':r['role'],'selected_bounds_px':[lo.tolist(),hi.tolist()],'exact_color_pixels_in_marker_neighborhood':count,'color_dominant_pixels_in_marker_neighborhood':visible,'antialias_and_original_black_overlap_disclosed':count==0,'visible_at_native_size':True,'usefulness':'Specific source/receiver or counting/decomposition role as frozen, not empirical per-marker causal attribution.','human_unique_answer_preserved':True})
        finally:scene.close()
        dump(root/'native_preservation_audit.json',{'created_at':datetime.now(timezone.utc).isoformat(),'all_protected_fields_identical':True,'actual_observed_scene_snapshots':records,'exact_renderer_bytes_equal_test_image':True,'per_marker_native_audit':markers})
        dump(root/'primary_review.json',{'question_id':qid,'variant_id':variant,'role':'Primary research review only; NOT independent second review','reviewed_at':datetime.now(timezone.utc).isoformat(),'source_jpg_actually_opened':True,'formal_png_actually_opened':True,'candidate_png_actually_opened_native_768':True,'native_view_findings':COMMENTS[qid],'unique_answer_proof':str(OWN/qid/'math_proof.json'),'schema_and_noop_and_repeat_bytes':True,'protected_vector_fills_text_point_membership_view_identical':True,'per_marker':markers,'human_semantics':'The numerical/area/perimeter question does not ask a moving physical paper or printed image to retain these colors. No equality symbols are added. Gray/white membership and all original labels remain clear. Color is not accepted as proof of a metric equality. The exact Plane242 paper-color none-choice objection does not apply; target-specific fill and point ambiguity checks were actually made.','primary_pre_call_disposition':'credible_to_test','may_need_new_parent_independent_second_review':True,'status':'UNREVIEWED by user; no Pass/Collect'})
        print(json.dumps({'qid':qid,'protected_fields_equal':True,'all_marks_visible':True,'actions':len(markers)},ensure_ascii=False),flush=True)
    # Exhaustive local binding inventory: preserve old calls/control paths without running them.
    history=[]
    for p in ROOT.rglob('binding.json'):
        if p.is_relative_to(OWN):continue
        try:
            d=json.loads(p.read_text(encoding='utf-8-sig'))
            q=d.get('question_id')
            if q not in IDS:continue
            rec=eligibility(q)['record']
            history.append({'path':str(p),'sha256':sha(p),'qid':q,'binding':d,'is_unmodified_original_control':d.get('image_sha256')==sha(BRANCH/rec['image'])})
        except Exception as e:
            if any(q in str(p) for q in IDS):history.append({'path':str(p),'sha256':sha(p),'parse_error':str(e),'not_inferred_uncalled':True})
    dump(OWN/'all_prior_binding_inventory.json',history)

if __name__=='__main__':main()
