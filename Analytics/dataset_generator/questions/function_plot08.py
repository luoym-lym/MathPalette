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


class Ana08:
    """Sampled instance. Values are constants."""

    def __init__(self):
        self.id = 'Ana08'
        self.source_dataset = 'DynaMath'
        self.query = 'Based on the graph of the function f(x), compute the arithmetic value of f(0) - \\lim_{x \\to 0^+} f(x).'
        self.answer = 3
        self.answer_type = 'number'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana08.png."""
        fig, ax = open_canvas()
        x1 = domain_linspace(-8, 0, 200, endpoint=True)
        x2 = domain_linspace(0, 8, 200, endpoint=True)
        f1 = np.full_like(x1, 2.0)
        f2 = x2 - 1.0
        plot_curve(ax, x1, f1)
        plot_curve(ax, x2, f2)
        scatter_points(ax, 0, 2, open_marker=False)
        scatter_points(ax, 0, -1, open_marker=True)
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
