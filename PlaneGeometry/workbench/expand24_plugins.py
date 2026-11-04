"""Use the frozen expand24 executor after ordinary workbench normalization."""
from author_plugins import PluginRenderer as PreviousAuthorRenderer
from expand24_adapter import frozen_engine
from renderer_adapter import RENDER_LOCK
from workbench_io import WorkbenchError, pixel_hash

class PluginRenderer(PreviousAuthorRenderer):
    def render(self, plugin, frozen=False):
        qid = plugin.get('question_id') if isinstance(plugin, dict) else None
        if not self.adapter.is_expand24(qid):
            return super().render(plugin, frozen=frozen)
        normalized = self.normalize(plugin)
        if frozen and normalized != plugin:
            raise WorkbenchError('Frozen plugin is not normalized', 409, 'integrity_error')
        with RENDER_LOCK:
            scene = self.adapter.scene(qid)
            try:
                engine = frozen_engine(self.adapter.branch)
                original = pixel_hash(engine.png_bytes(scene))
                if original != self.metadata[qid]['original_pixel_sha256']:
                    raise WorkbenchError('Original pixels changed', 409, 'baseline_mismatch')
                try:
                    engine.apply(scene, normalized, self.schema)
                except (ValueError, TypeError, KeyError) as exc:
                    raise WorkbenchError('Invalid expand24 action: ' + str(exc), 409, 'invalid_action') from exc
                data = engine.png_bytes(scene)
                digest = pixel_hash(data)
                if digest == original:
                    raise WorkbenchError('No visual change', code='no_visual_change')
                return normalized, data, digest
            finally:
                scene.close()
