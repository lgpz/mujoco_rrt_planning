import copy
from typing import Union, Iterable

import numpy as np


class RRTParameter:

    def __init__(self, start: Union[np.ndarray, Iterable], goal: Union[np.ndarray, Iterable],
                 expand_dis: float = 1.0, goal_sample_rate: float = 10.0, max_iter: int = 100,
                 animation: bool = False) -> None:
        super().__init__()
        self.__start = start
        self.__goal = goal
        self.__expand_dis = expand_dis
        self.__goal_sample_rate = goal_sample_rate
        self.__max_iter = max_iter
        self.__animation = animation

    @property
    def start(self):
        return copy.deepcopy(self.__start)

    @property
    def goal(self):
        return copy.deepcopy(self.__goal)

    @property
    def expand_dis(self):
        return self.__expand_dis

    @property
    def goal_sample_rate(self):
        return self.__goal_sample_rate

    @property
    def max_iter(self):
        return self.__max_iter

    @property
    def animation(self):
        return self.__animation
