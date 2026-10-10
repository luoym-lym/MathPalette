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
                          renderer_fingerprint, timestamp)


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

_WORKBENCH = Path(__file__).resolve().parents[3] / "special_variant_workbench"
if not (_WORKBENCH / "render_plugins.py").is_file():
    raise RuntimeError("Keep MathPalette/construct_dataset/special_variant and special_variant_workbench together.")
if str(_WORKBENCH) not in sys.path:
    sys.path.insert(0, str(_WORKBENCH))
from render_plugins import render_special_recipe

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
        self.adapter = RendererAdapter(self.config, expected)
        self.environment = environment_versions()
        self.signature = {"generator_version": GENERATOR_VERSION, "plugin_schema_version": SCHEMA_VERSION,
                          "environment": self.environment,
                          "baseline_fingerprint": self.adapter.manifest["fingerprint"],
                          "schema_sha256": file_hash(ROOT / "plugin.schema.json"),
                          "renderer_sha256": renderer_fingerprint()}
        progress_path = self.state_dir / "progress.json"
        if progress_path.exists():
            self.progress = read_json(progress_path)
            if self.progress["signature"] != self.signature:
                raise WorkbenchError("已有状态的基线、渲染器、schema 或依赖版本不一致；请恢复原版本。", 409, "version_mismatch")
            if self.progress["output_relative"] != self.output_relative.as_posix():
                raise WorkbenchError("正式输出目录结构与已有状态不一致。", 409, "output_changed")
        else:
            if (self.output / "accepted_index.jsonl").exists() or any(self.output.glob("Ana*/recipes.json")):
                raise WorkbenchError("正式 C 数据已存在但状态缺失；请恢复配套 state 备份，不能从空状态覆盖。", 409)
            self.progress = {"signature": self.signature, "output_relative": self.output_relative.as_posix(),
                             "current_question": "Ana01", "navigation_revision": 0,
                             "questions": {qid: {"revision": 0, "candidate_id": None, "accepted": [], "last_review": None}
                                           for qid in self.adapter.records}, "candidates": {}}
        metadata_path = self.state_dir / "scene_metadata.json"
        cache = read_json(metadata_path) if metadata_path.exists() else {}
        if cache.get("signature") == self.signature:
            self.metadata = cache["questions"]
        else:
            self.metadata = {}
            failures = []
            for index, qid in enumerate(self.adapter.records, 1):
                announce(f"无操作重绘校验 {qid} ({index}/80)")
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
        atomic_json(manifest_path, self.adapter.manifest)
        self._recover()
        self._validate_saved_files()
        atomic_json(progress_path, self.progress)

    def close(self):
        self.writer.close()

    def context_token(self):
        qid = self.progress["current_question"]
        question = self.progress["questions"][qid]
        return canonical_hash({"session": self.session_id, "question_id": qid,
                               "navigation_revision": self.progress["navigation_revision"],
                               "revision": question["revision"], "candidate_id": question["candidate_id"]})

    def _check_context(self, qid, token, replace=None):
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
        for qid, question in self.progress["questions"].items():
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
            if recipes:
                if read_json(contained_path(self.output, f"{qid}/recipes.json")) != recipes:
                    raise WorkbenchError(f"{qid}/recipes.json 与审核状态不一致。", 409, "integrity_error")
                if contained_path(self.output, f"{qid}/draw_variants.py").read_text(encoding="utf-8") != drawing_functions(recipes):
                    raise WorkbenchError(f"{qid}/draw_variants.py 与审核状态不一致。", 409, "integrity_error")
            all_recipes.extend(recipes)
            if question["candidate_id"]:
                self._verify_package(self.progress["candidates"][question["candidate_id"]])
        index_path = self.output / "accepted_index.jsonl"
        if all_recipes:
            expected = "".join(json.dumps(r, ensure_ascii=False, allow_nan=False) + "\n" for r in all_recipes)
            if not index_path.is_file() or index_path.read_text(encoding="utf-8") != expected:
                raise WorkbenchError("accepted_index.jsonl 与审核状态不一致。", 409, "integrity_error")

    def _accepted_path(self, relative):
        path = contained_path(self.dataset_root, relative)
        if not path.is_relative_to(self.output):
            raise WorkbenchError("正式 C 路径不在 output_dir 内。", code="unsafe_path")
        return path

    def _materialize(self, progress, qid):
        recipes = progress["questions"][qid]["accepted"]
        if recipes:
            atomic_json(contained_path(self.output, f"{qid}/recipes.json"), recipes)
            atomic_write(contained_path(self.output, f"{qid}/draw_variants.py"), drawing_functions(recipes))
        all_recipes = [r for q in progress["questions"].values() for r in q["accepted"]]
        if all_recipes:
            atomic_write(contained_path(self.output, "accepted_index.jsonl"), "".join(
                json.dumps(r, ensure_ascii=False, allow_nan=False) + "\n" for r in all_recipes))

    def _apply_transaction(self, transaction):
        progress = transaction["progress"]
        if progress["signature"] != self.signature:
            raise WorkbenchError("待恢复事务属于不同版本或基线。", 409)
        if transaction["kind"] == "pass":
            candidate, recipe = transaction["candidate"], transaction["recipe"]
            self._verify_package(candidate)
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
        else:
            raise WorkbenchError("无法识别待恢复事务。", 409)
        atomic_json(self.state_dir / "progress.json", progress)
        self.progress = progress
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
            if qid not in self.adapter.records:
                raise WorkbenchError("不存在此题号。")
            if qid != self.progress["current_question"]:
                progress = copy.deepcopy(self.progress)
                progress["current_question"] = qid
                progress["navigation_revision"] += 1
                atomic_json(self.state_dir / "progress.json", progress)
                self.progress = progress
            return self.snapshot()

    def validate(self, plugin_path):
        with self.submit_lock, RENDER_LOCK:
            self.adapter.assert_baseline()
            plugin = self.renderer.normalize(self._read_draft(plugin_path))
            return {"valid": True, "human_reviewed": False, "normalized_plugin": plugin,
                    "parameter_key": canonical_hash(plugin)}

    def drawing_scene(self, qid):
        from drawing_board import describe_scene
        with RENDER_LOCK:
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
            question = self.progress["questions"][qid]
            cid = question["candidate_id"]
            entry = str(ROOT / "agent_cli.py")
            draft_dir = str(self.root / "drafts" / qid)
            return {"session_id": self.session_id, "question_id": qid, "context_token": self.context_token(),
                    "question": self.adapter.records[qid]["question"], "answer": self.adapter.records[qid]["answer"],
                    "original_image_path": str(self.adapter.original_paths[qid].resolve()),
                    **self.adapter.sources[qid], "objects": self.metadata[qid]["objects"],
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
            question = self.progress["questions"][qid]
            accepted = [{**r, "image_url": f"/api/accepted-image/{qid}/{r['slot_id']}"} for r in question["accepted"]]
            error = self.errors.get(qid)
            generating = self.job and self.job["question_id"] == qid
            status = "generating" if generating else "error" if error else "pending" if context["candidate"] else "waiting"
            return {**context, "original_image_url": f"/api/original-image/{qid}", "status": status,
                    "error": error, "accepted": accepted, "review_token": self.review_token,
                    "poll_interval_ms": self.config["poll_interval_ms"],
                    "questions": [{"id": key, "accepted_count": len(q["accepted"]), "has_pending": bool(q["candidate_id"])}
                                  for key, q in self.progress["questions"].items()],
                    "accepted_total": sum(len(q["accepted"]) for q in self.progress["questions"].values())}

    def highlight(self, qid, oid):
        with RENDER_LOCK:
            self.adapter.assert_baseline()
            data = self.adapter.highlight(qid, oid)
            filename = f"reference-{qid}-{canonical_hash(oid)[:16]}.png"
            path = contained_path(self.root / "reproduced", filename)
            atomic_write(path, data)
            return {"reference_only": True, "image_path": str(path), "image_url": f"/api/reference-image/{filename}"}
