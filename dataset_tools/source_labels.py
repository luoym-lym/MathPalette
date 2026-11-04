"""Exact compatibility for the user-authorized source-label migration.

Archived recipes and approval wording remain immutable. Only the recorded hash
pairs are compatible; rendering still checks the saved variant's exact pixels.
"""
from pathlib import Path

from dataset_tools.catalog import digest, read

MIGRATION = Path(__file__).resolve().parents[1] / 'provenance/source_label_normalization_20261104.json'


def compatible_record_hash(branch, previous, record):
    current = digest(record)
    if previous == current:
        return True
    migration = read(MIGRATION)
    entry = migration['questions'].get(record.get('id'), {})
    return bool(entry.get('branch') == branch
                and record.get('source_dataset') == migration['source_dataset']
                and previous == entry.get('previous_record_sha256')
                and current == entry.get('record_sha256'))


def input_transition(branch, name):
    entry = read(MIGRATION)['input_transitions'].get(branch, {}).get(name, {})
    return [(entry['previous_sha256'], entry['current_sha256'])] if entry else []
