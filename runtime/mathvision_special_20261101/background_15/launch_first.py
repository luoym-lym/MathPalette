from tools_local import *
import subprocess
items=[('Solid94','full_cut_vertices_to_shallow_corner'),('Solid236','rhombus_to_square_edge_family_binding'),('Solid215','diagonal_base_to_vertical_face_binding'),('Solid235','horizontal_cut_to_side_glue_binding')]
for q,v in items:
 f=TASK/q/v;cmd=[sys.executable,'-X','utf8','-B',str(TASK/'run_candidate.py'),q,v]
 with (f/'api_stdout.log').open('xb') as out,(f/'api_stderr.log').open('xb') as err:
  p=subprocess.Popen(cmd,cwd=ROOT,stdout=out,stderr=err,creationflags=subprocess.CREATE_NO_WINDOW)
 write(f/'process_launch.json',{'pid':p.pid,'command':cmd,'launched_at':datetime.now(timezone.utc).isoformat()});print(q,p.pid,flush=True)
