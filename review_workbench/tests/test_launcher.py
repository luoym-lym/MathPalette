"""Source-specific launch selection; no environment installation or network."""
from pathlib import Path
import os
import unittest
from unittest.mock import patch
from review_workbench import launch_workbench as launcher


class LauncherTests(unittest.TestCase):
    def test_mathverse_environment_remains_exact(self):
        self.assertEqual(launcher.matching_sources(launcher.REQUIRED), ['MathVerse'])
        self.assertEqual(launcher.matching_sources({**launcher.REQUIRED, 'matplotlib':'3.10.8'}), [])

    def test_mathvision_environment_is_distinct_and_pinned(self):
        found = {**launcher.MATHVISION_REQUIRED, 'python':'3.12.14'}
        self.assertEqual(launcher.matching_sources(found), ['MathVision'])
        self.assertEqual(launcher.matching_sources({**found, 'freetype':'2.14.3'}), [])
        self.assertEqual(launcher.matching_sources({**found, 'python':'3.13.9'}), [])

    def test_bootstrap_honors_explicit_interpreter(self):
        with patch.dict(os.environ, {'MATHPALETTE_PYTHON': '/explicit/source/python'}):
            self.assertEqual(launcher.candidates(), [Path('/explicit/source/python')])
        root = Path(__file__).resolve().parents[2]
        for name in ('start_review.cmd', 'start_mathverse_review.cmd'):
            command = (root / name).read_text()
            self.assertLess(command.index('if defined MATHPALETTE_PYTHON'), command.index('if exist ".venv'))
            self.assertNotIn('pip install', command)


if __name__ == '__main__':
    unittest.main()
