from unittest import TestCase

import numpy as np

from arm.geometry import Point, Line

class TestLine(TestCase):
    def test_get_point0(self):
        pass

    def test_get_point1(self):
        pass

    def test_get_length(self):
        t0 = np.array([0.0, 0.0])
        t1 = np.array([0.2, 0.2])

        point0 = Point(t0)
        point1 = Point(t1)

        line = Line(point0, point1)
        print('length: ', line.get_length())

        line2 = Line()
        print('length: ', line2.get_length())

        line3 = Line((0, 0, 0), (1, 1, 1))
        print('length: ', line3.get_length())

        line4 = Line([0, 0, 0], [4, 4, 4])
        print('length: ', line4.get_length())
