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


class Ana16:
    """Sampled instance. Values are constants."""

    def __init__(self):
        self.id = 'Ana16'
        self.source_dataset = 'DynaMath'
        self.query = 'How many intersection points do the two curves y_1 and y_2 have in the interval [0, 2\\pi]?'
        self.answer = 2
        self.answer_type = 'number'
        self.subject = 'analytic geometry'
        self.level = 'high school'

    def draw(self, num=0, output_path=None):
        """Draw this instance. The image is image/Ana16.png."""
        fig, ax = open_canvas()
        x = domain_linspace(0, 2 * np.pi, 300, endpoint=True)
        y1 = 2.5 * np.cos(x)
        y2 = 2.5 * np.sin(x)
        plot_curve(ax, x, y1)
        plot_curve(ax, x, y2)
        label(ax, 0.3, 2.8, "y1", ha="left", va="bottom")
        label(ax, 2.2, 2.8, "y2", ha="left", va="bottom")
        destination = Path(output_path) if output_path is not None else _DATASET_ROOT / "image" / f"{self.id}.png"
        return finalize(fig, destination)
