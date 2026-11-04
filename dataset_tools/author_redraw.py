"""Reproduce an installed promote15 author original without changing shared renderers."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('question_id')
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    project = Path(__file__).resolve().parents[1]
    branch = 'PlaneGeometry' if args.question_id.startswith('Plane') else 'SolidGeometry' if args.question_id.startswith('Solid') else None
    if not branch: parser.error('Expected a Plane or Solid author question ID')
    sys.path.insert(0, str(project / branch / 'workbench'))
    from author_adapter import RendererAdapter, engine
    from workbench_io import load_config, pixel_hash
    adapter = RendererAdapter(load_config())
    if not adapter.is_author(args.question_id): parser.error('Not an installed author-promote15-v1 record')
    # Inspect verifies exact original pixels and the source identity before writing.
    adapter.inspect_question(args.question_id)
    scene = adapter.scene(args.question_id)
    try: data = engine(adapter.branch).png_bytes(scene)
    finally: scene.close()
    if pixel_hash(data) != pixel_hash(adapter.original_paths[args.question_id]):
        raise RuntimeError('Original pixel mismatch')
    target = args.output.resolve()
    if target.suffix.lower() != '.png' or target.is_relative_to(project / branch) or target.exists():
        parser.error('Output must be a new PNG outside the source branch')
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open('xb') as f: f.write(data)
    print(f'{target} {pixel_hash(data)}')


if __name__ == '__main__': main()
