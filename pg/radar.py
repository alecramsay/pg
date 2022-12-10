#!/usr/bin/env python3

"""
PLOT RADAR DIAGRAMS
"""

import chart_studio.plotly as py
import plotly.graph_objs as go  # https://plotly.com/python-api-reference/plotly.graph_objects.html

from .datatypes import *
from .data import *
from .helpers import *


def plot_radar_diagram(current: Plan, compare: Plan, plot_path: str) -> None:
    """
    https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html
    https://plotly.com/python/static-image-export/
    """

    size: int = 500
    bgcolor: str = "#fafafa"

    traces: list = []
    theta: list[str] = [
        "Proportionality",
        "Competitiveness",
        "Minority",
        "Compactness",
        "Splitting",
    ]
    theta += theta[:1]  # close the polygon

    # Current trace

    current_r: list[int] = [x for x in list(current.ratings)]
    current_r += current_r[:1]  # close the polygon
    current_positions: list[str] = text_position(current_r, 80)

    current_trace: py.Scatterpolar = go.Scatterpolar(
        name=current.name,
        mode="lines+markers+text",
        r=current_r,
        theta=theta,
        fill="toself",
        text=current_r,
        textposition=current_positions,
        fillcolor="rgba(44, 160, 44, 0.75)",
        marker=dict(color="black"),
        line=dict(color="black"),
    )

    # Compare trace

    compare_r: list[int] = [x for x in list(compare.ratings)]
    compare_r += compare_r[:1]  # close the polygon
    compare_positions: list[str] = text_position(compare_r, 80)

    compare_trace: py.Scatterpolar = go.Scatterpolar(
        name=compare.name,
        mode="lines+markers+text",
        r=compare_r,
        theta=theta,
        text="",  # Suppress the ratings -- compare_r,
        # textposition=compare_positions,
        fill="toself",
        fillcolor="rgba(255, 127, 14, 0.5)",
        marker=dict(color="#1f77b4"),
        line=dict(color="#1f77b4"),
    )

    traces.append(compare_trace)
    traces.append(current_trace)

    title: str = qualify_label(current.nickname)
    font_size: int = 16
    title_x: float = 0.5  # center

    layout: py.Layout = go.Layout(
        title=dict(text=title, x=title_x, font_size=font_size),
        polar=dict(
            bgcolor=bgcolor,
            angularaxis=dict(
                linewidth=1,
                linecolor="black",
                gridcolor="lightgrey",
                gridwidth=1,
                layer="below traces",
            ),
            radialaxis=dict(
                visible=True,
                gridcolor="lightgrey",
                gridwidth=1,
                range=[0, 100],
                showticklabels=False,
                layer="below traces",
            ),
        ),
        width=size,
        height=size,
        showlegend=False,
        paper_bgcolor=bgcolor,
        plot_bgcolor=bgcolor,
    )

    fig: py.Figure = go.Figure(data=traces, layout=layout)

    fig.write_image(plot_path)
    # fig.show()


### HELPERS ###


def text_position(ratings: list[int], move_value: int) -> list[str]:
    positions: list[str] = [
        "top right" if (ratings[0] < move_value) else "top left",
        "top center" if (ratings[1] < move_value) else "middle left",
        "top left" if (ratings[2] < move_value) else "middle right",
        "bottom left" if (ratings[3] < move_value) else "middle right",
        "bottom center" if (ratings[4] < move_value) else "middle left",
        "top right" if (ratings[5] < move_value) else "top left",
    ]

    return positions


# LIMIT WHAT GETS EXPORTED.


__all__: list[str] = ["plot_radar_diagram"]
