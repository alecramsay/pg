#!/bin/bash
#
# Duplicate a map
#
# For example:
#
# scripts/duplicate_map.sh NC Congress 2022 Official PG-OFFICIAL c62fa27b-1f4b-40ba-bcd7-9e2ca6f9df87
# scripts/duplicate_map.sh NC Congress 2022 Proportional PG-NOTABLE 7cfcec86-b8bf-41fa-a6c2-0be9b3799747
#

XX=$1
PLAN_TYPE=$2
YYYY=$3
GROUP=$4
LABEL=$5
ID=$6

ROOT=/Users/alecramsay/iCloud/dev/
SCRIPT_DIR=$ROOT\dra-cli

USER=alec@davesredistricting.org
PW=Front.Seat

$SCRIPT_DIR/draclient.js -u $USER -x $PW -i $ID -d -N \"$XX $YYYY $PLAN_TYPE \($GROUP\)\" -D \"Copy of $XX $GROUP\" -L $LABEL
# echo $SCRIPT_DIR/draclient.js -u $USER -x $PW -i $ID -d -N \"$XX $YYYY $PLAN_TYPE \($GROUP\)\" -D \"Copy of $XX $GROUP\" -L $LABEL