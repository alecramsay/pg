#!/bin/bash
#
# Import a baseline map from the 'baseline' repository
#
# For example:
#
# scripts/import_base_map.sh NC
#

XX=$1
YYYY=2020
YY=20
PLAN_NAME=Congress
PLAN_TYPE=$(echo "$PLAN_NAME" | tr '[:upper:]' '[:lower:]')
P=C
# UNITS=vtd
LABEL=baseline
ITER=100

SCRIPT_DIR=/Users/alecramsay/iCloud/dev/dra-cli
CSV_FILE=/Users/alecramsay/iCloud/dev/baseline/maps/$XX/$XX$YY$P\_$LABEL\_$ITER.csv

echo $SCRIPT_DIR/importmap.js -u alec@davesredistricting.org -f $CSV_FILE -T $PLAN_TYPE -N "$XX $YYYY $PLAN_NAME - Baseline" -D "Baseline map" -L "PG-BASELINE"
$SCRIPT_DIR/importmap.js -u alec@davesredistricting.org -f $CSV_FILE -T $PLAN_TYPE -N "$XX $YYYY $PLAN_NAME - Baseline" -D "Baseline map" -L "PG-BASELINE"