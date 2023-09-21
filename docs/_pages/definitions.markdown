---
layout: page
title: Definitions
permalink: definitions/
---

Census **blocks** are atomic units in redistricting -- They have shapes
and locations (which establish contiguity) and associated data (such as
**total population,** i.e. people of all ages).

Bigger geographic units include **precincts** which are collections of
adjacent blocks.

A redistricting **plan** or **map** -- we use the terms interchangeably
-- assigns census blocks to legislative districts, the standard
interchange format being a **block-assignment file**.

To be a valid plan, the partitioning of census blocks must yield
districts that are **contiguous** and have **'roughly equal'
population**.

Given two valid maps, the **district cores** are the subsets of block
assignments in the districts that yield the most shared total population
between corresponding districts of the two maps.

The **population geography** of a state ($\rho$) is the pattern of total
population by census block. Alternatively, it is the geographic
distribution of population density, or simply how many people live
where.

The **root map** for a state ($\alpha$) is its population geography
partitioned into districts such that the map has larger district cores
wrto other valid maps than any other valid map for the state.

As definitively identifying the starting point map for a state is
computationally infeasible, one can use heuristics to generate an
**approximate root map** ($\alpha'$).

One heuristic is minimizing the total **moment of inertia** (or energy)
of districts, using population for mass. For a single district, this
**population compactness** is the population-weighted squared distance
of the geographic unit from the district centroid:

<!-- MathJax -->
<!-- https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

\\[ PC=\sum_{1}^n (p(x)*d(x,s)^2) \\]

where

- \\( x \\) is a precinct assigned to the district
- \\( p(x) \\) is the population of the precinct
- precinct locations are the lat/lon of the precinct’s centroid
- \\( s \\) is the district centroid, which is the population-weighted average location of the precincts assigned to the district
- \\( d \\) is the distance function using planar Euclidean distances, treating one degree of latitude to be equal to one degree of longitude, independent of where on the globe the computation is being done

Dave's Redistricting (DRA) rates five quantifiable dimensions of
redistricting maps: proportionality, competitiveness, opportunity for
minority representation, compactness, and splitting. The
\[**ratings**\](https://medium.com/dra-2020/ratings-deep-dive-c03290659b7)
use a scale of \[0--100\] where bigger is always better.

In DRA, the \[**notable maps**\]
(https://medium.com/dra-2020/notable-maps-66d744933a48) for a state are
the five maps that individually maximize those ratings, i.e., most
proportional, least splitting, etc.