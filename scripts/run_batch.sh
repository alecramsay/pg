#!/bin/bash
#
# Diff maps for multiple states
#
# For example:
#
# scripts/run_batch.sh
#

scripts/pull_map_ratings.sh NC Congress Official 6e8268a4-3b9b-4140-8f99-e3544a2f0816

scripts/pull_map_ratings.sh NC Congress Proportional 7cfcec86-b8bf-41fa-a6c2-0be9b3799747
scripts/pull_map_ratings.sh NC Congress Competitive 40178c75-312d-4789-a457-d609b0d8a043
scripts/pull_map_ratings.sh NC Congress Minority 3b168396-6666-4167-830e-4500bde459fe
scripts/pull_map_ratings.sh NC Congress Compact 3bacb15d-e014-4764-9e8c-f238eb687d50
scripts/pull_map_ratings.sh NC Congress Splitting 82e6303c-e842-469b-b364-918bcacf9ef3
