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


class Ana13:
    """Sampled instance. Values are constants."""

    def __init__(self):
        self.id = 'Ana13'
        self.source_dataset = 'DynaMath'
        self.query = 'The rational function is of the form f(x) = \\frac{k}{x - p} + q. What is the value of the vertical asymptote parameter p?'
        self.answer = 3
        self.answer_type = 'integer'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana13.png."""
        fig, ax = open_canvas()
        x1 = domain_linspace(-8, 2.65, 200, endpoint=True)
        x2 = domain_linspace(3.35, 8, 200, endpoint=True)
        f1 = 2.0 / (x1 - 3.0) + 1.0
        f2 = 2.0 / (x2 - 3.0) + 1.0
        plot_curve(ax, x1, f1)
        plot_curve(ax, x2, f2)
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
