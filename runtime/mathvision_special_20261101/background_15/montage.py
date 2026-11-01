from tools_local import *
from PIL import Image,ImageDraw
for n,qs in enumerate([ASSIGNED[:10],ASSIGNED[10:]],1):
 out=Image.new('RGB',(1920,830),'white');d=ImageDraw.Draw(out)
 for i,q in enumerate(qs):
  p=TASK/q/'original.png'
  if not p.exists():continue
  im=Image.open(p).convert('RGB');im.thumbnail((384,384));x=i%5*384;y=i//5*415
  out.paste(im,(x,y+25));d.text((x+10,y+5),q,fill='black')
 out.save(TASK/f'original_montage_{n}.png')
