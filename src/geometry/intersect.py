from .point import Point
from .line import Line
from .line_segment import LineSegment
from .circle import Circle
from .distance import Distance


class Intersect:

    @staticmethod
    def check_point_to_circle(point: Point, circle: Circle) -> bool:
        return Distance.point_to_circle(point, circle) <= 0.0

    @staticmethod
    def check_line_to_circle(line: Line, circle: Circle):
        return Distance.line_to_circle(line, circle) <= 0.0

    @staticmethod
    def check_line_segment_to_circle(line_segment: LineSegment, circle: Circle):
        return Distance.line_segment_to_circle(line_segment, circle) <= 0.0
