from new_tools import *
sys.path.insert(0,str(ROOT/'runtime/mathvision_special_20261101/harness'))
from quicktest3_isolated import run_tests
qid,vid=sys.argv[1].split('/')
folder=HERE/qid/vid
write(folder/'eligibility_before_api.json',eligibility(qid))
assert json.loads((folder/'eligibility_before_api.json').read_text(encoding='utf-8'))['eligible']
run_tests('PlaneGeometry',qid,folder/'candidate.png',folder/'design.json',folder/'tests',runs=2)
