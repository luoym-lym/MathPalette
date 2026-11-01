from tools_b import *
from PIL import Image
q='Plane234';vid='three_feature_match_ignores_gray';out=HERE/q/vid
ctx=json.loads((out/'context.json').read_text(encoding='utf-8'));matrix=ctx['canvas']['data_to_pixel']
orig=Image.open(HERE/q/'original.png').convert('RGB');candidate=Image.open(out/'candidate.png').convert('RGB')
def transform(p):return [matrix[d][0]*p[0]+matrix[d][1]*p[1]+matrix[d][2] for d in [0,1]]
def cross(a,b,p):return (b[0]-a[0])*(p[1]-a[1])-(b[1]-a[1])*(p[0]-a[0])
counts=[]
for oid in ['sunray3','sunray4','sunray5','sunray6']:
 g=next(o['geometry'] for o in ctx['objects'] if o['id']==oid);vertices=[transform(c['point']) for c in g['commands'] if c['op'] in ['move','line']];rgb=tuple(bytes.fromhex(g['semantic_color'][1:]));ox=[];retained=[]
 for y in range(max(0,int(min(p[1] for p in vertices))),min(768,int(max(p[1] for p in vertices))+2)):
  for x in range(max(0,int(min(p[0] for p in vertices))),min(768,int(max(p[0] for p in vertices))+2)):
   signs=[cross(vertices[j],vertices[(j+1)%3],(x+.5,y+.5)) for j in range(3)]
   if not(all(v>=0 for v in signs) or all(v<=0 for v in signs)):continue
   if orig.getpixel((x,y))==rgb:
    ox.append([x,y])
    if candidate.getpixel((x,y))==rgb:retained.append([x,y])
 counts.append({'object_id':oid,'unchanged_semantic_fill_rgb':rgb,'full_original_fill_pixels_inside_existing_ray':len(ox),'identical_fill_pixels_still_visible':len(retained),'unchanged_fill_pixel_locations':retained})
assert next(r for r in counts if r['object_id']=='sunray5')['identical_fill_pixels_still_visible']>0
write(out/'semantic_fill_preservation_audit.json',{'question_id':q,'variant_id':vid,'actual_PNG_pixel_check':True,'rays':counts,'interpretation':'Outline overlays are permitted appearance operations and preserve semantic facecolors in the renderer. This additional pixel audit shows remaining original fill pixels; it does not substitute for a human legibility review. The sun is small in the full image and2pt source outlines occupy some edge pixels, so the independent reviewer should check the gray third ray carefully.','primary_review_caveat':'The original gray fill is retained but has limited small-image area; no claim that every original fill pixel remains unchanged.'})
print(json.dumps(counts,ensure_ascii=False))
