"""Frozen analytic-geometry questions.

Each class is one sampled instance. Numbers in __init__ are constants from
that sample. draw() does not choose parameters.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

_ROOT = Path(__file__).resolve().parents[1]
_DATASET_ROOT = _ROOT.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from common_renderer import (  # noqa: E402
    add_styled_patch,
    aux_hline,
    aux_vline,
    build_expression,
    domain_linspace,
    figure_label,
    fill_polygon,
    fill_region,
    finalize,
    label,
    open_canvas,
    plot_curve,
    scatter_points,
    slope_segments,
)


class Ana06:
    """Sampled instance. Values are constants."""

    def __init__(self):
        self.id = 'Ana06'
        self.source_dataset = 'DynaMath'
        self.query = 'The graph depicts a piecewise-defined function f(x). Find the value of the right-hand limit \\lim_{x \\to 2^+} f(x).'
        self.answer = 4
        self.answer_type = 'integer'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana06.png."""
        fig, ax = open_canvas()
        x1 = domain_linspace(-8, 2, 200, endpoint=True)
        x2 = domain_linspace(2, 8, 200, endpoint=True)
        f1 = 0.5 * x1 ** 2 - 1
        f2 = -x2 + 6
        plot_curve(ax, x1, f1)
        plot_curve(ax, x2, f2)
        scatter_points(ax, 2, 1, open_marker=False)
        scatter_points(ax, 2, 4, open_marker=True)
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
