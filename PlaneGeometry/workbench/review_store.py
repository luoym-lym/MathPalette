"""One writer, immutable candidates and recoverable human review transactions."""
from __future__ import annotations

import copy
import base64
import hashlib
import json
import os
import secrets
import threading
import uuid
from pathlib import Path

from render_plugins import PluginRenderer
from renderer_adapter import RENDER_LOCK, RendererAdapter
from workbench_io import (GENERATOR_VERSION, ROOT, SCHEMA_VERSION, WorkbenchError, atomic_json,
                          atomic_write, canonical_hash, contained_path, environment_versions,
                          file_hash, json_bytes, pixel_hash, protect_output_paths, read_json,
                          renderer_fingerprint, progress_renderer_matches, timestamp)


class StoreLock:
    """OS releases the process lock on crash, including on Windows."""
    def __init__(self, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.handle = path.open("a+b")
        try:
            if os.fstat(self.handle.fileno()).st_size == 0:
                self.handle.write(b"0")
                self.handle.flush()
            self.handle.seek(0)
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(self.handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            self.handle.close()
            raise WorkbenchError("此 C 状态目录已有运行中的服务。", 409, "writer_locked") from error

    def close(self):
        self.handle.close()


def drawing_functions(recipes):
    text = '''"""Offline redraw of frozen, human-reviewed C variants only."""
import json
import sys
from pathlib import Path

_WORKBENCH = Path(__file__).resolve().parents[2] / "workbench"
if not (_WORKBENCH / "render_plugins.py").is_file():
    raise RuntimeError("Keep PlaneGeometry/special_variant and PlaneGeometry/workbench together.")
if str(_WORKBENCH) not in sys.path:
    sys.path.insert(0, str(_WORKBENCH))
from replay_archived import render_special_recipe

def _draw(slot_id, output_path=None):
    recipes = json.loads(Path(__file__).with_name("recipes.json").read_text(encoding="utf-8"))
    recipe = next(r for r in recipes if r["slot_id"] == slot_id)
    return render_special_recipe(recipe, output_path)

'''
    for recipe in recipes:
        slot = recipe["slot_id"]
        text += f'def draw_{slot}(output_path=None):\n    return _draw("{slot}", output_path)\n\n'
    text += ("if __name__ == '__main__':\n"
             "    import argparse\n"
             "    parser = argparse.ArgumentParser(description='确定性重绘人工通过 C 图')\n"
             f"    parser.add_argument('slot_id', choices={[r['slot_id'] for r in recipes]!r})\n"
             "    parser.add_argument('--output', type=Path)\n"
             "    args = parser.parse_args()\n"
             "    print(json.dumps(_draw(args.slot_id, args.output), ensure_ascii=False))\n")
    return text


class Workbench:
    def __init__(self, config, announce=None):
        self.config = copy.deepcopy(config)
        protect_output_paths(self.config)
        self.root = Path(config["runtime_dir"])
        self.output = Path(config["output_dir"])
        self.dataset_root = Path(config["dataset_root"])
        if not self.output.is_relative_to(self.dataset_root) or self.output == self.dataset_root:
            raise WorkbenchError("output_dir 必须位于 dataset_root 内的独立 C 子目录。")
        self.output_relative = self.output.relative_to(self.dataset_root)
        self.state_dir = self.root / "state"
        self.lock, self.submit_lock = threading.RLock(), threading.Lock()
        self.job, self.errors = None, {}
        self.session_id, self.review_token = uuid.uuid4().hex, secrets.token_urlsafe(32)
        self.writer = StoreLock(self.state_dir / "workbench.lock")
        try:
            self._initialize(announce or (lambda message: None))
        except Exception:
            self.writer.close()
            raise

    def _initialize(self, announce):
        manifest_path = self.state_dir / "baseline_manifest.json"
        expected = read_json(manifest_path) if manifest_path.exists() else None
        self.adapter = RendererAdapter(self.config)
        self.environment = environment_versions()
        self.signature = {"generator_version": GENERATOR_VERSION, "plugin_schema_version": SCHEMA_VERSION,
                          "environment": self.environment,
                          "baseline_fingerprint": self.adapter.manifest["fingerprint"],
                          "schema_sha256": file_hash(ROOT / "plugin.schema.json"),
                          "renderer_sha256": renderer_fingerprint()}
        # Unreviewed initialization writes only runtime state. A Pass transaction
        # copies its exact input manifest into the durable branch output.
        for manifest in (expected, self.adapter.manifest):
            if manifest:
                atomic_json(contained_path(self.state_dir, f"baselines/{manifest['fingerprint']}.json"), manifest)
        progress_path = self.state_dir / "progress.json"
        if progress_path.exists():
            self.progress = read_json(progress_path)
            previous_signature = self.progress["signature"]
            snapshot = self.state_dir / "dataset_snapshot.json"
            old_records = read_json(snapshot) if snapshot.is_file() else None
            compatible_renderer = progress_renderer_matches(
                previous_signature, self.signature, self.adapter, expected, old_records)
            if any(previous_signature.get(key) != value and
                   not (key == "renderer_sha256" and compatible_renderer) for key, value in self.signature.items()
                   if key != "baseline_fingerprint"):
                raise WorkbenchError("渲染器、schema 或依赖版本不一致；请恢复原版本。", 409, "version_mismatch")
            if self.progress["output_relative"] != self.output_relative.as_posix():
                raise WorkbenchError("正式输出目录结构与已有状态不一致。", 409, "output_changed")
        else:
            self.progress = {"signature": self.signature, "output_relative": self.output_relative.as_posix(),
                             "current_question": "Plane01", "navigation_revision": 0,
                             "questions": {qid: {"revision": 0, "candidate_id": None, "accepted": [], "last_review": None}
                                           for qid in self.adapter.records}, "candidates": {}}
            # Runtime caches are disposable. Passed recipes and collection records
            # are the durable source of truth; never reset an existing collection.
            for qid, question in self.progress["questions"].items():
                recipes_path = self.output / qid / "recipes.json"
                if recipes_path.is_file():
                    question["accepted"] = read_json(recipes_path)
                collection_path = self.output / qid / "collection.json"
                if collection_path.is_file():
                    collection = read_json(collection_path)
                    question["collected"] = collection["status"] == "collected"
                    question["collection_record"] = collection.get("current", collection)
                    question["collection_history"] = collection.get("history", [])
        # Finish an interrupted save against its original session signature first.
        current_signature = self.signature
        self.signature = self.progress["signature"]
        self._recover()
        self.signature = current_signature
        inputs_changed = self.progress["signature"].get("baseline_fingerprint") != self.signature["baseline_fingerprint"]
        for qid in self.adapter.records:
            self.progress["questions"].setdefault(qid, {
                "revision": 0, "candidate_id": None, "accepted": [], "last_review": None})
        for question in self.progress["questions"].values():
            question.setdefault("collected", False)
            if question.get("collected"):
                question.setdefault("collected_at", question["collection_record"]["collected_at"])
            if inputs_changed and question["candidate_id"]:
                candidate = self.progress["candidates"][question["candidate_id"]]
                candidate["status"] = "stale_input"
                question["candidate_id"] = None
                question["revision"] += 1
        self.progress["signature"] = copy.deepcopy(self.signature)
        active = self.active_questions()
        if self.progress["current_question"] not in active:
            self.progress["current_question"] = active[0] if active else None
            self.progress["navigation_revision"] += 1
        metadata_path = self.state_dir / "scene_metadata.json"
        cache = read_json(metadata_path) if metadata_path.exists() else {}
        if cache.get("signature") == self.signature and all(qid in cache.get("questions", {}) for qid in active):
            self.metadata = cache["questions"]
        else:
            self.metadata = {}
            failures = []
            for index, qid in enumerate(active, 1):
                announce(f"无操作重绘校验 {qid} ({index}/{len(active)})")
                try:
                    self.metadata[qid] = self.adapter.inspect_question(qid)
                except WorkbenchError as error:
                    failures.append(str(error))
            if failures:
                raise WorkbenchError("原图校验失败：\n" + "\n".join(failures), 409, "baseline_mismatch")
            atomic_json(metadata_path, {"signature": self.signature, "questions": self.metadata})
        self.renderer = PluginRenderer(self.config, self.adapter, self.metadata)
        for name in ("candidates", "drafts", "reproduced"):
            (self.root / name).mkdir(parents=True, exist_ok=True)
        # Keep old manifests so stored recipes can still replay after other questions change.
        for manifest in (expected, self.adapter.manifest):
            if manifest:
                atomic_json(contained_path(self.state_dir, f"baselines/{manifest['fingerprint']}.json"), manifest)
        self._validate_saved_files()
        atomic_json(manifest_path, self.adapter.manifest)
        atomic_json(self.state_dir / "dataset_snapshot.json", self.adapter.records)
        atomic_json(progress_path, self.progress)

    def active_questions(self):
        return [qid for qid in self.adapter.records
                if not self.progress["questions"][qid].get("collected", False)]

    def _check_open_question(self, qid):
        if qid not in self.adapter.records:
            raise WorkbenchError("不存在此题号。", 404)
        if self.progress["questions"][qid].get("collected", False):
            raise WorkbenchError("此题已 Collect 并存档，请选择未完成的题目。", 409, "question_collected")

    def close(self):
        self.writer.close()

    def context_token(self):
        qid = self.progress["current_question"]
        if qid is None:
            return canonical_hash({"session": self.session_id, "question_id": None})
        question = self.progress["questions"][qid]
        return canonical_hash({"session": self.session_id, "question_id": qid,
                               "navigation_revision": self.progress["navigation_revision"],
                               "revision": question["revision"], "candidate_id": question["candidate_id"]})

    def _check_context(self, qid, token, replace=None):
        self._check_open_question(qid)
        if qid != self.progress["current_question"] or token != self.context_token():
            raise WorkbenchError("提交上下文已过期：工作台已切题、审核或收到新候选；重新读取 context。", 409, "stale_context")
        current = self.progress["questions"][qid]["candidate_id"]
        if current and replace != current:
            raise WorkbenchError(f"存在待审候选 {current}；用户要求修改时需 --replace {current}。", 409, "pending_candidate")
        if replace and current != replace:
            raise WorkbenchError("--replace 指定候选已不是当前待审图。", 409, "stale_candidate")

    def _package_file(self, candidate, name):
        package = contained_path(self.root / "candidates", candidate["candidate_id"])
        return contained_path(package, name)

    def _verify_package(self, candidate, require_image=True):
        manifest = read_json(self._package_file(candidate, "manifest.json"))
        keys = ("candidate_id", "question_id", "pixel_sha256", "png_sha256", "parameter_key",
                "plugin_sha256", "baseline_fingerprint", "generator_version", "environment", "context_token")
        if any(manifest.get(k) != candidate.get(k) for k in keys):
            raise WorkbenchError("候选清单与发布记录不符。", 409, "integrity_error")
        plugin_path = self._package_file(candidate, "plugin.json")
        plugin = read_json(plugin_path)
        if file_hash(plugin_path) != candidate["plugin_sha256"] or canonical_hash(plugin) != candidate["parameter_key"]:
            raise WorkbenchError("候选插件快照被改写。", 409, "integrity_error")
        if require_image:
            path = self._package_file(candidate, "image.png")
            if not path.is_file() or file_hash(path) != candidate["png_sha256"] or pixel_hash(path) != candidate["pixel_sha256"]:
                raise WorkbenchError("候选 PNG 丢失或被改写；无法审核。", 409, "integrity_error")
        return plugin

    def _validate_saved_files(self):
        all_recipes = []
        collected_records = []
        for qid, question in self.progress["questions"].items():
            if question.get("collected"):
                record = question["collection_record"]
                path = contained_path(self.output, f"{qid}/collection.json")
                expected_collection = {"question_id": qid, "status": "collected", "current": record,
                                       "history": question.get("collection_history", [])}
                if not path.is_file():
                    raise WorkbenchError(f"{qid} 完成收集记录与状态不一致。", 409, "integrity_error")
                stored_collection = read_json(path)
                # Older workbench versions stored the collection record directly.
                # Upgrade that representation in place while preserving the record.
                if stored_collection == record:
                    atomic_json(path, expected_collection)
                elif stored_collection != expected_collection:
                    raise WorkbenchError(f"{qid} 完成收集记录与状态不一致。", 409, "integrity_error")
                collected_records.append(record)
            elif question.get("collection_record"):
                path = contained_path(self.output, f"{qid}/collection.json")
                expected_collection = {"question_id": qid, "status": "reopened",
                                       "current": question["collection_record"],
                                       "history": question.get("collection_history", [])}
                if not path.is_file() or read_json(path) != expected_collection:
                    raise WorkbenchError(f"{qid} 重新打开记录与状态不一致。", 409, "integrity_error")
            recipes = question["accepted"]
            if [r["slot_id"] for r in recipes] != [f"C{i:02d}" for i in range(1, len(recipes) + 1)]:
                raise WorkbenchError(f"{qid} 正式槽位记录无效。", 409)
            for recipe in recipes:
                image, plugin = self._accepted_path(recipe["image_path"]), self._accepted_path(recipe["plugin_path"])
                if (not image.is_file() or file_hash(image) != recipe["png_sha256"] or
                        pixel_hash(image) != recipe["pixel_sha256"] or
                        not plugin.is_file() or file_hash(plugin) != recipe["plugin_sha256"] or
                        canonical_hash(read_json(plugin)) != recipe["parameter_key"]):
                    raise WorkbenchError(f"{qid}/{recipe['slot_id']} 正式图或参数丢失/损坏；请恢复备份。", 409, "integrity_error")
            if recipes or contained_path(self.output, f"{qid}/recipes.json").exists():
                if read_json(contained_path(self.output, f"{qid}/recipes.json")) != recipes:
                    raise WorkbenchError(f"{qid}/recipes.json 与审核状态不一致。", 409, "integrity_error")
                function_path = contained_path(self.output, f"{qid}/draw_variants.py")
                actual, wanted = function_path.read_text(encoding="utf-8"), drawing_functions(recipes)
                legacy = wanted.replace("from replay_archived import render_special_recipe", "from render_plugins import render_special_recipe")
                if actual == legacy:
                    atomic_write(function_path, wanted)
                elif actual != wanted:
                    raise WorkbenchError(f"{qid}/draw_variants.py 与审核状态不一致。", 409, "integrity_error")
            all_recipes.extend(recipes)
            if question["candidate_id"]:
                self._verify_package(self.progress["candidates"][question["candidate_id"]])
        index_path = self.output / "accepted_index.jsonl"
        if all_recipes or index_path.exists():
            expected = "".join(json.dumps(r, ensure_ascii=False, allow_nan=False) + "\n" for r in all_recipes)
            if not index_path.is_file() or index_path.read_text(encoding="utf-8") != expected:
                raise WorkbenchError("accepted_index.jsonl 与审核状态不一致。", 409, "integrity_error")
        if collected_records:
            path = self.output / "collected_index.jsonl"
            expected = "".join(json.dumps(record, ensure_ascii=False, allow_nan=False) + "\n" for record in collected_records)
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                raise WorkbenchError("collected_index.jsonl 与完成状态不一致。", 409, "integrity_error")

    def _accepted_path(self, relative):
        path = contained_path(self.dataset_root, relative)
        if not path.is_relative_to(self.output):
            raise WorkbenchError("正式 C 路径不在 output_dir 内。", code="unsafe_path")
        return path

    def _materialize(self, progress, qid):
        recipes = progress["questions"][qid]["accepted"]
        atomic_json(contained_path(self.output, f"{qid}/recipes.json"), recipes)
        atomic_write(contained_path(self.output, f"{qid}/draw_variants.py"), drawing_functions(recipes))
        all_recipes = [r for q in progress["questions"].values() for r in q["accepted"]]
        atomic_write(contained_path(self.output, "accepted_index.jsonl"), "".join(
            json.dumps(r, ensure_ascii=False, allow_nan=False) + "\n" for r in all_recipes))

    def _apply_deletion(self, transaction):
        # Read from a durable backup: a retry must not read files already renumbered.
        backup = contained_path(self.root, transaction["backup_path"])
        previous = transaction["before_recipes"]
        sources = {recipe["candidate_id"]: recipe for recipe in previous}
        for recipe in previous:
            for directory, suffix, digest in (("images", ".png", "png_sha256"),
                                               ("plugins", ".json", "plugin_sha256")):
                source = contained_path(backup, f"{directory}/{recipe['slot_id']}{suffix}")
                if not source.is_file() or file_hash(source) != recipe[digest]:
                    raise WorkbenchError("删除前备份丢失或损坏，无法安全恢复事务。", 409, "integrity_error")
        remaining = transaction["progress"]["questions"][transaction["question_id"]]["accepted"]
        destinations = set()
        for recipe in remaining:
            old = sources[recipe["candidate_id"]]
            for directory, suffix, key in (("images", ".png", "image_path"),
                                           ("plugins", ".json", "plugin_path")):
                target = self._accepted_path(recipe[key])
                source = contained_path(backup, f"{directory}/{old['slot_id']}{suffix}")
                atomic_write(target, source.read_bytes())
                destinations.add(target)
        # Remove only known former C paths, all resolved inside the C output directory.
        for recipe in previous:
            for key in ("image_path", "plugin_path"):
                target = self._accepted_path(recipe[key])
                if target not in destinations:
                    target.unlink(missing_ok=True)
        self._materialize(transaction["progress"], transaction["question_id"])

    def _materialize_collection(self, progress, qid):
        question = progress["questions"][qid]
        payload = {"question_id": qid,
                   "status": "collected" if question.get("collected") else "reopened",
                   "current": question.get("collection_record"),
                   "history": question.get("collection_history", [])}
        atomic_json(contained_path(self.output, f"{qid}/collection.json"), payload)

    def _apply_transaction(self, transaction):
        progress = transaction["progress"]
        if progress["signature"] != self.signature:
            raise WorkbenchError("待恢复事务属于不同版本或基线。", 409)
        if transaction["kind"] == "pass":
            candidate, recipe = transaction["candidate"], transaction["recipe"]
            self._verify_package(candidate)
            manifest = read_json(contained_path(self.state_dir, f"baselines/{recipe['baseline_fingerprint']}.json"))
            atomic_json(contained_path(self.output, f"_baselines/{recipe['baseline_fingerprint']}.json"), manifest)
            for source, key, digest_key in (("image.png", "image_path", "png_sha256"),
                                          ("plugin.json", "plugin_path", "plugin_sha256")):
                target = self._accepted_path(recipe[key])
                if target.exists():
                    if file_hash(target) != candidate[digest_key]:
                        raise WorkbenchError("正式槽位已有不同内容，拒绝覆盖。", 409, "slot_conflict")
                else:
                    atomic_write(target, self._package_file(candidate, source).read_bytes())
            self._materialize(progress, transaction["question_id"])
        elif transaction["kind"] == "reject":
            # Resolved path must be inside this one candidate package; never wildcard-delete.
            self._package_file(transaction["candidate"], "image.png").unlink(missing_ok=True)
        elif transaction["kind"] == "submit":
            self._verify_package(transaction["candidate"])
        elif transaction["kind"] == "delete_accepted":
            self._apply_deletion(transaction)
        elif transaction["kind"] == "collect":
            qid = transaction["question_id"]
            self._materialize_collection(progress, qid)
            records = [q["collection_record"] for q in progress["questions"].values() if q.get("collected")]
            atomic_write(self.output / "collected_index.jsonl", "".join(
                json.dumps(record, ensure_ascii=False, allow_nan=False) + "\n" for record in records))
        elif transaction["kind"] == "reopen":
            qid = transaction["question_id"]
            self._materialize_collection(progress, qid)
            records = [q["collection_record"] for q in progress["questions"].values() if q.get("collected")]
            atomic_write(self.output / "collected_index.jsonl", "".join(
                json.dumps(record, ensure_ascii=False, allow_nan=False) + "\n" for record in records))
        else:
            raise WorkbenchError("无法识别待恢复事务。", 409)
        atomic_json(self.state_dir / "progress.json", progress)
        self.progress = progress
        if (transaction["kind"] in ("pass", "delete_accepted") and
                self.dataset_root.resolve() == Path(self.config["dataset_file"]).resolve().parent and
                self.output.resolve() == self.dataset_root.resolve() / "special_variant"):
            from dataset_tools.catalog import build
            build(Path(self.config["dataset_file"]).resolve().parent.parent)
        (self.state_dir / "pending_transaction.json").unlink(missing_ok=True)

    def _recover(self):
        path = self.state_dir / "pending_transaction.json"
        if path.exists():
            self._apply_transaction(read_json(path))

    def _commit(self, transaction):
        atomic_json(self.state_dir / "pending_transaction.json", transaction)
        self._apply_transaction(transaction)

    def navigate(self, qid):
        with self.lock:
            self._recover()
            self._check_open_question(qid)
            if qid != self.progress["current_question"]:
                progress = copy.deepcopy(self.progress)
                progress["current_question"] = qid
                progress["navigation_revision"] += 1
                atomic_json(self.state_dir / "progress.json", progress)
                self.progress = progress
            return self.snapshot()

    def collect(self, qid, token):
        with self.submit_lock, self.lock:
            self._recover()
            question = self.progress["questions"].get(qid)
            if question and question.get("collected"):
                return self.snapshot()
            self._check_context(qid, token)
            if not question["accepted"]:
                raise WorkbenchError("先 Pass 保存至少一张 C 变体，再 Collect 完成整道题。")
            progress = copy.deepcopy(self.progress)
            question = progress["questions"][qid]
            question["collected"] = True
            question["collected_at"] = timestamp()
            question["revision"] += 1
            question["collection_record"] = {
                "question_id": qid, "status": "collected", "collected_at": question["collected_at"],
                "collection_number": len(question.get("collection_history", [])) + 1,
                "original_question": copy.deepcopy(self.adapter.records[qid]),
                "accepted_count": len(question["accepted"]),
                "slots": [r["slot_id"] for r in question["accepted"]],
            }
            active = [key for key in self.adapter.records if not progress["questions"][key].get("collected")]
            later = [key for key in active if key > qid]
            progress["current_question"] = later[0] if later else active[0] if active else None
            progress["navigation_revision"] += 1
            self._commit({"kind": "collect", "question_id": qid, "progress": progress})
            return self.snapshot()

    def _ensure_metadata(self, qid):
        """Collected questions are not inspected at startup; load them on reopen."""
        if qid in self.metadata or qid not in self.adapter.records:
            return
        meta = self.adapter.inspect_question(qid)
        with self.lock:
            self.metadata.setdefault(qid, meta)

    def reopen(self, qid, token):
        self._ensure_metadata(qid)
        with self.lock:
            self._recover()
            question = self.progress["questions"].get(qid)
            if not question:
                raise WorkbenchError("不存在此题号。", 404)
            if not question.get("collected"):
                return self.snapshot()
            if token != self.context_token():
                raise WorkbenchError("工作台已切题或更新，请刷新页面后重试。", 409, "stale_context")
            progress = copy.deepcopy(self.progress)
            question = progress["questions"][qid]
            previous = copy.deepcopy(question["collection_record"])
            previous["reopened_at"] = timestamp()
            question.setdefault("collection_history", []).append(previous)
            question["collected"] = False
            question["revision"] += 1
            progress["current_question"] = qid
            progress["navigation_revision"] += 1
            self._commit({"kind": "reopen", "question_id": qid, "progress": progress})
            return self.snapshot()

    def validate(self, plugin_path):
        with self.submit_lock, RENDER_LOCK:
            self.adapter.assert_baseline()
            plugin = self.renderer.normalize(self._read_draft(plugin_path))
            self._check_open_question(plugin["question_id"])
            return {"valid": True, "human_reviewed": False, "normalized_plugin": plugin,
                    "parameter_key": canonical_hash(plugin)}

    def quick_test_input(self, qid, cid, token, displayed_pixel, displayed_parameter):
        """Read precisely the displayed candidate; never include answer or plugin hints."""
        with self.lock:
            self._check_context(qid, token, cid)
            candidate = self.progress["candidates"].get(cid)
            if (not candidate or candidate["question_id"] != qid or candidate["status"] != "pending" or
                    self.progress["questions"][qid]["candidate_id"] != cid or
                    candidate["pixel_sha256"] != displayed_pixel or candidate["parameter_key"] != displayed_parameter):
                raise WorkbenchError("候选已更新，请等待当前图片载入后再测试。", 409, "stale_candidate")
            if self.job and self.job["question_id"] == qid:
                raise WorkbenchError("正在生成新候选，请稍候再测试。", 409, "generating")
            self.adapter.assert_baseline()
            self._verify_package(candidate)
            image = self._package_file(candidate, "image.png").read_bytes()
            if hashlib.sha256(image).hexdigest() != candidate["png_sha256"]:
                raise WorkbenchError("候选图片在读取时改变，请刷新后重试。", 409, "integrity_error")
            packet = {key: candidate[key] for key in
                      ("question_id", "candidate_id", "pixel_sha256", "png_sha256", "parameter_key")}
            packet.update(branch="PlaneGeometry", question=self.adapter.records[qid]["question"],
                          input_revision=self.context()["input_revision"])
            return packet, image

    def drawing_scene(self, qid):
        from drawing_board import describe_scene
        with RENDER_LOCK:
            self._check_open_question(qid)
            self.adapter.assert_baseline()
            return describe_scene(self.adapter, qid)

    def drawing_preview(self, plugin, token, replace=None):
        """Stateless preview: never replaces an agent's candidate or writes C data."""
        with self.submit_lock, RENDER_LOCK:
            self.adapter.assert_baseline()
            plugin = self.renderer.normalize(plugin)
            with self.lock:
                self._check_context(plugin["question_id"], token, replace)
            plugin, data, digest = self.renderer.render(plugin, frozen=True)
            with self.lock:
                self._check_context(plugin["question_id"], token, replace)
            return {"plugin": plugin, "pixel_sha256": digest, "parameter_key": canonical_hash(plugin),
                    "image_url": "data:image/png;base64," + base64.b64encode(data).decode("ascii")}

    def drawing_submit(self, plugin, token, replace, displayed_pixel, displayed_parameter):
        """Publish the exact preview as a normal candidate; Pass uses review()."""
        # No schema, renderer, recipe or generator-version changes are required.
        preview = self.drawing_preview(plugin, token, replace)
        if preview["pixel_sha256"] != displayed_pixel or preview["parameter_key"] != displayed_parameter:
            raise WorkbenchError("画板预览已变化，请等待最新图片后再保存。", 409, "stale_preview")
        draft = contained_path(self.root / "drafts", f"{plugin['question_id']}/board-{uuid.uuid4().hex}.json")
        atomic_json(draft, preview["plugin"])
        candidate = self.submit(draft, token, replace)
        if candidate["pixel_sha256"] != displayed_pixel or candidate["parameter_key"] != displayed_parameter:
            raise WorkbenchError("提交与画板预览不一致；已保留候选，请重新人工审核。", 409, "stale_preview")
        return {"candidate": candidate, "state": self.snapshot()}

    @staticmethod
    def _read_draft(plugin_path):
        path = Path(plugin_path).resolve()
        if not path.is_file() or path.stat().st_size > 1024 * 1024:
            raise WorkbenchError("草稿必须是存在且小于 1 MiB 的 JSON 文件。")
        # Only this complete read is used, even when the agent subsequently edits the draft.
        return read_json(path)

    def submit(self, plugin_path, token, replace=None):
        with self.submit_lock, RENDER_LOCK:
            qid = None
            try:
                self.adapter.assert_baseline()
                plugin = self.renderer.normalize(self._read_draft(plugin_path))
                qid = plugin["question_id"]
                with self.lock:
                    self._recover()
                    self._check_context(qid, token, replace)
                    self.job = {"question_id": qid, "status": "generating"}
                    self.errors.pop(qid, None)
                plugin, data, digest = self.renderer.render(plugin, frozen=True)
                self.adapter.assert_baseline()
                with self.lock:
                    self._check_context(qid, token, replace)
                    cid = uuid.uuid4().hex
                    candidate = {"candidate_id": cid, "question_id": qid, "status": "pending",
                                 "context_token": token, "created_at": timestamp(), "description": plugin["description"],
                                 "intent": plugin["intent"], "params": plugin["params"],
                                 "plugin_schema_version": SCHEMA_VERSION, **self.signature,
                                 "pixel_sha256": digest, "parameter_key": canonical_hash(plugin),
                                 "png_sha256": hashlib.sha256(data).hexdigest(),
                                 "plugin_sha256": hashlib.sha256(json_bytes(plugin)).hexdigest(),
                                 "image_path": f"candidates/{cid}/image.png",
                                 "plugin_path": f"candidates/{cid}/plugin.json"}
                    staging = contained_path(self.root / "candidates", f".publishing-{cid}")
                    staging.mkdir()
                    atomic_json(contained_path(staging, "plugin.json"), plugin)
                    atomic_write(contained_path(staging, "image.png"), data)
                    atomic_json(contained_path(staging, "manifest.json"), candidate)
                    os.replace(staging, contained_path(self.root / "candidates", cid))
                    progress = copy.deepcopy(self.progress)
                    if replace:
                        progress["candidates"][replace].update(status="superseded", superseded_by=cid)
                    progress["candidates"][cid] = candidate
                    question = progress["questions"][qid]
                    question["candidate_id"], question["revision"] = cid, question["revision"] + 1
                    self._commit({"kind": "submit", "candidate": candidate, "progress": progress})
                    return self._candidate_public(candidate)
            except Exception as error:
                with self.lock:
                    if qid:
                        self.errors[qid] = str(error)
                raise
            finally:
                with self.lock:
                    self.job = None

    def delete_accepted(self, qid, cid, slot, token, displayed_pixel, displayed_parameter):
        with self.lock:
            self._recover()
            candidate = self.progress["candidates"].get(cid)
            if candidate and candidate["question_id"] == qid and candidate["status"] == "deleted":
                return self.snapshot()
            self._check_open_question(qid)
            if qid != self.progress["current_question"] or token != self.context_token():
                raise WorkbenchError("题目或变体已更新，请刷新页面后再删除。", 409, "stale_context")
            if self.job and self.job["question_id"] == qid:
                raise WorkbenchError("正在生成候选，请稍候再删除。", 409, "generating")
            question = self.progress["questions"][qid]
            removed = next((r for r in question["accepted"] if r["candidate_id"] == cid), None)
            if not removed:
                raise WorkbenchError("这张已通过变体不存在。", 404, "accepted_not_found")
            if (removed["slot_id"] != slot or removed["pixel_sha256"] != displayed_pixel or
                    removed["parameter_key"] != displayed_parameter):
                raise WorkbenchError("待删除变体与页面显示不一致，请刷新后重试。", 409, "stale_variant")
            self.adapter.assert_baseline()
            previous = copy.deepcopy(question["accepted"])
            deletion_id, deleted_at = uuid.uuid4().hex, timestamp()
            backup_relative = f"deleted_variants/{qid}/{deletion_id}"
            backup = contained_path(self.root, backup_relative)
            for recipe in previous:
                for directory, suffix, key, digest in (
                        ("images", ".png", "image_path", "png_sha256"),
                        ("plugins", ".json", "plugin_path", "plugin_sha256")):
                    source = self._accepted_path(recipe[key])
                    if not source.is_file() or file_hash(source) != recipe[digest]:
                        raise WorkbenchError("正式图或参数已改变，拒绝删除；请先检查数据。", 409, "integrity_error")
                    atomic_write(contained_path(backup, f"{directory}/{recipe['slot_id']}{suffix}"), source.read_bytes())
            atomic_json(contained_path(backup, "deletion.json"), {
                "question_id": qid, "deleted_at": deleted_at, "removed_recipe": removed,
                "before_recipes": previous})
            progress = copy.deepcopy(self.progress)
            question = progress["questions"][qid]
            question["accepted"] = [r for r in question["accepted"] if r["candidate_id"] != cid]
            for index, recipe in enumerate(question["accepted"], 1):
                new_slot = f"C{index:02d}"
                recipe.update(slot_id=new_slot,
                    image_path=(self.output_relative / qid / "images" / f"{new_slot}.png").as_posix(),
                    plugin_path=(self.output_relative / qid / "plugins" / f"{new_slot}.json").as_posix())
                saved_candidate = progress["candidates"].get(recipe["candidate_id"])
                if saved_candidate:
                    saved_candidate.update(slot_id=new_slot, formal_image_path=recipe["image_path"],
                                           formal_plugin_path=recipe["plugin_path"])
            # A cold restore has durable recipes, but no old candidate packages.
            deleted = progress["candidates"].setdefault(cid, copy.deepcopy(removed))
            deleted.update(status="deleted", deleted_at=deleted_at, deletion_backup=backup_relative)
            for key in ("slot_id", "formal_image_path", "formal_plugin_path"):
                deleted.pop(key, None)
            if question["last_review"] and question["last_review"]["candidate_id"] == cid:
                question["last_review"] = None
            question["revision"] += 1
            question.setdefault("deletions", []).append({"candidate_id": cid, "slot_id": slot,
                "deleted_at": deleted_at, "backup_path": backup_relative})
            try:
                self._commit({"kind": "delete_accepted", "question_id": qid,
                    "backup_path": backup_relative, "before_recipes": previous, "progress": progress})
                self.errors.pop(qid, None)
            except Exception as error:
                self.errors[qid] = "删除保存未完成，事务将在重试或重启后恢复：" + str(error)
                raise
            return self.snapshot()

    def review(self, qid, cid, decision, token, displayed_pixel, displayed_parameter, note=""):
        with self.lock:
            self._recover()
            if decision not in ("pass", "reject") or not isinstance(note, str) or len(note) > 1000:
                raise WorkbenchError("审核动作或备注无效。")
            candidate = self.progress["candidates"].get(cid)
            if not candidate or candidate["question_id"] != qid:
                raise WorkbenchError("候选与题号不匹配。", 409, "stale_candidate")
            if displayed_pixel != candidate["pixel_sha256"] or displayed_parameter != candidate["parameter_key"]:
                raise WorkbenchError("请求不是已显示的候选快照。", 409, "stale_candidate")
            final_status = "passed" if decision == "pass" else "rejected"
            if candidate["status"] == final_status:
                return {"idempotent": True, "candidate": self._candidate_public(candidate)}
            if candidate["status"] != "pending" or qid != self.progress["current_question"] or token != self.context_token():
                raise WorkbenchError("候选已替换、已审核或页面已切题；请等待页面更新。", 409, "stale_candidate")
            if self.progress["questions"][qid]["candidate_id"] != cid:
                raise WorkbenchError("旧候选不能再审核。", 409, "stale_candidate")
            self.adapter.assert_baseline()
            plugin = self._verify_package(candidate)
            progress = copy.deepcopy(self.progress)
            reviewed_at = timestamp()
            updated = progress["candidates"][cid]
            updated.update(status=final_status, reviewed_at=reviewed_at, review_note=note)
            question = progress["questions"][qid]
            question["candidate_id"], question["revision"] = None, question["revision"] + 1
            question["last_review"] = {"candidate_id": cid, "decision": decision, "note": note,
                                       "reviewed_at": reviewed_at, "plugin": plugin}
            transaction = {"kind": decision, "question_id": qid, "candidate": candidate, "progress": progress}
            if decision == "pass":
                slot = f"C{len(question['accepted']) + 1:02d}"
                recipe = {**copy.deepcopy(plugin), "phase": "manual", "slot_id": slot,
                          "question_record_sha256": canonical_hash(self.adapter.records[qid]),
                          "candidate_id": cid, "parameter_key": candidate["parameter_key"],
                          "pixel_sha256": candidate["pixel_sha256"], "png_sha256": candidate["png_sha256"],
                          "plugin_sha256": candidate["plugin_sha256"], **self.signature,
                          "created_at": candidate["created_at"], "reviewed_at": reviewed_at, "status": "passed",
                          "image_path": (self.output_relative / qid / "images" / f"{slot}.png").as_posix(),
                          "plugin_path": (self.output_relative / qid / "plugins" / f"{slot}.json").as_posix()}
                updated["slot_id"], updated["formal_image_path"], updated["formal_plugin_path"] = slot, recipe["image_path"], recipe["plugin_path"]
                question["accepted"].append(recipe)
                transaction["recipe"] = recipe
            try:
                self._commit(transaction)
                self.errors.pop(qid, None)
            except Exception as error:
                self.errors[qid] = "保存失败，事务将在重试或重启后恢复：" + str(error)
                raise
            return {"idempotent": False, "candidate": self._candidate_public(self.progress["candidates"][cid])}

    def _candidate_public(self, candidate):
        result = copy.deepcopy(candidate)
        image = self._package_file(candidate, "image.png")
        result["image_path"] = str(image) if image.is_file() else None
        result["plugin_path"] = str(self._package_file(candidate, "plugin.json"))
        result["image_url"] = f"/api/candidate-image/{candidate['candidate_id']}" if image.is_file() else None
        if candidate.get("formal_image_path"):
            result["formal_image_path"] = str(self._accepted_path(candidate["formal_image_path"]))
            result["formal_plugin_path"] = str(self._accepted_path(candidate["formal_plugin_path"]))
        return result

    def status(self, cid):
        with self.lock:
            candidate = self.progress["candidates"].get(cid)
            if not candidate:
                raise WorkbenchError("候选 ID 不存在。", 404, "candidate_not_found")
            return self._candidate_public(candidate)

    def context(self):
        with self.lock:
            qid = self.progress["current_question"]
            if qid is None:
                return {"session_id": self.session_id, "question_id": None,
                        "context_token": self.context_token(), "question": "", "answer": None,
                        "objects": [], "candidate": None, "last_review": None,
                        "input_revision": None, "baseline_fingerprint": self.adapter.manifest["fingerprint"]}
            question = self.progress["questions"][qid]
            cid = question["candidate_id"]
            entry = str(ROOT / "agent_cli.py")
            draft_dir = str(self.root / "drafts" / qid)
            source_name = Path(self.adapter.sources[qid]["source_file"]).name
            files = self.adapter.manifest["files"]
            input_revision = canonical_hash({"record": self.adapter.records[qid], "files": {
                name: files[name] for name in self.adapter.dependencies(qid)}})
            return {"session_id": self.session_id, "question_id": qid, "context_token": self.context_token(),
                    "input_revision": input_revision,
                    "question": self.adapter.records[qid]["question"], "answer": self.adapter.records[qid]["answer"],
                    "original_image_path": str(self.adapter.original_paths[qid].resolve()),
                    **self.adapter.sources[qid], "objects": self.metadata[qid]["objects"],
                    "snap_points": self.metadata[qid]["snap_points"], "canvas": self.metadata[qid]["canvas"],
                    "candidate": self._candidate_public(self.progress["candidates"][cid]) if cid else None,
                    "last_review": copy.deepcopy(question["last_review"]),
                    "schema_path": str(ROOT / "plugin.schema.json"), "draft_directory": draft_dir,
                    "agent_prompt_path": str(ROOT / "agent_prompt.md"), "cli_entry": entry,
                    "commands": {name: f'python -B "{entry}" {name}' for name in ("context", "validate", "submit", "status", "highlight")},
                    "config_path": self.config["config_path"], "baseline_fingerprint": self.adapter.manifest["fingerprint"]}

    def snapshot(self):
        with self.lock:
            context = self.context()
            qid = context["question_id"]
            question = self.progress["questions"].get(qid, {"accepted": []})
            accepted = [{**r, "image_url": f"/api/accepted-image/{qid}/{r['slot_id']}?revision={r['png_sha256']}"}
                        for r in question["accepted"]]
            error = self.errors.get(qid)
            generating = self.job and self.job["question_id"] == qid
            status = "completed" if qid is None else "generating" if generating else "error" if error else "pending" if context["candidate"] else "waiting"
            return {**context, "original_image_url": f"/api/original-image/{qid}?revision={context['input_revision']}" if qid else None, "status": status,
                    "error": error, "accepted": accepted, "review_token": self.review_token,
                    "poll_interval_ms": self.config["poll_interval_ms"],
                    "questions": [{"id": key, "accepted_count": len(self.progress["questions"][key]["accepted"]),
                                   "has_pending": bool(self.progress["questions"][key]["candidate_id"])}
                                  for key in self.active_questions()],
                    "completed_questions": [{"id": key,
                                             "accepted_count": len(question["accepted"]),
                                             "collected_at": question["collected_at"]}
                                            for key, question in self.progress["questions"].items()
                                            if question.get("collected")],
                    "collected_total": sum(bool(q.get("collected")) for q in self.progress["questions"].values()),
                    "accepted_total": sum(len(q["accepted"]) for q in self.progress["questions"].values())}

    def highlight(self, qid, oid):
        with RENDER_LOCK:
            self._check_open_question(qid)
            self.adapter.assert_baseline()
            data = self.adapter.highlight(qid, oid)
            filename = f"reference-{qid}-{canonical_hash(oid)[:16]}.png"
            path = contained_path(self.root / "reproduced", filename)
            atomic_write(path, data)
            return {"reference_only": True, "image_path": str(path), "image_url": f"/api/reference-image/{filename}"}
