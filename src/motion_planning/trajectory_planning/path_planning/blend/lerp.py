import copy

import numpy as np


class Lerp:
    def __init__(self, p0: np.ndarray, p1: np.ndarray) -> None:
        super().__init__()
        self.p0 = copy.deepcopy(p0)
        self.p1 = copy.deepcopy(p1)

    def interpolate(self, s: float) -> np.ndarray:
        return self.p0 + s * (self.p1 - self.p0)

    @staticmethod
    def interpolate_static(p0: np.ndarray, p1: np.ndarray, s: float) -> np.ndarray:
        return p0 + s * (p1 - p0)
