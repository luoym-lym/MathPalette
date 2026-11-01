"""Exact compatibility for the Ana52 catalog-gap fix; rendering is unchanged."""
from workbench_io import ROOT, file_hash, read_json, renderer_fingerprint


def compatible_renderer(signature):
    current = renderer_fingerprint()
    schema = file_hash(ROOT / 'plugin.schema.json')
    if signature.get('schema_sha256') != schema:
        return False
    if signature.get('renderer_sha256') == current:
        return True
    known = read_json(ROOT / 'renderer_compatibility.json')
    return (current == known['current_renderer_sha256']
            and schema == known['schema_sha256']
            and signature.get('renderer_sha256') in known['previous_renderer_sha256'])
