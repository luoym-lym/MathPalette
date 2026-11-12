"""Tests for the current shared drawing protocol; v1 tests are archived."""
from pathlib import Path
import sys,unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from dataset_tools.test_drawing import DrawingTests
if __name__=='__main__':unittest.main()
