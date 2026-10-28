#!/usr/bin/env python3
"""Independent numerical checks of frozen constraints; no renderer imports."""
import collections,json,math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[3]

def verify(scene):
 checks=[];native=[];points=scene.get('points',{})
 def pt(x):return np.array(points[x] if isinstance(x,str) else x,dtype=float)
 def norm(x):return float(np.linalg.norm(x))
 def crossnorm(u,v):return abs(float(u[0]*v[1]-u[1]*v[0])) if len(u)==2 else norm(np.cross(u,v))
 def close(a,b):return math.isclose(a,b,rel_tol=1e-8,abs_tol=1e-8)
 for i,c in enumerate(scene.get('constraints',[])):
  typ=c['type'];out={'id':c.get('id',str(i)),'type':typ}
  try:
   if typ=='distance':
    a,b=map(pt,c['points']);v=norm(a-b);out.update(measured=v,expected=c['value'],passed=close(v,c['value']))
   elif typ=='angle':
    a,b,d=map(pt,c['points']);u=a-b;v=d-b
    angle=math.degrees(math.atan2(crossnorm(u,v),float(u@v)))
    if c.get('reflex'):angle=360-angle
    expected=c.get('degrees',c.get('value'));out.update(measured=angle,expected=expected,passed=abs(angle-expected)<=1e-7)
   elif typ=='on_circle':
    p=pt(c['point']);center=pt(c['center']);v=norm(p-center);out.update(measured=v,expected=c['radius'],passed=close(v,c['radius']))
   elif typ in ('perpendicular','parallel'):
    vals=c.get('segments')
    if vals:a,b=map(pt,vals[0]);d,e=map(pt,vals[1])
    else:a,b,d,e=map(pt,c['points'])
    u=b-a;v=e-d;denom=norm(u)*norm(v)
    residual=abs(float(u@v))/denom if typ=='perpendicular' else crossnorm(u,v)/denom
    out.update(normalized_residual=residual,passed=residual<=1e-8)
   elif typ=='equal_length':
    lengths=[norm(pt(a)-pt(b)) for a,b in c['segments']];out.update(measured=lengths,passed=all(close(x,lengths[0]) for x in lengths))
   elif typ=='collinear':
    ps=list(map(pt,c['points']));u=ps[1]-ps[0];span=max(norm(p-ps[0]) for p in ps)
    errors=[crossnorm(u,p-ps[0])/norm(u) for p in ps[2:]]
    out.update(perpendicular_residual=max(errors,default=0),passed=max(errors,default=0)<=max(1e-8,span*1e-8))
   elif typ=='coplanar':
    ps=np.array(list(map(pt,c['points'])));s=np.linalg.svd(ps-ps[0],compute_uv=False);residual=float(s[-1])
    out.update(singular_residual=residual,passed=residual<=max(1e-8,float(s[0])*1e-8))
   elif typ=='projected_tangent':
    arc=next(o for o in scene['objects'] if o['id']==c['circle'])
    radial=pt(c['point'])-pt(arc['center']);u=pt(arc['u']);v=pt(arc['v'])
    tangent=-float(radial@v)*u+float(radial@u)*v
    matrix=np.array(scene['projection']['matrix'],dtype=float)
    a,b=map(pt,c['segment']);direction=matrix@(b-a);projected=matrix@tangent
    residual=crossnorm(direction,projected)/(norm(direction)*norm(projected))
    out.update(normalized_projected_parallel_residual=residual,point_radius=norm(radial),passed=residual<=1e-8 and close(norm(radial),arc['radius']))
   else:
    native.append(out);continue
  except Exception as exc:out.update(passed=False,error=str(exc))
  checks.append(out)
 return checks,native

if __name__=='__main__':
 results=[]
 for d in sorted((ROOT/'review_candidates/mathvision/items').iterdir()):
  checks,native=verify(json.loads((d/'scene.json').read_text()));results.append({'id':d.name,'checks':checks,'native_extension_scope':native})
 out={'scope':'Independent arithmetic from frozen scene constraints, no renderer/report trust. Custom native geometry extensions remain explicitly separate.','items':results,'checked_count':sum(len(r['checks']) for r in results),'native_extension_count':sum(len(r['native_extension_scope']) for r in results),'failures':[{'id':r['id'],**c} for r in results for c in r['checks'] if not c['passed']]}
 output=ROOT/'.runtime/protocol_redraw/audit/independent_geometry.json';output.parent.mkdir(parents=True,exist_ok=True)
 output.write_text(json.dumps(out,indent=2)+'\n')
 print('independent constraints',out['checked_count'],'native extension scope',out['native_extension_count'],'failures',out['failures'])

 if __name__=='__main__': raise SystemExit(bool(out['failures']))
