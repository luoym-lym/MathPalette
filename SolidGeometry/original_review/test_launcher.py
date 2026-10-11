"""Standard-library launcher tests; no service, dependency install or real approval."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock

SPEC = importlib.util.spec_from_file_location('original_review_launcher', Path(__file__).with_name('launch_workbench.py'))
launcher = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(launcher)


class LauncherTests(unittest.TestCase):
    def test_root_pin_versions_and_python_patch_are_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'requirements.txt').write_text('matplotlib==3.11.2\nnumpy==2.5.3\npillow==12.3.0\n')
            expected = launcher.required_environment(root)
            self.assertEqual(expected, {'python': '3.13.9', 'matplotlib': '3.11.2', 'numpy': '2.5.3', 'pillow': '12.3.0'})

    def test_missing_pin_is_a_clear_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'requirements.txt').write_text('matplotlib==3.11.2\n')
            with self.assertRaisesRegex(ValueError, 'requirements.txt'):
                launcher.required_environment(root)

    def test_override_retains_venv_symlink_instead_of_resolving_to_base_python(self):
        if os.name == 'nt':
            self.skipTest('POSIX venv symlink regression; Windows uses the same non-resolving path code.')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            base = root / 'base python'; base.write_text('fixture')
            link = root / 'venv with spaces' / 'bin' / 'python'
            link.parent.mkdir(parents=True); link.symlink_to(base)
            with mock.patch.dict(os.environ, {'MATHPALETTE_PYTHON': str(link)}):
                self.assertEqual(launcher.python_candidates(root), [link.absolute()])
                self.assertNotEqual(launcher.python_candidates(root)[0], base)

    def test_override_missing_file_fails_without_silently_switching(self):
        with mock.patch.dict(os.environ, {'MATHPALETTE_PYTHON': '/this/interpreter/does/not/exist'}):
            with self.assertRaisesRegex(ValueError, 'MATHPALETTE_PYTHON'):
                launcher.python_candidates()

    def test_select_requires_all_exact_versions(self):
        required = {'python': '3.13.9', 'matplotlib': '3.11.2', 'numpy': '2.5.3', 'pillow': '12.3.0'}
        wrong = {**required, 'python': '3.13.8'}
        results = [subprocess.CompletedProcess([], 0, json.dumps(wrong), ''), subprocess.CompletedProcess([], 0, json.dumps(required), '')]
        with mock.patch.object(launcher, 'python_candidates', return_value=[Path('/wrong'), Path('/correct env/python')]), mock.patch.object(launcher.subprocess, 'run', side_effect=results) as run:
            path, actual = launcher.select_python(required)
            self.assertEqual(path, Path('/correct env/python'))
            self.assertEqual(actual, required)
            self.assertEqual(run.call_args.args[0][0], '/correct env/python')

    def test_no_environment_is_actionable_and_never_installs(self):
        with mock.patch.object(launcher, 'python_candidates', return_value=[]), mock.patch.object(launcher.subprocess, 'run') as run:
            with self.assertRaisesRegex(ValueError, '不会自动下载'):
                launcher.select_python({'python': '3.13.9'})
            run.assert_not_called()

    def test_check_does_not_start_server(self):
        with mock.patch.object(launcher, 'required_environment', return_value={}), mock.patch.object(launcher, 'select_python', return_value=(Path('/fixture/python'), {})), mock.patch.object(launcher.subprocess, 'call') as call:
            self.assertEqual(launcher.main(['--check']), 0)
            call.assert_not_called()

    def test_server_paths_are_separate_arguments_and_browser_optional(self):
        with tempfile.TemporaryDirectory(prefix='review space ') as tmp:
            root = Path(tmp)
            with mock.patch.object(launcher, 'required_environment', return_value={}), mock.patch.object(launcher, 'select_python', return_value=(Path('/python with spaces/python'), {})), mock.patch.object(launcher.subprocess, 'call', return_value=0) as call:
                self.assertEqual(launcher.main(['--root', str(root), '--port', '8771', '--no-browser']), 0)
                args = call.call_args.args[0]
                self.assertEqual(args[0], '/python with spaces/python')
                self.assertEqual(args[args.index('--root') + 1], str(root.resolve()))
                self.assertNotIn('--open-browser', args)


if __name__ == '__main__':
    unittest.main()
