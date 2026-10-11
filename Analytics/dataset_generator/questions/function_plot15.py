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


class Ana15:
    """Sampled instance. Values are constants."""

    def __init__(self):
        self.id = 'Ana15'
        self.source_dataset = 'DynaMath'
        self.query = 'Two sinusoidal functions y_1 and y_2 are plotted. Find the ratio of their amplitudes, \\frac{A(y_1)}{A(y_2)}.'
        self.answer = 2
        self.answer_type = 'number'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana15.png."""
        fig, ax = open_canvas()
        x = domain_linspace(-2 * np.pi, 2 * np.pi, 300, endpoint=True)
        y1 = 4.0 * np.cos(x)
        y2 = 2.0 * np.sin(x)
        plot_curve(ax, x, y1)
        plot_curve(ax, x, y2)
        label(ax, 0.4, 4.4, "y1", ha="left", va="bottom")
        label(ax, np.pi / 2 + 0.4, 2.4, "y2", ha="left", va="bottom")
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
