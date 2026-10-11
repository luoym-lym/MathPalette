"""Exercise approval rejection and workbench recovery using an isolated full copy."""
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(ROOT/'Analytics/workbench'))
from dataset_tools import catalog
from review_store import Workbench
from workbench_io import load_config
from replay_archived import render_special_recipe

def main():
    with tempfile.TemporaryDirectory(prefix='mathpalette-integrity-') as directory:
        root=Path(directory)/'dataset'
        shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','.env','.runtime','__pycache__','*.pyc','*.lock'))
        expected=catalog.catalog(root)
        expected_ids = {row['id'] for branch in catalog.BRANCHES
                        for row in catalog.rows(root/branch/'dataset.jsonl')}
        assert {row['id'] for row in expected} == expected_ids
        assert len(expected) == len(expected_ids)
        analytics_ids = {row['id'] for row in expected if row['branch'] == 'Analytics'}
        initially_collected = {path.parent.name for path in (root/'Analytics/special_variant').glob('*/collection.json')
                               if catalog.read(path).get('status') == 'collected'}
        initial_collected_total = len(initially_collected)
        assert initially_collected <= analytics_ids
        target_qid = next(row['id'] for row in expected
                          if row['branch'] == 'Analytics' and row['id'] not in initially_collected)
        initial_special_total=sum(len(row['special_plugins']) for row in expected if row['branch']=='Analytics')
        initial_target_special=len(next(row for row in expected if row['id']==target_qid)['special_plugins'])
        path=root/'Analytics/dataset.jsonl'
        before=path.read_bytes()
        rows=catalog.rows(path)
        rows[0]['answer']='test-only changed answer'
        path.write_text(''.join(json.dumps(r)+'\n' for r in rows),encoding='utf-8')
        try:
            catalog.assert_formal_dataset(path)
            raise AssertionError('Changed answer must invalidate original approval')
        except ValueError as error:
            assert 'approval' in str(error)
        path.write_bytes(before)

        # A desktop launcher must work even when its initial interpreter cannot
        # import third-party packages. It selects a verified environment first.
        launcher=root/'Analytics/workbench/launch_workbench.py'
        environment={**os.environ,'MATHPALETTE_PYTHON':sys.executable}
        result=subprocess.run([sys.executable,'-S','-X','utf8','-B',str(launcher),'--check'],
                              cwd=launcher.parent,env=environment,capture_output=True,
                              text=True,encoding='utf-8',timeout=60)
        assert result.returncode==0, result.stdout+result.stderr
        assert 'MathPalette Python:' in result.stdout
        check=json.loads(result.stdout[result.stdout.rfind('\n{')+1:])
        assert check['noop_pixels_match'] and check['questions_checked']==len(analytics_ids - initially_collected)
        assert check['collected_questions']==initial_collected_total and check['accepted_count']==initial_special_total
        progress=root/'.runtime/analytics_special/state/progress.json'
        saved=progress.read_bytes()
        environment['MATHPALETTE_PYTHON']=str(root/'missing-python.exe')
        result=subprocess.run([sys.executable,'-S','-X','utf8','-B',str(launcher),'--check'],
                              cwd=launcher.parent,env=environment,capture_output=True,
                              text=True,encoding='utf-8',timeout=30)
        assert result.returncode!=0 and 'MATHPALETTE_PYTHON' in result.stderr
        assert progress.read_bytes()==saved, 'An unavailable environment must not change review state'

        config=load_config(root/'Analytics/workbench/config.json')
        bench=Workbench(config)
        try:
            snapshot=bench.snapshot()
            assert snapshot['collected_total']==initial_collected_total
            assert snapshot['accepted_total']==initial_special_total
            assert snapshot['question_id']==target_qid
            scene=bench.drawing_scene(target_qid)
            assert scene['targets'], 'Direct ax.plot geometry must be selectable'
            plugin={'plugin_schema_version':'1.0.0','question_id':target_qid,'category':'C','operation':'C_manual',
                    'description':'isolated test','intent':'','params':{'actions':[
                        {**scene['presets']['point'],'id':'test_point','xy':[1,3]}]}}
            preview=bench.drawing_preview(plugin,bench.context_token())
            candidate=bench.drawing_submit(plugin,bench.context_token(),None,preview['pixel_sha256'],preview['parameter_key'])['candidate']
            bench.review(target_qid,candidate['candidate_id'],'pass',bench.context_token(),preview['pixel_sha256'],preview['parameter_key'],'isolated test only')
            recipe=bench.snapshot()['accepted'][-1]
            assert len(next(r for r in catalog.rows(root/'question_bank.jsonl') if r['id']==target_qid)['special_plugins'])==initial_target_special+1
            replay=render_special_recipe(recipe,config_path=root/'Analytics/workbench/config.json')
            assert replay['matches_accepted']
            bench.collect(target_qid,bench.context_token())
            assert bench.snapshot()['collected_total']==initial_collected_total+1
            bench.reopen(target_qid,bench.context_token())
            bench.navigate(target_qid)
            bench.delete_accepted(target_qid,recipe['candidate_id'],recipe['slot_id'],bench.context_token(),recipe['pixel_sha256'],recipe['parameter_key'])
            assert bench.snapshot()['accepted_total']==initial_special_total
            assert len(next(r for r in catalog.rows(root/'question_bank.jsonl') if r['id']==target_qid)['special_plugins'])==initial_target_special
        finally:
            bench.close()
        # A brand new runtime directory must recover durable Pass/Collect records.
        config['runtime_dir']=str(root/'.runtime/new_session')
        bench=Workbench(config)
        try:
            assert bench.snapshot()['collected_total']==initial_collected_total
            assert bench.snapshot()['accepted_total']==initial_special_total
        finally:
            bench.close()
    print('Launcher environment checks, approval rejection, Pass/Collect/reopen/delete, index sync, and cold recovery passed.')

if __name__=='__main__':
    main()
