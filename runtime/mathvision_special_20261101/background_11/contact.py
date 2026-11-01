from tools_local import *
from PIL import Image,ImageDraw
records={r['id']:r for r in rows(ROOT/'PlaneGeometry/dataset.jsonl')}
for group in range(4):
    qids=ASSIGNED[group*5:(group+1)*5]
    canvas=Image.new('RGB',(768*3,808*2),'white');draw=ImageDraw.Draw(canvas)
    for i,qid in enumerate(qids):
        im=Image.open(ROOT/'PlaneGeometry'/records[qid]['image']).convert('RGB')
        x=(i%3)*768;y=(i//3)*808
        canvas.paste(im,(x,y+40));draw.text((x+10,y+10),qid+' answer '+str(records[qid]['answer']),fill='black',font_size=24)
    canvas.save(HERE/f'originals_{group+1}.png')
write(HERE/'assignment_records.json',[records[q] for q in ASSIGNED])
