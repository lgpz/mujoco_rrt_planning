import copy
from typing import overload, Union, Iterable

import numpy as np

from .geometry import Geometry


class Point(Geometry):

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, t: Union[np.ndarray, Iterable, int, float]) -> None:
        ...

    @overload
    def __init__(self, t: Geometry) -> None:
        ...

    def __init__(self, t=None) -> None:
        super().__init__()
        if t is None:
            self.t = np.zeros(1)
        elif isinstance(t, (np.ndarray, Iterable, int, float)):
            self.t = np.array(t, dtype=np.float64)
        elif isinstance(t, Point):
            self.t = np.array(t.get_t())
        else:
            raise ValueError("bad argument to constructor")
        self.dim: int = self.t.size

    def __add__(self, other: Geometry):
        return Point(self.t + other.get_t())

    def __sub__(self, other: Geometry):
        return Point(self.t - other.get_t())

    def __mul__(self, other):
        return Point(other * self.t)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return Point(self.t / other)

    def __str__(self) -> str:
        return str(self.t)

    def get_tx(self) -> float:
        return self.t[0]

    def get_ty(self) -> float:
        return self.t[1]

    def get_tz(self) -> float:
        return self.t[2]

    def set_tx(self, num: float) -> None:
        self.t[0] = num

    def set_ty(self, num: float) -> None:
        self.t[1] = num

    def set_tz(self, num: float) -> None:
        self.t[2] = num


if __name__ == '__main__':
    t = np.array([2, 2])
    point = Point(t)
    tx = point.get_tx()
    ty = point.get_ty()
    # tz = point.get_z()
    tt = point.get_t()

    print('tx: ', tx)
    print('ty: ', ty)
    # print('tz: ', tz)
    print('tt: ', tt)

    t2 = np.array([3.0, 5.0])
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

    point8 = Point()
    print(point8.get_t())

    point9 = Point((9, 9, 9))
    print(point9.get_t())

    point10 = Point([10, 10, 10])
    print(point10.get_t())
