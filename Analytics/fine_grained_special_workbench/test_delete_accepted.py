"""Deletion/renumbering regression checks; writes only temporary dataset copies.

Use --serve to inspect the same isolated fixture with the real web interface.
"""
import argparse
import copy
import json
import shutil
import tempfile
import threading
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from review_store import Workbench
from replay_archived import render_special_recipe
from server import make_handler
from workbench_io import ROOT, file_hash, load_config, read_json


def fixture(parent):
    data = parent / "fine_grained_dataset"
    board = parent / "fine_grained_special_workbench"
    data.mkdir()
    board.mkdir()
    original = ROOT.parent / "fine_grained_dataset"
    shutil.copy2(original / "dataset.jsonl", data / "dataset.jsonl")
    for name in ("image", "dataset_generator"):
        shutil.copytree(original / name, data / name)
    for source in ROOT.iterdir():
        if source.is_file() and source.suffix in (".py", ".json"):
            shutil.copy2(source, board / source.name)
    config = load_config(board / "config.json")
    bench = Workbench(config)
    for coordinate in (2, 3, 4):
        pass_point(bench, coordinate)
    return config, bench


def pass_point(bench, coordinate):
    scene = bench.drawing_scene("Ana01")
    plugin = {"plugin_schema_version": "1.0.0", "question_id": "Ana01",
              "category": "C", "operation": "C_manual", "description": "isolated deletion test", "intent": "",
              "params": {"actions": [{**scene["presets"]["point"], "id": "point",
                                       "xy": [coordinate, coordinate]}]}}
    preview = bench.drawing_preview(plugin, bench.context_token())
    candidate = bench.drawing_submit(plugin, bench.context_token(), None,
                                    preview["pixel_sha256"], preview["parameter_key"])["candidate"]
    bench.review("Ana01", candidate["candidate_id"], "pass", bench.context_token(),
                 preview["pixel_sha256"], preview["parameter_key"])
    return bench.snapshot()["accepted"][-1]


def payload(recipe, state):
    return {"question_id": recipe["question_id"], "candidate_id": recipe["candidate_id"],
            "slot_id": recipe["slot_id"], "context_token": state["context_token"],
            "pixel_sha256": recipe["pixel_sha256"], "parameter_key": recipe["parameter_key"]}


def request(url, body=None, token=None, expected_status=200):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["X-Review-Token"] = token
    req = Request(url, data=None if body is None else json.dumps(body).encode(), headers=headers)
    try:
        response = urlopen(req, timeout=5)
    except HTTPError as error:
        response = error
    with response:
        assert response.status == expected_status, response.read()
        return json.load(response)


def check(config, bench):
    data = Path(config["dataset_root"])
    output = data / "special_variant" / "Ana01"
    baseline_hashes = {p: file_hash(p) for p in data.rglob("*")
                       if p.is_file() and not p.is_relative_to(data / "special_variant")}
    old = copy.deepcopy(bench.snapshot())
    http = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(bench))
    thread = threading.Thread(target=http.serve_forever, daemon=True)
    thread.start()
    url = f"http://127.0.0.1:{http.server_port}"
    try:
        state = request(url + "/api/state")
        middle = payload(old["accepted"][1], state)
        assert request(url + "/api/delete-accepted", middle, "wrong session", 403)["code"] == "invalid_session"
        assert request(url + "/api/delete-accepted", {**middle, "context_token": "old"},
                       state["review_token"], 409)["code"] == "stale_context"
        assert request(url + "/api/delete-accepted", {**middle, "parameter_key": "wrong"},
                       state["review_token"], 409)["code"] == "stale_variant"
        state = request(url + "/api/delete-accepted", middle, state["review_token"])
        assert [r["slot_id"] for r in state["accepted"]] == ["C01", "C02"]
        assert [r["candidate_id"] for r in state["accepted"]] == [old["accepted"][i]["candidate_id"] for i in (0, 2)]
        assert file_hash(output / "images" / "C02.png") == old["accepted"][2]["png_sha256"]
        assert file_hash(output / "plugins" / "C02.json") == old["accepted"][2]["plugin_sha256"]
        assert not (output / "images" / "C03.png").exists()
        assert not (output / "plugins" / "C03.json").exists()
        assert "draw_C03" not in (output / "draw_variants.py").read_text(encoding="utf-8")
        backup = read_json(next((Path(config["runtime_dir"]) / "deleted_variants").glob("Ana01/*/deletion.json")))
        assert backup["removed_recipe"]["candidate_id"] == middle["candidate_id"]
        assert len(backup["before_recipes"]) == 3
        for recipe in state["accepted"]:
            assert render_special_recipe(recipe, config_path=config["config_path"])["matches_accepted"]
        # Old-page retries must never delete the variant now occupying C02.
        assert request(url + "/api/delete-accepted", middle, state["review_token"])["accepted_total"] == 2
        assert request(url + "/api/delete-accepted", payload(old["accepted"][2], old),
                       state["review_token"], 409)["code"] == "stale_context"
        with urlopen(url + state["accepted"][1]["image_url"]) as response:
            assert response.status == 200
        state = request(url + "/api/collect", {"question_id": "Ana01", "context_token": state["context_token"]}, state["review_token"])
        request(url + "/api/delete-accepted", payload(old["accepted"][0], state), state["review_token"], 409)
        state = request(url + "/api/reopen", {"question_id": "Ana01", "context_token": state["context_token"]}, state["review_token"])
        while state["accepted"]:
            state = request(url + "/api/delete-accepted", payload(state["accepted"][0], state), state["review_token"])
        assert state["accepted_total"] == 0
        assert read_json(output / "recipes.json") == []
        assert not list((output / "images").glob("C*.png"))
        assert not list((output / "plugins").glob("C*.json"))
        assert (data / "special_variant" / "accepted_index.jsonl").read_text() == ""
    finally:
        http.shutdown()
        thread.join(timeout=5)
        http.server_close()
    recipe = pass_point(bench, 5)
    assert recipe["slot_id"] == "C01"
    # Simulate interruption after file renumbering but before metadata is saved.
    original_materialize = bench._materialize
    def interrupted(*args):
        raise OSError("simulated interrupted deletion")
    bench._materialize = interrupted
    try:
        bench.delete_accepted("Ana01", recipe["candidate_id"], recipe["slot_id"], bench.context_token(),
                              recipe["pixel_sha256"], recipe["parameter_key"])
        raise AssertionError("Interruption must leave a recoverable transaction")
    except OSError:
        assert (bench.state_dir / "pending_transaction.json").is_file()
    finally:
        bench._materialize = original_materialize
    bench.close()
    restarted = Workbench(config)
    try:
        assert restarted.snapshot()["accepted_total"] == 0
        assert not (restarted.state_dir / "pending_transaction.json").exists()
        assert read_json(output / "recipes.json") == []
        restored = pass_point(restarted, 6)
        assert restored["slot_id"] == "C01"
        assert render_special_recipe(restored, config_path=config["config_path"])["matches_accepted"]
        assert all(file_hash(p) == digest for p, digest in baseline_hashes.items())
    finally:
        restarted.close()
    print(json.dumps({"http_delete": True, "stale_request_safe": True, "renumber": True,
                      "redraw": True, "delete_all": True, "new_pass": True,
                      "restart_recovery": True, "baseline_unchanged": True, "formal_c_written": False}))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--serve", action="store_true")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="mathpalette-delete-") as directory:
        config, bench = fixture(Path(directory))
        if not args.serve:
            try:
                check(config, bench)
            finally:
                bench.close()
            return
        http = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(bench))
        print(json.dumps({"url": f"http://127.0.0.1:{http.server_port}", "temp_root": directory}), flush=True)
        try:
            http.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            http.server_close()
            bench.close()


if __name__ == "__main__":
    main()
