import own_runtime as rt
from fractions import Fraction as F
import math

meta=rt.read(rt.OWN/'Plane202/context.json')
segments=[o['geometry']['points'] for o in meta['objects'] if o['geometry'].get('head_stroke')]
def rational_point(p):return tuple(F(str(v)) for v in p)
segments=[tuple(map(rational_point,s)) for s in segments]
def squared_distance(p,s):
    a,b=s;v=(b[0]-a[0],b[1]-a[1]);w=(p[0]-a[0],p[1]-a[1])
    vv=v[0]*v[0]+v[1]*v[1];wv=w[0]*v[0]+w[1]*v[1]
    if wv<=0:return w[0]*w[0]+w[1]*w[1]
    if wv>=vv:return (p[0]-b[0])**2+(p[1]-b[1])**2
    return w[0]*w[0]+w[1]*w[1]-wv*wv/vv
certificates=[]
for witness in [(.35,-.93),(-.35,.93)]:
    p=rational_point(witness)
    distances=[squared_distance(p,s) for s in segments]
    value=min(distances);idx=distances.index(value)
    assert value>F(1,1000)
    certificates.append({'reflected_snout_witness':witness,'closest_segment_object':'o'+str(idx+1),
        'minimum_squared_distance_exact':{'numerator':str(value.numerator),'denominator':str(value.denominator)},
        'strict_lower_bound_squared_distance':'1/1000','bound_verified_by_integer_rational_comparison':True,
        'coordinate_interpretation':'Exact decimal rationals of the saved full-precision JSON coordinate strings. No renderer, coordinate or replay tolerance introduced.'})
rt.save(rt.OWN/'Plane202/mathematics_rigor_supplement.json',{'created_at':rt.now(),
    'all_1600_head_segments_considered':len(segments),'diagonal_exclusion_certificates':certificates,
    'horizontal_vertical_proof':'Four sets are exact independent-sign reflections of all400 upper-left segments; stored calculation verifies1600/1600 multiset equality for each midline.',
    'original_unique_answer':2,'no_model_output_used_as_proof':True,
    'scope':'Arithmetic supplement; all frozen candidate design.json, plugin.json, PNG and original proof_calculation.json retained unchanged.'})
print('Exact rational snout-gap certificates saved')
