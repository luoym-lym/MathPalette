"""Use the versioned author executor after the ordinary workbench guards."""
from mathvision_plugins import PluginRenderer as MathVisionRenderer
from render_plugins import check_schema
from renderer_adapter import RENDER_LOCK
from workbench_io import WorkbenchError, pixel_hash
from author_adapter import engine


class PluginRenderer(MathVisionRenderer):
    def normalize(self, plugin):
        qid = plugin.get('question_id') if isinstance(plugin, dict) else None
        if self.adapter.is_author(qid):
            check_schema(plugin, self.schema, self.schema)
            points = {o['id'] for o in self.metadata[qid]['objects'] if o['kind'] == 'point'}
            for action in plugin.get('params', {}).get('actions', []):
                if action.get('type') == 'add_point' and action.get('filled') is False:
                    raise WorkbenchError('Frozen author renderer does not support open added points')
                if action.get('type') == 'set_object_style' and action.get('target') in points:
                    if any(k in action for k in ('interval', 'linewidth_pt', 'linestyle')):
                        raise WorkbenchError('Point targets support color only')
        return super().normalize(plugin)

    def render(self, plugin, frozen=False):
        qid = plugin.get('question_id') if isinstance(plugin, dict) else None
        if not self.adapter.is_author(qid): return super().render(plugin, frozen=frozen)
        normalized = self.normalize(plugin)
        if frozen and normalized != plugin:
            raise WorkbenchError('Frozen plugin is not normalized', 409, 'integrity_error')
        with RENDER_LOCK:
            scene = self.adapter.scene(qid)
            try:
                native = engine(self.adapter.branch)
                original = pixel_hash(native.png_bytes(scene))
                if original != self.metadata[qid]['original_pixel_sha256']:
                    raise WorkbenchError('Author baseline changed', 409, 'baseline_mismatch')
                try: native.apply(scene, normalized, self.schema)
                except (ValueError, KeyError, TypeError) as exc:
                    raise WorkbenchError(f'Invalid author action: {exc}', 409, 'invalid_action') from exc
                data = native.png_bytes(scene)
                digest = pixel_hash(data)
                if digest == original: raise WorkbenchError('No visual change', code='no_visual_change')
                return normalized, data, digest
            finally: scene.close()
