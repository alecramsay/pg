#!/usr/bin/env python3

"""
DATA STRUCTURES
"""

from shapely.geometry import shape, Polygon, MultiPolygon
from typing import Optional

from .readwrite import *
from .datatypes import *
from .moi import *


class State:
    """A container for all things related to a state"""

    features: Optional[dict[str, Feature]]
    total_pop: Optional[int]
    xmin: Optional[float]
    ymin: Optional[float]
    xmax: Optional[float]
    ymax: Optional[float]

    def __init__(self) -> None:
        self.features = None
        self.total_pop = None
        self.xmin = None
        self.ymin = None
        self.xmax = None
        self.ymax = None

    def load_features(self, rel_path: str) -> None:
        """Re-hydrate a dict of Features serialized to a CSV"""

        features: dict[str, Feature] = dict()
        self.total_pop = 0

        types: list = [str, int, float, float]
        rows: list[dict[str, int | float]] = read_typed_csv(rel_path, types)

        for row in rows:
            geoid: str = str(row["GEOID"])
            pop: int = int(row["POP"])
            x: float = float(row["X"])
            y: float = float(row["Y"])

            feature: Feature = Feature(xy=Coordinate(x, y), pop=pop)
            features[geoid] = feature

            self.total_pop += pop

        self.features = features

    def load_shape(self, rel_path: str) -> None:
        """
        Load the shape for a state from a shapefile.
        """
        self.shape: Polygon | MultiPolygon = load_state_shape(rel_path, "GEOID20")
        # TYPE HINT
        self.xmin, self.ymin, self.xmax, self.ymax = self.shape.bounds


class Plan:
    """
    A container for all things related to a plan.
    """

    def __init__(self) -> None:
        self.name: str = None
        self.nickname: str = None

        self.state: State = None

        self._assignments: list[Assignment] = None
        self._districts: dict[int, District] = None
        self.ratings: Ratings = None

        # TODO - More ...

    def set_state(self, state: State) -> None:
        self.state = state

    def load_assignments(self, rel_path: str) -> None:
        """
        Load assignments from a CSV file.
        """
        types: list = [str, int]
        districts_by_geoid: list[dict[str, int]] = read_typed_csv(rel_path, types)
        self._assignments = [
            Assignment(item["GEOID20"], item["District"]) for item in districts_by_geoid
        ]

    def assignments(self) -> list[Assignment]:
        if self._assignments:
            return self._assignments

        raise Exception("Assignments not loaded.")

    def districts(self) -> dict[int, District]:
        """
        Return a list of Districts.
        """
        if self._districts:
            return self._districts

        if self.state is None:
            raise Exception("State data not loaded yet.")

        # Invert the plan, save the results, and return them.

        inverted: dict[int, District] = dict()

        for row in self.assignments():
            geoid: str = row.geoid

            # HACK - Skip water-only blocks.
            if geoid[5:7] == "99":
                continue
            # HACK: These two unpopulated blocks are missing from the NY Most Compact plan.
            if geoid in ["360610001001001", "360610001001000"]:
                continue

            i: int = row.district
            if i not in inverted:
                d: District = {"geoids": set(), "xy": Coordinate(0, 0), "pop": 0}
                inverted[i] = d

            inverted[i]["geoids"].add(geoid)

        self._districts = inverted
        self._calc_district_centroids()

        return self._districts

    def _calc_district_centroids(self) -> None:
        for _, district in self.districts().items():
            xsum: float = 0
            ysum: float = 0
            total: int = 0

            for geoid in district["geoids"]:
                feature: Feature = self.state.features[geoid]
                total += feature.pop
                xsum += feature.xy.x * feature.pop
                ysum += feature.xy.y * feature.pop

            district["xy"] = Coordinate(xsum / total, ysum / total)
            district["pop"] = total

    def calc_moi(self) -> float:
        districts: dict[int, District] = self.districts()
        n: int = len(districts)
        moi: float = 0.0

        for _, district in districts.items():
            moi += calc_moi(district["geoids"], district["xy"], self.state.features)

        moi /= n

        return moi


# LIMIT WHAT GETS EXPORTED.


__all__: list[str] = ["State", "Plan"]
