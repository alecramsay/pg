---
layout: page
title: Definition
permalink: definition/
---

Our baseline districts minimize the total moment of inertia (or energy) of districts, using population for mass. We call this “population compactness.”

The population compactness of a single district is the population-weighted squared distance of the precincts from the district centroid:

<!-- MathJax -->
<!-- https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

\\[ PC=\sum_{1}^n p(x)*d(x,s)^2 \\]

where

- \\( x \\) is a precinct assigned to the district
- \\( p(x) \\) is the population of the precinct
- precinct locations are the lat/lon of the precinct’s centroid
- \\( s \\) is the district centroid, which is the population-weighted average location of the precincts assigned to the district
- \\( d \\) is the distance function using planar Euclidean distances, treating one degree of latitude to be equal to one degree of longitude, independent of where on the globe the computation is being done

Our baseline maps meet four additional constraints:

- Complete – all precincts are assigned to districts
- Contiguous – the precincts in each district are contiguous
- Splitting – no precincts are split, and
- Population deviation – 2% or less

From an initial, random districting, our algorithm greedily searches for the most population-compact districting.  Because this algorithm is not guaranteed to find the best districting, we run it 100 times and take the best map that meets these four constraints.

By this definition, each state has exactly one baseline plan. 
