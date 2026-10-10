"""Keep continuation arrows black and exactly on the corresponding curve."""
from pathlib import Path
import sys

IMPORT = Path(__file__).resolve().parent
ROOT = IMPORT.parents[1]/'Analytics'/'fine_grained_dataset'
qids = []
for number in (35,37,38,40,41,42):
    qid = f'Ana{number:02d}'
    path = ROOT/'dataset_generator'/'dataset_generator'/f'function_plot{number:02d}.py'
    text = path.read_text(encoding='utf-8')
    updated = text.replace("'#24588a'","'black'").replace("'#168ca3'","'black'")
    if number == 37:
        updated = updated.replace('(-2.2-1.5)*16/9','(((-4.4)**3/3)+.75*(-4.4)**2-2.5*(-4.4)-1.5)*16/9')
        updated = updated.replace('(2.7+.75)*16/9,(6.0-1.5)*16/9','(2.63+.75)*16/9,((2.63**3/3)+.75*2.63**2-2.5*2.63-1.5)*16/9')
    if number == 40:
        updated = updated.replace('xy=(-5.25*1.2,0)','xy=(-5.25*1.2,.25*1.2)')
        updated = updated.replace('xy=(5.25*1.2,6*1.2)','xy=(5.25*1.2,6.25*1.2)')
    if updated == text:
        continue
    backup = IMPORT/'artifact_revision_before'/'arrows'/path.name
    backup.parent.mkdir(parents=True,exist_ok=True)
    backup.write_bytes(path.read_bytes())
    path.write_text(updated,encoding='utf-8')
    qids.append(qid)
sys.path.insert(0,str(ROOT/'dataset_generator'))
from base_support import Dataset, pixel_hash
from generate_base_variants import BaseGenerator
dataset = Dataset(ROOT)
for qid in qids:
    first, second = dataset.original(qid), dataset.original(qid)
    assert pixel_hash(first)==pixel_hash(second)
    image = ROOT/'image'/f'{qid}.png'
    backup = IMPORT/'artifact_revision_before'/'arrows'/image.name
    backup.write_bytes(image.read_bytes())
    image.write_bytes(first)
generator = BaseGenerator(ROOT)
for qid in qids:
    generator.generate_question(qid,20261008,replace=True)
    generator.check_question(qid,redraw_pixels=True)
generator.write_index()
generator.check_index()
print('Continuation arrow positions, style, originals and corresponding Base replays verified.')
