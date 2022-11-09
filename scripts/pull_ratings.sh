#!/bin/bash
#
# Pull the ratings for a map
#
# For example:
#
# scripts/pull_ratings.sh NC Congress Official 6e8268a4-3b9b-4140-8f99-e3544a2f0816
# scripts/pull_ratings.sh NC Congress Proportional 7cfcec86-b8bf-41fa-a6c2-0be9b3799747
#

XX=$1
TYPE=$2
SUBTYPE=$3
MAP_ID=$4

SCRIPT_DIR=/Users/alecramsay/iCloud/dev/dra-cli
OUT_FILE=/Users/alecramsay/iCloud/dev/pg/temp/$XX\_$TYPE\_$SUBTYPE.json

# $SCRIPT_DIR/getmap.js -m -i $MAP_ID | grep score_ > $OUT_FILE

echo "{" > $OUT_FILE
$SCRIPT_DIR/getmap.js -m -i $MAP_ID | grep score_ >> $OUT_FILE
echo "}" >> $OUT_FILE
