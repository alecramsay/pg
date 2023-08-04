#!/bin/bash
#
# Run a batch of commands
#
# For example:
#
# scripts/pull_ratings_EXPLICIT.sh
#

XX=WV
OFFICIAL=8b2f8ec2-1d12-468a-b445-11c9f6097f74
PROPORTIONAL=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
COMPETITIVE=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
MINORITY=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
COMPACT=d0785c40-b290-4c44-9f29-48f28edaf96e
SPLITTING=0556f0d1-950d-4581-8777-67cc912d7280
BASELINE=a0a0dbd0-e472-47c1-b3c6-e1e51219fabc

scripts/pull_map_ratings.sh $XX Congress Official $OFFICIAL
scripts/pull_map_ratings.sh $XX Congress Proportional $PROPORTIONAL
scripts/pull_map_ratings.sh $XX Congress Competitive $COMPETITIVE
scripts/pull_map_ratings.sh $XX Congress Minority $MINORITY
scripts/pull_map_ratings.sh $XX Congress Compact $COMPACT
scripts/pull_map_ratings.sh $XX Congress Splitting $SPLITTING
scripts/pull_map_ratings.sh $XX Congress Baseline $BASELINE

#