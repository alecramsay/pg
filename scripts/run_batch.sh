#!/bin/bash
#
# Diff maps for multiple states
#
# For example:
#
# scripts/run_batch.sh
#
# -i 052e108a-b9f9-4c83-a135-5d5a839e176d

ROOT=/Users/alecramsay/iCloud/dev/
SCRIPT_DIR=$ROOT\dra-cli

$SCRIPT_DIR/draclient.js -u alec@davesredistricting.org -x Front.Seat -i 052e108a-b9f9-4c83-a135-5d5a839e176d -d -N "NC 2022 test name" -D "Copy of ..." -L PG-OFFICIAL