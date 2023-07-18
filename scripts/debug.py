#!/usr/bin/env python3
#

"""
DEBUGGING DRIVER
"""

from pg import *

./geoid.py cores \
--assignments ~/personal/pg/data/NC/*{Baseline,Compact,Competitive,Minority,Proportional,Splitting}*.csv \
--maxcores ~/Downloads/NC-all-maxcore-pop.csv \
--diff ~/Downloads/NC-all-diff.csv \
--population ~/personal/baseline/data/NC/NC_2020_block_data.csv

pass
