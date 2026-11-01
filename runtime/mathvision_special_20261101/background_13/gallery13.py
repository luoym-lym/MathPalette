from tools13 import *
from PIL import Image,ImageDraw
for j in range(4):
    ids=ASSIGNED[j*5:j*5+5];canvas=Image.new('RGB',(1152,824),'white');d=ImageDraw.Draw(canvas)
    for i,qid in enumerate(ids):
        im=Image.open(TASK/qid/'original.png').convert('RGB');im.thumbnail((384,384))
        x=(i%3)*384;y=(i//3)*412
        canvas.paste(im,(x,y+28));d.text((x+12,y+5),qid+' / '+str(AD.records[qid]['answer']),fill='black')
    canvas.save(TASK/f'original_sheet_{j+1}.png')
