"""Pure preparation of a reviewed MathVision item; never writes or approves."""
from pathlib import Path
import json
import os
import re


def _json(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode('utf-8')


def prepare(root, row, formal_id):
    root = Path(root)
    package = root / 'review_candidates/mathvision'
    branch = row['subject']
    prefix = {'PlaneGeometry': 'Plane', 'SolidGeometry': 'Solid'}[branch]
    if not re.fullmatch(prefix + r'(?:0[1-9]|[1-9][0-9]+)', formal_id):
        raise ValueError('Formal ID must match its branch and positive canonical number')
    from dataset_tools.catalog import FORMAL_SCENE_FIELDS
    item = root / row['candidate_path']
    item = item.parent
    native = json.loads((item / 'scene.json').read_text(encoding='utf-8'))
    allowed = FORMAL_SCENE_FIELDS[branch]
    missing = allowed - native.keys()
    if missing:
        raise ValueError('Native scene cannot be promoted without inventing fields: ' + ', '.join(sorted(missing)))
    formal = {k: row[k] for k in ('source_dataset', 'source_key', 'question', 'answer', 'answer_type')}
    formal['id'] = formal_id
    if 'choices' in row:
        formal['choices'] = row['choices']
    number = formal_id[len(prefix):]
    original_suffix = Path(row['original_image']).suffix.lower()
    formal.update(image=f'image/{formal_id}.png', original_image=f'originals/{formal_id}{original_suffix}',
                  scene=f'dataset_generator/scenes/{formal_id}.json',
                  script=f'dataset_generator/{prefix.lower()}_plot{number}.py')
    scene = {k: native[k] for k in allowed}
    scene.update(id=formal_id, status='user_approved', source_dataset='MathVision',
                 source_image=f'../../{formal["original_image"]}')
    writes = {f'{branch}/{formal[key]}': (root / row[key]).read_bytes() for key in ('image', 'original_image')}
    writes[f'{branch}/{formal["scene"]}'] = _json(scene)
    helper = f'{branch}/dataset_generator/mathvision_renderers'
    for source in sorted((package / 'shared').rglob('*')):
        if source.is_file() and '__pycache__' not in source.parts and source.suffix != '.pyc' and not source.name.startswith('test_'):
            writes[f'{helper}/{source.relative_to(package / "shared").as_posix()}'] = source.read_bytes()
    item_relative = f'{helper}/items/{formal_id}'
    execution = json.loads((item / 'execution.json').read_text(encoding='utf-8'))
    native_files = set(execution['files']) - {execution['original_image_name']}
    native_files.update(('execution.json', 'source_redraw.py'))
    # Semantic decisions are frozen drawing inputs for the protocol redraw.
    # Keep them with the native scene when preparing an isolated formal replay.
    if (item / 'protocol_review.json').is_file():
        native_files.add('protocol_review.json')
    for name in sorted(native_files):
        writes[f'{item_relative}/{name}'] = (item / name).read_bytes()
    formal['runtime_dependencies'] = sorted(p[len(branch) + 1:] for p in writes if p.startswith(helper + '/'))
    # Copy no candidate reference PNG into runtime dependencies. The native script
    # must produce a new image from the scene and vector code in a clean directory.
    script_path = Path(branch) / formal['script']
    relative = lambda path: os.path.relpath(path, script_path.parent).replace('\\', '/')
    fields = {k: formal[k] for k in ('id', 'source_dataset', 'question', 'answer', 'answer_type')}
    fields.update(subject=branch)
    if 'choices' in formal:
        fields['choices'] = formal['choices']
    script = f'''"""Frozen native MathVision redraw; importing does not write files."""
from pathlib import Path
import importlib.util
import json
HERE = Path(__file__).resolve().parent
class {formal_id}:
    def __init__(self):
        self.__dict__.update({fields!r})
        self.query = self.question
        self.level = None
        self.scene_path = HERE / {relative(branch + '/' + formal['scene'])!r}
    def get_scene(self):
        return json.loads(self.scene_path.read_text(encoding='utf-8'))
    def draw(self, num=0, output_path=None):
        if output_path is None and isinstance(num, (str, Path)):
            output_path = num
        output = Path(output_path) if output_path else HERE.parents[1] / '.runtime/mathvision_redraw' / '{formal_id}.png'
        spec = importlib.util.spec_from_file_location('mathvision_native_runtime', HERE / {relative(helper + '/runtime.py')!r})
        runtime = importlib.util.module_from_spec(spec); spec.loader.exec_module(runtime)
        return runtime.draw(HERE / {relative(item_relative)!r}, HERE / {relative(helper + '/native')!r}, output,
                            formal_scene=self.scene_path, original_image=HERE / {relative(branch + '/' + formal['original_image'])!r})
    def redraw(self, output_path=None):
        return self.draw(output_path=output_path)
if __name__ == '__main__':
    import sys
    print({formal_id}().draw(output_path=sys.argv[1] if len(sys.argv) > 1 else None))
'''
    writes[script_path.as_posix()] = script.encode('utf-8')
    notes = json.loads((root / row['provenance']).read_text(encoding='utf-8'))
    notes.update(source_key=row['source_key'], candidate_id=row['id'],
                 verification=json.loads((root / row['verification']).read_text(encoding='utf-8')),
                 geometry_notes={'additional_model_evidence': {k:v for k,v in native.items() if k not in allowed},
                                 'execution': 'Native semantic extras are retained in fingerprinted runtime dependencies; formal scene controls canonical geometry.'})
    if (item / 'protocol_review.json').is_file():
        notes['geometry_notes']['protocol_redraw'] = json.loads((item / 'protocol_review.json').read_text(encoding='utf-8'))
    return formal, writes, notes
