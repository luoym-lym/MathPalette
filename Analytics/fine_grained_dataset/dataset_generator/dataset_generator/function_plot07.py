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


class Ana07:
    """Sampled instance. Values are constants."""

    def __init__(self):
        self.id = 'Ana07'
        self.source_dataset = 'DynaMath'
        self.query = 'At what value of x in the interval [-6, 6] does the function f(x) fail to be continuous?'
        self.answer = -1
        self.answer_type = 'integer'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana07.png."""
        fig, ax = open_canvas()
        x1 = domain_linspace(-8, -1, 200, endpoint=True)
        x2 = domain_linspace(-1, 8, 200, endpoint=True)
        f1 = x1 + 4
        f2 = -0.5 * (x2 - 1) ** 2 - 1
        plot_curve(ax, x1, f1)
        plot_curve(ax, x2, f2)
        scatter_points(ax, -1, 3, open_marker=True)
        scatter_points(ax, -1, -3, open_marker=False)
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
