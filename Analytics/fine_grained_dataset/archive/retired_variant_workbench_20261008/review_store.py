"""Serialized review workflow with a recoverable write-ahead transaction.

progress.json is authoritative. recipes, functions, the global index and
availability are materialized before the progress commit. A pending journal
is rolled forward on restart; no decision is counted twice.
"""

from __future__ import annotations

import copy
import json
import os
import random
import secrets
import threading
import uuid
from pathlib import Path

from generate_variants import FINITE, GROUPS, OPERATIONS, VariantGenerator, parameter_key
from renderer_adapter import RendererAdapter
from workbench_io import (GENERATOR_VERSION, ROOT, WorkbenchError, atomic_json,
                          atomic_write, canonical_hash, contained_path,
                          environment_versions, load_config, pixel_hash, read_json, timestamp)


class StoreLock:
    """One writer process per state directory, released by the OS on crash."""
    def __init__(self, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.handle = path.open("a+b")
        try:
            # Windows denies reads of a byte locked by another process. Check
            # file size without reading that byte before attempting the lock.
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
            raise WorkbenchError("这个工作台目录已有运行中的服务，请使用现有窗口。", 409) from error

    def close(self):
        self.handle.close()


def drawing_functions(recipes):
    slots = [recipe["slot_id"] for recipe in recipes]
    text = '''"""Deterministic redraw functions for the human-reviewed slots only."""
from pathlib import Path
import json
import sys

_WORKBENCH = Path(__file__).resolve().parents[2]
if not (_WORKBENCH / "generate_variants.py").is_file():
    _WORKBENCH = Path(__RENDERER_ROOT__)
if str(_WORKBENCH) not in sys.path:
    sys.path.insert(0, str(_WORKBENCH))
from generate_variants import render_recipe

def _draw(slot_id, output_path=None):
    recipes = json.loads(Path(__file__).with_name("recipes.json").read_text(encoding="utf-8"))
    recipe = next(r for r in recipes if r["slot_id"] == slot_id)
    return render_recipe(recipe, output_path)

'''.replace("__RENDERER_ROOT__", repr(str(ROOT)))
    for slot in slots:
        text += f'def draw_{slot}(output_path=None):\n    return _draw("{slot}", output_path)\n\n'
    text += ("if __name__ == '__main__':\n"
             "    import argparse\n"
             "    parser = argparse.ArgumentParser(description='按冻结参数重绘人工通过图')\n"
             f"    parser.add_argument('slot_id', choices={slots!r})\n"
             "    parser.add_argument('--output', type=Path)\n"
             "    args = parser.parse_args()\n"
             "    print(_draw(args.slot_id, args.output))\n")
    return text


class Workbench:
    def __init__(self, root=None, config=None, announce=None):
        self.root = Path(root or ROOT).resolve()
        self.config = config or load_config()
        source = Path(self.config["source_dir"]).resolve()
        if self.root.is_relative_to(source) or source.is_relative_to(self.root):
            raise WorkbenchError("工作台输出目录与只读原始输入目录必须相互独立。")
        self.lock = threading.RLock()
        self.root.mkdir(parents=True, exist_ok=True)
        for directory in ("state", "candidates", "accepted", "reproduced"):
            if not (self.root / directory).resolve().is_relative_to(self.root):
                raise WorkbenchError(f"{directory} 目录不能通过链接指向工作台之外。")
        self.writer = StoreLock(self.root / "state" / "workbench.lock")
        try:
            self._initialize(announce or (lambda message: None))
        except Exception:
            self.writer.close()
            raise

    def _initialize(self, announce):
        manifest_path = self.root / "state" / "baseline_manifest.json"
        expected = read_json(manifest_path) if manifest_path.exists() else None
        self.adapter = RendererAdapter(self.config["source_dir"], expected, self.config["integer_tolerance"])
        self.environment = environment_versions()
        self.signature = {"generator_version": GENERATOR_VERSION, "environment": self.environment,
                          "baseline_fingerprint": self.adapter.manifest["fingerprint"],
                          "config_fingerprint": canonical_hash(self.config)}
        progress_path = self.root / "state" / "progress.json"
        self.progress = read_json(progress_path) if progress_path.exists() else None
        if self.progress and self.progress.get("signature") != self.signature:
            raise WorkbenchError("配置、依赖或生成器版本与已有进度不同，请恢复原审核环境；不要删除已有进度。", 409)
        availability_path = self.root / "state" / "availability.json"
        cached = read_json(availability_path) if availability_path.exists() else {}
        if cached.get("signature") == self.signature:
            self.metadata = cached["prechecks"]
        else:
            self.metadata = {}
            for index, qid in enumerate(self.adapter.records, 1):
                announce(f"校验原图并检查操作可用性：{qid} ({index}/80)")
                self.metadata[qid] = self.adapter.inspect_question(qid)
        self.generator = VariantGenerator(self.config, self.adapter, self.metadata)
        if not self.progress:
            self.progress = {"schema_version": 1, "signature": self.signature, "current_question": "Ana01",
                             "questions": {qid: self._empty_question(qid) for qid in self.adapter.records}}
        atomic_json(manifest_path, self.adapter.manifest)
        self._recover()
        self._validate_saved_files()
        for directory in ("candidates", "accepted", "reproduced"):
            (self.root / directory).mkdir(exist_ok=True)
        self._materialize(self.progress, self.progress["current_question"])

    def close(self):
        self.writer.close()

    def _empty_question(self, qid):
        return {"accepted": [], "candidate": None, "history": [], "error": None,
                "operations": {op: {**check, "covered": False, "coverage_resolved": check["status"] != "available"}
                               for op, check in self.metadata[qid]["operations"].items()}}

    def _validate_saved_files(self):
        for qid, question in self.progress["questions"].items():
            counts = self.counts(question)
            if max(counts.values()) > 5 or len({r["slot_id"] for r in question["accepted"]}) != len(question["accepted"]):
                raise WorkbenchError(f"{qid} 已有槽位记录无效，请保留文件并检查备份。", 409)
            hashes = [r["pixel_sha256"] for r in question["accepted"]]
            if len(set(hashes)) != len(hashes) or self.metadata[qid]["original_pixel_sha256"] in hashes:
                raise WorkbenchError(f"{qid} 的通过图有像素重复。", 409)
            for recipe in question["accepted"]:
                image = contained_path(self.root / "accepted", Path(recipe["image_path"]).relative_to("accepted"))
                if not image.is_file() or pixel_hash(image) != recipe["pixel_sha256"]:
                    raise WorkbenchError(f"已通过图片丢失或损坏：{qid}/{recipe['slot_id']}；请从备份恢复。", 409)

    @staticmethod
    def counts(question):
        return {category: sum(r["category"] == category for r in question["accepted"]) for category in GROUPS}

    def plan(self, qid, progress=None):
        question = (progress or self.progress)["questions"][qid]
        counts = self.counts(question)
        category = next((group for group in GROUPS if counts[group] < 5), None)
        if category is None:
            return {"phase": "complete", "category": None, "operations": [], "slot_id": None}
        coverage = [op for op in GROUPS[category] if question["operations"][op]["status"] == "available"
                    and not question["operations"][op]["coverage_resolved"]]
        operations = coverage[:1] or [op for op in GROUPS[category] if question["operations"][op]["status"] == "available"]
        return {"phase": "coverage" if coverage else "fill", "category": category,
                "operations": operations, "slot_id": f"{category}{counts[category] + 1:02d}",
                "blocked": not operations}

    def _availability(self, progress):
        return {"signature": self.signature, "prechecks": self.metadata,
                "questions": {qid: {"operations": question["operations"], "counts": self.counts(question),
                                    "plan": self.plan(qid, progress)} for qid, question in progress["questions"].items()}}

    def _persist(self, progress):
        atomic_json(self.root / "state" / "availability.json", self._availability(progress))
        atomic_json(self.root / "state" / "progress.json", progress)

    def _materialize(self, progress, qid):
        recipes = progress["questions"][qid]["accepted"]
        if recipes:
            directory = self.root / "accepted" / qid
            atomic_json(directory / "recipes.json", recipes)
            atomic_write(directory / "draw_variants.py", drawing_functions(recipes))
        all_recipes = [recipe for question in progress["questions"].values() for recipe in question["accepted"]]
        atomic_write(self.root / "accepted_index.jsonl", "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in all_recipes))
        self._persist(progress)

    def _candidate_path(self, candidate):
        relative = Path(candidate["image_path"])
        if not relative.parts or relative.parts[0] != "candidates" or relative.suffix != ".png":
            raise WorkbenchError("无效候选路径，已阻止文件操作。")
        return contained_path(self.root / "candidates", relative.relative_to("candidates"))

    def _delete_candidate(self, candidate):
        # Only one resolved file inside candidates/ is ever deleted.
        self._candidate_path(candidate).unlink(missing_ok=True)

    def _apply_transaction(self, transaction):
        candidate = transaction["candidate"]
        candidate_path = self._candidate_path(candidate)
        if transaction["kind"] == "pass":
            recipe = transaction["recipe"]
            target = contained_path(self.root / "accepted", Path(recipe["image_path"]).relative_to("accepted"))
            if not target.exists() or pixel_hash(target) != candidate["pixel_sha256"]:
                if not candidate_path.is_file() or pixel_hash(candidate_path) != candidate["pixel_sha256"]:
                    raise WorkbenchError("候选 PNG 丢失或损坏，无法完成保存。", 409)
                atomic_write(target, candidate_path.read_bytes())
            self._materialize(transaction["progress"], transaction["question_id"])
            self._delete_candidate(candidate)
        else:
            self._delete_candidate(candidate)
            self._materialize(transaction["progress"], transaction["question_id"])
        self.progress = transaction["progress"]
        (self.root / "state" / "pending_transaction.json").unlink()

    def _recover(self):
        journal = self.root / "state" / "pending_transaction.json"
        if journal.exists():
            transaction = read_json(journal)
            if transaction["progress"]["signature"] != self.signature:
                raise WorkbenchError("待恢复事务属于不同的基线或环境。", 409)
            self._apply_transaction(transaction)

    def _commit(self, transaction):
        atomic_json(self.root / "state" / "pending_transaction.json", transaction)
        self._apply_transaction(transaction)

    @staticmethod
    def tried_keys(question):
        return {r["parameter_key"] for r in question["accepted"] + question["history"]
                if r.get("decision") != "skipped"}

    def _update_exhaustion(self, qid, question, operation):
        if operation in FINITE and question["operations"][operation]["status"] == "available":
            if not self.generator.remaining_finite(qid, operation, self.tried_keys(question)):
                question["operations"][operation].update({"status": "exhausted", "coverage_resolved": True,
                    "reason": "有限参数均已审核，或已排除像素重复及无视觉变化的结果。"})

    def ensure_candidate(self):
        with self.lock:
            self._recover()
            qid = self.progress["current_question"]
            question = self.progress["questions"][qid]
            if question["candidate"]:
                candidate = question["candidate"]
                path = self._candidate_path(candidate)
                if not path.exists():
                    # Restore the frozen candidate, never sample a replacement.
                    data, digest = self.generator.render(qid, candidate["operation"], candidate["params"])
                    if digest != candidate["pixel_sha256"]:
                        raise WorkbenchError("待审核候选无法按冻结参数恢复相同像素。", 409)
                    atomic_write(path, data)
                elif pixel_hash(path) != candidate["pixel_sha256"]:
                    raise WorkbenchError("待审核候选文件被修改，请恢复文件后重试。", 409)
                return
            question["error"] = None
            for operation in OPERATIONS:
                self._update_exhaustion(qid, question, operation)
            while True:
                plan = self.plan(qid)
                if plan["phase"] == "complete" or plan["blocked"]:
                    self._persist(self.progress)
                    return
                operation = secrets.choice(plan["operations"])
                question["error_operation"] = operation
                tried = self.tried_keys(question)
                seen_hashes = {r["pixel_sha256"] for r in question["accepted"] + question["history"]
                               if r.get("decision") != "skipped"}
                seen_hashes.add(self.metadata[qid]["original_pixel_sha256"])
                failures = []
                for _ in range(self.config["max_candidate_attempts"]):
                    seed = secrets.randbits(63)
                    params = self.generator.sample(qid, operation, random.Random(seed), tried)
                    if params is None:
                        if operation in FINITE:
                            question["operations"][operation].update({"status": "exhausted", "coverage_resolved": True,
                                                                       "reason": "没有尚未尝试的有限参数。"})
                            break
                        failures.append("没有合法可采样位置")
                        continue
                    key = parameter_key(operation, params)
                    if key in tried:
                        continue
                    try:
                        data, digest = self.generator.render(qid, operation, params)
                    except WorkbenchError as error:
                        failures.append(str(error))
                        continue
                    if digest in seen_hashes:
                        question["history"].append({"candidate_id": uuid.uuid4().hex, "operation": operation,
                            "phase": plan["phase"], "params": params, "seed": seed, "parameter_key": key,
                            "pixel_sha256": digest, "decision": "discarded_duplicate", "reviewed_at": timestamp()})
                        tried.add(key)
                        self._update_exhaustion(qid, question, operation)
                        continue
                    candidate_id = uuid.uuid4().hex
                    candidate = {"question_id": qid, "category": plan["category"], "operation": operation,
                                 "phase": plan["phase"], "candidate_id": candidate_id, "seed": seed,
                                 "params": params, "parameter_key": key,
                                 "image_path": f"candidates/{candidate_id}.png", "pixel_sha256": digest,
                                 "status": "unreviewed", "created_at": timestamp(),
                                 "generator_version": GENERATOR_VERSION, "environment": self.environment,
                                 "baseline_fingerprint": self.adapter.manifest["fingerprint"]}
                    path = self._candidate_path(candidate)
                    atomic_write(path, data)
                    question["candidate"] = candidate
                    try:
                        self._persist(self.progress)
                    except Exception:
                        question["candidate"] = None
                        self._delete_candidate(candidate)
                        raise
                    return
                if question["operations"][operation]["status"] == "exhausted":
                    continue
                question["error"] = (f"{operation} 在 {self.config['max_candidate_attempts']} 次构造内未得到有效新图。"
                                     "可重试或跳过此类型。" + (" 原因：" + failures[-1] if failures else ""))
                question["error_operation"] = operation
                self._persist(self.progress)
                return

    def _generate_safely(self):
        try:
            self.ensure_candidate()
        except Exception as error:
            question = self.progress["questions"][self.progress["current_question"]]
            question["error"] = f"生成或保存候选失败：{error}"
            try:
                self._persist(self.progress)
            except OSError:
                pass

    def navigate(self, qid):
        with self.lock:
            self._recover()
            if qid not in self.adapter.records:
                raise WorkbenchError("不存在此题号。")
            self.progress["current_question"] = qid
            self._persist(self.progress)
            self._generate_safely()
            return self.snapshot()

    def review(self, candidate_id, decision):
        with self.lock:
            self._recover()
            self.adapter.assert_baseline()
            if decision not in ("pass", "reject"):
                raise WorkbenchError("无效审核动作。")
            qid = self.progress["current_question"]
            question = self.progress["questions"][qid]
            previous = next((r for q in self.progress["questions"].values() for r in q["history"]
                             if r["candidate_id"] == candidate_id), None)
            if previous:
                if previous["decision"] != decision:
                    raise WorkbenchError("该候选已审核，不能改变另一张图的状态。", 409)
                return self.snapshot()  # Idempotent transport retry; no new side effect.
            candidate = question["candidate"]
            if not candidate or candidate["candidate_id"] != candidate_id:
                raise WorkbenchError("候选已过期，请刷新后审核当前图片。", 409)
            path = self._candidate_path(candidate)
            if not path.is_file() or pixel_hash(path) != candidate["pixel_sha256"]:
                raise WorkbenchError("当前候选 PNG 缺失或被修改，未执行审核。", 409)
            future = copy.deepcopy(self.progress)
            target = future["questions"][qid]
            target["candidate"] = None
            target["error"] = None
            history = {key: candidate[key] for key in ("candidate_id", "operation", "phase", "parameter_key", "pixel_sha256")}
            history.update({"decision": decision, "reviewed_at": timestamp()})
            transaction = {"kind": decision, "question_id": qid, "candidate": candidate, "progress": future}
            if decision == "pass":
                category = candidate["category"]
                count = self.counts(target)[category]
                if count >= 5:
                    raise WorkbenchError("此组已有 5 张通过图，未覆盖其他槽位。", 409)
                if any(r["pixel_sha256"] == candidate["pixel_sha256"] for r in target["accepted"]):
                    raise WorkbenchError("此题已有像素相同的通过图，不能重复计数。", 409)
                slot = f"{category}{count + 1:02d}"
                recipe = {**candidate, "slot_id": slot, "image_path": f"accepted/{qid}/images/{slot}.png",
                          "status": "passed", "reviewed_at": history["reviewed_at"]}
                target["accepted"].append(recipe)
                target["operations"][candidate["operation"]].update({"covered": True, "coverage_resolved": True})
                transaction["recipe"] = recipe
            else:
                history.update({key: candidate[key] for key in ("params", "seed")})
            target["history"].append(history)
            self._update_exhaustion(qid, target, candidate["operation"])
            if decision == "pass" and all(v == 5 for v in self.counts(target).values()):
                ids = list(future["questions"])
                after = ids[ids.index(qid) + 1:] + ids[:ids.index(qid)]
                next_id = next((item for item in after if any(v < 5 for v in self.counts(future["questions"][item]).values())), None)
                if next_id:
                    future["current_question"] = next_id
            self._commit(transaction)
            self._generate_safely()
            return self.snapshot()

    def skip(self, candidate_id=None, reason="用户选择暂不继续尝试此类型。", operation=None):
        with self.lock:
            self._recover()
            qid = self.progress["current_question"]
            question = self.progress["questions"][qid]
            candidate = question["candidate"]
            if candidate:
                if candidate_id != candidate["candidate_id"]:
                    raise WorkbenchError("候选已过期，请刷新。", 409)
                operation = candidate["operation"]
            elif candidate_id:
                raise WorkbenchError("当前没有此候选。", 409)
            elif operation != question.get("error_operation"):
                raise WorkbenchError("请指定当前生成失败的类型。", 409)
            if operation not in OPERATIONS or question["operations"][operation]["status"] != "available":
                raise WorkbenchError("该操作不在可跳过的状态。", 409)
            future = copy.deepcopy(self.progress)
            target = future["questions"][qid]
            target["operations"][operation].update({"status": "skipped", "coverage_resolved": True, "reason": reason[:500]})
            target["candidate"] = None
            target["error"] = None
            if candidate:
                target["history"].append({**{key: candidate[key] for key in
                    ("candidate_id", "operation", "phase", "parameter_key", "pixel_sha256", "params", "seed")},
                    "decision": "skipped", "reviewed_at": timestamp()})
                self._commit({"kind": "skip", "question_id": qid, "candidate": candidate, "progress": future})
            else:
                self._persist(future)
                self.progress = future
            self._generate_safely()
            return self.snapshot()

    def retry(self, operation=None):
        with self.lock:
            self._recover()
            question = self.progress["questions"][self.progress["current_question"]]
            if operation:
                state = question["operations"].get(operation)
                if not state or state["status"] != "skipped":
                    raise WorkbenchError("只能恢复用户跳过的类型。")
                state.update({"status": "available", "reason": "", "coverage_resolved": state["covered"]})
                self._persist(self.progress)
            self._generate_safely()
            return self.snapshot()

    def snapshot(self):
        with self.lock:
            qid = self.progress["current_question"]
            question = self.progress["questions"][qid]
            candidate = copy.deepcopy(question["candidate"])
            recovering = (self.root / "state" / "pending_transaction.json").exists()
            if recovering:
                candidate = None
            elif candidate:
                candidate["image_url"] = f"/media/candidate/{candidate['candidate_id']}?cid={candidate['candidate_id']}"
            plan = self.plan(qid)
            counts = self.counts(question)
            accepted = [dict(r, image_url=f"/media/accepted/{qid}/{r['slot_id']}?hash={r['pixel_sha256']}") for r in question["accepted"]]
            coverage = {op: 0 for op in OPERATIONS}
            shortages, questions, total, completed = [], [], 0, 0
            for item, value in self.progress["questions"].items():
                item_counts = self.counts(value)
                total += sum(item_counts.values())
                done = all(v == 5 for v in item_counts.values())
                completed += int(done)
                item_plan = self.plan(item)
                questions.append({"id": item, "counts": item_counts, "complete": done,
                                  "blocked": item_plan.get("blocked", False), "has_candidate": bool(value["candidate"])})
                for recipe in value["accepted"]:
                    coverage[recipe["operation"]] += 1
                for category in GROUPS:
                    if item_counts[category] < 5:
                        shortages.append({"question_id": item, "category": category, "missing": 5 - item_counts[category],
                                          "blocked": item_plan.get("category") == category and item_plan.get("blocked", False)})
            operation = candidate["operation"] if candidate else question.get("error_operation") if question["error"] else (
                plan["operations"][0] if plan["operations"] else None)
            return {"current_question": qid, "question": self.adapter.records[qid], "counts": counts,
                    "plan": plan, "candidate": candidate, "accepted": accepted, "operations": question["operations"],
                    "operation_names": OPERATIONS, "current_operation": operation,
                    "error": "上次保存或删除尚未完成，请点击重试恢复事务。" if recovering else question["error"],
                    "recovery_required": recovering, "original_url": f"/media/original/{qid}", "questions": questions,
                    "precheck": {key: self.metadata[qid][key] for key in
                                 ("original_point_count", "unsupported_geometry", "integer_points")},
                    "global": {"accepted": total, "target": 800, "completed_questions": completed,
                               "total_questions": 80, "pending_slots": 800 - total,
                               "pending_candidates": sum(bool(q["candidate"]) for q in self.progress["questions"].values()),
                               "coverage": coverage, "shortages": shortages}, "baseline_fingerprint": self.adapter.manifest["fingerprint"]}
