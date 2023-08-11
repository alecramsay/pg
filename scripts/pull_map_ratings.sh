#!/bin/bash
#
# Pull the ratings for a map
#
# For example:
#
# scripts/pull_map_ratings.sh NC 2022 Congress Official 6e8268a4-3b9b-4140-8f99-e3544a2f0816 ~/Downloads/NC
#

XX=$1
YYYY=$2
TYPE=$3
LABEL=$4
GUID=$5
OUTPUT_DIR=$6

SCRIPT_DIR=/Users/alecramsay/iCloud/dev/dra-cli
OUT_FILE=$OUTPUT_DIR/$XX\_$YYYY\_$TYPE\_$LABEL\_ratings.json

echo "{" > $OUT_FILE
$SCRIPT_DIR/getmap.js -m -i $GUID | grep score_ >> $OUT_FILE
echo "}" >> $OUT_FILE
