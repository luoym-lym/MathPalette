import env
from env import OWN, PROJECT, SHARED
from prepare import IDS, read, dump, sha
import json
from fractions import Fraction as F
from collections import Counter
from itertools import combinations

ITEMS=PROJECT/'PlaneGeometry/dataset_generator/mathvision_renderers/shared_e4e003f51742cf00/items'

def area(p): return abs(sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(p,p[1:]+p[:1])))/2
def clip(poly,axis,c,less):
    out=[]
    for a,b in zip(poly,poly[1:]+poly[:1]):
        ain=a[axis]<=c if less else a[axis]>=c
        bin=b[axis]<=c if less else b[axis]>=c
        if ain: out.append(a)
        if ain!=bin:
            t=(c-a[axis])/(b[axis]-a[axis]);out.append(tuple(a[k]+t*(b[k]-a[k]) for k in range(2)))
    return out

def clip_linear(poly,A,B,C):
    out=[]
    val=lambda p:A*p[0]+B*p[1]+C
    for a,b in zip(poly,poly[1:]+poly[:1]):
        va,vb=val(a),val(b)
        if va>=0: out.append(a)
        if (va>=0)!=(vb>=0):
            t=va/(va-vb);out.append(tuple(a[k]+t*(b[k]-a[k]) for k in range(2)))
    return out

def main():
    history={}
    for q in IDS:
        files=read(OWN/q/'history_files.json')
        entries=[]
        for f in files:
            p=__import__('pathlib').Path(f['path'])
            if p.suffix!='.json': continue
            try: data=read(p)
            except json.JSONDecodeError as e:
                entries.append({**f,'parse_error':str(e),'bytes_preserved':True,'never_repair_or_retry':True});continue
            if p.name in ['design.json','plugin.json','prescreen.json','primary_visual_review.json','prescreen_assessment.json','assessment.json','manual_final_review.json']:
                if p.name in ['prescreen_assessment.json','assessment.json']:
                    data={k:v for k,v in data.items() if k not in ['formal_record','eligibility_at_prescreen_close','diagnostic_remaining_record']}
                entries.append({**f,'read_full_original_json':True,'content':data})
            if p.name.endswith('_response.json'):
                content=data['choices'][0]['message'].get('content')
                entries.append({**f,'entire_raw_response_read':True,'full_response':data,'full_final_content':content,'finish_reason':data['choices'][0].get('finish_reason')})
        if q=='Plane407':
            d=read(SHARED/'background_03/plane_worker/mathematical_audit.json')[q]
            entries.append({'path':str(SHARED/'background_03/plane_worker/mathematical_audit.json'),'content':d,'sha256':sha(SHARED/'background_03/plane_worker/mathematical_audit.json')})
        dump(OWN/q/'history_audit.json',entries)
        history[q]={'historical_files':len(files),'saved_designs':[e['path'] for e in entries if e.get('path','').endswith('/design.json') or e.get('path','').endswith('\\design.json')],'old_response_count':sum(e.get('entire_raw_response_read',False) for e in entries),'malformed':[e['path'] for e in entries if 'parse_error' in e]}
    dump(OWN/'history_inventory.json',history)
    # Exact lattice units for Plane405: (x,y/h), h=sqrt(3)/2.
    shade=[(F(2),F(0)),(F(9,2),F(0)),(F(9,2),F(5)),(F(2),F(4))]
    cells=[]
    for j in range(7):
        for i in range(7-j):
            x=F(i)+F(j,2)
            cells.append([(x,F(j)),(x+1,F(j)),(x+F(1,2),F(j+1))])
            if i<6-j:cells.append([(x+1,F(j)),(x+F(3,2),F(j+1)),(x+F(1,2),F(j+1))])
    pieces=[]
    for n,cell in enumerate(cells):
        p=cell
        for A,B,C in [(1,0,-F(2)),(-1,0,F(9,2)),(0,1,0),(F(2,5),-1,F(16,5))]:
            p=clip_linear(p,A,B,C) if p else []
        a=area(p) if p else F(0)
        pieces.append({'cell_index':n,'cell_xy_y_over_h':[[str(v) for v in p] for p in cell],'shaded_unit_triangle_area':str(2*a),'actual_shaded_polygon':[[str(v) for v in p] for p in p]})
    total=sum(F(c['shaded_unit_triangle_area']) for c in pieces)
    counts=Counter(c['shaded_unit_triangle_area'] for c in pieces)
    result={'coordinate_system':'(x,y/h), h=sqrt(3)/2; each unit triangle has area1/2 here and4cm2 physically','shaded_vertices':[[str(v) for v in p] for p in shade],'exact_unit_triangle_area':str(2*area(shade)),'independent_clipping_sum':str(total),'correct_cm2':str(total*4),'cell_fraction_counts':dict(counts),'positive_cells':sum(F(c['shaded_unit_triangle_area'])>0 for c in pieces),'whole_cells':sum(F(c['shaded_unit_triangle_area'])==1 for c in pieces),'cell_decomposition':pieces}
    dump(OWN/'Plane405/exact_math.json',result)
    print(json.dumps(history,ensure_ascii=False));print(json.dumps({k:v for k,v in result.items() if k!='cell_decomposition'}))

if __name__=='__main__': main()
