"""Frozen-coordinate adapter for MathVerse analytic graph redraws.

MathVerse source graphs use several numerical windows.  Each question freezes
one affine map from source coordinates into the standard [-8, 8] display box;
tick locations are mapped by the same transform and retain their source labels.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from PIL import Image

from common_renderer import (  # noqa: F401
    open_canvas, plot_curve, scatter_points, label, aux_hline, aux_vline,
    add_styled_patch, fill_region, fill_polygon, figure_label,
)

DISPLAY = (-8.0, 8.0)
_VIEWS = {}


def set_view(ax, *, center, scale, x_ticks, y_ticks, xlabel="x", ylabel="y",
             x_label_step=1, y_label_step=1, x_grid_step=1, y_grid_step=1,
             grid=True, y_axis=True, x_axis=True, origin_label=True,
             xlabel_position=None, xlabel_rotation=0):
    """Freeze a uniform affine display map; ``scale`` is displayed units/source unit."""
    sx, sy = (float(scale), float(scale)) if isinstance(scale, (int, float)) else (float(scale[0]), float(scale[1]))
    _VIEWS[id(ax)] = (tuple(center), sx, sy, tuple(x_ticks), tuple(y_ticks), xlabel, ylabel,
                      x_label_step, y_label_step, x_grid_step, y_grid_step, grid, y_axis, x_axis, origin_label,
                      xlabel_position, xlabel_rotation)


def map_point(x, y, center, scale):
    sx, sy = (scale, scale) if isinstance(scale, (int, float)) else scale
    return (float(x) - center[0]) * sx, (float(y) - center[1]) * sy


def lock_view(ax):
    center, sx, sy, x_ticks, y_ticks, xlabel, ylabel, x_label_step, y_label_step, x_grid_step, y_grid_step, grid, y_axis, x_axis, origin_label, xlabel_position, xlabel_rotation = _VIEWS[id(ax)]
    ax.set_autoscale_on(False)
    ax.set_xlim(DISPLAY)
    ax.set_ylim(DISPLAY)
    ax.set_aspect("equal", adjustable="box")
    x_major = [x for x in x_ticks if x % x_grid_step == 0]
    y_major = [y for y in y_ticks if y % y_grid_step == 0]
    x_minor = [x for x in x_ticks if x not in x_major]
    y_minor = [y for y in y_ticks if y not in y_major]
    ax.set_xticks([(x-center[0])*sx for x in x_major])
    ax.set_xticklabels([str(x) if x and x % x_label_step == 0 else "" for x in x_major])
    ax.set_xticks([(x-center[0])*sx for x in x_minor], minor=True)
    if y_axis:
        ax.set_yticks([(y-center[1])*sy for y in y_major])
        ax.set_yticklabels([str(y) if y and y % y_label_step == 0 else "" for y in y_major])
        ax.set_yticks([(y-center[1])*sy for y in y_minor], minor=True)
    else:
        ax.set_yticks([])
    ax.set_axisbelow(True)
    if grid:
        ax.grid(True, which="major", color="#E0E0E0", linestyle="-", linewidth=0.5, zorder=0)
    else:
        ax.grid(False, which="both")
    if not y_axis:
        ax.grid(False, axis="y", which="both")
    ax.spines["left"].set_position(("data", (0-center[0])*sx))
    ax.spines["bottom"].set_position(("data", (0-center[1])*sy))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    if not y_axis:
        ax.spines["left"].set_visible(False)
    if not x_axis:
        ax.spines["bottom"].set_visible(False)
    ax.tick_params(which="major", labelsize=12, width=0.8, length=3.5, colors="black")
    ax.tick_params(which="minor", labelsize=12, width=0.8, length=2.0, colors="black")
    for tick in list(ax.get_xticklabels()) + list(ax.get_yticklabels()):
        tick.set_fontname("DejaVu Sans")
        tick.set_fontsize(12)
        tick.set_bbox({"facecolor": "#FFFFFF", "edgecolor": "none", "pad": 0.12, "alpha": 0.92})
    # The zero tick is intentionally blank on both axes; show it once at origin.
    ox, oy = -center[0]*sx, -center[1]*sy
    zero = getattr(ax, "_mp_origin_zero", None)
    if zero is not None:
        zero.set_position((ox+0.22, oy-0.28))
        zero.set_visible(bool(y_axis and origin_label))
        zero.set_text("0")
    # open_canvas places axis names as figure-level text. Replace those names
    # idempotently so mapped tick axes do not retain duplicate x/y labels.
    fig = ax.figure
    for text in list(fig.texts):
        text.remove()
    ax.set_xlabel(""); ax.set_ylabel("")
    if xlabel:
        xpos = xlabel_position or (0.948, 0.52)
        fig.text(xpos[0], xpos[1], xlabel, ha="left", va="center", rotation=xlabel_rotation, fontsize=12, fontname="DejaVu Sans", color="black")
    if ylabel:
        fig.text(0.52, 0.948, ylabel, ha="center", va="bottom", fontsize=12, fontname="DejaVu Sans", color="black")
    return ax


def finalize(fig, output_path):
    """Save with the shared 768px canvas while preserving this module's mapping."""
    if not fig.axes:
        raise RuntimeError("figure has no axes")
    lock_view(fig.axes[0])
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destination, dpi=100, facecolor="#FFFFFF")
    plt.close(fig)
    with Image.open(destination) as image:
        if image.size != (768, 768):
            raise RuntimeError(f"{destination.name} is {image.size}, expected 768x768")
    return {"width_px": 768, "height_px": 768, "coordinate_mapping": "question-frozen affine"}
