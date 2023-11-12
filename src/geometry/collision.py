import copy
from typing import overload, Union, Iterable

from .circle import Circle
from .point import Point
from .line import Line
from .line_segment import LineSegment
from .intersect import Intersect


class Collision:
    def __init__(self, obstacles: Iterable[Circle]) -> None:
        super().__init__()
        self.obstacles = copy.deepcopy(obstacles)

    def check_point(self, point: Point) -> bool:
        for obstacle in self.obstacles:
            if Intersect.check_point_to_circle(point, obstacle):
                return True
        return False

    def check_line(self, line: Line):
        for obstacle in self.obstacles:
            if Intersect.check_line_to_circle(line, obstacle):
                return True
        return False

    def check_line_segment(self, line_segment: LineSegment):
        for obstacle in self.obstacles:
            if Intersect.check_line_segment_to_circle(line_segment, obstacle):
                return True
        return False
