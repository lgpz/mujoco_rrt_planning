import unittest

import numpy as np
from spatialmath import SO3

from arm.motion_planning.trajectory_planning.path_planning import JointParameter, PathPlanner
from arm.motion_planning.trajectory_planning.path_planning import LinePositionParameter, OneAttitudeParameter, \
    CartesianParameter, CartesianPlanner

q0 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
q1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

t0 = np.array([0, 1, 0])
t1 = np.array([1, 0, 0])
tc = np.array([0, 0, 0])

R0 = SO3.Rx(np.pi / 6)
R1 = SO3.RPY([np.pi / 3, np.pi / 4, np.pi / 6])
vec_n = np.array([0, 0, 1])


class MyTestCase(unittest.TestCase):

    def test_joint_planner(self):
        joint_parameter = JointParameter(q0, q1)
        joint_planner = PathPlanner(joint_parameter)
        t = joint_planner.interpolate(0.2)
        print(t)

    def test_line_one_parameter(self):
        line_position_parameter = LinePositionParameter(t0, t1)
        one_attitude_parameter = OneAttitudeParameter(R0, R1)
        cartesian_parameter = CartesianParameter(line_position_parameter, one_attitude_parameter)
        planner = CartesianPlanner(cartesian_parameter)
        t = planner.interpolate(0)
        print(t)


if __name__ == '__main__':
    unittest.main()
