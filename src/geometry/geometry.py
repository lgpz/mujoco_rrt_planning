import copy
from abc import ABC, abstractmethod

import numpy as np


class Geometry(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.t = None

    def get_t(self) -> np.ndarray:
        return copy.deepcopy(self.t)

    def get_t_3d(self) -> np.ndarray:
        t = self.get_t()
        if t.size == 2:
            return np.append(t, 0.0)
        elif t.size == 3:
            return t
