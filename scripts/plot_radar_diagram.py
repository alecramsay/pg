#!/usr/bin/env python3

"""
Plot radar diagram comparing two maps

For example:

$ scripts/plot_radar_diagram.py NC Official Baseline
$ scripts/plot_radar_diagram.py NC Proportional Baseline

For documentation, type:

$ scripts/plot_radar_diagram.py -h

"""

import argparse
from argparse import ArgumentParser, Namespace
import chart_studio.plotly as py
import plotly.graph_objs as go  # https://plotly.com/python-api-reference/plotly.graph_objects.html
from typing import TypedDict

from pg import *


### PARSE ARGS ###

parser: ArgumentParser = argparse.ArgumentParser(
    description="Plot a radar diagram comparing two maps"
)

parser.add_argument("state", help="The two-character state code (e.g., MD)", type=str)
parser.add_argument("current", help="The current (top) map", type=str)
parser.add_argument("compare", help="The compare (bottom) map", type=str)

parser.add_argument(
    "-v", "--verbose", dest="verbose", action="store_true", help="Verbose mode"
)

args: Namespace = parser.parse_args()

xx: str = args.state
current_subtype: str = args.current
compare_subtype: str = args.compare


### CONSTRUCT FILE NAMES ###

current_file: str = f"temp/{xx}{yy}_{type}_{current_subtype}.json"
compare_file: str = f"temp/{xx}{yy}_{type}_{compare_subtype}.json"

plot_file: str = f"{xx}{yy}_{type}_{current_subtype}_radar"


### LOAD RATINGS ###


current_ratings: Ratings = cull_ratings(load_json(current_file))
compare_ratings: Ratings = cull_ratings(load_json(compare_file))


### PLOT RADAR DIAGRAM ###


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


current_name: str = f"{xx}{yy} {type} {current_subtype}"
compare_name: str = f"{xx}{yy} {type} {compare_subtype}"


class Plan(TypedDict):
    name: str
    nickname: str
    ratings: Ratings


current_plan: Plan = {
    "name": current_name,
    "nickname": current_subtype,
    "ratings": current_ratings,
}
compare_plan: Plan = {
    "name": compare_name,
    "nickname": compare_subtype,
    "ratings": compare_ratings,
}


def plot_radar_diagram(current: Plan, compare: Plan) -> None:
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

    current_r: list[int] = [x for x in current["ratings"].values()]
    current_r += current_r[:1]  # close the polygon
    current_positions: list[str] = text_position(current_r, 80)

    current_trace: py.Scatterpolar = go.Scatterpolar(
        name=current["name"],
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

    compare_r: list[int] = [x for x in compare["ratings"].values()]
    compare_r += compare_r[:1]  # close the polygon
    compare_positions: list[str] = text_position(compare_r, 80)

    compare_trace: py.Scatterpolar = go.Scatterpolar(
        name=compare["name"],
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

    title: str = qualify_label(current["nickname"])
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

    fig.write_image(content_dir + plot_file + ".png")
    # fig.show()


plot_radar_diagram(current_plan, compare_plan)

pass
