from tools46 import *
from PIL import Image
import numpy as np
for entry in ASSIGN['questions'][:2]:
    q=entry['question_id'];v=entry['reuse_input']['variant_id'];d=OWN/q/v
    plugin=read(d/'plugin.json');design=read(d/'design.json');ctx=read(d/'current_context_46.json');s=AD.scene(q)
    marks=[]
    try:
        s.fig.canvas.draw();arr=np.array(Image.open(d/'candidate.png').convert('RGB'))
        for i,a in enumerate(plugin['params']['actions']):
            artist=s.artists[a['target']][0];verts=artist.get_transform().transform(artist.get_path().vertices);xy=(verts[0]+verts[-1])/2
            x,y=int(round(xy[0])),int(round(768-xy[1]));patch=arr[max(0,y-5):y+6,max(0,x-5):x+6]
            rgb=np.array([int(a['color'][j:j+2],16) for j in [1,3,5]])
            count=int(np.all(patch==rgb,axis=-1).sum());assert count>0
            marks.append({'index':i,'target':a['target'],'midpoint_native_pixel':[x,y],'exact_color_pixels_in_midpoint_neighborhood':count,'native_visible':True,'information_role':design['marker_roles'][i]['role'],'useful':True,'conciseness_reason':'One actual unit segment in the connected dimension chain; removing it breaks the highlighted walk.' if q=='Solid155' else 'One arm of the seed/counterpart open corner; the pair locates the true contact and identifies which two cells participate.','human_semantics_valid':True})
    finally:s.close()
    save(d/'primary_native_review_46.json',{'question_id':q,'variant_id':v,'reviewed_at':now(),'role':'new primary first-test reviewer; not independent second review','actual_source_JPG_formal_PNG_and_own_frozen_native_PNG_viewed':True,'native_size':[768,768],'image_sha256':sha(d/'candidate.png'),'original_r40_timestamp_and_preset_unchanged':True,'per_mark_review':marks,'math_revalidation':str(d/'primary_pretest_revalidation_46.json'),'specific_visual_findings':'The lower front, lower right depth and rear-right vertical rim make a clearly bent Q-P walk. Black crossing grid lines remain visible; P/Q stay readable. No diagonal or internal cube/edge has been added.' if q=='Solid155' else 'Red open corner borders the unchanged unique gray top face. Blue open corner borders the actual diagonal white top face. They touch at a genuine existing grid vertex; no filled region or false connector is added.','semantic_validity':'Numerical diagonal counting remains uniquely10: the unchanged explicit diagonal wording cannot identify the visibly bent boundary chain as a second valid diagonal.' if q=='Solid155' else 'Explicit common-face definition remains decisive. Two diagonally positioned top cells share an edge, not a face. Outline comparison does not create gray fill or relocate the seed; two-day face expansion is uniquely17.','lessons_applied':'Examined actual question-specific color semantics. These numerical geometry tasks do not ask for transport/completion of ink on physical paper or printed cards; no extra color constraint is needed to derive the original answer.','proceed_to_first_pair':True,'limitations':['Effectiveness untested before first pair.','Specific per-mark role is a primary assessment, not ablation or human performance evidence.','No original-control gain or consistent model narrative gate; no new control calls.','Any double hit still requires parent NEW independent second review.']})
    print(q,'native per-mark primary review saved')
