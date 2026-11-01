"""Load the immutable, content-addressed authored-question renderer."""
import hashlib
import importlib.util
from pathlib import Path
_PATH = Path(__file__).with_name('frozen_5090f6c84b1c5d62') / 'common_renderer.py'
if hashlib.sha256(_PATH.read_bytes()).hexdigest() != '5090f6c84b1c5d624b000dcb3143dd7586d671695f7bd3486ae206f1f978e490':
    raise ValueError('Frozen authored renderer has changed')
_SPEC = importlib.util.spec_from_file_location('_authored_frozen_5090f6c84b1c5d62', _PATH)
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)
render_scene = _MODULE.render_scene
validate_scene = _MODULE.validate_scene
image_bytes = _MODULE.image_bytes
draw = _MODULE.draw
