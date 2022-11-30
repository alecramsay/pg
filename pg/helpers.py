#!/usr/bin/env python3

"""
HELPERS
"""

from .types import *


# RATINGS


def cull_ratings(raw_in: dict) -> Ratings:
    r: Ratings = Ratings(
        proportionality=int(raw_in["score_proportionality"]),
        competitiveness=int(raw_in["score_competitiveness"]),
        minority_opportunity=int(raw_in["score_minorityRights"]),
        compactness=int(raw_in["score_compactness"]),
        splitting=int(raw_in["score_splitting"]),
    )

    return r


# MISCELLANEOUS


def qualify_label(label: str) -> str:
    """
    Add 'Most', 'Least', and 'Best' prefixes to Notables labels.
    """
    if label == "Official":
        return label
    if label == "Splitting":
        return f"Least {label}"
    if label in ["Proportional", "Competitive", "Compact"]:
        return f"Most {label}"
    if label == "Minority":
        return f"Best {label}"
    return label


# DON'T LIMIT WHAT GETS EXPORTED.
