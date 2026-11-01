"""Small, question-scoped input checks for interactive workbench operations."""
from pathlib import Path


def assert_question_inputs(adapter, qid, error_type, file_hash):
    if qid not in adapter.records:
        raise error_type('不存在此题号。', 404)
    if hasattr(adapter, 'dependencies'):
        dependencies = adapter.dependencies(qid)
    elif hasattr(adapter, 'question_dependencies'):
        dependencies = adapter.question_dependencies(qid)
    else:
        source = Path(adapter.sources[qid]['source_file']).name
        dependencies = ('common_renderer.py', 'protocol.json', f'image/{qid}.png',
                        f'question_classes/{source}')
    # The small dataset file also binds the displayed question and answer. There
    # is no need to read every other question's images, scenes and renderers.
    for name in ('dataset.jsonl', *dependencies):
        try:
            unchanged = file_hash(adapter.input_files[name]) == adapter.manifest['files'][name]
        except OSError:
            unchanged = False
        if not unchanged:
            raise error_type('本题输入在运行期间改变，请重启工作台。', 409, 'baseline_changed')
