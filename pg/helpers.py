#!/usr/bin/env python3

"""
HELPERS
"""

from typing import TypedDict


# RATINGS


class Ratings(TypedDict):
    proportionality: int
    competitiveness: int
    minority_opportunity: int
    compactness: int
    splitting: int


def cull_ratings(raw_in: dict) -> Ratings:
    r: Ratings = {
        "proportionality": int(raw_in["score_proportionality"]),
        "competitiveness": int(raw_in["score_competitiveness"]),
        "minority_opportunity": int(raw_in["score_minorityRights"]),
        "compactness": int(raw_in["score_compactness"]),
        "splitting": int(raw_in["score_splitting"]),
    }

    return r


# FILE NAMES & PATHS


def file_name(parts: list[str], delim: str = "_", ext: str = None) -> str:
    """
    Construct a file name with parts separated by the delimeter and ending with the extension.
    """
    name: str = delim.join(parts) + "." + ext if ext else delim.join(parts)

    return name


def path_to_file(parts: list[str], naked: bool = False) -> str:
    """
    Return the directory path to a file (but not the file).
    """

    rel_path: str = "/".join(parts)

    if not naked:
        rel_path = rel_path + "/"

    return rel_path


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
        return f"Best {label} Representation"
    raise ValueError(f"Unknown map label: {label}")


def is_water_only(geoid) -> bool:
    """
    Return True if the block geoid has a water-only signature, False otherwise.
    """
    return geoid[5:7] == "99"
