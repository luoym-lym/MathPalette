"""Narrow adapter for the versioned promote15 author renderer."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

from matplotlib.collections import PathCollection
from matplotlib.patches import Patch
from mathvision_adapter import RendererAdapter as MathVisionAdapter
from renderer_adapter import RENDER_LOCK
from workbench_io import ROOT, WorkbenchError, contained_path, pixel_hash, read_json

FAMILIES = {
    "Plane506": ("Plane506", "tiling"), "Plane507": ("Plane511", "connect"),
    "Plane508": ("Plane512", "connect"), "Plane509": ("Plane513", "connect"),
    "Plane510": ("Plane517", "delete_points"), "Plane511": ("Plane519", "delete_points"),
    "Solid249": ("Solid249", "folding"), "Solid250": ("Solid254", "cube"),
    "Solid251": ("Solid256", "cube"), "Solid252": ("Solid259", "octahedron"),
    "Solid253": ("Solid260", "octahedron"), "Solid254": ("Solid261", "octahedron"),
    "Solid255": ("Solid262", "octahedron"), "Solid256": ("Solid267", "surface"),
    "Solid257": ("Solid268", "surface"),
}
EXECUTORS = tuple("workbench/" + n for n in
                  ("author_adapter.py", "author_plugins.py", "author_board.py", "author_replay.py",
                   "review_store.py", "replay_archived.py"))


def is_author_record(record):
    if not isinstance(record, dict) or record.get("id") not in FAMILIES:
        return False
    qid = record["id"]
    old, _ = FAMILIES[qid]
    wanted = f"dataset_generator/author_promote15_v1/items/{qid}/scene.json"
    dependencies = record.get("runtime_dependencies", [])
    expected = {wanted, "dataset_generator/author_promote15_v1/native_renderer.py",
                "dataset_generator/author_promote15_v1/author_partial_style.py"}
    return (record.get("source_dataset") == "Author Designed" and
            record.get("source_key") == f"author-promote15:{old}" and
            isinstance(dependencies, list) and len(dependencies) == len(expected) and
            set(dependencies) == expected)


def engine(branch):
    path = branch / "dataset_generator/author_promote15_v1/native_renderer.py"
    name = "_author_promote15_" + branch.name
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def explicit_points(frozen, family):
    """Only explicit vertices/endpoints; never infer circle centers or intersections."""
    points = []
    def add(p):
        xy = [float(p[0]), float(p[1])]
        if xy not in points:
            points.append(xy)
    if family in ("connect", "delete_points"):
        for value in frozen["points"].values():
            add(value["xy"] if isinstance(value, dict) else value)
    elif family == "octahedron":
        for edge in frozen["planar_net"]["edges"]:
            for p in edge["planar_endpoints"]: add(p)
    else:
        for obj in frozen["objects"]:
            if family == "tiling": values = (obj["p1"], obj["p2"])
            elif family == "cube": values = obj["xy"]
            elif family == "folding": values = (obj["a"], obj["b"]) if obj.get("type") == "line" else ()
            elif family == "surface":
                m = frozen["projection"]["matrix"]
                values = [[sum(m[j][i] * p[i] for i in range(3)) for j in range(2)] for p in obj["points"]]
            else: values = ()
            for p in values: add(p)
    return [{"id": f"author_snap_{i}", "label": "", "xy": p, "kind": "original_point",
             "source": "frozen_scene"} for i, p in enumerate(points)]


class RendererAdapter(MathVisionAdapter):
    def __init__(self, config, expected_manifest=None):
        super().__init__(config)
        self.branch = Path(config["dataset_file"]).resolve().parent
        for name in EXECUTORS:
            self.input_files[name] = self.branch / name
        # Solid's legacy adapter does not index runtime dependencies.
        for qid, record in self.records.items():
            if self.is_author(qid):
                for name in record["runtime_dependencies"]:
                    self.input_files["author_runtime/" + name] = contained_path(self.branch, name)
        self.manifest = self.make_manifest()
        if expected_manifest and self.manifest != expected_manifest:
            raise WorkbenchError("Author baseline changed", 409, "baseline_changed")

    def is_author(self, qid):
        return is_author_record(self.records.get(qid))

    def author_dependencies(self, qid):
        return (*("author_runtime/" + p for p in self.records[qid]["runtime_dependencies"]), *EXECUTORS)

    def dependencies(self, qid):
        parent = super()
        original = (parent.dependencies(qid) if hasattr(parent, "dependencies")
                    else parent.question_dependencies(qid))
        return (*original, *self.author_dependencies(qid)) if self.is_author(qid) else original

    def question_dependencies(self, qid):
        original = super().question_dependencies(qid)
        return (*original, *self.author_dependencies(qid)) if self.is_author(qid) else original

    def scene(self, qid):
        if not self.is_author(qid): return super().scene(qid)
        path = contained_path(self.branch, f"dataset_generator/author_promote15_v1/items/{qid}/scene.json")
        frozen = read_json(path)
        if frozen.get("id") != qid or frozen.get("source_dataset") != "Author Designed":
            raise WorkbenchError("Author scene identity changed", 409, "baseline_changed")
        family = FAMILIES[qid][1]
        with RENDER_LOCK:
            scene = engine(self.branch).capture(frozen, family)
            scene.snap_points = explicit_points(frozen, family)
            if family == "surface":
                visibility = {o["id"]: "hidden" if o["linestyle"] == "dashed" else "visible" for o in frozen["objects"]}
                for obj in scene.objects: obj["frozen_visibility"] = visibility[obj["id"]]
            return scene

    def inspect_question(self, qid):
        if not self.is_author(qid): return super().inspect_question(qid)
        from author_board import describe_captured_scene
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                digest = pixel_hash(engine(self.branch).png_bytes(scene))
                if digest != pixel_hash(self.original_paths[qid]):
                    raise WorkbenchError("Author no-op pixels differ", 409, "baseline_mismatch")
                board = describe_captured_scene(scene, qid)
                return {"original_pixel_sha256": digest, "objects": scene.objects,
                        "snap_points": scene.snap_points, "canvas": board,
                        "xlim": board["xlim"], "ylim": board["ylim"]}
            finally: scene.close()

    def highlight(self, qid, oid):
        if not self.is_author(qid): return super().highlight(qid, oid)
        with RENDER_LOCK:
            scene = self.scene(qid)
            try:
                if oid not in scene.artists: raise WorkbenchError("Unknown target")
                for artist in scene.artists[oid]:
                    if isinstance(artist, PathCollection):
                        artist.set_facecolor("#E11D48"); artist.set_edgecolor("#E11D48")
                    elif isinstance(artist, Patch): artist.set_edgecolor("#E11D48")
                    else: artist.set_color("#E11D48")
                scene.fig.text(.02, .98, f"REFERENCE ONLY: {qid} / {oid}", color="#E11D48", fontsize=11, va="top")
                return engine(self.branch).png_bytes(scene)
            finally: scene.close()
