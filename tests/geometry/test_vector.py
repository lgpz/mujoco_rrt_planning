from unittest import TestCase

import numpy as np

from arm.geometry import Point, Vector


class TestVector(TestCase):
    def test_vector0(self):
        t0_0 = np.array([1, 2, 3])
        t1_0 = np.array([2, 3, 4])
        vector0 = Vector(t0_0, t1_0)
        print('vector0: ', vector0.get_t())

    def test_vector1(self):
        t0_0 = np.array([1, 2, 3])
        t1_0 = np.array([2, 3, 4])
        vector0 = Vector(t0_0, t1_0)

        t0_1 = np.array([3, 4, 5])
        t1_1 = np.array([7, 6, 5])
        vector1 = Vector(t0_1, t1_1)

        vector2 = vector0 + vector1
        print(vector2.get_t())

    def test_vector2(self):
        vector2 = Vector()
        print("vector2: ", vector2.get_t())

    def test_vector3(self):
        vector3 = Vector((4, 4, 4))
        print("vector3: ", vector3.get_t())

    def test_vector4(self):
        vector4 = Vector((4, 4, 4), [5, 5, 5])
        print("vector5: ", vector4.get_t())
