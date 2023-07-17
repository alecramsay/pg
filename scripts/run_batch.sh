#!/bin/bash
#
# Run a batch of commands
#
# For example:
#
# scripts/run_batch.sh
#

XX=ID
OFFICIAL=ab09bc34-c83d-4327-9b59-c53c71682151
PROPORTIONAL=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
COMPETITIVE=f404dcbc-4763-4405-8ee8-9de38763ab9c
MINORITY=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
COMPACT=c04b3d59-ad9b-4d34-a56c-a40e4a2faaaf
SPLITTING=0549f613-9577-4a0f-ba17-f821552e3512
BASELINE=e6f75d1c-4756-4ebe-99fe-9012d6777ed8

scripts/pull_map_ratings.sh $XX Congress Official $OFFICIAL
scripts/pull_map_ratings.sh $XX Congress Proportional $PROPORTIONAL
scripts/pull_map_ratings.sh $XX Congress Competitive $COMPETITIVE
scripts/pull_map_ratings.sh $XX Congress Minority $MINORITY
scripts/pull_map_ratings.sh $XX Congress Compact $COMPACT
scripts/pull_map_ratings.sh $XX Congress Splitting $SPLITTING
scripts/pull_map_ratings.sh $XX Congress Baseline $BASELINE

#