import copy

import numpy as np


class Point:
    def __init__(self, t: tuple) -> None:
        super().__init__()
        self.t = np.array(t)
        self.dim = self.t.size

    def __add__(self, other):
        return Point(self.t + other.t)

    def __sub__(self, other):
        return Point(self.t - other.t)

    def __mul__(self, other):
        return Point(other * self.t)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return Point(self.t / other)

    def get_x(self) -> float:
        return self.t[0]

    def get_y(self) -> float:
        return self.t[1]

    def get_z(self) -> float:
        return self.t[2]

    def get_t(self) -> np.ndarray:
        return copy.deepcopy(self.t)


if __name__ == '__main__':
    t = (2.0, 2.0)
    point = Point(t)
    tx = point.get_x()
    ty = point.get_y()
    # tz = point.get_z()
    tt = point.get_t()

    print('tx: ', tx)
    print('ty: ', ty)
    # print('tz: ', tz)
    print('tt: ', tt)

    t2 = (3.0, 5.0)
    point2 = Point(t2)
    point3 = point + point2
    print(point3.get_t())

    point4 = point3 - point2
    print('sub')
    print(point4.get_t())

    print('mul')
    point5 = point4 * 2
    print(point5.get_t())
    point6 = 2 * point4
    print(point6.get_t())

    print('div')
    point7 = point4 / 3
    print(point7.get_t())
