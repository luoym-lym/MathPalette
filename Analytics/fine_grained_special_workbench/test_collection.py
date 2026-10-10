"""Integration smoke check. All review operations use temporary dataset copies."""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from review_store import Workbench
from replay_archived import render_special_recipe
from renderer_adapter import RendererAdapter, scene_png
from workbench_io import ROOT, atomic_write, load_config, pixel_hash, WorkbenchError


def main():
    with tempfile.TemporaryDirectory(prefix="mathpalette-four-c-") as directory:
        parent = Path(directory)
        data = parent / "fine_grained_dataset"
        board = parent / "fine_grained_special_workbench"
        original = ROOT.parent / "fine_grained_dataset"
        data.mkdir()
        shutil.copy2(original / "dataset.jsonl", data / "dataset.jsonl")
        shutil.copytree(original / "image", data / "image")
        shutil.copytree(original / "dataset_generator", data / "dataset_generator")
        board.mkdir()
        for source in ROOT.iterdir():
            if source.is_file() and source.suffix in (".py", ".json"):
                shutil.copy2(source, board / source.name)
        config = load_config(board / "config.json")
        workbench = Workbench(config)
        try:
            count = len(workbench.adapter.records)
            assert count >= 4
            assert [q["id"] for q in workbench.snapshot()["questions"]] == [f"Ana{i:02d}" for i in range(1, count + 1)]
            for i in range(1, 5):
                scene = workbench.drawing_scene(f"Ana{i:02d}")
                assert (scene["width"], scene["height"]) == (768, 768)
                assert scene["targets"]
                assert scene["presets"]["point"]["color"] == "#DC2626"
            scene = workbench.drawing_scene("Ana01")
            plugin = {"plugin_schema_version": "1.0.0", "question_id": "Ana01",
                      "category": "C", "operation": "C_manual", "description": "test only", "intent": "",
                      "params": {"actions": [
                          {**scene["presets"]["point"], "id": "test_point", "xy": [2, 3]},
                          {**scene["presets"]["line"], "id": "test_line", "endpoints": [[0, 0], [2, 3]]},
                          {"type": "set_curve_style", "target": scene["targets"][0]["id"],
                           "color": "#DC2626", "linestyle": "dashed"}]}}
            preview = workbench.drawing_preview(plugin, workbench.context_token())
            assert not list((data / "special_variant").glob("Ana*/recipes.json"))
            result = workbench.drawing_submit(plugin, workbench.context_token(), None,
                                             preview["pixel_sha256"], preview["parameter_key"])
            candidate = result["candidate"]
            workbench.review("Ana01", candidate["candidate_id"], "pass", workbench.context_token(),
                             preview["pixel_sha256"], preview["parameter_key"], "isolated integration test")
            assert workbench.snapshot()["accepted_total"] == 1
            recipe = workbench.snapshot()["accepted"][0]
            replay = render_special_recipe(recipe, config_path=board / "config.json")
            assert replay["matches_accepted"]
            assert pixel_hash(replay["image_path"]) == preview["pixel_sha256"]
            output = data / "special_variant" / "Ana01"
            assert (output / "plugins" / "C01.json").is_file()
            assert recipe["image_path"] == "special_variant/Ana01/images/C01.png"
            assert len((data / "special_variant" / "accepted_index.jsonl").read_text().splitlines()) == 1
            redraw = subprocess.run([sys.executable, "-B", str(output / "draw_variants.py"), "C01"],
                                    cwd=parent, capture_output=True, text=True)
            assert redraw.returncode == 0, redraw.stderr
            saved_recipes = (output / "recipes.json").read_bytes()
            before_pixels = (output / "images" / "C01.png").read_bytes()
            workbench.collect("Ana01", workbench.context_token())
            assert "Ana01" not in [q["id"] for q in workbench.snapshot()["questions"]]
            assert workbench.snapshot()["question_id"] == "Ana02"
            assert (output / "collection.json").is_file()
            try:
                workbench.navigate("Ana01")
                raise AssertionError("Collected questions must not be editable")
            except WorkbenchError as error:
                assert error.code == "question_collected"
            assert workbench.collect("Ana01", "duplicate retry")["collected_total"] == 1
            workbench.navigate("Ana05")
            old_revision = workbench.snapshot()["input_revision"]
            pending_plugin = {**plugin, "question_id": "Ana05", "params": {"actions": [
                {**scene["presets"]["point"], "id": "test_point", "xy": [2, 3]}]}}
            pending_preview = workbench.drawing_preview(pending_plugin, workbench.context_token())
            pending = workbench.drawing_submit(pending_plugin, workbench.context_token(), None,
                                               pending_preview["pixel_sha256"], pending_preview["parameter_key"])["candidate"]
        finally:
            workbench.close()

        # Change actual geometry, original PNG and question text of an unfinished seed.
        source = data / "dataset_generator" / "dataset_generator" / "function_plot05.py"
        code = source.read_text(encoding="utf-8")
        assert "self.shift = 2" in code
        source.write_text(code.replace("self.shift = 2", "self.shift = 3"), encoding="utf-8")
        updated_adapter = RendererAdapter(config)
        new_scene = updated_adapter.scene("Ana05")
        try:
            png, _ = scene_png(new_scene)
            atomic_write(data / "image" / "Ana05.png", png)
        finally:
            new_scene.close()
        records = [json.loads(line) for line in (data / "dataset.jsonl").read_text(encoding="utf-8").splitlines()]
        records[4]["question"] = "Updated unfinished question: find g(x)."
        records[4]["answer"] = "(x - 3)^2"
        (data / "dataset.jsonl").write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")
        restarted = Workbench(config)
        try:
            assert restarted.snapshot()["accepted_total"] == 1
            assert restarted.snapshot()["question_id"] == "Ana05"
            assert restarted.snapshot()["input_revision"] != old_revision
            assert restarted.snapshot()["question"] == records[4]["question"]
            assert restarted.snapshot()["candidate"] is None
            assert restarted.status(pending["candidate_id"])["status"] == "stale_input"
            assert "Ana01" not in [q["id"] for q in restarted.snapshot()["questions"]]
            assert (output / "recipes.json").read_bytes() == saved_recipes
            assert (output / "images" / "C01.png").read_bytes() == before_pixels
            historical = render_special_recipe(recipe, config_path=board / "config.json")
            assert historical["matches_accepted"]
            redraw = subprocess.run([sys.executable, "-B", str(output / "draw_variants.py"), "C01"],
                                    cwd=parent, capture_output=True, text=True)
            assert redraw.returncode == 0, redraw.stderr
            # Exercise the last-question path and the all-complete snapshot.
            for question in list(restarted.snapshot()["questions"]):
                qid = question["id"]
                restarted.navigate(qid)
                next_plugin = {**pending_plugin, "question_id": qid}
                preview = restarted.drawing_preview(next_plugin, restarted.context_token())
                candidate = restarted.drawing_submit(next_plugin, restarted.context_token(), None,
                                                      preview["pixel_sha256"], preview["parameter_key"])["candidate"]
                restarted.review(qid, candidate["candidate_id"], "pass", restarted.context_token(),
                                 preview["pixel_sha256"], preview["parameter_key"])
                restarted.collect(qid, restarted.context_token())
            assert restarted.snapshot()["questions"] == []
            assert restarted.snapshot()["question_id"] is None
            assert restarted.snapshot()["status"] == "completed"
            assert restarted.snapshot()["collected_total"] == count
            returned = restarted.reopen(f"Ana{count:02d}", restarted.context_token())
            assert returned["question_id"] == f"Ana{count:02d}"
            assert f"Ana{count:02d}" in [q["id"] for q in returned["questions"]]
            assert returned["collected_total"] == count - 1
            collection = json.loads((data / "special_variant" / f"Ana{count:02d}" / "collection.json").read_text())
            assert collection["status"] == "reopened" and len(collection["history"]) == 1
            recollected = restarted.collect(f"Ana{count:02d}", restarted.context_token())
            assert recollected["question_id"] is None and recollected["collected_total"] == count
            collection = json.loads((data / "special_variant" / f"Ana{count:02d}" / "collection.json").read_text())
            assert collection["status"] == "collected" and len(collection["history"]) == 1
        finally:
            restarted.close()
        complete = Workbench(config)
        try:
            assert complete.snapshot()["question_id"] is None
            assert complete.snapshot()["collected_total"] == count
        finally:
            complete.close()

        # A new seed becomes the sole pending question on the next restart.
        new_id = f"Ana{count + 1:02d}"
        new_source = source.with_name(f"function_plot{count + 1:02d}.py")
        new_source.write_text(source.read_text(encoding="utf-8").replace("Ana05", new_id), encoding="utf-8")
        shutil.copy2(data / "image" / "Ana05.png", data / "image" / f"{new_id}.png")
        records.append({**records[4], "id": new_id, "image": f"image/{new_id}.png"})
        (data / "dataset.jsonl").write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")
        extended = Workbench(config)
        try:
            assert extended.snapshot()["question_id"] == new_id
            assert [q["id"] for q in extended.snapshot()["questions"]] == [new_id]
        finally:
            extended.close()
    print(json.dumps({"questions": count, "scene_export": True, "isolated_pass": True,
                      "offline_redraw": True, "restart": True, "collect": True,
                      "unfinished_update": True, "stale_candidate": True, "all_complete": True,
                      "new_question": True, "formal_c_written": False}))


if __name__ == "__main__":
    main()
