"""Local dataset loading and deterministic rendering for the Base pipeline."""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import io
import json
import os
import platform
import re
import sys
import tempfile
from contextlib import contextmanager
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent


def now():
    return datetime.now(timezone.utc).isoformat()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")


def digest(value):
    return hashlib.sha256(value).hexdigest()


def canonical_hash(value):
    return digest(json.dumps(value, sort_keys=True, ensure_ascii=False,
                             separators=(",", ":"), allow_nan=False).encode("utf-8"))


def parse_json(text):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result
    def invalid(value):
        raise ValueError(f"Non-finite JSON number: {value}")
    return json.loads(text, object_pairs_hook=unique, parse_constant=invalid)


def read_json(path):
    return parse_json(Path(path).read_text(encoding="utf-8-sig"))


def atomic_write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, str):
        data = data.encode("utf-8")
    descriptor, temporary = tempfile.mkstemp(prefix="." + path.name, suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def inside(root, relative):
    root = Path(root).resolve()
    path = (root / relative).resolve()
    if path == root or not path.is_relative_to(root):
        raise ValueError(f"Path escapes dataset: {relative}")
    return path


def question_id(value):
    if not isinstance(value, str) or not re.fullmatch(r"Ana(?:0[1-9]|[1-9][0-9]+)", value):
        raise ValueError(f"Invalid question ID: {value!r}")
    return value


def validate_record(row):
    if not {"id", "question", "answer", "image"}.issubset(row):
        raise ValueError("Each dataset row requires id/question/answer/image.")
    question_id(row["id"])
    if not isinstance(row["question"], str) or not row["question"].strip():
        raise ValueError("Question text is empty.")
    if type(row["answer"]) not in (int, float, str):
        raise ValueError("Answer must be a number or string.")
    json_bytes(row)  # Reject NaN and infinity.
    if row["image"] != f"image/{row['id']}.png":
        raise ValueError("Original image must be image/<question_id>.png.")


def load_records(root):
    path = Path(root) / "dataset.jsonl"
    project = Path(root).resolve().parent
    if str(project) not in sys.path:
        sys.path.insert(0, str(project))
    from dataset_tools.catalog import assert_formal_dataset
    assert_formal_dataset(path)
    rows = [parse_json(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    for row in rows:
        validate_record(row)
    if [row["id"] for row in rows] != [f"Ana{i:02d}" for i in range(1, len(rows) + 1)]:
        raise ValueError("Dataset IDs must be unique, ordered, and consecutive from Ana01.")
    return {row["id"]: row for row in rows}


def pixel_hash(data):
    source = io.BytesIO(data) if isinstance(data, bytes) else data
    with Image.open(source) as original:
        image = original.convert("RGBA")
        return digest(f"{image.width}x{image.height}:RGBA:".encode() + image.tobytes())


def png_bytes(fig, background="#FFFFFF"):
    buffer = io.BytesIO()
    fig.savefig(buffer, dpi=100, facecolor=background, transparent=False)
    data = buffer.getvalue()
    with Image.open(io.BytesIO(data)) as image:
        if image.size != (768, 768) or image.convert("RGBA").getextrema()[3] != (255, 255):
            raise ValueError("Expected an opaque 768 x 768 PNG.")
    return data


def environment():
    return {"python": platform.python_version(), **{name: version(name)
            for name in ("matplotlib", "numpy", "pillow")}}


@contextmanager
def dataset_lock(root):
    path = inside(root, ".base_pipeline.lock")
    with path.open("a+b") as handle:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b"0")
            handle.flush()
        handle.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            raise ValueError("Another Base/prepare process is using this dataset.") from None
        try:
            yield
        finally:
            handle.seek(0)
            if os.name == "nt":
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(handle, fcntl.LOCK_UN)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Dataset:
    def __init__(self, root=ROOT):
        self.root = Path(root).resolve()
        self.records = load_records(self.root)
        self.helpers = inside(self.root, "dataset_generator")
        self.sources = {}
        for path in sorted((self.helpers / "questions").glob("function_plot*.py")):
            for node in ast.parse(path.read_text(encoding="utf-8-sig")).body:
                if isinstance(node, ast.ClassDef) and node.name.startswith("Ana"):
                    qid = question_id(node.name)
                    if qid in self.sources:
                        raise ValueError(f"Duplicate question class: {qid}")
                    self.sources[qid] = path
        self.renderer = load_module("_base_common_renderer", self.helpers / "common_renderer.py")
        self.modules = {}

    def load_question(self, qid):
        question_id(qid)
        if qid not in self.sources:
            raise ValueError(f"Missing class {qid} in function_plot*.py.")
        source = self.sources[qid]
        if source not in self.modules:
            old_path, previous = sys.path[:], sys.modules.get("common_renderer")
            try:
                sys.path.insert(0, str(self.helpers))
                sys.modules["common_renderer"] = self.renderer
                self.modules[source] = load_module("_base_" + source.stem, source)
            finally:
                sys.path[:] = old_path
                if previous is None:
                    sys.modules.pop("common_renderer", None)
                else:
                    sys.modules["common_renderer"] = previous
        module = self.modules[source]
        question = getattr(module, qid)()
        row = {"id": question.id, "question": question.query, "answer": question.answer,
               "image": f"image/{qid}.png"}
        validate_record(row)
        if row["id"] != qid:
            raise ValueError(f"Class name and self.id disagree: {qid}")
        if qid in self.records and any(row[k] != self.records[qid][k] for k in row):
            raise ValueError(f"Class and dataset row disagree: {qid}")
        return module, question, row

    @contextmanager
    def scene(self, qid):
        module, question, _ = self.load_question(qid)
        captured, before = [], set(plt.get_fignums())
        original_finalize = module.finalize
        def capture(fig, destination):
            self.renderer.lock_view(fig.axes[0])
            captured.append(fig)
            return {}
        module.finalize = capture
        try:
            question.draw(0)
            if len(captured) != 1 or len(captured[0].axes) != 1:
                raise ValueError(f"Expected one figure and one axes: {qid}")
            yield captured[0]
        finally:
            module.finalize = original_finalize
            for number in set(plt.get_fignums()) - before:
                plt.close(number)

    def original(self, qid):
        with self.scene(qid) as fig:
            return png_bytes(fig)

    def baseline(self, qid):
        _, _, row = self.load_question(qid)
        paths = [self.sources[qid], self.helpers / "common_renderer.py", self.helpers / "protocol.json",
                 inside(self.root, row["image"])]
        record = self.records[qid]
        if record.get("scene"):
            paths.append(inside(self.root, record["scene"]))
        paths.extend(inside(self.root, p) for p in record.get("runtime_dependencies", []))
        return {"record": row, "files": {p.relative_to(self.root).as_posix(): digest(p.read_bytes()) for p in paths}}

    def verify_original(self, qid):
        data = self.original(qid)
        if pixel_hash(data) != pixel_hash(inside(self.root, self.records[qid]["image"])):
            raise ValueError(f"Original image does not match its frozen drawing script: {qid}")
        return data


def pending_special(root):
    """Derived from formal Collect records; the workbench imports new rows on restart."""
    pending = []
    for qid in load_records(root):
        path = inside(root, f"special_variant/{qid}/collection.json")
        if not path.exists() or read_json(path).get("status") != "collected":
            pending.append(qid)
    return pending
