"""Actual standard-library bootstrap and invalid-environment integration checks."""
from __future__ import annotations

import os
import subprocess
import sys
import unittest
from unittest.mock import patch

from launch_workbench import required_environment, select_python
from test_support import IsolatedRepository, file_hashes


class LauncherIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = IsolatedRepository(1)
        self.root = self.fixture.root
        self.launcher = self.root / 'SolidGeometry/original_review/launch_workbench.py'

    def tearDown(self):
        self.fixture.close()

    def test_standard_library_only_start_can_select_pinned_render_python(self):
        before = file_hashes(self.root)
        result = subprocess.run([sys.executable, '-S', '-B', str(self.launcher), '--root', str(self.root), '--check'],
                                env={**os.environ, 'MATHPALETTE_PYTHON': sys.executable},
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('3.13.9', result.stdout)
        self.assertIn('环境检查通过', result.stdout)
        self.assertEqual(file_hashes(self.root), before)
        self.assertFalse((self.root / '.runtime').exists())

    def test_missing_override_is_explicit_and_does_not_change_state(self):
        before = file_hashes(self.root)
        result = subprocess.run([sys.executable, '-S', '-B', str(self.launcher), '--check'],
                                env={**os.environ, 'MATHPALETTE_PYTHON': str(self.root / 'missing-python.exe')},
                                capture_output=True, text=True, timeout=30)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('MATHPALETTE_PYTHON', result.stderr)
        self.assertEqual(file_hashes(self.root), before)
        self.assertFalse((self.root / '.runtime').exists())

    def test_mismatched_versions_fail_without_installing_or_accepting_near_match(self):
        required = required_environment(self.root)
        fake = subprocess.CompletedProcess([], 0, '{"python":"3.13.10","matplotlib":"3.10.0","numpy":"2.2.0","pillow":"11.1.0"}', '')
        with patch('launch_workbench.python_candidates', return_value=[sys.executable]), \
                patch('launch_workbench.subprocess.run', return_value=fake) as command:
            with self.assertRaisesRegex(ValueError, '未找到匹配'):
                select_python(required, self.root)
        self.assertEqual(command.call_count, 1)
        self.assertIn('-c', command.call_args.args[0])
        self.assertNotIn('pip', ' '.join(command.call_args.args[0]))


if __name__ == '__main__':
    unittest.main()
