"""Bind the new analytic originals/provenance without changing the Base engine."""
from pathlib import Path
import hashlib
import json
import re
import shutil
import sys

IMPORT = Path(__file__).resolve().parent
ROOT = IMPORT.parents[1]/'Analytics'/'fine_grained_dataset'
assignments = json.loads((IMPORT/'assignments.json').read_text(encoding='utf-8'))
manifest = {r['source_key']:r for r in json.loads((IMPORT/'source_manifest.json').read_text(encoding='utf-8'))}
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()

# Keep the earlier transcoded preview too; save the JPEG bytes without conversion.
source65 = manifest['s3109']
exact_copy = ROOT/'originals'/'Ana65.jpg'
shutil.copyfile(IMPORT/source65['source_image'], exact_copy)
provenance65 = ROOT/'provenance'/'MathVerse'/'Ana65.json'
metadata = json.loads(provenance65.read_text(encoding='utf-8'))
metadata['preserved_source_copy'] = 'originals/Ana65.jpg'
metadata['source_image_content_format'] = 'JPEG'
metadata['original_png_note'] = 'Ana65.png is the earlier transcoded preview; Ana65.jpg preserves exact source bytes.'
provenance65.write_text(json.dumps(metadata,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

for row in assignments:
    if row['branch']!='Analytics':
        continue
    qid = row['id']
    provenance = ROOT/'provenance'/'MathVerse'/f'{qid}.json'
    metadata = json.loads(provenance.read_text(encoding='utf-8'))
    copy_path = ROOT/metadata['preserved_source_copy']
    assert sha(copy_path)==manifest[row['source_key']]['source_image_sha256'], qid
    module = ROOT/'dataset_generator'/'dataset_generator'/f'function_plot{int(qid[3:]):02d}.py'
    text = module.read_text(encoding='utf-8')
    constants = (f'_PROVENANCE_PATH = {provenance.relative_to(ROOT).as_posix()!r}\n'
                 f'_PROVENANCE_SHA256 = {sha(provenance)!r}\n'
                 f'_SOURCE_COPY_PATH = {metadata["preserved_source_copy"]!r}\n'
                 f'_SOURCE_COPY_SHA256 = {sha(copy_path)!r}\n')
    if '_PROVENANCE_PATH =' not in text:
        text = re.sub(r'(_HELPER_SHA256 = [^\n]+\n)',r'\1\n'+constants,text,count=1)
        insertion = ('\n    for relative, expected in ((_PROVENANCE_PATH, _PROVENANCE_SHA256),'
                     '(_SOURCE_COPY_PATH, _SOURCE_COPY_SHA256)):\n'
                     '        actual = hashlib.sha256((_DATASET_ROOT / relative).read_bytes()).hexdigest()\n'
                     '        if actual != expected:\n'
                     '            raise RuntimeError(f"Frozen MathVerse dependency changed: {relative}")\n')
        text = text.replace('\n\ndef _finish(',insertion+'\n\ndef _finish(',1)
    else:
        text = re.sub(r'_PROVENANCE_PATH = [^\n]+\n_PROVENANCE_SHA256 = [^\n]+\n_SOURCE_COPY_PATH = [^\n]+\n_SOURCE_COPY_SHA256 = [^\n]+\n',lambda _:constants,text,count=1)
    module.write_text(text,encoding='utf-8')

sys.path.insert(0,str(ROOT/'dataset_generator'))
from generate_base_variants import BaseGenerator
from base_support import canonical_hash
generator = BaseGenerator(ROOT)
for row in assignments:
    if row['branch']!='Analytics':
        continue
    qid = row['id']
    recipes = json.loads((ROOT/'base_variant'/qid/'recipes.json').read_text(encoding='utf-8'))
    changed = canonical_hash(recipes[0]['baseline']) != canonical_hash(generator.dataset.baseline(qid))
    generator.generate_question(qid,20261008,replace=changed)
    generator.check_question(qid,redraw_pixels=True)
    print(f'{qid}: source/provenance/helper bound, four Base replayed',flush=True)
generator.write_index()
generator.check_index()
print('46 originals and 184 Base verified; global index current.',flush=True)
