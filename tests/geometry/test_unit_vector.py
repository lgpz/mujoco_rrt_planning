from unittest import TestCase

import numpy as np

from arm.geometry import Point, UnitVector

class TestUnitVector(TestCase):
    def test_unit_vector(self):
        t = np.array([2.0, 2.0])
        point = Point(t)

        t0 = np.array([0.0, 0.0])
        t1 = np.array([1.0, 1.0])
        unit_vector = UnitVector(t0, t1)
        print('unit vector: ', unit_vector.get_t())

        point_unit_vector = point + unit_vector
        print(point_unit_vector.get_t())

    def test_unit_vector2(self):
        t = np.array([2.0, 2.0])
        point = Point(t)

        unit_vector = UnitVector(point)
        print('unit vector: ', unit_vector.get_t())

    def test_unit_vector3(self):
        t = np.array([2.0, 2.0])
        point = Point(t)

        unit_vector = UnitVector(point, point+point)
        print('unit vector: ', unit_vector.get_t())
