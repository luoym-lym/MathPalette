"""Offline checks that relocation preserves inputs and completed trace trials."""
import copy
import json
import tempfile
import unittest
from pathlib import Path

from evaluate import DATASET_ROOT, DEFAULT_ENV_FILE, Trace, digest, load_dataset, relocated_trace_config
from evaluate_special import load_special
from evaluate_variants import load_variants


def signature(config):
    return digest(json.dumps(config, ensure_ascii=False, sort_keys=True, allow_nan=False).encode("utf-8"))


class RelocationTests(unittest.TestCase):
    def test_default_paths_and_all_dataset_loaders(self):
        self.assertEqual(DEFAULT_ENV_FILE.parent, DATASET_ROOT.parent.parent)
        path = DATASET_ROOT / "dataset.jsonl"
        originals, _, _ = load_dataset(path)
        variants, _, _, _ = load_variants(path)
        special, _, _, _ = load_special(path)
        self.assertEqual(len(variants), 4 * len(originals))
        self.assertGreater(len(special), 0)

    def test_only_path_change_can_resume(self):
        old = {"dataset": str(DATASET_ROOT.parent.parent / "fine_grained_dataset/dataset.jsonl"),
               "dataset_sha256": "same-data", "images_sha256": {"Ana01": "same-image"},
               "model": "same-model", "trials_per_question": 1}
        current = {**old, "dataset": str(DATASET_ROOT / "dataset.jsonl")}
        self.assertTrue(relocated_trace_config(old, current, signature(old)))
        for field, value in (("dataset_sha256", "changed-data"), ("images_sha256", {"Ana01": "changed-image"}),
                             ("model", "changed-model"), ("trials_per_question", 2)):
            self.assertFalse(relocated_trace_config(old, {**current, field: value}, signature(old)))
        self.assertFalse(relocated_trace_config(old, current, "invalid-signature"))
        self.assertFalse(relocated_trace_config({**old, "dataset": "unrelated.jsonl"}, current, signature(old)))
        row = {"id": "Ana01", "question": "unchanged", "answer": 1, "image": "image/Ana01.png", "image_sha256": "same-image"}
        with tempfile.TemporaryDirectory(prefix="mathpalette-trace-relocation-") as directory:
            path = Path(directory) / "trace.json"
            trace = Trace(path, signature(old), old, [row])
            trace.update_trial(0, 0, status="completed", correct=True)
            completed = copy.deepcopy(trace.data["questions"])
            moved = Trace(path, signature(current), current, [row])
            self.assertEqual(moved.data["questions"], completed)
            self.assertEqual(moved.data["summary"]["mean_accuracy"], 1)
            self.assertEqual(len(moved.data["path_migrations"]), 1)
            with self.assertRaisesRegex(ValueError, "different data or evaluation settings"):
                Trace(path, signature({**current, "model": "changed"}), {**current, "model": "changed"}, [row])


if __name__ == "__main__":
    unittest.main(verbosity=2)
