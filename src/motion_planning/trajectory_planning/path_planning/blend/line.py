import copy

import numpy as np

from point import Point


class Line:
    def __init__(self, point0: Point, point1: Point) -> None:
        super().__init__()
        self.point0 = copy.deepcopy(point0)
        self.point1 = copy.deepcopy(point1)
        self.length = np.linalg.norm(self.point1 - self.point0)

    def get_point0(self) -> Point:
        return copy.deepcopy(self.point0)

    def get_point1(self) -> Point:
        return copy.deepcopy(self.point1)


if __name__ == '__main__':
    pass
