#!/usr/bin/env python3

"""
UTILITIES
"""


def is_water_only(geoid):
    """
    Return True if the block geoid has a water-only signature, False otherwise.
    """
    return geoid[5:7] == "99"
