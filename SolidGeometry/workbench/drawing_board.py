"""Browser drawing helpers; all final images still use the frozen C renderer."""
from __future__ import annotations

import copy

import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import to_hex
from matplotlib.path import Path

from renderer_adapter import RENDER_LOCK


# Annotation-only additions; the original solid renderer stays frozen.
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
            scene.fig.set_dpi(100)
            scene.fig.canvas.draw()
            width, height = scene.fig.canvas.get_width_height()
            bbox = scene.ax.get_window_extent()
            targets = []
            for obj in scene.objects:
                if not obj["styleable"]:
                    continue
                owned = scene.artists[obj["id"]]
                paths, styles = [], []
                for artist in owned:
                    paths.extend(_pixel_paths(artist.get_path(), artist.get_transform(), width, height))
                    styles.append("dashed" if artist.is_dashed() else "solid")
                color = to_hex(owned[0].get_color()).upper()
                linewidth = float(owned[0].get_linewidth())
                targets.append({"id": obj["id"], "kind": obj["kind"], "paths": paths,
                                "source_call": obj["source_call"], "color": color,
                                "linewidth_pt": linewidth,
                                "linestyle": styles[0] if len(set(styles)) == 1 else "mixed",
                                "fragment_linestyles": styles,
                                "frozen_visibility": obj["frozen_visibility"]})
            # Store both directions so JS handles resizing without rounding away precision.
            transform = scene.ax.transData.get_affine().get_matrix()
            flip = np.array([[1, 0, 0], [0, -1, height], [0, 0, 1]])
            forward = flip @ transform
            return {"question_id": qid, "width": width, "height": height,
                    "plot_bounds": [float(bbox.x0), float(height - bbox.y1),
                                    float(bbox.x1), float(height - bbox.y0)],
                    "data_to_pixel": forward.tolist(), "pixel_to_data": np.linalg.inv(forward).tolist(),
                    "xlim": list(scene.ax.get_xlim()), "ylim": list(scene.ax.get_ylim()),
                    "targets": targets, "presets": copy.deepcopy(PRESETS),
                    "coordinate_system": "frozen_projected_2d", "branch": "SolidGeometry",
                    "snap_points": [{**copy.deepcopy(p), "pixel": (forward @ [*p["xy"], 1])[:2].tolist()}
                                    for p in scene.snap_points]}
        finally:
            scene.close()
