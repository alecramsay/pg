---
layout: page
title: Example
permalink: example/

xx: "NC"
small-radar-width: 300
big-radar-width: 500
map-width: 700
---

This is an annotated example of the analysis of a state's political geography, using North Carolina as an example.
There is a separate page for each state. 

At the top is a summary of what the various exhibits reveal. That is not shown here.

{% assign xx = page.xx %}

<!-- SUMMARY ANALYSIS -->

<!-- BASELINE DISTRICTS -->

[First the baseline districts are shown.
You can click on the image to go to the map in DRA.]

{% capture baseline-png %}
{{ site.baseurl }}/assets/images/{{ xx }}_2020_Congress_Baseline_map.png
{% endcapture %}
{% assign baseline-png = baseline-png | strip_newlines %}

{% assign state = site.data.states | where:"xx", xx | first %}

{% capture baseline-link %}
https://davesredistricting.org/join/{{ state["baseline"] }}
{% endcapture %}
{% assign baseline-link = baseline-link | strip_newlines %}

<h3>Baseline Districts</h3>

<p>These are the baseline congressional districts:</p>
<p style="text-align: left">
    <a href="{{ baseline-link }}">
        <img src="{{ baseline-png }}" alt="Baseline districts" title="Click to view the map in Dave's Redistricting"
            width="{{ page.map-width }}" />
    </a>
</p>

<h3>Ratings vs. Baseline</h3>

[Then the ratings for the Official and the five Notable Maps that maximizing proportionality, 
competitiveness, minority representation, compactness, and splitting are compared to the ratings 
of the baseline map.
First with a set of pairwise radar diagrams.]

<!-- RADAR DIAGRAMS -->

<p>These radar diagrams compare the ratings of official map and the five notable maps with the baseline map:</p>

<table style="border:0px">
    <tr>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Official_radar.png"
                alt="{{ site.data.maps[0].label }}" title="{{ site.data.maps[0].label }}"
                width="{{ page.small-radar-width }}" />
        </td>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Proportional_radar.png"
                alt="{{ site.data.maps[1].qualified-label }}" title="{{ site.data.maps[1].qualified-label }}"
                width="{{ page.small-radar-width }}" />
        </td>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Competitive_radar.png"
                alt="{{ site.data.maps[2].qualified-label }}" title="{{ site.data.maps[2].qualified-label }}"
                width="{{ page.small-radar-width }}" />
        </td>
    </tr>
    <tr>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Minority_radar.png"
                alt="{{ site.data.maps[3].qualified-label }}" title="{{ site.data.maps[3].qualified-label }}"
                width="{{ page.small-radar-width }}" />
        </td>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Compact_radar.png"
                alt="{{ site.data.maps[4].qualified-label }}" title="{{ site.data.maps[4].qualified-label }}"
                width="{{ page.small-radar-width }}" />
        </td>
        <td style="border:0px">
            <img src="{{ site.baseurl }}/assets/images/{{ xx }}_2022_Congress_Splitting_radar.png"
                alt="{{ site.data.maps[3].qualified-label }}" title="{{ site.data.maps[3].qualified-label }}"
                width="{{ page.small-radar-width }}" />
        </td>
    </tr>
</table>

<!-- RATINGS TABLE -->

[Then in tabular form for convenience.]

{% capture ratings-file %}
{{ xx }}_2022_Congress_ratings
{% endcapture %}
{% assign ratings-file = ratings-file | strip_newlines %}

{% assign ratings = site.data[ratings-file] %}

<style>
    #ratings-table {
        width: 900px;
    }

    .bold-row {
        font-weight: bold;
    }

    #official-intersections-table {
        width: 410px;
    }

    #proportional-intersections-table {
        width: 410px;
    }

    #competitive-intersections-table {
        width: 410px;
    }

    #minority-intersections-table {
        width: 410px;
    }

    #compact-intersections-table {
        width: 410px;
    }

    #splitting-intersections-table {
        width: 410px;
    }

    .ag-header-cell.text-center {
        .ag-header-cell-label {
            justify-content: center;
        }
    }

    .ag-header-cell.text-right {
        .ag-header-cell-label {
            justify-content: right;
        }
    }

    .ag-theme-alpine {
        --ag-font-family: 'Source Code Pro', monospace;
        /* --ag-font-family: Inconsolata; */
    }
</style>

<div id="ratings-table" class="ag-theme-alpine">
</div>

<!-- Common grid functionality -->
<script src="{{ site.baseurl }}/assets/js/grid.js"></script>

<!-- Grid -->
<script type="text/javascript" charset="utf-8">
    const ratingsColumns = [
        {field: 'Map', width: 190, unSortIcon: true},
        {field: 'Proportionality', width: 165, comparator: numericComparator, sortingOrder: ['desc', 'asc'], ...centeredColumn},
        {field: 'Competitiveness', width: 165, comparator: numericComparator, sortingOrder: ['desc', 'asc'], ...centeredColumn},
        {field: 'Minority', width: 120, comparator: numericComparator, sortingOrder: ['desc', 'asc'], ...centeredColumn},
        {field: 'Compactness', width: 130, comparator: numericComparator, sortingOrder: ['desc', 'asc'], ...centeredColumn},
        {field: 'Splitting', width: 125, comparator: numericComparator, sortingOrder: ['desc', 'asc'], ...centeredColumn},
    ];

    const ratingsOptions = {
        defaultColDef: {
            sortable: true,
            // resizable: true,
        },
        rowClassRules: {
            'bold-row': function (params) {return params.data.Map === "Official" || params.data.Map === "Baseline";},
        },
        columnDefs: ratingsColumns,
        domLayout: 'autoHeight',
        onGridReady: (event) => {renderRatingsTable(event.api)}
    };

    const eRatingsGridDiv = document.getElementById('ratings-table');
    new agGrid.Grid(eRatingsGridDiv, ratingsOptions);

    const ratingsCSV = 'https://raw.githubusercontent.com/alecramsay/pg/main/docs/_data/{{ ratings-file }}.csv';
    // const ratingsCSV = 'https://raw.githubusercontent.com/alecramsay/pg/main/docs/_data/NC_2022_Congress_ratings.csv';

    function renderRatingsTable(api)
    {
        Papa.parse(ratingsCSV, {
            header: true,
            download: true,
            complete: response =>
            {
                data = response.data;
                data.pop();
                // console.log("Finished:", data);

                api.setRowData(data);
                api.sizeColumnsToFit();
            }
        })
    }

</script>

<!-- MAPS TABS -->

<h3>Districts vs. Baseline</h3>

[At the bottom are a set of tabs, one for each of the six maps compared to the baseline map. 
For each map, there is: 

* an image of the map which you can click on to see in DRA, 
* an image of the regions formed by intersecting the district boundaries of the two maps, and
* a table showing data for each intersecting region]

<p>These tabs compare the district boundaries of official map and the five notable maps with the baseline map:</p>

<script src="{{ site.baseurl }}/assets/js/tabs.js"></script>

<!-- Tab links -->
<div class="tab">
    <button class="tablinks" onclick="openTab(event, '{{ site.data.maps[0].label }}')" id="defaultOpen">{{
        site.data.maps[0].qualified-label }}</button>
    <button class="tablinks" onclick="openTab(event, '{{ site.data.maps[1].label }}')">{{
        site.data.maps[1].qualified-label
        }}</button>
    <button class="tablinks" onclick="openTab(event, '{{ site.data.maps[2].label }}')">{{
        site.data.maps[2].qualified-label
        }}</button>
    <button class="tablinks" onclick="openTab(event, '{{ site.data.maps[3].label }}')">{{
        site.data.maps[3].qualified-label
        }}</button>
    <button class="tablinks" onclick="openTab(event, '{{ site.data.maps[4].label }}')">{{
        site.data.maps[4].qualified-label
        }}</button>
    <button class="tablinks" onclick="openTab(event, '{{ site.data.maps[5].label }}')">{{
        site.data.maps[5].qualified-label
        }}</button>
</div>

<!-- Tab content -->

<!-- Official -->
{% include detail.html index=0 %}

<!-- Most Proportional -->
{% include detail.html index=1 %}

<!-- Most Competitive -->
{% include detail.html index=2 %}

<!-- Best Minority -->
{% include detail.html index=3 %}

<!-- Most Compact -->
{% include detail.html index=4 %}

<!-- Least Splitting -->
{% include detail.html index=5 %}

<!-- Show the Official tab by default -->
<script>
  // Get the element with id="defaultOpen" and click on it
  document.getElementById("defaultOpen").click();
</script>