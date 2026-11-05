"""Special actions on real extensions95 contours, preserving frozen fills."""
from expand24_plugins import PluginRenderer as PreviousRenderer
from expand24_adapter import frozen_engine
from extensions95_adapter import png_bytes
from renderer_adapter import RENDER_LOCK
from workbench_io import WorkbenchError, pixel_hash


class PluginRenderer(PreviousRenderer):
    def render(self, plugin, frozen=False):
        qid = plugin.get('question_id') if isinstance(plugin, dict) else None
        if not self.adapter.is_extensions95(qid):
            return super().render(plugin, frozen=frozen)
        normalized = self.normalize(plugin)
        if frozen and normalized != plugin:
            raise WorkbenchError('Frozen plugin is not normalized', 409, 'integrity_error')
        with RENDER_LOCK:
            scene = self.adapter.scene(qid)
            try:
                original = pixel_hash(png_bytes(scene))
                if original != self.metadata[qid]['original_pixel_sha256']:
                    raise WorkbenchError('Original pixels changed', 409, 'baseline_mismatch')
                try:
                    frozen_engine(self.adapter.branch).apply(scene, normalized, self.schema)
                except (ValueError, TypeError, KeyError) as exc:
                    raise WorkbenchError('Invalid extensions95 action: ' + str(exc), 409, 'invalid_action') from exc
                data = png_bytes(scene)
                digest = pixel_hash(data)
                if digest == original:
                    raise WorkbenchError('No visual change', code='no_visual_change')
                return normalized, data, digest
            finally:
                scene.close()
