"""Small persistence helpers shared by the service and deterministic renderer."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import tempfile
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
GENERATOR_VERSION = "1.0.0"


class WorkbenchError(Exception):
    def __init__(self, message, status=400):
        super().__init__(message)
        self.status = status


def timestamp():
    return datetime.now(timezone.utc).isoformat()


def canonical_hash(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False, allow_nan=False,
                   separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def pixel_hash(image_or_path):
    if isinstance(image_or_path, Image.Image):
        image = image_or_path.convert("RGBA")
    else:
        with Image.open(image_or_path) as loaded:
            image = loaded.convert("RGBA")
    prefix = f"{image.width}x{image.height}:RGBA:".encode("ascii")
    return hashlib.sha256(prefix + image.tobytes()).hexdigest()


def environment_versions():
    return {"python": platform.python_version(), **{
        name: version(name) for name in ("matplotlib", "numpy", "pillow")
    }}


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


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
    atomic_write(path, json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n")


def contained_path(directory, relative):
    directory = Path(directory).resolve()
    target = (directory / relative).resolve()
    if not target.is_relative_to(directory) or target == directory:
        raise WorkbenchError("路径不在指定目录内，已阻止此操作。")
    return target


def load_config(path=None):
    config_path = Path(path or ROOT / "config.json").resolve()
    config = read_json(config_path)
    config["source_dir"] = str((config_path.parent / config["source_dir"]).resolve())
    if config["quota_per_category"] != 5:
        raise WorkbenchError("本工作台要求每题 A=5、B=5。")
    if not (0 < config["integer_tolerance"] <= 1e-8):
        raise WorkbenchError("整数验证容差须大于 0 且不超过 1e-8。")
    if len(config["background_colors"]) != 2 or config["max_candidate_attempts"] < 1:
        raise WorkbenchError("须配置两种背景色及有限的候选构造次数。")
    return config
