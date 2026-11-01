"""Allow only the recorded review-workflow optimization when replaying old PNGs."""
from workbench_io import ROOT, read_json


def compatible_workflow_input(name, previous, current):
    if previous == current:
        return True
    pair = read_json(ROOT / 'workflow_compatibility.json')['files'].get(name)
    return bool(pair and previous == pair['previous_sha256'] and current == pair['current_sha256'])


def compatible_workflow_manifest(previous, current):
    return bool(previous and previous['environment'] == current['environment']
                and previous['files'].keys() == current['files'].keys()
                and all(compatible_workflow_input(name, value, current['files'][name])
                        for name, value in previous['files'].items()))
