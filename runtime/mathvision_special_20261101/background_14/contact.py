from tools import *
from PIL import Image,ImageDraw
for k in range(0,len(ASSIGNED),4):
    sheet=Image.new('RGB',(1536,1600),'white');d=ImageDraw.Draw(sheet)
    for j,qid in enumerate(ASSIGNED[k:k+4]):
        pic=Image.open(TASK/qid/'original.png').convert('RGB')
        x=(j%2)*768;y=(j//2)*800;sheet.paste(pic,(x,y+30));d.text((x+15,y+8),qid,fill='black')
    sheet.save(TASK/f'contact_{k//4+1}.png')
