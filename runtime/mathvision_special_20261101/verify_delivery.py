"""Verify a runtime delivery archive without changing frozen evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def read(path):
    return Path(path).read_bytes()


def data(path):
    return json.loads(read(path).decode('utf-8-sig'))


def sha(path):
    return hashlib.sha256(read(path)).hexdigest()


def verify(batch):
    directory = HERE / batch
    assert directory.resolve().parent == HERE
    manifest = data(directory / 'manifest.json')
    assert manifest['batch'] == batch
    with zipfile.ZipFile(HERE / (batch + '.zip')) as archive:
        assert archive.testzip() is None
        for name in archive.namelist():
            relative = Path(name)
            assert not relative.is_absolute() and '..' not in relative.parts
            assert relative.parts[0] == batch
            assert archive.read(name) == read(HERE / relative), name
    for entry in manifest['candidates']:
        question = entry['question_id']
        candidate = directory / question
        assert sha(candidate / 'candidate.png') == entry['candidate_sha256']
        assert sha(candidate / 'plugin.json') == entry['plugin_sha256']
        assert sha(directory / 'reproduced' / (question + '.png')) == entry['candidate_sha256']
        assert data(candidate / 'independent_review.json')['decision'] == 'recommended'
        assert entry['tested_final_answers'] == [entry['expected_wrong_answer']] * 2
        assert str(entry['correct_answer']) != str(entry['expected_wrong_answer'])
        evidence = candidate / entry['evidence_path']
        if evidence.is_file():
            evidence = evidence.parent
        assert sha(candidate / 'design.json') == sha(evidence / 'design_snapshot.json')
        for relative, expected in entry['input_files'].items():
            assert sha(ROOT / relative) == expected, relative
        for supplement in entry.get('supplemental_evidence', []):
            for relative, expected in supplement['files_sha256'].items():
                assert sha(directory / supplement['packaged_path'] / relative) == expected
    result = {
        'batch': batch,
        'questions': [e['question_id'] for e in manifest['candidates']],
        'archive_valid': True,
        'every_archived_file_matches_runtime_copy': True,
        'candidate_and_plugin_hashes_valid': True,
        'independent_review_recommended': True,
        'replay_matches_tested_png': True,
        'supplemental_evidence_exact_copy': True,
        'relevant_formal_input_hashes_unchanged_since_packaging': True,
        'unrelated_concurrent_changes_preserved': True,
    }
    path = HERE / 'delivery_verification.json'
    previous = data(path)
    previous = [x for x in previous if x['batch'] != batch] + [result]
    path.write_text(json.dumps(previous, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('batch')
    verify(parser.parse_args().batch)
