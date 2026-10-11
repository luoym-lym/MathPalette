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

class Ana03:
    """Sampled instance from DynaMath. Values are constants."""

    def __init__(self):
        self.id = 'Ana03'
        self.source_dataset = 'DynaMath'
        self.a = -2
        self.b = 1
        self.c = 2
        self.query = 'Part of the graph of f(x) = x^3 + bx^2 + cx + d is shown. What is b?'
        self.answer = -1
        self.answer_type = 'number'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana03.png."""
        fig, ax = open_canvas()
        x = domain_linspace(-10, 10, 200, endpoint=True)
        cubic = x ** 3 - (self.a + self.b + self.c) * x ** 2 + (self.a * self.b + self.c * self.b + self.a * self.c) * x - self.a * self.b * self.c
        plot_curve(ax, x, cubic)
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
