---
layout: page
title: Variations
permalink: variations/
---

The main contribution of this site is a framework for understanding the redistricting process as
the trading off of a mix of policy objectives in the context of an underlying population distribution.
We instantiate that framework and use it to illustrate the tradeoffs in congressional redistricting state by state.

We hope others will adopt this general approach, even if they make different specific choices.

### Data

- Like Dave's Redistricting (DRA), we use 2020 census VTD shapes ("precincts") wherever we can. 
  Similarly, in a few states (CA, OR, and WV), we use blockgroups (BGs).
  One might choose to use BGs everywhere instead of VTDs.
  Alternatively, one might choose to use state precincts, especially the latest ones instead of census VTDs.
- We use the offical 2020 census total population counts from DRA for all states.
  One might choose to use adjusted totals, e.g., that reallocate prisoner populations, if a state has adopted them.
  Or one might want to use mid-decade census estimates, as we approach the next redistricting cycle.
  Or one might want to develop baseline districts using voting-age population (VAP) or even citizen voting-age population (CVAP).

### Baseline

- We developed a heuristic approach for finding the lowest energy map for a state, based on
  Balzer's capacity-constrained Voronoi tessellation (CCVT) algorithm using only census populations. 
  We embed it into multi-step process to ensure that the resulting map is complete, contiguous, and 
  doesn't split any precincts.
  We run the process 100 times with random starting points and choose the map with the lowest energy
  that has a population deviation of 2% or less.
  One can imagine myriad variations, including:
  increasing the number of iterations (e.g., 1000); 
  relaxing or tightening the 2% population deviation threshold;
  trying to keep cities and/or counties intact, if possible;
  using a different objective functions than the energy function we used; or
  using an altogether different approach, such as Markov chain Monte Carlo (MCMC),
  for exploring the space of possible baseline maps.
- One can also imagine looking for "peephole optimizations" &#8212; single precinct moves and/or swaps &#8212; 
  that would decrease total energy.

### Maps

- We use the official maps that were in place for the 2022 congressional elections.
  One might want to use newer maps that have been adopted (e.g., as a result of court challenges).
- Similarly, as a *proxy* for the maps in a state that optimize the five key dimension rated in DRA
  &#8212; proportionality, competitiveness, opportunity for minority representation, compactness, and county-district splitting &#8212;
  we use a snapshot of DRA's [notable maps](https://medium.com/dra-2020/notable-maps-66d744933a48)
  at a point in time with some minor corrections and modifications, 
  Instead of using this user-generated content, one might want to select maps from a large ensemble of
  automatically generated maps (e.g., using Markov chain Monte Carlo (MCMC)).

### Comparisons

- We compare maps on the five dimensions on which DRA rates maps 
  (see [Ratings: Deep Dive](https://medium.com/dra-2020/ratings-deep-dive-c03290659b7)).
  One might choose to use different metrics for evaluating one or more of these dimensions.
  Or one might ignore one or more of these dimensions.
  Or one might add others, e.g., communities of interest, incumbency, etc.
  Or some combination.
  There's nothing magic about the dimensions we've chosen, except they're what DRA uses because they
  were readily quantifiable and easy to compute and have been generally accepted.

### Miscellaneous

- We analyze the tradeoffs for congressional redistricting.
  One could take a simlar approach to state legislative or even local redistricting.

There are lots of possibilities for analysis within this framework.
