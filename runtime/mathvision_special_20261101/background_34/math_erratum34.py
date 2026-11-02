from tools34 import *
from math34 import area
draft=read(UNIT/'Plane338/primary_math_audit.json')
corrected=__import__('copy').deepcopy(draft)
rect=35
top=area([(1,6),(8,6),(8,5)])
right=area([(8,5),(8,1),(5,1)])
left=area([(1,1),(5,1),(2,2),(1,6)])
assert str(top)=='7/2' and right==6 and str(left)=='9/2' and rect-top-right-left==21
corrected['proof']['alternative_bounding_rectangle_check']='Bounding rectangle x=1..8,y=1..6 has35cells. Complement is top right triangle7/2, bottom right triangle6, and lower-left quadrilateral9/2; sum14. Gray35-14=21cells=84cm2.'
corrected['proof']['complement_exact_areas']=[str(top),str(right),str(left)]
corrected['corrected_at']=now()
corrected['correction_record']={'draft_preserved_unmodified':'primary_math_audit.json','draft_sha256':sha(UNIT/'Plane338/primary_math_audit.json'),
      'erratum':'primary_math_erratum_pretest.json','reason':'Correct the optional verbal complement decomposition; original exact shoelace result and unique answer unchanged. No candidate or calls for Plane338.'}
write(UNIT/'Plane338/primary_math_audit_corrected.json',corrected)
print(json.dumps({'Plane338_corrected_optional_check':True,'area':84,'draft_preserved':True}))
