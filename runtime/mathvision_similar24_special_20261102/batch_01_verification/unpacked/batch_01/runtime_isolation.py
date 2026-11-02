"""Runtime-only temp routing and Python filesystem write guard.

The checked-in MathVision bridge hardcodes .runtime for temporary scene copies.
Only that path is replaced in the loaded function; drawing code stays identical.
No file in the library is edited. Call after selecting runtime cache env vars.
"""
from pathlib import Path
import inspect
import os
import sys

PROJECT = next(parent for parent in Path(__file__).resolve().parents
               if (parent / 'MATHPALETTE_PROTOCOL.md').is_file())
RUNTIME = (PROJECT / 'runtime').resolve()

def install(temporary_directory, guard_writes=True):
    target = Path(temporary_directory).resolve()
    if not target.is_relative_to(RUNTIME):
        raise ValueError('Temporary root must be below runtime/')
    target.mkdir(parents=True, exist_ok=True)
    if str(PROJECT) not in sys.path:
        sys.path.insert(0, str(PROJECT))
    import dataset_tools.mathvision_workbench as bridge
    if not getattr(bridge, '_task_runtime_redirected', False):
        source = inspect.getsource(bridge.build_scene)
        old = "temporary_root = branch_root.parent / '.runtime/mathvision_workbench'"
        if source.count(old) != 1:
            raise RuntimeError('Unknown MathVision temporary path implementation; stop')
        source = source.replace(old, 'temporary_root = Path(' + repr(str(target)) + ')')
        exec(compile(source, str(Path(__file__).resolve()), 'exec'), bridge.__dict__)
        bridge._task_runtime_redirected = True
        bridge._task_runtime_directory = str(target)
    if guard_writes and not getattr(bridge, '_task_runtime_write_guard', False):
        def check(path):
            if isinstance(path, int) or path is None:
                return
            resolved = Path(os.fsdecode(path)).resolve()
            if not resolved.is_relative_to(RUNTIME):
                raise PermissionError('Task write outside root runtime/ blocked: ' + str(resolved))

        def guard(event, args):
            if event == 'open':
                path, mode, flags = args
                if flags & (os.O_WRONLY | os.O_RDWR | os.O_APPEND | os.O_CREAT | os.O_TRUNC):
                    check(path)
            elif event in ('os.mkdir','os.remove','os.rmdir','os.unlink','os.chmod','os.utime','os.truncate'):
                check(args[0])
            elif event in ('os.rename','os.replace','os.link','os.symlink'):
                check(args[0]); check(args[1])
        sys.addaudithook(guard)
        bridge._task_runtime_write_guard = True
    return {'temporary_root': bridge._task_runtime_directory, 'write_guard':guard_writes,
            'library_files_modified':False,'drawing_operations_modified':False}
