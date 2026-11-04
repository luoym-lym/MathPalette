"""Only the recorded review-workflow transitions preserve saved rendering."""
TRANSITIONS = {
    'workbench/replay_archived.py': (
        '9e632053c7a216b65344e30b6bb85c0ad1897d727077863c546af8b541e8fce4',
        '48e2bf62395b9af3522814894558b4726b6572e8f58fb11cd7cd1b2c82ac767c'),
    'workbench/review_store.py': (
        '618b8c7b3ab9d413b392ebfa6ce3aae46b2f284915a789b1a6ca53b8dd3c519d',
        '24c3d465f34f2f6e692242e9c44028c0fe34393446ed72172382125b37abdce9'),
    'workbench/author_replay.py': (
        '487b1754721c9d25c99f91b0832f7831c178f43dc09cd0d45ec7e46457f45000',
        'ba4de126f2613212b8face7552e22ddfa95128b386a0015e2b018097ad8806d2'),
}

ADDITIONAL_TRANSITIONS = {'workbench/review_store.py': [['24c3d465f34f2f6e692242e9c44028c0fe34393446ed72172382125b37abdce9', '723912ae95d6b3bd6c206767bbaa0fd6fe567deaf6fc4c87a0b7f31d6324f02e']], 'workbench/replay_archived.py': [['48e2bf62395b9af3522814894558b4726b6572e8f58fb11cd7cd1b2c82ac767c', 'cbb103e88eb80feda7a65b360531ac9785c340cd3d66af91b00e7a2daca46329']]}

def compatible_workflow_input(name, previous, current):
    if previous == current:
        return True
    from dataset_tools.source_labels import input_transition
    edges = ([TRANSITIONS[name]] if name in TRANSITIONS else []) + ADDITIONAL_TRANSITIONS.get(name, [])
    edges += input_transition('SolidGeometry', name)
    seen, pending = set(), [previous]
    while pending:
        value = pending.pop()
        if value == current:
            return True
        if value not in seen:
            seen.add(value)
            pending.extend(b for a, b in edges if a == value)
    return False
