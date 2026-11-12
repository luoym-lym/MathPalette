"""Replay passed Special recipes through the unified drawing protocol."""
from __future__ import annotations
from pathlib import Path
import importlib.util
import json
import tempfile
import sys
from functools import lru_cache

from dataset_tools.unified_workbench import canonical_hash,file_hash,pixel_hash


@lru_cache(maxsize=3)
def _adapter(config_json):
    from renderer_adapter import RendererAdapter
    return RendererAdapter(json.loads(config_json))


def render_special_recipe(recipe,output_path=None,config_path=None):
    recipe={k:v for k,v in recipe.items() if k!='image_url'}
    from workbench_io import (WorkbenchError,load_config,read_json,contained_path,
                              atomic_write,environment_versions,GENERATOR_VERSION,SCHEMA_VERSION,
                              renderer_fingerprint)
    from render_plugins import PluginRenderer
    config=load_config(config_path)
    branch=Path(config['dataset_file']).resolve().parent
    project=branch.parent
    qid=recipe.get('question_id');slot=recipe.get('slot_id')
    if recipe.get('status')!='passed' or recipe.get('plugin_schema_version')!=SCHEMA_VERSION:
        raise WorkbenchError('Only a saved passed Special can be replayed',409,'version_mismatch')
    if recipe.get('environment')!=environment_versions():
        raise WorkbenchError('Saved rendering environment changed',409,'environment_changed')
    if not isinstance(qid,str) or not isinstance(slot,str):
        raise WorkbenchError('Missing question or Special slot',409,'integrity_error')
    records=read_json(contained_path(config['output_dir'],qid+'/recipes.json'))
    saved=next((r for r in records if r.get('slot_id')==slot),None)
    if saved is None or canonical_hash(saved)!=canonical_hash(recipe):
        raise WorkbenchError('Recipe is not the current saved Special',409,'integrity_error')
    plugin={k:recipe[k] for k in ('plugin_schema_version','question_id','category','operation','description','intent','params')}
    if canonical_hash(plugin)!=recipe['parameter_key'] or file_hash(contained_path(config['dataset_root'],recipe['plugin_path']))!=recipe['plugin_sha256']:
        raise WorkbenchError('Frozen plugin changed',409,'integrity_error')
    if file_hash(contained_path(config['dataset_root'],recipe['image_path']))!=recipe['png_sha256']:
        raise WorkbenchError('Accepted Special PNG changed',409,'integrity_error')
    adapter=_adapter(json.dumps(config,sort_keys=True))
    from dataset_tools.workbench_inputs import assert_question_inputs
    assert_question_inputs(adapter,qid,WorkbenchError,file_hash)
    if qid not in adapter.records:
        raise WorkbenchError('Unknown original question',404)
    migration=read_json(project/'provenance/drawing_protocol_integration_20261112.json')
    content_hash=canonical_hash({k:v for k,v in recipe.items()
                                if k not in ('slot_id','image_path','plugin_path')})
    # Deleting a saved slot renumbers later slots. Its reviewed content and
    # frozen drawing retain their identity across that path-only operation.
    proof=next((p for key,p in migration.get('specials',{}).items()
                if key.startswith(qid+'_') and p.get('recipe_content_sha256')==content_hash),None)
    migrated=proof is not None
    if migrated:
        if (file_hash(project/'dataset_tools/drawing.py')!=migration['drawing_module_sha256'] or
                canonical_hash(adapter.records[qid])!=migration['questions'][qid]['new_record_sha256'] or
                file_hash(adapter.source_paths[qid])!=migration['questions'][qid]['new_script_sha256']):
            raise WorkbenchError('Original or shared protocol changed after migration',409,'baseline_changed')
        module_path=branch/proof['drawing_module']
        if file_hash(module_path)!=proof['drawing_module_sha256']:
            raise WorkbenchError('Frozen unified Special drawing changed',409,'renderer_changed')
        spec=importlib.util.spec_from_file_location('_unified_special_'+qid,module_path)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        runtime=project/'.runtime/unified_replay';runtime.mkdir(parents=True,exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=qid+'-',dir=runtime) as temporary:
            image=Path(temporary)/'image.png'
            getattr(module,proof['function'])(image)
            data=image.read_bytes()
        digest=pixel_hash(data)
        if digest!=proof['render_pixel_sha256']:
            raise WorkbenchError('Unified Special redraw differs from its verified migration',409,'reproduction_mismatch')
    else:
        if (recipe.get('generator_version')!=GENERATOR_VERSION or
                recipe.get('question_record_sha256')!=canonical_hash(adapter.records[qid])):
            raise WorkbenchError('Question or generator changed since Pass',409,'baseline_changed')
        if (recipe.get('renderer_sha256')!=renderer_fingerprint() or
                recipe.get('schema_sha256')!=file_hash(branch/'workbench/plugin.schema.json')):
            raise WorkbenchError('Special renderer or schema changed since Pass',409,'renderer_changed')
        baseline=read_json(contained_path(config['output_dir'],'_baselines/'+recipe['baseline_fingerprint']+'.json'))
        if canonical_hash({k:baseline[k] for k in ('files','environment')})!=recipe['baseline_fingerprint']:
            raise WorkbenchError('Saved input manifest changed',409,'integrity_error')
        if any(baseline['files'].get(name)!=adapter.manifest['files'][name]
               for name in adapter.dependencies(qid)) or baseline['environment']!=adapter.environment:
            raise WorkbenchError('Question drawing inputs changed since Pass',409,'baseline_changed')
        metadata={qid:adapter.inspect_question(qid)}
        renderer=PluginRenderer(config,adapter,metadata)
        _,data,digest=renderer.render(plugin,frozen=True)
        if digest!=recipe['pixel_sha256']:
            raise WorkbenchError('Redraw differs from the accepted Special',409,'reproduction_mismatch')
    target=Path(output_path).resolve() if output_path else Path(config['runtime_dir'])/'reproduced'/qid/(slot+'.png')
    target=target.resolve()
    if target.suffix.lower()!='.png' or target.is_relative_to(project) and not target.is_relative_to(project/'.runtime'):
        raise WorkbenchError('Replay into project .runtime or an external PNG',code='unsafe_path')
    if target in adapter.input_files.values():
        raise WorkbenchError('Cannot overwrite a frozen drawing input',code='unsafe_path')
    atomic_write(target,data)
    matches=digest==recipe['pixel_sha256']
    return {'image_path':str(target),'pixel_sha256':digest,'matches_accepted':matches,
            'migration_verified':bool(migrated),'render_equivalent':matches or bool(migrated),
            'accepted_pixel_sha256':recipe['pixel_sha256']}


def draw_slot(branch,qid,slot,output_path=None):
    root=Path(__file__).resolve().parents[1]
    recipe=next((r for r in json.loads((root/branch/'special_variant'/qid/'recipes.json').read_text())
                 if r['slot_id']==slot),None)
    if recipe is None:
        raise ValueError('Unknown current Special slot: '+str(slot))
    from dataset_tools.unified_workbench import RENDER_LOCK
    names=('workbench_io','renderer_adapter','render_plugins','partial_style','drawing_board')
    with RENDER_LOCK:
        old_path=sys.path[:]
        previous={name:sys.modules.pop(name,None) for name in names}
        sys.path.insert(0,str(root/branch/'workbench'))
        try:
            return render_special_recipe(recipe,output_path,root/branch/'workbench/config.json')['image_path']
        finally:
            sys.path[:]=old_path
            for name in names:
                sys.modules.pop(name,None)
                if previous[name] is not None:
                    sys.modules[name]=previous[name]
