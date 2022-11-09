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
import numpy as np  # DELETE

from pg import *


### PARSE ARGS ###

# TODO - Parse command-line args
xx: str = "NC"
yy: str = "22"
type: str = "Congress"
current_subtype: str = "Official"
compare_subtype: str = "Baseline"


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
    ratings: Ratings


current_plan: Plan = {"name": current_name, "ratings": current_ratings}
compare_plan: Plan = {"name": compare_name, "ratings": compare_ratings}

# TODO - DELETE
def example_plot() -> None:
    np.random.seed(1)

    N = 100
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    sz = np.random.rand(N) * 30

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y,
            mode="markers",
            marker=go.scatter.Marker(
                size=sz, color=colors, opacity=0.6, colorscale="Viridis"
            ),
        )
    )

    # fig.show()
    fig.write_image("content/" + plot_file + ".png")


def plot_radar_diagram(current: Plan, compare: Plan) -> None:
    """
    https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html
    https://plotly.com/python/static-image-export/
    """

    # TODO
    # * Border not completing
    # * Values underneath?

    traces: list = []
    theta: list[str] = [
        "Proportionality",
        "Competitiveness",
        "Minority",
        "Compactness",
        "Splitting",
    ]

    # Current trace

    current_r: list[int] = [x for x in current["ratings"].values()]
    current_r += current_r[:1]

    current_trace: py.Scatterpolar = go.Scatterpolar(
        name=current["name"],
        mode="lines+markers+text",
        r=current_r,
        theta=theta,
        fill="toself",
        text="",  # Suppress the current ratings
        fillcolor="rgba(44, 160, 44, 0.5)",
        marker={"color": "black"},
        line={"color": "black"},
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
        # TODO
        # dimensions: dimensions, TODO - ???
        fill="toself",
        fillcolor="rgba(255, 127, 14, 0.5)",
        text=compare_r,
        textposition=compare_positions,
    )

    # TODO: HACK - Add ghost traces???

    # traces.append(compare_ghost)
    # traces.append(current_ghost)
    traces.append(compare_trace)
    traces.append(current_trace)

    # TODO - Decide on title template
    title: str = "Ratings: " + current["name"]
    font_size: int = 16
    title_x: float = 0.5

    layout: py.Layout = go.Layout(
        title=dict(text=title, x=title_x, font_size=font_size),
        polar=dict(radialaxis=dict(visible=True, range=[0, 100], showticklabels=False)),
        showlegend=False,
    )
    """
    TODO
    radarLayout = {
      title: {
        text: radarTitle,
        x: titleX,
        font: {
          size: fontSize
        }
      },
      polar:
      {
        radialaxis:
        {
          visible: true,
          range: [0, 100],
          showticklabels: false
        }
      },
      hovermode: 'closest',
      showlegend: bLegend,
      legend: {
        orientation: 'h',   // show entries horizontally
        xanchor: 'center',  // use center of legend as anchor
        x: 0.5              // put legend in center of x-axis
      },
      annotations: radarAnnotations,
      paper_bgcolor: MA.appBackgroundColor,
      plot_bgcolor: MA.appBackgroundColor
    };
    """

    fig: py.Figure = go.Figure(data=traces, layout=layout)
    py.plot(fig, filename=plot_file)


plot_radar_diagram(current_plan, compare_plan)

pass
