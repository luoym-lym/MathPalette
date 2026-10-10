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

class Ana02:
    """Sampled instance of source question Q89. Values are constants."""

    def __init__(self):
        self.id = 'Ana02'
        self.source_id = 'Q89'
        self.a = 1.9
        self.b = 1.5
        self.c = 0.0
        self.d = -0.4
        self.query = 'The function value f(1) is ____ f(-1) choice: (A) smaller than (B) larger than (C) equal to'
        self.answer = 'B'
        self.answer_type = 'multiple choice'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana02.png."""
        fig, ax = open_canvas()
        constant_a = self.a
        constant_b = self.b
        constant_c = self.c
        constant_d = self.d
        x = domain_linspace(-10, 10, 200, endpoint=True)
        cubic = constant_a * x ** 3 + constant_b * x ** 2 + constant_c * x + constant_d
        plot_curve(ax, x, cubic)
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
