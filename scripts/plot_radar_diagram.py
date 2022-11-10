#!/usr/bin/env python3
#
# Plot radar diagram comparing two maps
#
# For example:
#
# $ scripts/plot_radar_diagram.py NC Official Baseline
#

import chart_studio.plotly as py
import plotly.graph_objs as go  # https://plotly.com/python-api-reference/plotly.graph_objects.html
from typing import TypedDict, Any

from pg import *


### PARSE ARGS ###

xx: str = "NC"
yy: str = "22"
type: str = "Congress"
current_subtype: str = "Official"
compare_subtype: str = "Baseline"

show_plot: bool = True
write_png: bool = False


### CONSTRUCT PATHS ###

current_file: str = f"temp/{xx}{yy}_{type}_{current_subtype}.json"
compare_file: str = f"temp/{xx}{yy}_{type}_{compare_subtype}.json"

plot_file: str = f"{xx}{yy}_{type}_{current_subtype}_radar"


### LOAD RATINGS ###


class Ratings(TypedDict):
    proportionality: int
    competitiveness: int
    minority_opportunity: int
    compactness: int
    splitting: int


def cull_ratings(raw_in: dict) -> Ratings:
    r: Ratings = {
        "proportionality": int(raw_in["score_proportionality"]),
        "competitiveness": int(raw_in["score_competitiveness"]),
        "minority_opportunity": int(raw_in["score_minorityRights"]),
        "compactness": int(raw_in["score_compactness"]),
        "splitting": int(raw_in["score_splitting"]),
    }

    return r


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

    current_trace: py.Scatterpolar = go.Scatterpolar(
        name=current["name"],
        mode="lines+markers+text",
        r=current_r,
        theta=theta,
        fill="toself",
        text="",  # Suppress the current ratings
        fillcolor="rgba(44, 160, 44, 0.75)",
        marker=dict(color="black"),
        line=dict(color="black"),
    )

    # Compare trace

    compare_r: list[int] = [x for x in compare["ratings"].values()]
    compare_r += compare_r[:1]
    compare_positions: list[str] = text_position(compare_r, 80)

    compare_trace: py.Scatterpolar = go.Scatterpolar(
        name=compare["name"],
        mode="lines+markers+text",
        r=compare_r,
        theta=theta,
        text=compare_r,
        textposition=compare_positions,
        fill="toself",
        fillcolor="rgba(255, 127, 14, 0.5)",
        marker=dict(color="orange"),
        line=dict(color="orange"),
    )

    traces.append(compare_trace)
    traces.append(current_trace)

    title: str = current["nickname"]
    font_size: int = 16
    title_x: float = 0.5

    layout: py.Layout = go.Layout(
        title=dict(text=title, x=title_x, font_size=font_size),
        polar=dict(
            bgcolor=bgcolor,
            angularaxis=dict(linewidth=1, showline=True, linecolor="black"),
            radialaxis=dict(
                visible=True,
                gridcolor="lightgrey",
                gridwidth=1,
                range=[0, 100],
                showticklabels=False,
            ),
        ),
        width=size,
        height=size,
        showlegend=False,
        paper_bgcolor=bgcolor,
        plot_bgcolor=bgcolor,
    )

    fig: py.Figure = go.Figure(data=traces, layout=layout)
    # py.plot(fig, filename=plot_file)

    if show_plot:
        fig.show()
    if write_png:
        fig.write_image("content/" + plot_file + ".png")


plot_radar_diagram(current_plan, compare_plan)

pass
