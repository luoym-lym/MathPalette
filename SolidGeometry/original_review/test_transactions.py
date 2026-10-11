"""Original Pass/Delete transaction, replay, isolation, and crash regression tests.

Every repository and candidate is synthetic and disposable. No automated test
records approvals or removes candidates from the delivery checkout.
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import copy
import json
import subprocess
import sys
import threading
import unittest
from unittest.mock import patch
import uuid

from importer import ReviewError, fingerprint, payload_paths
from store import ReviewStore
import store as store_module
from dataset_tools import catalog
from test_support import IsolatedRepository, file_hashes, read_json, read_rows, write_json


class SimulatedPowerLoss(BaseException):
    pass


class OriginalTransactionTests(unittest.TestCase):
    def setUp(self):
        self.fixture = IsolatedRepository(2)
        self.root = self.fixture.root
        self.store = ReviewStore(self.root)
        self.initial = catalog.catalog(self.root)
        self.next_number = max(int(row['id'][5:]) for row in self.initial if row['branch'] == 'SolidGeometry') + 1
        self.next_id = f'Solid{self.next_number:02d}'

    def tearDown(self):
        self.fixture.close()

    def displayed(self, index=0, store=None):
        store = store or self.store
        cid = self.fixture.candidates[index]['id']
        return next(row for row in store.navigate(cid)['candidates'] if row['id'] == cid)

    def mutate(self, action='pass', index=0, *, store=None, request=None, row=None):
        store = store or self.store
        row = row or self.displayed(index, store)
        return getattr(store, action + '_candidate')(row['id'], row['content_sha256'], request or uuid.uuid4().hex)

    def test_read_and_navigation_never_import_or_approve(self):
        before = file_hashes(self.root)
        state = self.store.snapshot()
        self.assertEqual(state['counts'], {'total': 2, 'pending': 2, 'passed': 0, 'deleted': 0})
        self.displayed(1)
        self.assertEqual(file_hashes(self.root), before)
        self.assertEqual(catalog.catalog(self.root), self.initial)

    def test_pass_minimal_package_approval_index_renderer_and_special_compatibility(self):
        source = self.fixture.candidates[0]
        before = file_hashes(self.root, include_staging=False)
        result = self.mutate()['result']
        qid = result['formal_id']
        self.assertEqual(qid, self.next_id)
        after = catalog.catalog(self.root)
        self.assertEqual(len(after), len(self.initial) + 1)
        self.assertEqual(after, read_rows(self.root / 'question_bank.jsonl'))
        self.assertEqual(after[:-1], self.initial)
        record = after[-1]
        self.assertEqual(record['answer'], source['answer'])
        self.assertEqual(record['source_dataset'], 'SOLIDGEO')
        approval = read_json(self.root / 'provenance/approvals.json')['approvals'][qid]
        self.assertEqual(approval['reviewer'], 'user')
        self.assertEqual(approval['instruction'], 'Pass (原题通过)')
        self.assertTrue(approval['approved_at_utc'])
        scene = read_json(self.root / record['scene'])
        self.assertEqual(set(scene), catalog.FORMAL_SCENE_FIELDS['SolidGeometry'])
        self.assertEqual(scene['id'], qid)
        notes = read_json(self.root / 'provenance/source_notes.json')[qid]['original_review']
        self.assertEqual(notes['candidate_sha256'], result['candidate_sha256'])
        self.assertEqual(notes['verification'], source['verification'])
        mutable = {'SolidGeometry/dataset.jsonl', 'provenance/approvals.json',
                   'provenance/source_notes.json', 'question_bank.jsonl'}
        after_files = file_hashes(self.root, include_staging=False)
        for path, digest in before.items():
            if path not in mutable:
                self.assertEqual(after_files[path], digest, path)
        self.assertNotIn(source['id'], {row['id'] for row in read_rows(self.fixture.manifest)})
        for relative in source['paths'].values():
            self.assertFalse((self.root / relative).exists(), relative)
        script = r'''
import importlib.util,json,sys
from pathlib import Path
root=Path(sys.argv[1]); qid=sys.argv[2]
sys.path.insert(0,str(root)); sys.path.insert(0,str(root/'SolidGeometry/workbench'))
from dataset_tools import catalog
from workbench_io import load_config
from renderer_adapter import RendererAdapter
from drawing_board import describe_scene
row=next(r for r in catalog.rows(root/'SolidGeometry/dataset.jsonl') if r['id']==qid)
spec=importlib.util.spec_from_file_location('approved_fixture',root/'SolidGeometry'/row['script'])
module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
question=getattr(module,qid)()
assert question.query==row['question'] and question.answer==row['answer']
assert question.answer_type==row['answer_type'] and question.get_scene()['id']==qid
adapter=RendererAdapter(load_config(root/'SolidGeometry/workbench/config.json'))
meta=adapter.inspect_question(qid)
board=describe_scene(adapter,qid)
assert meta['original_pixel_sha256'] and board['targets']
print(json.dumps({'formal_id':qid,'special_targets':len(board['targets']),'pixels_match':True}))
'''
        checked = subprocess.run([sys.executable, '-B', '-c', script, str(self.root), qid],
                                 capture_output=True, text=True, timeout=90)
        self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
        self.assertTrue(json.loads(checked.stdout)['pixels_match'])

    def test_double_click_replay_and_restart_import_exactly_once(self):
        row = self.displayed()
        request = uuid.uuid4().hex
        first = self.mutate(row=row, request=request)['result']
        after = file_hashes(self.root)
        for store, token in [(self.store, request), (self.store, uuid.uuid4().hex),
                             (ReviewStore(self.root), request), (ReviewStore(self.root), uuid.uuid4().hex)]:
            self.assertEqual(self.mutate(store=store, row=row, request=token)['result'], first)
            self.assertEqual(file_hashes(self.root), after)
        self.assertEqual(len(catalog.catalog(self.root)), len(self.initial) + 1)

    def test_request_id_cannot_be_reused_for_other_action_or_candidate(self):
        row = self.displayed()
        request = uuid.uuid4().hex
        self.mutate(row=row, request=request)
        for action, index, item in [('delete', 0, row), ('pass', 1, self.displayed(1))]:
            with self.subTest(action=action, index=index), self.assertRaises(ReviewError) as caught:
                self.mutate(action, index, row=item, request=request)
            self.assertEqual(caught.exception.code, 'request_conflict')

    def test_new_idempotency_key_for_completed_action_stays_bound_to_that_action(self):
        row = self.displayed()
        self.mutate(row=row)
        replay_key = uuid.uuid4().hex
        self.mutate(row=row, request=replay_key)
        restarted = ReviewStore(self.root)
        with self.assertRaises(ReviewError) as caught:
            self.mutate(index=1, store=restarted, request=replay_key)
        self.assertEqual(caught.exception.code, 'request_conflict')

    def test_fresh_restart_does_not_trust_modified_audit_payload_or_answer(self):
        for field in ('provenance', 'answer'):
            with self.subTest(field=field):
                fixture = IsolatedRepository(1)
                try:
                    if field == 'answer':
                        fixture.edit(0, {'answer': '999'})
                        fixture.commit_candidates()
                    else:
                        path = payload_paths(fixture.root, fixture.candidates[0])['provenance']
                        path.write_bytes(path.read_bytes() + b'\n')
                        # Make the changed asset safely recoverable so this test
                        # specifically reaches frozen-review baseline checking.
                        fixture.commit_candidates()
                    fresh = ReviewStore(fixture.root)
                    row = fresh.snapshot()['candidates'][0]
                    self.assertFalse(row['eligible'])
                    before = file_hashes(fixture.root)
                    with self.assertRaises(ReviewError) as caught:
                        fresh.pass_candidate(row['id'], row['content_sha256'], uuid.uuid4().hex)
                    self.assertEqual(caught.exception.code, 'ineligible_candidate')
                    self.assertEqual(file_hashes(fixture.root), before)
                finally:
                    fixture.close()

    def test_independent_server_processes_allocate_distinct_formal_ids(self):
        rows = [self.displayed(0), self.displayed(1)]
        code = """
import json,sys,uuid
from store import ReviewStore
store=ReviewStore(sys.argv[1]); row=json.loads(sys.argv[2])
result=store.pass_candidate(row['id'],row['content_sha256'],uuid.uuid4().hex)
print(json.dumps(result['result']))
"""
        processes = [subprocess.Popen([sys.executable, '-B', '-c', code, str(self.root), json.dumps(row)],
                     cwd=str(__import__('pathlib').Path(__file__).parent),
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) for row in rows]
        try:
            results = []
            for process in processes:
                stdout, stderr = process.communicate(timeout=90)
                self.assertEqual(process.returncode, 0, stdout + stderr)
                results.append(json.loads(stdout))
            self.assertEqual({row['formal_id'] for row in results},
                             {self.next_id, f'Solid{self.next_number + 1:02d}'})
            self.assertEqual(len(catalog.catalog(self.root)), len(self.initial) + 2)
        finally:
            for process in processes:
                if process.poll() is None:
                    process.kill()
                    process.wait(5)

    def test_pass_cleanup_preserves_untracked_and_shared_files(self):
        first, second = self.fixture.candidates
        paths = payload_paths(self.root, first)
        untracked = paths['scene'].parent / 'untracked-user-note.txt'
        untracked.write_text('preserve unique user work')
        # A provenance reference from another candidate protects this owned asset.
        second['source_notes']['shared_fixture'] = first['paths']['provenance']
        self.fixture.save()
        shared = paths['provenance']
        result = self.mutate()['result']
        self.assertTrue(shared.exists())
        self.assertEqual(untracked.read_text(), 'preserve unique user work')
        self.assertIn(shared.relative_to(self.root).as_posix(), result['preserved_shared_files'])
        self.assertNotIn(first['id'], {row['id'] for row in read_rows(self.fixture.manifest)})
        self.assertEqual(len(catalog.catalog(self.root)), len(self.initial) + 1)

    def test_existing_approval_corruption_blocks_import_without_refreshing_it(self):
        path = self.root / 'SolidGeometry/dataset.jsonl'
        rows = read_rows(path)
        rows[0]['answer'] = '999'
        from test_support import write_rows
        write_rows(path, rows)
        before = file_hashes(self.root)
        with self.assertRaises(ValueError):
            self.mutate()
        self.assertEqual(file_hashes(self.root), before)

    def test_stale_metadata_and_asset_hashes_cannot_be_passed_or_deleted(self):
        row = self.displayed()
        old = copy.deepcopy(self.fixture.candidates[0])
        self.fixture.edit(0, {'answer': 'different'})
        for action in ('pass', 'delete'):
            with self.subTest(action=action), self.assertRaises(ReviewError) as caught:
                self.mutate(action, row=row)
            self.assertEqual(caught.exception.code, 'stale_candidate')
        self.fixture.candidates[0] = old
        self.fixture.save()
        path = payload_paths(self.root, old)['provenance']
        path.write_bytes(path.read_bytes() + b'\n')
        with self.assertRaises(ReviewError) as caught:
            self.mutate(row=row)
        self.assertEqual(caught.exception.code, 'stale_candidate')
        self.assertEqual(catalog.catalog(self.root), self.initial)

    def test_failed_eligibility_never_creates_formal_side_effects(self):
        self.fixture.edit(0, {'pass_eligible': False, 'pass_blockers': ['unverified answer']})
        self.fixture.commit_candidates()
        row = self.displayed()
        before = file_hashes(self.root)
        with self.assertRaises(ReviewError) as caught:
            self.mutate(row=row)
        self.assertEqual(caught.exception.code, 'ineligible_candidate')
        self.assertEqual(file_hashes(self.root), before)

    def test_parallel_tabs_same_candidate_and_distinct_candidates_allocate_once(self):
        rows = [self.displayed(0), self.displayed(1)]
        stores = [ReviewStore(self.root) for _ in range(4)]
        barrier = threading.Barrier(4)
        def task(index):
            barrier.wait(10)
            return self.mutate(index=index % 2, store=stores[index], row=rows[index % 2])['result']
        with ThreadPoolExecutor(max_workers=4) as workers:
            results = list(workers.map(task, range(4)))
        self.assertEqual(results[0]['formal_id'], results[2]['formal_id'])
        self.assertEqual(results[1]['formal_id'], results[3]['formal_id'])
        self.assertEqual({r['formal_id'] for r in results}, {self.next_id, f'Solid{self.next_number + 1:02d}'})
        self.assertEqual(len(catalog.catalog(self.root)), len(self.initial) + 2)
        self.assertEqual(ReviewStore(self.root).snapshot()['counts']['passed'], 2)

    def test_restored_formal_data_with_ahead_high_water_blocks_without_writes(self):
        row = self.displayed()
        self.store.state['next_solid_number'] = self.next_number + 3
        write_json(self.store.state_path, self.store.state)
        before = file_hashes(self.root)
        before_state = self.store.state_path.read_bytes()
        with self.assertRaises(ReviewError) as caught:
            self.mutate(row=row)
        self.assertEqual(caught.exception.code, 'formal_numbering_conflict')
        self.assertEqual(file_hashes(self.root), before)
        self.assertEqual(self.store.state_path.read_bytes(), before_state)
        self.assertFalse(self.store.journal_path.exists())
        self.assertEqual(catalog.catalog(self.root), self.initial)

    def test_preexisting_formal_artifact_is_not_overwritten(self):
        target = self.root / f'SolidGeometry/image/{self.next_id}.png'
        target.write_bytes(b'preexisting unrelated file')
        with self.assertRaises(ReviewError) as caught:
            self.mutate()
        self.assertEqual(caught.exception.code, 'formal_collision')
        self.assertEqual(target.read_bytes(), b'preexisting unrelated file')

    def test_duplicate_source_is_not_imported_twice(self):
        self.fixture.edit(1, {'source_key': self.fixture.candidates[0]['source_key']})
        self.fixture.commit_candidates()
        self.mutate()
        with self.assertRaises(ReviewError) as caught:
            self.mutate(index=1)
        self.assertEqual(caught.exception.code, 'duplicate_source')

    def test_delete_removes_all_tracked_owned_files_and_no_formal_data(self):
        row = self.displayed()
        paths = list(payload_paths(self.root, self.fixture.candidates[0]).values())
        extra = paths[0].parent / 'tracked-diagnostic.txt'
        extra.write_text('fixture output')
        self.fixture.commit_candidates()
        untracked = paths[0].parent / 'untracked-user-notes.txt'
        untracked.write_text('unique user work; preserve')
        before = file_hashes(self.root, include_staging=False)
        result = self.mutate('delete', row=row)['result']
        for path in [*paths, extra]:
            self.assertFalse(path.exists(), path)
        self.assertEqual(untracked.read_text(), 'unique user work; preserve')
        self.assertEqual(file_hashes(self.root, include_staging=False), before)
        self.assertEqual([r['id'] for r in read_rows(self.fixture.manifest)], [self.fixture.candidates[1]['id']])
        self.assertEqual(set(result['deleted_files']), {p.relative_to(self.root).as_posix() for p in [*paths, extra]})
        self.assertEqual(catalog.catalog(self.root), self.initial)
        # A replay after every owned file has disappeared is still idempotent.
        self.assertEqual(self.mutate('delete', row=row)['result'], result)
        self.assertEqual(ReviewStore(self.root).snapshot()['counts']['deleted'], 1)

    def test_delete_preserves_shared_candidate_references_and_dependencies(self):
        first, second = self.fixture.candidates
        shared = payload_paths(self.root, first)['original_image']
        second['original_image'] = first['original_image']
        second['paths']['original'] = first['paths']['original']
        scene_path = payload_paths(self.root, second)['scene']
        scene = read_json(scene_path)
        scene['source_image'] = f"../{first['id']}/source.png"
        write_json(scene_path, scene)
        self.fixture.seal(second)
        self.fixture.save()
        self.fixture.commit_candidates()
        result = self.mutate('delete')['result']
        self.assertTrue(shared.is_file())
        self.assertIn(shared.relative_to(self.root).as_posix(), result['preserved_shared_files'])
        survivor = self.displayed(1)
        self.assertTrue(survivor['eligible'], survivor['ineligible_reasons'])
        for path in payload_paths(self.root, second).values():
            self.assertTrue(path.is_file())
        self.assertEqual(catalog.catalog(self.root), self.initial)

    def test_delete_blocks_dirty_tracked_assets_even_if_they_are_staged(self):
        target = payload_paths(self.root, self.fixture.candidates[0])['provenance']
        target.write_bytes(target.read_bytes() + b'\n')
        for staged in (False, True):
            if staged:
                self.fixture.git('add', '--', str(target.relative_to(self.root)))
            row = self.displayed()
            before = file_hashes(self.root)
            with self.subTest(staged=staged), self.assertRaises(ReviewError):
                self.mutate('delete', row=row)
            self.assertEqual(file_hashes(self.root), before)

    def test_delete_traversal_symlink_and_non_candidate_assets_never_escape(self):
        outside = self.root.parent / 'protected.txt'
        outside.write_text('untouched')
        first = self.fixture.candidates[0]
        target = payload_paths(self.root, first)['provenance']
        target.unlink()
        target.symlink_to(outside)
        before = file_hashes(self.root, include_staging=False)
        with self.assertRaises(ReviewError):
            self.mutate('delete')
        self.assertEqual(outside.read_text(), 'untouched')
        self.assertEqual(file_hashes(self.root, include_staging=False), before)

    def test_all_pass_failure_boundaries_restore_exact_durable_bytes(self):
        self._assert_failure_boundaries('pass')

    def test_all_delete_failure_boundaries_restore_exact_durable_bytes(self):
        self._assert_failure_boundaries('delete')

    def _assert_failure_boundaries(self, action):
        # Learn all exposed write/unlink boundaries from a successful disposable
        # run, then inject failure at each boundary in a brand-new repository.
        observed = []
        self.store.failpoint = observed.append
        self.mutate(action)
        self.assertIn('prepared', observed)
        self.assertIn('files_written', observed)
        self.assertIn('committed', observed)
        for stage in observed:
            if stage == 'committed':
                continue
            with self.subTest(action=action, stage=stage):
                fixture = IsolatedRepository(1)
                try:
                    store = ReviewStore(fixture.root)
                    row = store.snapshot()['candidates'][0]
                    before = file_hashes(fixture.root)
                    before_state = store.state_path.read_bytes() if store.state_path.exists() else None
                    def fail(current):
                        if current == stage:
                            raise RuntimeError('injected transaction failure: ' + stage)
                    store.failpoint = fail
                    with self.assertRaisesRegex(RuntimeError, 'injected transaction failure'):
                        getattr(store, action + '_candidate')(row['id'], row['content_sha256'], uuid.uuid4().hex)
                    self.assertEqual(file_hashes(fixture.root), before)
                    self.assertEqual(store.state_path.read_bytes() if store.state_path.exists() else None, before_state)
                    recovered = ReviewStore(fixture.root)
                    self.assertEqual(recovered.snapshot()['counts']['pending'], 1)
                    self.assertFalse(recovered.journal_path.exists())
                    self.assertEqual(catalog.catalog(fixture.root), self.initial)
                finally:
                    fixture.close()

    def test_process_interruption_before_commit_rolls_back_after_restart(self):
        for action in ('pass', 'delete'):
            for stage in ('prepared', 'files_written',
                          'after_unlink:staging/solidgeo/candidates/SOLIDGEO_TEST_001/scene.json'):
                with self.subTest(action=action, stage=stage):
                    fixture = IsolatedRepository(1)
                    try:
                        store = ReviewStore(fixture.root)
                        row = store.snapshot()['candidates'][0]
                        before = file_hashes(fixture.root)
                        def crash(current):
                            if current == stage:
                                raise SimulatedPowerLoss(stage)
                        store.failpoint = crash
                        with self.assertRaises(SimulatedPowerLoss):
                            getattr(store, action + '_candidate')(row['id'], row['content_sha256'], uuid.uuid4().hex)
                        self.assertTrue(store.journal_path.exists())
                        recovered = ReviewStore(fixture.root)
                        self.assertEqual(file_hashes(fixture.root), before)
                        self.assertEqual(recovered.snapshot()['counts']['pending'], 1)
                        self.assertFalse(recovered.journal_path.exists())
                    finally:
                        fixture.close()

    def test_commit_is_durable_despite_lost_response_or_process_interruption(self):
        for exception in (RuntimeError, SimulatedPowerLoss):
            with self.subTest(exception=exception.__name__):
                fixture = IsolatedRepository(1)
                try:
                    store = ReviewStore(fixture.root)
                    row = store.snapshot()['candidates'][0]
                    request = uuid.uuid4().hex
                    def crash(stage):
                        if stage == 'committed':
                            raise exception('lost response after durable commit')
                    store.failpoint = crash
                    with self.assertRaises(exception):
                        store.pass_candidate(row['id'], row['content_sha256'], request)
                    recovered = ReviewStore(fixture.root)
                    self.assertEqual(recovered.snapshot()['counts']['passed'], 1)
                    self.assertEqual(len(catalog.catalog(fixture.root)), len(self.initial) + 1)
                    replay = recovered.pass_candidate(row['id'], row['content_sha256'], request)
                    self.assertEqual(replay['result']['formal_id'], self.next_id)
                finally:
                    fixture.close()

    def test_dirty_candidate_metadata_is_preserved_for_both_pass_and_delete(self):
        for action in ('pass', 'delete'):
            with self.subTest(action=action):
                fixture = IsolatedRepository(1)
                try:
                    fixture.candidates[0]['source_notes']['unique_user_edit'] = 'not committed to Git'
                    fixture.save()
                    store = ReviewStore(fixture.root)
                    row = store.snapshot()['candidates'][0]
                    before = file_hashes(fixture.root)
                    with self.assertRaises(ReviewError):
                        getattr(store, action + '_candidate')(row['id'], row['content_sha256'], uuid.uuid4().hex)
                    self.assertEqual(file_hashes(fixture.root), before)
                    self.assertEqual(read_rows(fixture.manifest)[0]['source_notes']['unique_user_edit'], 'not committed to Git')
                    self.assertEqual(store.snapshot()['counts']['pending'], 1)
                finally:
                    fixture.close()

    def test_previous_removals_do_not_block_clean_rows_in_dirty_manifest(self):
        for actions in (('delete', 'pass'), ('pass', 'delete'), ('delete', 'delete'), ('pass', 'pass')):
            with self.subTest(actions=actions):
                fixture = IsolatedRepository(2)
                try:
                    store = ReviewStore(fixture.root)
                    baseline_count = len(catalog.catalog(fixture.root))
                    for action in actions:
                        row = store.snapshot()['candidates'][0]
                        result = getattr(store, action + '_candidate')(row['id'], row['content_sha256'], uuid.uuid4().hex)
                        self.assertEqual(result['result']['action'], action)
                    self.assertEqual(read_rows(fixture.manifest), [])
                    self.assertEqual(len(catalog.catalog(fixture.root)), baseline_count + actions.count('pass'))
                    self.assertEqual(store.snapshot()['counts']['pending'], 0)
                finally:
                    fixture.close()

    def test_external_manifest_edits_are_preserved_without_partial_import(self):
        for action in ('pass', 'delete'):
            with self.subTest(action=action):
                fixture = IsolatedRepository(2)
                try:
                    store = ReviewStore(fixture.root)
                    row = store.snapshot()['candidates'][0]
                    baseline = catalog.catalog(fixture.root)
                    edited_bytes = []
                    def edit(stage):
                        if stage == 'prepared':
                            fixture.candidates[1]['source_notes']['new_user_note'] = 'keep uncommitted metadata'
                            fixture.save()
                            edited_bytes.append(fixture.manifest.read_bytes())
                    store.failpoint = edit
                    with self.assertRaises(ReviewError) as caught:
                        getattr(store, action + '_candidate')(row['id'], row['content_sha256'], uuid.uuid4().hex)
                    self.assertEqual(caught.exception.code, 'stale_candidate')
                    self.assertEqual(fixture.manifest.read_bytes(), edited_bytes[0])
                    self.assertEqual(catalog.catalog(fixture.root), baseline)
                    self.assertEqual(store.snapshot()['counts']['pending'], 2)
                    for candidate in fixture.candidates:
                        for path in payload_paths(fixture.root, candidate).values():
                            self.assertTrue(path.exists())
                finally:
                    fixture.close()

    def test_external_candidate_edits_during_transaction_survive_rollback(self):
        for action in ('pass', 'delete'):
            for stage in ('prepared', 'before_unlink:staging/solidgeo/candidates/SOLIDGEO_TEST_001/provenance.json'):
                with self.subTest(action=action, stage=stage):
                    fixture = IsolatedRepository(1)
                    try:
                        store = ReviewStore(fixture.root)
                        row = store.snapshot()['candidates'][0]
                        target = payload_paths(fixture.root, fixture.candidates[0])['provenance']
                        new_bytes = target.read_bytes() + b'\n  '
                        before_formal = file_hashes(fixture.root, include_staging=False)
                        def edit(current):
                            if current == stage:
                                target.write_bytes(new_bytes)
                        store.failpoint = edit
                        with self.assertRaises(ReviewError) as caught:
                            getattr(store, action + '_candidate')(row['id'], row['content_sha256'], uuid.uuid4().hex)
                        self.assertEqual(caught.exception.code, 'stale_candidate')
                        self.assertEqual(target.read_bytes(), new_bytes)
                        self.assertEqual(file_hashes(fixture.root, include_staging=False), before_formal)
                        recovered = ReviewStore(fixture.root)
                        self.assertEqual(recovered.snapshot()['counts']['pending'], 1)
                        self.assertEqual(read_rows(fixture.manifest)[0]['id'], row['id'])
                        self.assertFalse(recovered.journal_path.exists())
                    finally:
                        fixture.close()

    def test_external_formal_file_created_after_prepare_is_preserved(self):
        target = self.root / f'SolidGeometry/image/{self.next_id}.png'
        def edit(stage):
            if stage == 'prepared':
                target.write_bytes(b'new unique user content')
        self.store.failpoint = edit
        with self.assertRaises(ReviewError):
            self.mutate()
        self.assertEqual(target.read_bytes(), b'new unique user content')
        self.assertEqual(catalog.catalog(self.root), self.initial)
        self.assertEqual(self.store.snapshot()['counts']['pending'], 2)

    def test_abrupt_process_exit_after_payload_unlink_recovers_on_startup(self):
        code = """
import json,os,sys,uuid
from store import ReviewStore
store=ReviewStore(sys.argv[1]); row=store.snapshot()['candidates'][0]
def crash(stage):
    if stage.startswith('after_unlink:'):
        os._exit(91)
store.failpoint=crash
getattr(store,sys.argv[2]+'_candidate')(row['id'],row['content_sha256'],uuid.uuid4().hex)
raise RuntimeError('The requested abrupt-exit stage was not reached')
"""
        for action in ('pass', 'delete'):
            with self.subTest(action=action):
                fixture = IsolatedRepository(1)
                try:
                    before = file_hashes(fixture.root)
                    process = subprocess.run([sys.executable, '-B', '-c', code, str(fixture.root), action],
                                             cwd=str(__import__('pathlib').Path(__file__).parent),
                                             capture_output=True, text=True, timeout=90)
                    self.assertEqual(process.returncode, 91, process.stdout + process.stderr)
                    journal = fixture.root / '.runtime/solidgeo-original-review/transaction.json'
                    self.assertTrue(journal.exists())
                    recovered = ReviewStore(fixture.root)
                    self.assertEqual(file_hashes(fixture.root), before)
                    self.assertEqual(recovered.snapshot()['counts']['pending'], 1)
                    self.assertFalse(journal.exists())
                finally:
                    fixture.close()

    def test_recovery_cleans_only_transaction_owned_temporary_files(self):
        row = self.displayed()
        def crash(stage):
            if stage == 'prepared':
                raise SimulatedPowerLoss(stage)
        self.store.failpoint = crash
        with self.assertRaises(SimulatedPowerLoss):
            self.mutate(row=row)
        journal = read_json(self.store.journal_path)
        target = self.root / 'SolidGeometry/dataset.jsonl'
        owned = target.with_name('.' + target.name + '.' + journal['id'] + '.tmp')
        owned.write_bytes(b'partial transaction bytes')
        other = target.with_name('.' + target.name + '.other-user-work.tmp')
        other.write_bytes(b'unrelated unique bytes')
        recovered = ReviewStore(self.root)
        self.assertFalse(owned.exists())
        self.assertEqual(other.read_bytes(), b'unrelated unique bytes')
        self.assertEqual(recovered.snapshot()['counts']['pending'], 2)

    def test_preexisting_approval_temporary_file_is_not_overwritten(self):
        temporary = self.root / 'provenance/approvals.json.tmp'
        temporary.write_bytes(b'preexisting unique user work')
        before = file_hashes(self.root)
        with self.assertRaises(ReviewError):
            self.mutate()
        self.assertEqual(file_hashes(self.root), before)
        self.assertEqual(temporary.read_bytes(), b'preexisting unique user work')

    def test_shared_helper_preimage_guards_preserve_external_edits(self):
        for relative in ('provenance/approvals.json', 'provenance/approvals.json.tmp', 'question_bank.jsonl'):
            with self.subTest(relative=relative):
                fixture = IsolatedRepository(1)
                try:
                    store = ReviewStore(fixture.root)
                    row = store.snapshot()['candidates'][0]
                    initial_catalog = catalog.catalog(fixture.root)
                    target = fixture.root / relative
                    original = target.read_bytes() if target.exists() else b''
                    edited = original + b'\n '
                    def edit(stage):
                        if stage == 'files_written':
                            target.write_bytes(edited)
                    store.failpoint = edit
                    with self.assertRaises(ReviewError) as caught:
                        store.pass_candidate(row['id'], row['content_sha256'], uuid.uuid4().hex)
                    self.assertEqual(caught.exception.code, 'stale_candidate')
                    self.assertEqual(target.read_bytes(), edited)
                    self.assertEqual(catalog.catalog(fixture.root), initial_catalog)
                    self.assertEqual(store.snapshot()['counts']['pending'], 1)
                finally:
                    fixture.close()

    def test_catalog_and_approval_internal_failures_roll_back(self):
        for target in ('approve', 'build_locked'):
            with self.subTest(target=target):
                row = self.displayed()
                before = file_hashes(self.root)
                owner = store_module.question_review if target == 'approve' else catalog
                with patch.object(owner, target, side_effect=OSError('injected catalog failure')):
                    with self.assertRaisesRegex(OSError, 'injected catalog failure'):
                        self.mutate(row=row)
                self.assertEqual(file_hashes(self.root), before)
                self.assertFalse(self.store.journal_path.exists())


if __name__ == '__main__':
    unittest.main()
