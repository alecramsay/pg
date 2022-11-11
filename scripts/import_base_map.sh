#!/bin/bash
#
# Import a baseline map from the 'baseline' repository
#
# For example:
#
# scripts/import_base_map.sh NC Congress blocks
#

XX=$1
YYYY=2020
PLAN_TYPE=$2
UNITS=$3

SCRIPT_DIR=/Users/alecramsay/iCloud/dev/dra-cli
CSV_FILE=/Users/alecramsay/iCloud/dev/baseline/results/$XX/$XX\_$YYYY\_$PLAN_TYPE\_$UNITS.csv

$SCRIPT_DIR/importmap.js -u alec@davesredistricting.org -f $CSV_FILE -T $PLAN_TYPE -N "$XX $YYYY $PLAN_TYPE (Baseline)" -D "Baseline map, $UNITS" -L "PG-BASELINE"
