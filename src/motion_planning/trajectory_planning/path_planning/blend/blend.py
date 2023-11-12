import copy
from typing import Union, Iterable, List, Tuple

import numpy as np

from ..path_planner import PathPlanner


class Blend:
    def __init__(self, path_planners: Union[List[PathPlanner], Tuple[PathPlanner]],
                 radii: Union[np.ndarray, Iterable, int, float]) -> None:
        super().__init__()
        self.planners = copy.deepcopy(path_planners)
        self.radii = copy.deepcopy(radii)
        self.s_array = []

    def plan(self) -> None:
        length1 = np.linalg.norm(self.planners[0].interpolate(1.0) - self.planners[0].interpolate(1.0))
        self.s_array.append(length1 - self.radii[0])

        length2 = np.linalg.norm(self.planners[1].interpolate(1.0) - self.planners[1].interpolate(1.0))
        s2 = self.radii[0] / length2

    def interpolate(self, s: float) -> np.ndarray:
        pass


if __name__ == "__main__":
    pass
