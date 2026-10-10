"""Exercise approval rejection and workbench recovery using an isolated full copy."""
import copy
import json
from pathlib import Path
import shutil
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
        assert len(expected)==77
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

        config=load_config(root/'Analytics/workbench/config.json')
        bench=Workbench(config)
        try:
            snapshot=bench.snapshot()
            assert snapshot['collected_total']==20
            assert snapshot['accepted_total']==72
            assert snapshot['question_id']=='Ana21'
            scene=bench.drawing_scene('Ana21')
            assert scene['targets'], 'Direct ax.plot geometry must be selectable'
            plugin={'plugin_schema_version':'1.0.0','question_id':'Ana21','category':'C','operation':'C_manual',
                    'description':'isolated test','intent':'','params':{'actions':[
                        {**scene['presets']['point'],'id':'test_point','xy':[1,3]}]}}
            preview=bench.drawing_preview(plugin,bench.context_token())
            candidate=bench.drawing_submit(plugin,bench.context_token(),None,preview['pixel_sha256'],preview['parameter_key'])['candidate']
            bench.review('Ana21',candidate['candidate_id'],'pass',bench.context_token(),preview['pixel_sha256'],preview['parameter_key'],'isolated test only')
            recipe=bench.snapshot()['accepted'][0]
            assert len(next(r for r in catalog.rows(root/'question_bank.jsonl') if r['id']=='Ana21')['special_plugins'])==1
            replay=render_special_recipe(recipe,config_path=root/'Analytics/workbench/config.json')
            assert replay['matches_accepted']
            bench.collect('Ana21',bench.context_token())
            assert bench.snapshot()['collected_total']==21
            bench.reopen('Ana21',bench.context_token())
            bench.navigate('Ana21')
            bench.delete_accepted('Ana21',recipe['candidate_id'],recipe['slot_id'],bench.context_token(),recipe['pixel_sha256'],recipe['parameter_key'])
            assert bench.snapshot()['accepted_total']==72
            assert not next(r for r in catalog.rows(root/'question_bank.jsonl') if r['id']=='Ana21')['special_plugins']
        finally:
            bench.close()
        # A brand new runtime directory must recover durable Pass/Collect records.
        config['runtime_dir']=str(root/'.runtime/new_session')
        bench=Workbench(config)
        try:
            assert bench.snapshot()['collected_total']==20
            assert bench.snapshot()['accepted_total']==72
        finally:
            bench.close()
    print('Approval rejection, Pass/Collect/reopen/delete, index sync, and cold recovery passed.')

if __name__=='__main__':
    main()
