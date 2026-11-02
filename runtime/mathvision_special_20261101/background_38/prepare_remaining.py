from common38 import *
import runpy
for q in ['Plane229','Plane250','Plane254','Plane256','Plane258']:
    sys.argv=['design38.py',q]
    runpy.run_path(str(TASK/'design38.py'),run_name='__main__')
