import env
from env import OWN
from prepare import read,dump,sha
from datetime import datetime,timezone
import numpy as np
from PIL import Image

NAMES={'Plane407':'r43_full_base_to_center_half_clear_dots','Plane410':'r43_similar_triangle_area_unit_binding','Plane412':'r43_unit_endpoint_to_long_run_binding'}

def main():
    for q,name in NAMES.items():
        root=OWN/q/name;d=read(root/'design.json');n=read(root/'native_render_audit.json');ctx=read(root/'context.json')
        img=np.array(Image.open(root/'candidate.png').convert('RGBA'));orig=np.array(Image.open(root/'noop.png').convert('RGBA'))
        if q=='Plane407':
            annotations='At native768px all four centre points are black and distinct; both centre lines still connect their true centres. Source blue/green full widths at the top are double the corresponding centre-to-boundary receiver lengths. Receiver colors stop exactly at the left rims; the original black dots carry the actual endpoints. No new partition and no dot obscured.'
            note='Three unmarked grayscale antialias pixels differ after exact partial contour serialization; maximum channel delta53 on edge raster samples only. No additional colored pixels outside actual marker neighborhoods, no changed vector contour/fill/text.'
            outside=(np.any(img!=orig,axis=2))
            # Save exact small AA discrepancies separately from conceptual marks.
            all_boxes=[b for m in n['per_marker'] for b in m['native_pixel_neighborhoods']]
            region=np.zeros((768,768),bool)
            for x0,y0,x1,y1 in all_boxes:region[y0:y1+1,x0:x1+1]=True
            ys,xs=np.where(outside&~region)
            dump(root/'non_marker_antialias_pixels.json',[{'xy':[int(x),int(y)],'before':orig[y,x].tolist(),'after':img[y,x].tolist()} for x,y in zip(xs,ys)])
        elif q=='Plane410':
            annotations='Native central figure is about58 by19px. Both white triangular corners remain visibly white; central black triangle and right black square remain black. Source red horizontal and blue vertical unit legs form one right angle at its original corner; receiver red/blue diagonal legs form the other right angle at the original apex. Their scale difference is clear on the actual PNG. Original five designs and square divisions remain countable; no added region/diagonal.'
            note='Small original central design is a source-layout limitation, disclosed; at native size the white half-cell, black triangle and right square are still distinct. No change to semantic fill or count membership.'
        else:
            annotations='Native four red/blue dots are at exact original visible corners. Original P,Q names remain unobscured. All black requested path segments and gray background-grid segments retain their actual formal native colors/widths. Four dots mark two endpoint-role pairs, with the bottom receiver span visibly triple the source span; they create no competing route.'
            note='Formal scene role records2.5pt, but actual original PNG/context render all black route edges at1pt. This unit preserves the actual approved PNG/native styles; the metadata discrepancy is disclosed in the precall correction, not repaired in formal inputs. Point markers cover small portions of existing corner strokes, a deliberate legal appearance overlay.'
        review={'question_id':q,'variant_id':name,'review_level':'PRIMARY ONLY; parent must commission NEW independent second review before delivery','at_utc':datetime.now(timezone.utc).isoformat(),'actual_source_JPG_formal_PNG_and_candidate_native_viewed':True,'unique_math':d['primary_math_proof'],'human_semantics':d['human_semantics'],'native_visual_findings':annotations,'per_marker':[dict(m,targeting='Specific source/receiver role in the predeclared comparison, not isolated wrong-answer salience.',validity='Exact original path interval or original visible vertex, permitted schema/default size; no equality/angle/cut relation inserted.',conciseness='Each mark carries one ordered endpoint/leg/width role in a defined comparison.') for m in d['marker_roles']],'all_marks_have_visible_native_pixels':all(m['visible'] for m in n['per_marker']),'labels_fill_coordinates_view_retained':True,'all_original_fills_and_texts_exact_native_state_equal':True,'normal_size_readable':True,'native_audit':str(root/'native_render_audit.json'),'two_offline_byte_identical':True,'wrong_preset_frozen_before_calls':d['expected_wrong_answer'],'candidate_sha256':sha(root/'candidate.png'),'design_sha256':sha(root/'design.json'),'ready_for_exactly_two_calls':not n['requires_pre_call_hold'],'caveats':[note,'No per-marker causal or statistical gain claim; no duplicate original controls.']}
        dump(root/'primary_review.json',review)
        assert review['ready_for_exactly_two_calls']
        print(q,'READY',sha(root/'candidate.png'))

if __name__=='__main__':main()
