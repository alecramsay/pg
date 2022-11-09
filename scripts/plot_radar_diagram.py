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
from typing import TypedDict
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
    return {
        "proportionality": raw_in["score_proportionality"],
        "competitiveness": raw_in["score_competitiveness"],
        "minority_opportunity": raw_in["score_minorityRights"],
        "compactness": raw_in["score_compactness"],
        "splitting": raw_in["score_splitting"],
    }


current_ratings: Ratings = cull_ratings(load_json(current_file))
compare_ratings: Ratings = cull_ratings(load_json(compare_file))


### PLOT RADAR DIAGRAM ###

current_title: str = f"{xx}{yy} {type} {current_subtype}"
compare_title: str = f"{xx}{yy} {type} {compare_subtype}"

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


# TODO - plot radar diagram
def plot_radar_diagram() -> None:
    """
    https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html
    https://plotly.com/python/renderers/
    https://plotly.com/python/static-image-export/
    """

    traces: list = []

    layout: py.Layout = go.Layout(
        title="Pairwise Comparison",
        # width=svSize,
        # height=svSize,
        # xaxis=dict(
        #     title="Vote fraction",
        #     range=x_range,
        #     dtick=0.05,
        #     tickformat=".2f",
        #     # tickformat=".0%",
        #     showgrid=True,
        #     gridcolor="lightgrey",
        # ),
        # yaxis=dict(
        #     title="Seat fraction",
        #     range=y_range,
        #     scaleanchor="x",
        #     scaleratio=1,
        #     dtick=0.05,
        #     tickformat=".2f",
        #     # tickformat=".0%",
        #     showgrid=True,
        #     gridcolor="lightgrey",
        # ),
        # dragmode="zoom",
        # hovermode="closest",
        # showlegend=False,
        # paper_bgcolor=bgcolor,
        # plot_bgcolor=bgcolor,
    )

    fig: py.Figure = go.Figure(data=traces, layout=layout)
    py.plot(fig, filename=plot_file)


plot_radar_diagram()

pass

"""
// From dra-client:

export function renderRadarDiagram(config: RadarConfig): void
{
  const bLegend: boolean = config.radarLegendOn;
  const bValues: boolean = config.radarValuesOn;

  // Drive the internal configuration switches off of the calling context
  const radarCompareOn: boolean = (config.context >= RadarContext.CompareTwo) ? true : false;
  // const radarTitleOn: boolean = true; <<< title set below using context
  const radarLabelsOn: boolean = (config.context == RadarContext.ComparePairs) ? false : true;

  let bCompare: boolean = radarCompareOn && config.compareSessionProps ? true : false;

  if (!config.profile || !config.scorecard)
    return;
  
  const name = config.profile.name;
  let compareName = '';

  // RADAR DIAGRAM

  let radarTraces: any[] = [];
  let radarLayout: any = {};
  let radarConfig: any = {};
  {
    // Define trace for the current map

    let compareTrace: any;
    let compareGhost: any;
    let currentGhost: any;
    let ratings = bCompare ? sessionPropsToRatings(config.compareSessionProps) : null;
    bCompare = bCompare && !!ratings;     // Only compare if something has been selected to compare

    // No partisan data - Revised the labels
    // Use full labels if labels are on; otherwise elide them to one character
    const dimensions: string[] = config.bHidePartisanData ? 
    [
      Ratings.equitable.label,
      Ratings.compact.label,
      Ratings.cohesive.label,
      Ratings.equitable.label
    ] : 
    [
      Ratings.unbiased.label,
      Ratings.competitive.label,
      Ratings.equitable.label,
      Ratings.compact.label,
      Ratings.cohesive.label,
      Ratings.unbiased.label
    ];
    const shortLabels = config.bHidePartisanData ? [ "M", "C'", "S", "M" ] : [ "P", "C", "M", "C'", "S", "P" ];
    const theta = radarLabelsOn ? dimensions : shortLabels;

    // No partisan data - Revised the current data
    const rCurrent: number[] = config.bHidePartisanData ?
    [
      config.scorecard.minority.score,
      config.scorecard.compactness.score,
      config.scorecard.splitting.score,
      config.scorecard.minority.score
    ] :
    [
      config.scorecard.partisan.bias.score,
      config.scorecard.partisan.responsiveness.score,
      config.scorecard.minority.score,
      config.scorecard.compactness.score,
      config.scorecard.splitting.score,
      config.scorecard.partisan.bias.score,
    ];
    const reqsAnnotation: string = 'Requirements: ' + (requirementsPass(config.reqsChecklist, config.targetPopEqual) ? 'Met' : 'Not met');

    // No partisan data - Revised the text positions
    const currentPositions: string[] = getTextPosition(rCurrent, 80, config.bHidePartisanData);

    let currentHover: string[] = [];
    for (var i = 0; i < dimensions.length; i++)
    {
      currentHover.push(`${rCurrent[i]}: ${dimensions[i]}<extra></extra>`);
    }

    let currentTrace: any =
      {
        name: name,
        type: 'scatterpolar',
        mode: 'lines+markers+text',
        r: rCurrent,
        theta: theta,
        fill: 'toself',
        text: (bValues && !bCompare) ? rCurrent : '',
        textposition: (bValues && !bCompare) ? currentPositions : '',
        hoverinfo: (bValues && !bCompare) ? 'none' : 'points',
        hovertemplate: (bValues && !bCompare) ? '' : currentHover,
        // hovertemplate: (bValues && !bCompare) ? '' : "%{r}<extra></extra>",
        showlegend: false
      };

    // Change the default coloring of the current/base map <<< for all scenarios/cases
    currentTrace.fillcolor = 'rgba(44, 160, 44, 0.5)';
    currentTrace.marker = {color: 'black'};
    currentTrace.line = {color: 'black'};
  
    if (bCompare)
    {
      // Get properties of the map to compare to
      compareName = (config.compareOrder ? String(config.compareOrder) + ' – ' : '') + config.compareSessionProps.name;

      // No partisan data - Revised the compare data
      const rCompare = config.bHidePartisanData ?
      [
        ratings.minorityRights,
        ratings.compactness,
        ratings.splitting,
        ratings.minorityRights
      ] :
      [
        ratings.proportionality,
        ratings.competitiveness,
        ratings.minorityRights,
        ratings.compactness,
        ratings.splitting,
        ratings.proportionality
      ];

      const comparePositions: string[] = getTextPosition(rCompare, 80, config.bHidePartisanData);

      let compareHover: string[] = [];
      for (var i = 0; i < dimensions.length; i++)
      {
        compareHover.push(`${rCompare[i]}: ${dimensions[i]}<extra></extra>`);
      }

      compareTrace =
      {
        name: compareName,
        type: 'scatterpolar',
        mode: 'lines+markers+text',
        r: rCompare,
        theta: theta,
        dimensions: dimensions,
        fill: 'toself',
        fillcolor: 'rgba(255, 127, 14, 0.5)',
        text: rCompare,
        textposition: comparePositions,
        hoverinfo: 'points',
        hovertemplate: compareHover,
        // hoverinfo: 'none',
        // hovertemplate: '',
        showlegend: false
      };

      // HACK - Add traces to eliminate the weird Aa in the legend
      compareGhost = Util.deepCopy(compareTrace);
      delete compareGhost.text;
      delete compareGhost.textposition;
      delete compareGhost.hoverinfo;
      delete compareGhost.hovertemplate;
      compareGhost.mode = 'lines+markers';
      compareGhost.showlegend = bLegend;

      currentGhost = Util.deepCopy(currentTrace);
      delete currentGhost.text;
      delete currentGhost.textposition;
      delete currentGhost.hoverinfo;
      delete currentGhost.hovertemplate;
      currentGhost.mode = 'lines+markers';
      currentGhost.showlegend = bLegend;

      // Push the traces in the order to achieve the desired behavior
      radarTraces.push(compareGhost);
      radarTraces.push(currentGhost);
      radarTraces.push(compareTrace);
    }

    radarTraces.push(currentTrace);

    let radarTitle: string = 'Ratings: ' + name;
    let fontSize: number = 16;
    let titleX = 0.5;           // Centert the title 

    if (config.context == RadarContext.ComparePairs) {
      radarTitle = compareName;

      const maxTitleLength = 50;
      if (maxTitleLength < compareName.length) {
        radarTitle = compareName.substring(0, maxTitleLength) + ' ...';
      }

      fontSize = 12;
    }

    const radarAnnotations = bCompare ? [] :
    [
      {
        x: 0,
        y: 0,
        text: bAnnotateDiagram ? reqsAnnotation : '',
        showarrow: false,
        xshift: 65,
        yshift: -20
      }
    ];

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

    // Configure hover menu options & behavior

    radarConfig = {
      toImageButtonOptions: {
        format: 'png', // one of png, svg, jpeg, webp
        filename: 'ratings-diagram'
      },
      // Remove all the plotly hover commands, except download
      modeBarButtonsToRemove: ['zoom2d', 'select2d', 'lasso2d', 'toggleHover'],
      displayModeBar: true,
      displaylogo: false,
      responsive: true
    };
    Plotly.newPlot(config.div, radarTraces, radarLayout, radarConfig);
  }
}

"""
