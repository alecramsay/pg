#!/bin/bash
#
# Diff maps for multiple states
#
# For example:
#
# scripts/run_batch.sh
#

scripts/diff_maps.py MD 2022 congressional
scripts/diff_maps.py NC 2022 congressional
scripts/diff_maps.py NY 2022 congressional
scripts/diff_maps.py PA 2022 congressional
scripts/diff_maps.py VA 2022 congressional
