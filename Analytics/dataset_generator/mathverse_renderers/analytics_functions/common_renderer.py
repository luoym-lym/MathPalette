"""Shared canvas and style for MathPalette analytic-geometry redraws.

Question renderers must draw through these helpers. Axis limits, colors,
and line widths set here are applied again at save time so a question
cannot leave a different viewport or stroke behind.
"""

from __future__ import annotations

import json
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings("ignore", category=RuntimeWarning)
from matplotlib.patches import Circle, Ellipse, Polygon
from PIL import Image

ROOT = Path(__file__).resolve().parent
PROTOCOL = json.loads((ROOT / "protocol.json").read_text(encoding="utf-8"))

VIEW = tuple(PROTOCOL["axes"]["xlim"])
CURVE_COLOR = PROTOCOL["curve"]["color"]
CURVE_WIDTH = float(PROTOCOL["curve"]["linewidth_pt"])
GRID_COLOR = PROTOCOL["grid"]["color"]
GRID_WIDTH = float(PROTOCOL["grid"]["linewidth_pt"])
POINT_AREA = float(PROTOCOL["scatter"]["area_pt2"])
POINT_EDGE_WIDTH = float(PROTOCOL["scatter"]["edge_linewidth_pt"])
REGION_FACE = PROTOCOL["region_fill"]["facecolor"]
REGION_ALPHA = float(PROTOCOL["region_fill"]["alpha"])
SLOPE_WIDTH = float(PROTOCOL["slope_segment"]["width_axes_fraction"])
FIGSIZE = tuple(PROTOCOL["figure"]["figsize_in"])
DPI = int(PROTOCOL["figure"]["dpi"])
AXES_POSITION = PROTOCOL["figure"]["axes_position"]
FONT_FAMILY = PROTOCOL["font"]["family"]
FONT_SIZE = int(PROTOCOL["font"]["size_pt"])
MARKER_CIRCLE_RADIUS = 0.3

plt.rcParams.update(
    {
        "font.family": FONT_FAMILY,
        "font.size": FONT_SIZE,
        "mathtext.fontset": PROTOCOL["font"]["mathtext_fontset"],
        "text.color": CURVE_COLOR,
        "axes.labelcolor": CURVE_COLOR,
        "axes.edgecolor": CURVE_COLOR,
        "axes.linewidth": CURVE_WIDTH,
        "axes.unicode_minus": False,
        "xtick.color": CURVE_COLOR,
        "ytick.color": CURVE_COLOR,
        "xtick.labelsize": FONT_SIZE,
        "ytick.labelsize": FONT_SIZE,
        "lines.color": CURVE_COLOR,
        "lines.linewidth": CURVE_WIDTH,
        "lines.linestyle": "-",
        "lines.marker": "None",
        "figure.dpi": DPI,
        "savefig.dpi": DPI,
        "savefig.facecolor": "#FFFFFF",
        "savefig.pad_inches": 0.0,
        "axes.formatter.useoffset": False,
    }
)


def open_canvas(xlabel=None, ylabel=None):
    """Create the 768×768 protocol figure and return (fig, ax)."""
    fig = plt.figure(figsize=FIGSIZE, dpi=DPI, facecolor="#FFFFFF")
    fig.patch.set_alpha(1.0)
    ax = fig.add_axes(AXES_POSITION, facecolor="#FFFFFF")
    _place_axis_names(fig, xlabel or PROTOCOL["axes"]["xlabel"], ylabel or PROTOCOL["axes"]["ylabel"])
    ax.grid(
        True,
        which="major",
        color=GRID_COLOR,
        linestyle="-",
        linewidth=GRID_WIDTH,
        zorder=0,
    )
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(CURVE_COLOR)
    ax.spines["bottom"].set_color(CURVE_COLOR)
    ax.spines["left"].set_linewidth(CURVE_WIDTH)
    ax.spines["bottom"].set_linewidth(CURVE_WIDTH)
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    ax.tick_params(which="major", labelsize=FONT_SIZE, width=0.8, length=3.5, colors=CURVE_COLOR)
    lock_view(ax)
    return fig, ax


def _place_axis_names(fig, xlabel, ylabel):
    """Put axis names at the positive ends so they do not follow the origin spines."""
    fig.text(
        0.948,
        0.52,
        xlabel,
        ha="left",
        va="center",
        fontsize=FONT_SIZE,
        fontname=FONT_FAMILY,
        color=CURVE_COLOR,
    )
    fig.text(
        0.52,
        0.948,
        ylabel,
        ha="center",
        va="bottom",
        fontsize=FONT_SIZE,
        fontname=FONT_FAMILY,
        color=CURVE_COLOR,
    )


def _place_origin_zero(ax):
    """One zero, sitting just to the lower right of the origin."""
    previous = getattr(ax, "_mp_origin_zero", None)
    if previous is not None:
        previous.remove()
    ax._mp_origin_zero = ax.text(
        0.22,
        -0.28,
        "0",
        ha="left",
        va="top",
        fontsize=FONT_SIZE,
        fontname=FONT_FAMILY,
        color=CURVE_COLOR,
        zorder=6,
        clip_on=False,
        bbox={"facecolor": "#FFFFFF", "edgecolor": "none", "pad": 0.05, "alpha": 0.92},
    )


def lock_view(ax):
    """Force the fixed square window. Call after any artist that may autoscale."""
    ax.set_autoscale_on(False)
    ax.set_xlim(VIEW[0], VIEW[1])
    ax.set_ylim(VIEW[0], VIEW[1])
    ticks = list(range(int(VIEW[0]), int(VIEW[1]) + 1))
    tick_labels = ["" if tick == 0 else str(tick) for tick in ticks]
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(tick_labels)
    ax.set_yticklabels(tick_labels)
    ax.minorticks_off()
    ax.set_aspect("equal", adjustable="box")
    ax.set_position(AXES_POSITION)
    for label in list(ax.get_xticklabels()) + list(ax.get_yticklabels()):
        label.set_fontname(FONT_FAMILY)
        label.set_fontsize(FONT_SIZE)
        label.set_bbox({"facecolor": "#FFFFFF", "edgecolor": "none", "pad": 0.12, "alpha": 0.92})
    _place_origin_zero(ax)


def domain_linspace(start, stop, num=200, endpoint=True):
    """Sample a 1D interval inside the fixed window.

    A symmetric plotting window that already spans at least 12 units and
    reaches ±6 is treated as an unrestricted graph and drawn on [-8, 8].
    Shorter intervals and one-sided pieces are only clipped to the window.
    """
    start = float(start)
    stop = float(stop)
    num = int(num)
    lo, hi = (start, stop) if start <= stop else (stop, start)
    span = hi - lo
    wide_symmetric = lo < 0 < hi and abs(lo) >= 6 and abs(hi) >= 6 and span >= 12
    if wide_symmetric:
        new_lo, new_hi = -8.0, 8.0
        if span > 0:
            num = max(num, int(round(num * (new_hi - new_lo) / span)))
    else:
        new_lo = max(lo, -8.0)
        new_hi = min(hi, 8.0)
        if new_hi < new_lo:
            return np.array([np.nan, np.nan])
    if stop < start:
        new_lo, new_hi = new_hi, new_lo
    num = max(num, 2)
    return np.linspace(new_lo, new_hi, num, endpoint=endpoint)


def _as_real_series(values):
    array = np.asarray(values)
    if np.iscomplexobj(array):
        real = np.real(array).astype(float)
        real[np.abs(np.imag(array)) > 1e-8] = np.nan
        return real
    real = np.asarray(array, dtype=float)
    return real


def _break_poles(y):
    """Break the stroke at non-finite samples and at sign-changing poles."""
    y = np.array(y, dtype=float, copy=True)
    y[~np.isfinite(y)] = np.nan
    if y.size < 2:
        return y
    left = y[:-1]
    right = y[1:]
    finite = np.isfinite(left) & np.isfinite(right)
    pole = finite & (np.abs(left) > 12) & (np.abs(right) > 12) & ((left * right) < 0)
    y[1:][pole] = np.nan
    return y


def plot_curve(ax, x, y):
    x_values = _as_real_series(x).reshape(-1)
    y_values = _break_poles(_as_real_series(y).reshape(-1))
    ax.plot(
        x_values,
        y_values,
        color=CURVE_COLOR,
        linestyle="-",
        linewidth=CURVE_WIDTH,
        marker=None,
        zorder=2,
        solid_capstyle="butt",
    )
    return ax


def scatter_points(ax, x, y, open_marker=False):
    if open_marker:
        ax.scatter(
            x,
            y,
            s=POINT_AREA,
            facecolors="#FFFFFF",
            edgecolors=CURVE_COLOR,
            linewidths=POINT_EDGE_WIDTH,
            zorder=4,
        )
    else:
        ax.scatter(
            x,
            y,
            s=POINT_AREA,
            c=CURVE_COLOR,
            edgecolors=CURVE_COLOR,
            linewidths=POINT_EDGE_WIDTH,
            zorder=4,
        )
    return ax


def label(ax, x, y, text, ha="center", va="center"):
    text = "" if text is None else str(text)
    kwargs = {
        "fontsize": FONT_SIZE,
        "color": CURVE_COLOR,
        "ha": ha,
        "va": va,
        "zorder": 5,
        "clip_on": False,
    }
    if "$" not in text:
        kwargs["fontname"] = FONT_FAMILY
    ax.text(x, y, text, **kwargs)
    return ax


def figure_label(fig, text):
    """Mathematical label that already belonged on the figure, not the question stem."""
    fig.text(
        0.52,
        0.978,
        "" if text is None else str(text),
        ha="center",
        va="top",
        fontsize=FONT_SIZE,
        fontname=FONT_FAMILY,
        color=CURVE_COLOR,
    )
    return fig


def aux_vline(ax, x, ymin, ymax):
    ax.vlines(
        x,
        ymin,
        ymax,
        colors=CURVE_COLOR,
        linestyles="solid",
        linewidth=CURVE_WIDTH,
        zorder=2,
    )
    return ax


def aux_hline(ax, y, xmin, xmax):
    ax.hlines(
        y,
        xmin,
        xmax,
        colors=CURVE_COLOR,
        linestyles="solid",
        linewidth=CURVE_WIDTH,
        zorder=2,
    )
    return ax


def fill_region(ax, x, y1, y2=0):
    ax.fill_between(
        np.asarray(x, dtype=float),
        _as_real_series(y1),
        _as_real_series(y2),
        facecolor=REGION_FACE,
        edgecolor="none",
        alpha=REGION_ALPHA,
        zorder=1,
    )
    return ax


def fill_polygon(ax, x, y):
    ax.fill(
        np.asarray(x, dtype=float),
        _as_real_series(y),
        facecolor=REGION_FACE,
        edgecolor="none",
        alpha=REGION_ALPHA,
        zorder=1,
    )
    return ax


def add_styled_patch(ax, patch):
    """Draw a geometric outline, or a standard point if the circle is only a marker."""
    if isinstance(patch, Circle) and float(patch.get_radius()) <= MARKER_CIRCLE_RADIUS:
        center = patch.center
        scatter_points(ax, [center[0]], [center[1]], open_marker=False)
        return ax
    patch.set_edgecolor(CURVE_COLOR)
    patch.set_linewidth(CURVE_WIDTH)
    patch.set_linestyle("-")
    patch.set_fill(False)
    patch.set_facecolor("none")
    patch.set_alpha(1.0)
    patch.set_zorder(2)
    ax.add_patch(patch)
    return ax


def slope_segments(ax, x, y, u, v, scale=60):
    u_values = _as_real_series(u)
    v_values = _as_real_series(v)
    finite = np.isfinite(u_values) & np.isfinite(v_values)
    u_values = np.where(finite, u_values, 0.0)
    v_values = np.where(finite, v_values, 0.0)
    ax.quiver(
        x,
        y,
        u_values,
        v_values,
        scale=scale,
        color=CURVE_COLOR,
        width=SLOPE_WIDTH,
        headwidth=0,
        headlength=0,
        headaxislength=0,
        zorder=2,
    )
    return ax


def build_expression(coefficients, variables):
    """Piecewise-title helper copied from the source generator."""
    terms = []
    for coeff, var in zip(coefficients, variables):
        if coeff == 0:
            continue
        sign = "+" if coeff > 0 else "-"
        abs_coeff = abs(coeff)
        if abs_coeff == 1 and var != "":
            term = f"{var}"
        else:
            term = f"{abs_coeff}{var}"
        if terms:
            term = f"{sign} {term}"
        elif coeff < 0:
            term = f"-{term}"
        terms.append(term)
    return " ".join(terms) if terms else "0"


def _collection_points(collection):
    """Data coordinates for lines, markers, fills, and slope-field bases."""
    offsets = np.asarray(collection.get_offsets())
    real_offsets = (
        offsets.ndim == 2
        and offsets.shape[-1] == 2
        and offsets.shape[0] >= 1
        and not (offsets.shape[0] == 1 and np.allclose(offsets, 0))
    )
    chunks = []
    if real_offsets:
        chunks.append(offsets)
    for path in collection.get_paths():
        vertices = np.asarray(path.vertices, dtype=float)
        if vertices.ndim != 2 or vertices.shape[1] != 2 or len(vertices) < 2:
            continue
        # Scatter markers are unit paths; their data location is in the offsets.
        if real_offsets and np.max(np.abs(vertices)) <= 0.55:
            continue
        chunks.append(vertices)
    return chunks


def _finite_points(array):
    points = np.asarray(array, dtype=float)
    if points.size == 0:
        return np.empty((0, 2))
    if points.ndim == 1:
        return np.empty((0, 2))
    if points.shape[-1] != 2:
        return np.empty((0, 2))
    points = points.reshape(-1, 2)
    mask = np.isfinite(points).all(axis=1)
    return points[mask]


def measure_content(ax):
    """Return whether any geometry falls outside the window or none falls inside."""
    chunks = []
    for line in ax.lines:
        xdata = np.asarray(line.get_xdata(), dtype=float).reshape(-1)
        ydata = np.asarray(line.get_ydata(), dtype=float).reshape(-1)
        count = min(xdata.size, ydata.size)
        if count:
            chunks.append(np.column_stack([xdata[:count], ydata[:count]]))
    for collection in ax.collections:
        chunks.extend(_collection_points(collection))
    for patch in ax.patches:
        vertices = patch.get_path().transformed(patch.get_patch_transform()).vertices
        chunks.append(vertices)
    points = np.vstack([_finite_points(chunk) for chunk in chunks]) if chunks else np.empty((0, 2))
    if points.size == 0:
        return {"clipped_content": False, "out_of_view": True, "finite_points": 0}
    outside = (
        (points[:, 0] < VIEW[0] - 1e-6)
        | (points[:, 0] > VIEW[1] + 1e-6)
        | (points[:, 1] < VIEW[0] - 1e-6)
        | (points[:, 1] > VIEW[1] + 1e-6)
    )
    inside = (
        (points[:, 0] >= VIEW[0] - 1e-6)
        & (points[:, 0] <= VIEW[1] + 1e-6)
        & (points[:, 1] >= VIEW[0] - 1e-6)
        & (points[:, 1] <= VIEW[1] + 1e-6)
    )
    return {
        "clipped_content": bool(outside.any()),
        "out_of_view": not bool(inside.any()),
        "finite_points": int(points.shape[0]),
    }


def finalize(fig, output_path):
    """Lock the protocol window, save, and report pixel size plus clipping."""
    if not fig.axes:
        raise RuntimeError("figure has no axes")
    ax = fig.axes[0]
    lock_view(ax)
    content = measure_content(ax)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=DPI, facecolor="#FFFFFF")
    plt.close(fig)
    with Image.open(output_path) as image:
        width, height = image.size
    if (width, height) != (768, 768):
        raise RuntimeError(f"{output_path.name} is {width}x{height}, expected 768x768")
    content["width_px"] = width
    content["height_px"] = height
    return content
