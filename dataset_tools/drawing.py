"""Small, source-independent drawing API. Unified frozen rendering protocol.

Question classes own geometry and construction. This module owns the canvas,
default appearance, basic artists, projection, and PNG/SVG output only.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import io

import matplotlib
matplotlib.use("Agg")
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from matplotlib.path import Path as VectorPath
from matplotlib.transforms import Affine2D as VectorTransform
from matplotlib.transforms import Bbox as VectorBox
from matplotlib.patches import Arc, Circle, PathPatch, Polygon
from matplotlib.collections import LineCollection, PolyCollection
import numpy as np
from PIL import Image


@dataclass(frozen=True)
class Protocol:
    name: str
    font_size: int
    axes_position: tuple
    coordinate_axes: bool = False


ANALYTICS = Protocol("Analytics", 12, (.12, .12, .80, .80), True)
PLANE = Protocol("PlaneGeometry", 16, (.05, .05, .90, .90))
SOLID = Protocol("SolidGeometry", 16, (.05, .05, .90, .90))
PROTOCOL_VERSION = "2.0.0"


class Canvas:
    """One protocol canvas. Use as a context manager to isolate Matplotlib state."""

    def __init__(self, protocol, *, xlim=(-8, 8), ylim=(-8, 8),
                 projection=None, origin=(0, 0, 0), offset=(0, 0),
                 xlabel="x", ylabel="y", axes_position=None, coordinate_axes=None):
        limits = np.asarray([xlim, ylim], dtype=float)
        if limits.shape != (2, 2) or not np.isfinite(limits).all():
            raise ValueError("Finite x/y limits required")
        spans = np.diff(limits, axis=1).ravel()
        if np.any(spans <= 0) or not np.isclose(*spans, rtol=1e-10, atol=1e-10):
            raise ValueError("The fixed viewport must be square")
        self.protocol = protocol
        self.projection = None if projection is None else np.asarray(projection, dtype=float)
        self.origin, self.offset = np.asarray(origin, dtype=float), np.asarray(offset, dtype=float)
        if self.projection is not None and (self.projection.shape != (2, 3)
                or not np.isfinite(self.projection).all() or np.linalg.matrix_rank(self.projection) != 2):
            raise ValueError("A finite rank-two 2x3 projection is required")
        if (self.origin.shape != (3,) or self.offset.shape != (2,)
                or not np.isfinite(self.origin).all() or not np.isfinite(self.offset).all()):
            raise ValueError("Invalid projection origin/offset")
        settings = {**matplotlib.rcParamsDefault, "backend": "Agg",
                    "font.family": "DejaVu Sans", "font.size": protocol.font_size,
                    "mathtext.fontset": "dejavusans", "lines.scale_dashes": False,
                    "path.simplify": protocol.coordinate_axes, "svg.fonttype": "path",
                    "svg.hashsalt": "MathPalette.unified.2",
                    "savefig.bbox": None, "savefig.transparent": False}
        if protocol.coordinate_axes:
            settings["axes.unicode_minus"] = False
        self._context = matplotlib.rc_context(settings)
        self.settings = settings.copy()
        self._context.__enter__()
        try:
            self.fig = Figure(figsize=(7.68, 7.68), dpi=100, facecolor="white")
            FigureCanvasAgg(self.fig)
            self.ax = self.fig.add_axes(axes_position or protocol.axes_position, facecolor="white")
            self.ax.set(xlim=xlim, ylim=ylim, aspect="equal")
            self.ax.set_autoscale_on(False)
            self.artists = {}
            if protocol.coordinate_axes if coordinate_axes is None else coordinate_axes:
                self._coordinate_axes(xlim, ylim, xlabel, ylabel)
            else:
                self.ax.set_axis_off()
            self.fig.canvas.draw()
        except BaseException:
            self._context.__exit__(None, None, None)
            raise

    def __enter__(self):
        return self

    def __exit__(self, *error):
        self._context.__exit__(*error)

    def _coordinate_axes(self, xlim, ylim, xlabel, ylabel):
        ax = self.ax
        ax.grid(True, which="major", color="#E0E0E0", linestyle="-", linewidth=.5, zorder=0)
        ax.set_axisbelow(True)
        for side in ("top", "right"):
            ax.spines[side].set_visible(False)
        for side in ("left", "bottom"):
            ax.spines[side].set(position=("data", 0), color="black", linewidth=1)
        ax.xaxis.set_ticks_position("bottom")
        ax.yaxis.set_ticks_position("left")
        ax.tick_params(which="major", labelsize=12, width=.8, length=3.5, colors="black")
        for axis, limits in ((ax.xaxis, xlim), (ax.yaxis, ylim)):
            ticks = np.arange(np.ceil(limits[0]), np.floor(limits[1]) + 1)
            axis.set_ticks(ticks)
            axis.set_ticklabels(["" if t == 0 else str(int(t)) for t in ticks])
            for label in axis.get_ticklabels():
                label.set_bbox({"facecolor": "white", "edgecolor": "none", "pad": .12, "alpha": .92})
        ax.minorticks_off()
        ax.text(.22, -.28, "0", ha="left", va="top", fontsize=12,
                color="black", zorder=6, clip_on=False,
                bbox={"facecolor": "white", "edgecolor": "none", "pad": .05, "alpha": .92})
        self.fig.text(.948, .52, xlabel, ha="left", va="center", fontsize=12, color="black")
        self.fig.text(.52, .948, ylabel, ha="center", va="bottom", fontsize=12, color="black")

    def project(self, xyz):
        if self.projection is None:
            raise ValueError("This canvas has no 3D projection")
        points = np.asarray(xyz, dtype=float)
        if points.ndim == 0 or points.shape[-1] != 3 or not np.isfinite(points).all():
            raise ValueError("Finite 3D coordinates required")
        return (self.projection @ (points - self.origin).T).T + self.offset

    def _register(self, artist, id):
        if id is not None:
            artist.set_gid(id)
            self.artists.setdefault(id, []).append(artist)
        return artist

    def line(self, points, *, id=None, simplify=None, **style):
        points = np.asarray(points, dtype=float)
        if points.ndim == 3 and points.shape[-1] == 2:
            defaults = {"colors": "black", "linewidths": 1, "zorder": 2}
            defaults.update(style)
            artist = LineCollection(points, **defaults)
            self.ax.add_collection(artist)
            return self._register(artist, id)
        if points.ndim != 2 or points.shape[1] != 2 or len(points) < 1:
            raise ValueError("A line/marker needs 2D points")
        defaults = {"color": "black", "linewidth": 1, "linestyle": "solid",
                    "solid_capstyle": "round", "dash_capstyle": "butt",
                    "antialiased": True, "marker": None, "zorder": 2}
        defaults.update(style)
        artist = self.ax.plot(*points.T, **defaults)[0]
        if simplify is not None:
            artist.get_path().should_simplify = simplify
        return self._register(artist, id)

    def point(self, points, *, id=None, filled=True, **style):
        points = np.asarray(points, dtype=float).reshape(-1, 2)
        defaults = {"s": 36, "facecolors": "black" if filled else "white",
                    "edgecolors": "black", "linewidths": 1, "zorder": 4,
                    "marker": "o", "antialiaseds": True}
        defaults.update(style)
        return self._register(self.ax.scatter(*points.T, **defaults), id)

    def path(self, vertices, codes, *, id=None, simplify=None, coordinates="data", **style):
        defaults = {"facecolor": "none", "edgecolor": "black", "linewidth": 1,
                    "capstyle": "round", "antialiased": True, "zorder": 2}
        defaults.update(style)
        if coordinates == "pixels":
            defaults["transform"] = VectorTransform().scale(.01) + self.fig.dpi_scale_trans
        elif coordinates != "data":
            raise ValueError("Path coordinates must be data or pixels")
        path = VectorPath(vertices, codes)
        if simplify is not None:
            path.should_simplify = simplify
        artist = PathPatch(path, **defaults)
        self.ax.add_patch(artist)
        return self._register(artist, id)

    def circle(self, center, radius, *, id=None, simplify=None, **style):
        defaults = {"facecolor": "none", "edgecolor": "black", "linewidth": 1,
                    "antialiased": True, "zorder": 2}
        defaults.update(style)
        artist = Circle(center, radius, **defaults)
        self.ax.add_patch(artist)
        return self._register(artist, id)

    def arc(self, center, radius, start, end, *, radius_pt=False, id=None, **style):
        if radius_pt:
            radius *= np.ptp(self.ax.get_xlim()) / self.ax.bbox.width * self.fig.dpi / 72
        defaults = {"edgecolor": "black", "linewidth": 1, "zorder": 3}
        defaults.update(style)
        artist = Arc(center, 2 * radius, 2 * radius, theta1=start, theta2=end, **defaults)
        self.ax.add_patch(artist)
        return self._register(artist, id)

    def fill(self, points, *, id=None, **style):
        defaults = {"facecolor": "#D0D0D0", "edgecolor": "none", "alpha": .45, "zorder": 1}
        defaults.update(style)
        if isinstance(points[0][0], (list, tuple, np.ndarray)):
            artist = PolyCollection(points, **defaults)
            self.ax.add_collection(artist)
        else:
            artist = Polygon(points, closed=True, **defaults)
            self.ax.add_patch(artist)
        return self._register(artist, id)

    def text(self, text, xy, *, offset_pt=None, vertex=False, id=None, coordinates="data", **style):
        defaults = {"fontfamily": "DejaVu Sans", "fontsize": 18 if vertex else self.protocol.font_size,
                    "fontstyle": "italic" if vertex else "normal", "color": "black",
                    "ha": "center", "va": "center", "zorder": 5, "clip_on": False}
        defaults.update(style)
        if coordinates == "figure":
            artist = self.fig.text(*xy, text, **defaults)
        elif coordinates != "data":
            raise ValueError("Text coordinates must be data or figure")
        elif offset_pt is None:
            artist = self.ax.text(*xy, text, **defaults)
        else:
            artist = self.ax.annotate(text, xy=xy, xytext=offset_pt, textcoords="offset points", **defaults)
        return self._register(artist, id)

    def save(self, output_path):
        target = Path(output_path).resolve()
        if target.suffix.lower() not in (".png", ".svg"):
            raise ValueError("Output must be PNG or SVG")
        project = next((p for p in Path(__file__).resolve().parents if (p / "MATHPALETTE_PROTOCOL.md").is_file()), None)
        if project is not None and target.is_relative_to(project) and not target.is_relative_to(project / ".runtime"):
            raise ValueError("Redraw output must be outside formal source directories")
        stream = io.BytesIO()
        vector = target.suffix.lower() == ".svg"
        self.fig.savefig(stream, format="svg" if vector else "png", dpi=100,
                         facecolor="white", transparent=False, bbox_inches=None, pad_inches=0,
                         metadata={"Date": None} if vector else {})
        data = stream.getvalue()
        if not vector:
            with Image.open(io.BytesIO(data)) as image:
                if image.size != (768, 768) or image.convert("RGBA").getextrema()[3] != (255, 255):
                    raise ValueError("Output must be an opaque 768x768 PNG")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        return str(target)
