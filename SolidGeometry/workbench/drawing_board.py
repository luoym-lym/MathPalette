"""Hit targets for the unified SolidGeometry protocol."""
from dataset_tools.drawing_board import PRESETS, _pixel_paths, describe_scene
from dataset_tools.drawing_board import describe_captured_scene as _describe

def describe_captured_scene(scene, qid):
    return _describe(scene, qid, 'SolidGeometry')
