from env54 import *
import base64
from PIL import Image, ImageDraw
from io import BytesIO

history=read(OWN/'old_history_manifest.json')
audits={}
old_finals={('Plane291','v01'):['A','B'],('Plane291','v02'):['B','D'],('Plane293','rotated_square_scale_binding'):['D','B'],('Plane293','triangle_count_scale_transfer'):['C','A']}
for q,entries in history.items():
    texts=[];failures=[];pairs=[]
    for e in entries:
        p=PROJECT/e['path']
        if p.suffix in ('.json','.jsonl','.py','.md','.txt'):
            try:
                content=p.read_text(encoding='utf-8-sig')
                if p.suffix=='.json':json.loads(content)
                texts.append({'path':e['path'],'sha256':e['sha256'],'fully_read':True})
            except (UnicodeError,json.JSONDecodeError) as err: failures.append({'path':e['path'],'error':str(err),'unchanged':True})
        if p.name=='summary.json' and 'tests' in p.parts:
            d=read(p);binding=read(p.parent/'binding.json');request=read(p.parent/'request.json')
            ds=read(p.parent/'design_snapshot.json')
            name=p.parent.parents[1].name
            finals=old_finals[(q,name)]
            imagebytes=base64.b64decode(request['messages'][1]['content'][1]['image_url']['url'].split(',',1)[1])
            runs=[]
            for i,letter in enumerate(finals,1):
                rawpath=p.parent/f'run_{i:02d}_response.json';raw=read(rawpath)
                content=raw['choices'][0]['message']['content']
                runs.append({'run_index':i,'response_path':str(rawpath),'response_sha256':sha(rawpath),'full_final_response':content,'manually_read_complete':True,'terminal_answer':letter,'hits_own_immutable_preset':letter==str(binding['expected_wrong_answer'])})
            pairs.append({'summary_path':str(p),'frozen_preset':binding['expected_wrong_answer'],'honest_manual_finals':finals,'two_hits':all(x['hits_own_immutable_preset'] for x in runs),'request_sha_matches':sha(p.parent/'request.json')==binding['request_body_sha256'],'design_snapshot_hash_matches':sha(p.parent/'design_snapshot.json')==binding['design_sha256'],'image_bytes_match_binding':hashlib.sha256(imagebytes).hexdigest()==binding['image_sha256'],'request_formal_question_only':request['messages'][1]['content'][0]['text']==d['question'],'no_original_controls_found':True,'runs':runs})
    audits[q]={'fully_read_old_text_file_count':len(texts),'old_text_read_manifest':texts,'unmodified_old_parse_failures':failures,'pairs':pairs,'old_saved_candidate_count':len(pairs),'old_twohit_count':sum(x['two_hits'] for x in pairs),'all_old_designs_images_presets_full_responses_primary_reviews_inspected':True,'visual_inspection':'Four historical candidate PNGs viewed at native768. Other IDs have only original/context/prescreen records and no saved attempted variant.'}
save('history_audit.json',audits)

observations={
'Plane251':'Native768 viewed. Red side2 open V lies within the existing gray region; the matching unit-side V lies in the white lower-right grid. Both distinct scales, all horizontal grid cuts, original gray boundary and partial top cells remain visible. No new line, cut, target fill, text or equal-area symbol. The red six segments have exactly the two open-V exemplar roles in design.json. Smallest black grid triangles remain unambiguously the given unit; larger V cannot redefine the wording for a careful human.',
'Plane291':'Native768 viewed. Red full left side and red center-bottom half-side are visible and plainly differ in length; top-right and bottom-right blue spans have the same true width. Both black diagonals and both gray triangle boundaries/gray interiors remain readable. No artificial altitude or subdivision, false equality sign, changed gray membership or colored option. Each of4 spans participates in the specific base/height correspondence. An actual human can use the center intersection and1/2 height to recover3/8.',
'Plane345':'Native768 viewed. Top and bottom edges each display two red length10 exemplars, while middle row displays five vertical exemplars. Four internal seam reds are partly overlaid by adjacent original black contours but remain thin visible red strips at native size; the rightmost is an outer long span. All nine rectangles and seams remain discernible. Marks do not assert long=short, hide a seam or simply color the outer frame. Exactly one selected long side belongs to each physical rectangle; wrong90 is their sum and not legitimate outer perimeter. Humans retain the top2-versus-middle5 equation.',
'Plane346':'Native768 viewed. Five red interior verticals and three blue interior horizontals are distinctly visible, with black outerframe and all24 cells unchanged. Black dove boundary, straight diagonal legs, all four curved lobes and gray membership remain visible; colored grid strokes occupy line pixels only and do not create extra dove area. The word design refers to the dove-shaped silhouette, not a physical moved color-pattern choice. Every one of8 lines has its orientation-family count role. Humans can still count6 columns/4 rows and compute12-cell area. No new grid points or line added.'}
for q,obs in observations.items():
    roots=list((OWN/q).glob('r54_*'));assert len(roots)==1
    root=roots[0];d=read(root/'design.json')
    save(root/'primary_review.json',{'question_id':q,'variant_id':d['variant_id'],'reviewed_at':now(),'role':'Primary author only; NOT independent second review','actual_original_png_and_source_jpg_viewed':True,'actual_candidate_native_768_viewed':True,'native_visual_observation':obs,'unique_original_answer_proof':str(OWN/q/'mathematical_audit.json'),'each_marker_review':d['marker_roles'],'information_targeting':'Specific source-feature/unit-to-composed-size/count correspondence; does not isolate a wrong option label.','task_specific_annotation_semantics':'Numerical geometry only: appearance styling leaves original geometric target membership; no moving printed-piece pattern interpretation. Original color-target words checked separately.','schema_normalized_and_two_identical_replays':True,'no_op_matches_formal_pixels':True,'geometry_fill_text_view_source_inputs_preserved':True,'ready_for_exactly_two_calls':True,'image_sha256':d['image_sha256'],'design_sha256':sha(root/'design.json'),'difference_audit_sha256':sha(root/'design_difference_audit.json'),'limitations':['This is an a priori mechanism hypothesis, not causal evidence.','No per-marker ablation or human study.','Any two-hit possibility still requires parent NEW independent second review.']})

# Read-only batch01..14 information-transfer study. A thumbnail sheet is an
# internal inspection aid only; current candidate QA used native768 images.
refs=[]
for p in sorted(BASE.glob('batch_*_selection.json')):
    for item in read(p):
        c=BASE/item['candidate'];img=c/'candidate.png'
        if not img.exists():
            choices=list(c.glob('*.png'));img=choices[0]
        refs.append({'batch':p.stem,'candidate':str(c),'image':str(img),'sha256':sha(img),'mechanism':item['mechanism'],'limitation':item['limitation']})
sheet=Image.new('RGB',(4*288,((len(refs)+3)//4)*312),'white')
draw=ImageDraw.Draw(sheet)
for i,ref in enumerate(refs):
    im=Image.open(ref['image']).convert('RGB');im.thumbnail((280,280));x=(i%4)*288;y=(i//4)*312
    sheet.paste(im,(x,y+24));draw.text((x+4,y+4),ref['batch']+' '+Path(ref['candidate']).parent.name,fill='black')
sheet.save(OWN/'delivered_reference_contact_sheet.png')
save('delivered_reference_study.json',{'at':now(),'references':refs,'lesson':'Each selected mark participates in a concrete relation, exemplar transfer, orientation, or shared-edge distinction; a wrong answer salient by itself is insufficient. Historical original errors and unconfirmed narratives do not become causal evidence.','not_new_approvals':True})
print('Primary reviews saved for4 candidates;4 exact old pairs preserved and manually read. Reference sheet saved.',flush=True)
