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


class Ana12:
    """Sampled instance. Values are constants."""

    def __init__(self):
        self.id = 'Ana12'
        self.source_dataset = 'DynaMath'
        self.query = 'The quadratic function is given by f(x) = ax^2 + bx + c. What is the value of the constant term c?'
        self.answer = -3
        self.answer_type = 'number'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana12.png."""
        fig, ax = open_canvas()
        x = domain_linspace(-5, 6, 300, endpoint=True)
        y = 0.5 * x ** 2 - x - 3
        plot_curve(ax, x, y)
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
