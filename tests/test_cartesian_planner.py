import unittest

import numpy as np
from spatialmath import SO3

from arm.motion_planning.trajectory_planning.path_planning.cartesian_planning import OneAttitudeParameter
from arm.motion_planning.trajectory_planning.path_planning.cartesian_planning import LinePositionParameter, \
    CartesianParameter, CartesianPlanner

t0 = np.array([0, 1, 0])
t1 = np.array([1, 0, 0])
tc = np.array([0, 0, 0])

R0 = SO3.Rx(np.pi / 6)
R1 = SO3.RPY([np.pi / 3, np.pi / 4, np.pi / 6])
vec_n = np.array([0, 0, 1])


class MyTestCase(unittest.TestCase):

    def test_cartesian_planner(self):
        line_attitude_parameter = LinePositionParameter(t0, t1)
        one_attitude_parameter = OneAttitudeParameter(R0, R1)
        cartesian_parameter = CartesianParameter(line_attitude_parameter, one_attitude_parameter)
        planner = CartesianPlanner(cartesian_parameter)
        t = planner.interpolate(1)
        print(t)


if __name__ == '__main__':
    unittest.main()
