from tools45 import *
from PIL import Image
import numpy as np
q='Solid97';f=next((TASK/q).glob('r45_*/design.json')).parent
ctx=read(f/'context.json');s=read(TASK/q/'source_scene_snapshot.json');p=s['projection']
a=np.array(Image.open(TASK/q/'original.png').convert('RGBA'));b=np.array(Image.open(f/'candidate.png').convert('RGBA'));checks=[]
for o in ctx['objects']:
    if o['type']!='point':continue
    world=o['geometry']['point'];xy=np.array(p['matrix'])@(np.array(world)-p['origin'])+p['offset'];pixel=np.array(ctx['canvas']['data_to_pixel'])@[*xy,1]
    cx,cy=pixel[:2];x0,x1=int(cx)-8,int(cx)+9;y0,y1=int(cy)-8,int(cy)+9
    equal=np.array_equal(a[y0:y1,x0:x1],b[y0:y1,x0:x1]);assert equal
    checks.append({'id':o['id'],'world':world,'exact_projected_xy':xy.tolist(),'pixel_center':pixel[:2].tolist(),'raster_box':[x0,y0,x1,y1],'pixels_equal':equal})
assert len(checks)==16
write(f/'pip_pixel_preservation.json',{'checked_at':now(),'pip_count':16,'all16_native_pip_regions_identical':True,'checks':checks,'qualification':'The capture records point artists with artist_count0; the earlier generic artist-loop found0 regions. This supplemental audit uses every actual native point and frozen projection/canvas transform, so it verifies all16 real pip regions, rather than interpreting the empty artist list as proof.'})
print('all16 pip raster regions identical')
