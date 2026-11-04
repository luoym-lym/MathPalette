"""Allow only the recorded review-workflow optimization when replaying old PNGs."""
from workbench_io import ROOT, read_json


def compatible_workflow_input(name, previous, current):
    if previous == current:
        return True
    from dataset_tools.source_labels import input_transition
    data = read_json(ROOT / 'workflow_compatibility.json')
    pair = data['files'].get(name)
    edges = [(pair['previous_sha256'], pair['current_sha256'])] if pair else []
    edges.extend((p['previous_sha256'], p['current_sha256']) for p in data.get('transitions', {}).get(name, []))
    edges.extend(input_transition('PlaneGeometry', name))
    # A chain is valid only through explicitly recorded transitions.
    seen, pending = set(), [previous]
    while pending:
        value = pending.pop()
        if value == current:
            return True
        if value not in seen:
            seen.add(value)
            pending.extend(b for a, b in edges if a == value)
    return False


def compatible_workflow_manifest(previous, current):
    return bool(previous and previous['environment'] == current['environment']
                and previous['files'].keys() == current['files'].keys()
                and all(compatible_workflow_input(name, value, current['files'][name])
                        for name, value in previous['files'].items()))
