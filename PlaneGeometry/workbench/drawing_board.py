"""Browser drawing helpers; all final images still use the frozen C renderer."""
from __future__ import annotations

import copy

import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import to_hex
from matplotlib.path import Path

from renderer_adapter import RENDER_LOCK


# Geometry annotation presets are fixed by the confirmed workbench requirements.
PRESETS = {
    "point": {"type": "add_point", "filled": True, "color": "#DC2626",
              "size_pt2": 50, "edge_linewidth_pt": 1.0},
    "line": {"type": "add_line", "color": "#2563EB", "linestyle": "dashed",
             "linewidth_pt": 1.0, "dash_pattern_pt": [3.7, 1.6]},
    "colors": ["#DC2626", "#2563EB", "#16A34A", "#EA580C"],
    "object_colors": ["#DC2626", "#2563EB", "#16A34A", "#EA580C", "#000000"],
}


def _pixel_paths(path, transform, width, height):
    """Flatten real artist paths, including Bézier outlines, into image pixels.

    Keep MOVETO breaks and clip huge/out-of-view segments before exporting;
    neither a NaN break nor a gap between separate paths becomes clickable.
    """
    pixel_path = path.transformed(transform)
    paths, current = [], []
    for vertices, code in pixel_path.iter_segments(
            remove_nans=True, clip=(0, 0, width, height), simplify=False, curves=False):
        if code == Path.MOVETO:
            if len(current) > 1:
                paths.append(current)
            current = [[float(vertices[0]), float(height - vertices[1])]]
        elif code == Path.LINETO:
            current.append([float(vertices[0]), float(height - vertices[1])])
        elif code == Path.CLOSEPOLY and current:
            current.append(current[0][:])
    if len(current) > 1:
        paths.append(current)
    return paths


def describe_scene(adapter, qid):
    """Use Matplotlib's actual transforms, not the UI thumbnail dimensions."""
    with RENDER_LOCK:
        scene = adapter.scene(qid)
        try:
            return describe_captured_scene(scene, qid)
        finally:
            scene.close()


def describe_captured_scene(scene, qid):
    scene.fig.set_dpi(100)
    scene.fig.canvas.draw()
    width, height = scene.fig.canvas.get_width_height()
    bbox = scene.ax.get_window_extent()
    targets = []
    for obj in scene.objects:
        if not obj["styleable"]:
            continue
        paths, styles = [], []
        for artist in scene.artists[obj["id"]]:
                if isinstance(artist, LineCollection):
                    source_paths = [Path(segment) for segment in artist.get_segments()]
                    color = to_hex(artist.get_colors()[0]).upper()
                    linewidth = float(artist.get_linewidths()[0])
                    dashed = artist.get_linestyles()[0][1] is not None
                else:
                    source_paths = [artist.get_path()]
                    color = to_hex(artist.get_color() if hasattr(artist, "get_color")
                                   else artist.get_edgecolor()).upper()
                    linewidth = float(artist.get_linewidth())
                    dashed = artist.get_linestyle() not in ("-", "solid", "None", "none", "")
                paths.extend(points for path in source_paths
                             for points in _pixel_paths(path, artist.get_transform(), width, height))
                styles.append({"color": color, "linewidth_pt": linewidth,
                               "linestyle": "dashed" if dashed else "solid"})
        targets.append({"id": obj["id"], "kind": obj["kind"], "paths": paths,
                        "source_call": obj["source_call"], **styles[0], "fragment_styles": styles})
    # The actual affine transforms account for the frozen viewport and equal aspect.
    transform = scene.ax.transData.get_affine().get_matrix()
    flip = np.array([[1, 0, 0], [0, -1, height], [0, 0, 1]])
    forward = flip @ transform
    points = [{**copy.deepcopy(point), "pixel": (forward @ [*point["xy"], 1])[:2].tolist()}
              for point in scene.snap_points]
    return {"question_id": qid, "branch": "PlaneGeometry", "width": width, "height": height,
            "plot_bounds": [float(bbox.x0), float(height - bbox.y1), float(bbox.x1), float(height - bbox.y0)],
            "data_to_pixel": forward.tolist(), "pixel_to_data": np.linalg.inv(forward).tolist(),
            "xlim": [float(x) for x in scene.ax.get_xlim()], "ylim": [float(y) for y in scene.ax.get_ylim()],
            "targets": targets, "snap_points": points, "presets": copy.deepcopy(PRESETS)}
