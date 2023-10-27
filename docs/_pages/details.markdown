---
layout: page
title: How It Works
permalink: details/
---

We explore two ideas here:

-   The most population compact map is the natural starting point for redistricting
    &#8212; all redistricting plans for a state are informed by it; and

-   Comparing redistricting plans to that starting point highlights the mix of policy
    choices (trade-offs) that the mapmakers made.

By population geography we mean how many people live where in a state.

From here on, **bolded** terms are defined on the [Glossary](./glossary.markdown) page.

In more detail:

1.  We introduce the concept of a **root plan** or **root map** that
    partitions a state's unique **population geography** into a set
    of districts with the lowest overall **edit distance** to all other valid maps.
    Due to computational limitations, one can only *approximate* the root map. 

2.  We argue that maximally **population compact** districts are the natural starting point for redistricting. 

    The fundamental principle of these maps is that people who live near each other will tend to be in the same district. 
    Moreover, they are a good heuristic for approximating root maps. 

    Maps that are highly compact geometrically also tend to have low overall edit distances to other valid maps
    &#8212; slightly lower than population compact maps. 
    But as Chief Justice Earl Warren said in his landmark *Reynold v. Sims* decision, 
    "Legislators represent people, not trees or acres." 
    so the heuristic we use to approximate root maps is to maximize population compactness.

    Roughly speaking, population-compact districts form a
    [Voronoi diagram](https://en.wikipedia.org/wiki/Voronoi_diagram).
 
    We impose three additional constraints on our approximation:

    -   Each district is contiguous
    -   No precincts are split, and
    -   **Population deviation** is 2% or less

    From an initial, random districting, our algorithm greedily searches
    for the most population-compact districting. Because this algorithm is
    not guaranteed to find the best districting, we run it 100 times and
    take the best qualifying map.

3.  We also believe it is logical to think of other maps in terms of deltas from these root maps.
    A root map isn't a priori (or independently) normative though.
    Think of it like the origin on a set of axes:
    it's simply the place from which you describe other points.

4.  We generate proximal root maps for 42 states apportioned two or more
    congressional districts in the 2020 census. We exclude Hawaii and
    Maine, due to data issues.

5.  We compare these root maps to the five **notable maps**
    from Dave's Redistricting (DRA)
    for each state that individually optimize for proportionality,
    competitiveness, minority representation, compactness, and
    county-district splitting.

6.  Despite optimizing on these different dimensions, these maps share
    substantial **common core districts** with the root map, an average of
    nearly two thirds of the population-weighted assignments (65.9%).
    This reinforces our hypothesis that maximizing the overall
    population compactness of districts is a good way to characterize
    population geography.

7.  Then we compare the DRA **ratings**
    for these divergent maps to those for the root map showing some
    major quantifiable policy trade-offs inherent in congressional
    redistricting for each state. These contrasts put policy choices
    framed by the underlying population geography in sharp relief.

    Again, these root maps are not normative 
    &#8212; they aren't what we think redistricting plans *should* be.
    Given their very low overall edit distance to other valid maps,
    all redistricting plans for a state are unavoidably informed by them, and
    they are easy to understand conceptually 
    &#8212; people who live near each other will tend to be in the same district.

    Hence, they provide a good baseline against which to evaluate and compare plans.

8.  Finally, we compare the official map for each state to the root
    districts showing the mix of policy choices (trade-offs) that each
    state made.

For more background, see the [Background](./background.markdown) page. 