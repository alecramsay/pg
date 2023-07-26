#!/bin/bash
#
# Run a batch of commands
#
# For example:
#
# scripts/run_batch.sh
#

scripts/compare_plan_to_baseline.py -s NC -l Official
scripts/compare_plan_to_baseline.py -s NC -l Proportional
scripts/compare_plan_to_baseline.py -s NC -l Competitive
scripts/compare_plan_to_baseline.py -s NC -l Minority
scripts/compare_plan_to_baseline.py -s NC -l Compact
scripts/compare_plan_to_baseline.py -s NC -l Splitting

#