---
layout: page
title: Glossary
permalink: glossary/
---

**Block-assignment file:** A CSV file with a row for each census
**block** that consists of the geoid for the block and the **district**
to which it is assigned. This is the standard interchange format for
redistricting plans.

**Block:** Census blocks are the atomic units in redistricting. They
have shapes and locations (which establish contiguity) and associated
data (such as **total population**).

**Common core districts:** Given two valid **maps**, the common core
districts are the subsets of **block** assignments in the **districts**
that yield the most shared **total population** between corresponding
**districts** of the two **maps**.

**District:** A set of census **blocks** assigned to the same district
identifier. Because the **blocks** must be contiguous, districts
partition a state into non-overlapping geographic regions.

**Edit distance:** Given two valid maps, the edit distance is the
minimum **total population** of the **blocks** that must be reassigned
to transform one **map** into the other.

**Map:** A synonym for **plan**. We use the terms interchangeably.

**Notable map:** In DRA, the [notable maps]
(https://medium.com/dra-2020/notable-maps-66d744933a48) for a state are
the five **maps** that individually maximize those **ratings**, i.e.,
most proportional, least splitting, etc.

**Plan:** A redistricting plan or map partitions a state's **population
geography** into legislative **districts**. To be a **valid plan**, the
districts must be contiguous and have 'roughly equal' population.

**Population compactness:** One heuristic for generating an approximate
**root map** for a state is minimizing the total moment of inertia (or
energy) of **districts**, using population for mass. We call this
"population compactness." For a single **district** defined in terms of
**precincts**, it is the sum of the population-weighted squared distance
of the **precincts** from the **district** centroid:

<!-- MathJax -->
<!-- https://math.meta.stackexchange.com/questions/5020/mathjax-basic-tutorial-and-quick-reference -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

\[ PC=\sum_{1}^n (p(x)*d(x,s)^2) \]

> where

-   \\( x \\) is **precinct** assigned to the **district**
-   \\( p(x) \\) is its **total population**
-   locations are the lat/lon of the **precinct's** centroid
-   \\( s \\) is the **district** centroid, which is the population-weighted
    average location of the **precincts** assigned to the **district**
-   \\( d \\) is the distance function using planar Euclidean distances,
    treating one degree of latitude to be equal to one degree of
    longitude, independent of where on the globe the computation is
    being done

**Population deviation:** The population of the most populous district
minus the population of the least populous district divided by the
average district population, expressed as a percentage.

**Population geography:** The pattern of **total population** by census
**block** across a state. Alternatively, it is the geographic
distribution of population density, or simply how many people live
where.

**Precinct:** Collections of adjacent **blocks** defined by states
and/or the Census Bureau which refers to them as VTDs (voting tabulation
districts).

**Ratings:** Dave's Redistricting (DRA) rates five quantifiable
dimensions of redistricting **maps**: proportionality, competitiveness,
opportunity for minority representation, compactness, and splitting. The
[ratings](https://medium.com/dra-2020/ratings-deep-dive-c03290659b7)
use a scale of [0--100] where bigger is always better.

**Root map:** The **map** for a state that has the greatest **total
population** of its **common core districts** wrto other valid maps. 
In other words, it has the lowest total **edit distance** from all other 
valid maps. As definitively identifying the root districts for a state is 
computationally infeasible, one can use heuristics to generate an 
*approximate* root map.

**Total population:** The number of people of all ages for a census
geography, such as a **block** or **precinct**. Contrast this with
voting-age population which is the number of people 18 or older.