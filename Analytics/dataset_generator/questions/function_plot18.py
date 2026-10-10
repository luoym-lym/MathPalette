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


class Ana18:
    """Sampled instance. Values are constants."""

    def __init__(self):
        self.id = 'Ana18'
        self.source_dataset = 'DynaMath'
        self.query = 'The parabola g(x) is obtained by translating the parent parabola f(x) = x^2. What are the coordinates of the vertex of g(x)? Please answer in the format (x, y).'
        self.answer = '(-3, -2)'
        self.answer_type = 'text'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana18.png."""
        fig, ax = open_canvas()
        x = domain_linspace(-7, 5, 300, endpoint=True)
        f = x ** 2
        g = (x + 3.0) ** 2 - 2.0
        plot_curve(ax, x, f)
        plot_curve(ax, x, g)
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
