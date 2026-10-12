"""Portable paths, strict JSON, atomic files and content hashes for C only."""
from __future__ import annotations

import hashlib
import io
import json
import os
import platform
import sys
import tempfile
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
GENERATOR_VERSION = "Plane-C-1.0.0"
SCHEMA_VERSION = "1.0.0"
PATH_KEYS = ("dataset_file", "original_image_dir", "common_renderer_file",
             "protocol_file", "question_class_dir", "dataset_root", "output_dir", "runtime_dir")


class WorkbenchError(Exception):
    def __init__(self, message, status=400, code="invalid_request"):
        super().__init__(message)
        self.status = status
        self.code = code


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode("utf-8")


def canonical_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                    allow_nan=False, separators=(",", ":")).encode("utf-8")).hexdigest()


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pixel_hash(image_or_path):
    if isinstance(image_or_path, bytes):
        image_or_path = io.BytesIO(image_or_path)
    if isinstance(image_or_path, Image.Image):
        image = image_or_path.convert("RGBA")
    else:
        with Image.open(image_or_path) as loaded:
            image = loaded.convert("RGBA")
    prefix = f"{image.width}x{image.height}:RGBA:".encode("ascii")
    return hashlib.sha256(prefix + image.tobytes()).hexdigest()


def environment_versions():
    return {"python": platform.python_version(), **{name: version(name)
            for name in ("matplotlib", "numpy", "pillow")}}


def renderer_fingerprint():
    return canonical_hash({name: file_hash(ROOT / name) for name in
                           ("renderer_adapter.py", "render_plugins.py", "workbench_io.py")})


def renderer_matches(recipe, adapter):
    current = renderer_fingerprint()
    if recipe.get("renderer_sha256") == current:
        return True
    project = ROOT.parent.parent
    if str(project) not in sys.path:
        sys.path.insert(0, str(project))
    from dataset_tools.legacy_variant_compatibility import legacy_renderer_matches
    record = adapter.records.get(recipe.get("question_id"), {})
    return legacy_renderer_matches(ROOT.parent.name + "/Special",
                                   recipe.get("renderer_sha256"), current,
                                   record, adapter.manifest["files"])


def progress_renderer_matches(previous, current, adapter, old_manifest, old_records):
    project = ROOT.parent.parent
    if str(project) not in sys.path:
        sys.path.insert(0, str(project))
    from dataset_tools.legacy_variant_compatibility import legacy_progress_matches
    return legacy_progress_matches(ROOT.parent.name + "/Special", previous, current,
                                   adapter.records, adapter.manifest, old_manifest, old_records)


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"重复 JSON 字段：{key}")
        result[key] = value
    return result


def parse_json(text):
    def invalid_constant(value):
        raise ValueError(f"不接受非有限数值：{value}")
    try:
        return json.loads(text, parse_constant=invalid_constant, object_pairs_hook=_unique_object)
    except (ValueError, UnicodeError) as error:
        raise WorkbenchError(f"JSON 无效：{error}", code="invalid_json") from error


def read_json(path):
    try:
        return parse_json(Path(path).read_text(encoding="utf-8-sig"))
    except OSError as error:
        raise WorkbenchError(f"无法读取 JSON 文件 {path}：{error}", code="file_unavailable") from error


def atomic_write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(data, str):
        data = data.encode("utf-8")
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def atomic_json(path, value):
    atomic_write(path, json_bytes(value))


def contained_path(directory, relative):
    directory = Path(directory).resolve()
    target = (directory / relative).resolve()
    if not target.is_relative_to(directory) or target == directory:
        raise WorkbenchError("路径不在指定目录内，已阻止此操作。", code="unsafe_path")
    return target


def load_config(path=None):
    path = Path(path or ROOT / "config.json").resolve()
    config = read_json(path)
    for key in PATH_KEYS:
        config[key] = str((path.parent / config[key]).resolve())
    config["config_path"] = str(path)
    if config["host"] not in ("127.0.0.1", "localhost"):
        raise WorkbenchError("工作台仅绑定本机 127.0.0.1/localhost。")
    if type(config["port"]) is not int or not 0 <= config["port"] <= 65535:
        raise WorkbenchError("port 必须是 0～65535 的整数。")
    if not 250 <= config["poll_interval_ms"] <= 10000:
        raise WorkbenchError("poll_interval_ms 必须在 250～10000 之间。")
    return config


def protect_output_paths(config):
    """C outputs can be siblings of baseline folders, never their ancestors."""
    files = [Path(config[k]).resolve() for k in ("dataset_file", "common_renderer_file", "protocol_file")]
    folders = [Path(config[k]).resolve() for k in ("original_image_dir", "question_class_dir")]
    folders.append(Path(config["dataset_root"]).resolve() / "base_variant")
    runtime = Path(config["runtime_dir"]).resolve()
    output = Path(config["output_dir"]).resolve()
    for target in (runtime, output):
        if any(f.is_relative_to(target) or target.is_relative_to(f) for f in folders):
            raise WorkbenchError("输出目录不能包含或位于原图、原题类或 A/B 目录。", code="unsafe_path")
        if any(f.is_relative_to(target) or target == f for f in files):
            raise WorkbenchError("输出目录不能包含只读输入文件。", code="unsafe_path")
    if output.is_relative_to(runtime) or runtime.is_relative_to(output):
        raise WorkbenchError("runtime_dir 与 output_dir 必须相互独立。", code="unsafe_path")
    for name in ("state", "candidates", "drafts", "reproduced"):
        if not (runtime / name).resolve().is_relative_to(runtime):
            raise WorkbenchError(f"{name} 不能通过链接指向 runtime_dir 之外。", code="unsafe_path")
