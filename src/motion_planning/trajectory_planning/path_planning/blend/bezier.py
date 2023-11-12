import copy

import numpy as np

from lerp2 import Lerp
from line import Line
from point import Point


class Bezier:
    def __init__(self, vs: list) -> None:
        super().__init__()
        self.vs = copy.deepcopy(vs)

    def interpolate(self, s: float) -> Point:
        size = len(self.vs)
        v1 = self.vs[:-1]
        v2 = self.vs[1:]
        if size > 2:
            # bezier1 = Bezier(v1)
            # bezier2 = Bezier(v2)
            # v = Lerp.interpolate_static(bezier1.interpolate(s), bezier2.interpolate(s), s)
            v = Lerp.interpolate_static(Bezier.interpolate_static(v1, s), Bezier.interpolate_static(v2, s), s)
        else:
            v = Lerp.interpolate_static(v1, v2, s)
        return v

    @staticmethod
    def interpolate_static(vs: list, s: float) -> Point:
        size = len(vs)
        v1 = vs[:-1]
        v2 = vs[1:]
        if size > 2:
            v = Lerp.interpolate_static(Bezier.interpolate_static(v1, s), Bezier.interpolate_static(v2, s), s)
        else:
            v = Lerp.interpolate_static(v1[0], v2[0], s)
        return v


if __name__ == '__main__':
    # vs = np.array([
    #     [0, 1, 2, 3],
    #     [0, 0, 2, 3],
    #     [0, 0, 0, 0]
    # ])
    v0 = Point((0, 0, 0))
    v1 = Point((1, 0, 0))
    v2 = Point((2, 2, 0))
    v3 = Point((3, 3, 0))
    vs = [v0, v1, v2, v3]
    bezier = Bezier(vs)
    for s in np.linspace(0, 1, 101):
        vi = bezier.interpolate(s)
        # vi = Bezier.interpolate_static(vs, s)
        print(vi.get_t())
