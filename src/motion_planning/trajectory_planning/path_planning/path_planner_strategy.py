from abc import ABC

from src.interface import Strategy

from .path_parameter import PathParameter


class PathPlannerStrategy(Strategy, ABC):

    def __init__(self, parameter: PathParameter):
        super().__init__(parameter)
