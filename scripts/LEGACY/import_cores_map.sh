#!/bin/bash
#
# Import a core district map 
#
# For example:
#
# scripts/import_cores_map.sh NC Proportional
#

XX=$1
LABEL=$2

YYYY=2022
PLAN_NAME=Congress
PLAN_TYPE=$(echo "$PLAN_NAME" | tr '[:upper:]' '[:lower:]')

SCRIPT_DIR=/Users/alecramsay/iCloud/dev/dra-cli
CSV_FILE=/Users/alecramsay/iCloud/dev/pg/data/$XX/$XX\_$YYYY\_$PLAN_NAME\_$LABEL\_cores_all.csv

# echo $SCRIPT_DIR/importmap.js -u alec@davesredistricting.org -f $CSV_FILE -T $PLAN_TYPE -N "$XX $YYYY $PLAN_NAME - $LABEL Cores" -D "$LABEL-Baseline district cores" -L "PG-CORES"
$SCRIPT_DIR/importmap.js -u alec@davesredistricting.org -f $CSV_FILE -T $PLAN_TYPE -N "$XX $YYYY $PLAN_NAME - $LABEL Cores" -D "$LABEL-Baseline district cores" -L "PG-CORES"