from unittest import TestCase

from arm.geometry import Point, Circle, Distance, Line, LineSegment


class TestDistance(TestCase):
    def test_point_to_point(self):
        point0 = Point((0, 0, 0))
        point1 = Point((1, 1, 1))
        distance_point_to_point = Distance.point_to_point(point0, point1)
        print('distance point to point: ', distance_point_to_point)

    def test_point_to_circle(self):
        point = Point((1, 1))
        circle = Circle((0, 0), 1)
        distance_point_to_circle = Distance.point_to_circle(point, circle)
        print('distance point to circle: ', distance_point_to_circle)

    def test_point_to_line(self):
        point = Point((1, 1, 1))

        line = Line((0, 0, 0), (0.5, 0, 0))

        distance = Distance.point_to_line(point, line)
        print('distance: ', distance)

    def test_point_to_line_segment(self):
        point = Point((1, 1, 1))

        line_segment = LineSegment((0, 0, 0), (0.5, 0, 0))

        distance = Distance.point_to_line_segment(point, line_segment)
        print('distance: ', distance)

    def test_line_to_circle(self):
        line = Line((0, 0), (0.5, 0))
        circle = Circle((1, 1), 1)

        distance = Distance.line_to_circle(line, circle)
        print('distance: ', distance)

    def test_line_segment_to_circle(self):
        line_segment = LineSegment((0, 0), (0.5, 0))
        circle = Circle((1, 1), 1)

        distance = Distance.line_segment_to_circle(line_segment, circle)
        print('distance: ', distance)
