#!/usr/bin/env python3

"""
Calculate the average overlap by state.

Raw data from:

$ grep average *.html

in the docs/_includes directory.

"""


overlaps: dict = {
    "AL": 0.66,
    "AR": 0.77,
    "AZ": 0.53,
    "CA": 0.63,
    "CO": 0.57,
    "CT": 0.69,
    "FL": 0.67,
    "GA": 0.56,
    "IA": 0.81,
    "ID": 0.55,
    "IL": 0.58,
    "IN": 0.69,
    "KS": 0.64,
    "KY": 0.73,
    "LA": 0.63,
    "MA": 0.64,
    "MD": 0.63,
    "MI": 0.62,
    "MN": 0.57,
    "MO": 0.71,
    "MS": 0.71,
    "MT": 0.69,
    "NC": 0.62,
    "NE": 0.78,
    "NH": 0.62,
    "NJ": 0.65,
    "NM": 0.69,
    "NV": 0.67,
    "NY": 0.65,
    "OH": 0.60,
    "OK": 0.59,
    "OR": 0.62,
    "PA": 0.61,
    "RI": 0.84,
    "SC": 0.66,
    "TN": 0.64,
    "TX": 0.60,
    "UT": 0.64,
    "VA": 0.67,
    "WA": 0.65,
    "WI": 0.60,
    "WV": 0.98,
}

average_overlap: float = (sum(overlaps.values()) / len(overlaps)) * 100

print(f"Average overlap: {average_overlap:.2f}")

pass

### END ###
