import copy

from point import Point


class Lerp:
    def __init__(self, point0: Point, point1: Point) -> None:
        super().__init__()
        self.point0 = copy.deepcopy(point0)
        self.point1 = copy.deepcopy(point1)

    def interpolate(self, s: float) -> Point:
        return self.point0 + s * (self.point1 - self.point0)

    @staticmethod
    def interpolate_static(point0: Point, point1: Point, s: float) -> Point:
        return point0 + s * (point1 - point0)


if __name__ == '__main__':
    t0 = (2, 3)
    t1 = (4, 7)
    point0 = Point(t0)
    point1 = Point(t1)

    point_s = Lerp.interpolate_static(point0, point1, 0.5)
    print(point_s.get_t())
