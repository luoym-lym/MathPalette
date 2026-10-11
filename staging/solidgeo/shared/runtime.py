"""Read-only scene reproduction for isolated review candidates."""
from pathlib import Path
import importlib.util
import json

ROOT = Path(__file__).resolve().parents[3]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def draw(scene_path, output_path, renderer):
    scene_path, output_path = Path(scene_path), Path(output_path)
    if output_path.suffix.lower() not in ('.png', '.svg'):
        raise ValueError('Output must be PNG or SVG')
    if output_path.resolve().is_relative_to(ROOT) and not output_path.resolve().is_relative_to(ROOT / '.runtime'):
        raise ValueError('Write reproductions under .runtime or outside the repository')
    scene = json.loads(scene_path.read_text(encoding='utf-8'))
    vector = output_path.suffix.lower() == '.svg'
    if renderer == 'SolidGeometry':
        module = load('_solidgeo_current', ROOT / 'SolidGeometry/dataset_generator/common_renderer.py')
        data = module.image_bytes(scene, vector=vector)[0]
    else:
        module = load('_solidgeo_' + renderer, Path(__file__).with_name(renderer + '_renderer.py'))
        if renderer == 'nets':
            data = module.image_bytes(scene, 'svg' if vector else 'png')
        elif renderer == 'special':
            data = module.render(scene, vector=vector)[0]
        else:
            data = module.render(scene, vector=vector)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(data)
    return str(output_path)
