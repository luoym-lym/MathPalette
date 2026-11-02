from bootstrap import *
import runpy
source=BASE/'background_57'/'Solid234'/'r57_maximum_generator_to_cut_trace'
script=BASE/'validate_candidate_replay.py'
sys.argv=[str(script),'--question','Solid234','--candidate',str(source),'--output',str(HERE/'offline')]
runpy.run_path(str(script),run_name='__main__')
