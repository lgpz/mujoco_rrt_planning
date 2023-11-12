from unittest import TestCase

import numpy as np
from spatialmath import SO3

from arm.motion_planning.trajectory_planning import *

t0 = np.array([0, 1, 0])
t1 = np.array([1, 0, 0])
R0 = SO3.Rx(np.pi / 6)
R1 = SO3.RPY([np.pi / 3, np.pi / 4, np.pi / 6])

line_position_parameter = LinePositionParameter(t0, t1)
one_attitude_parameter = OneAttitudeParameter(R0, R1)
cartesian_parameter = CartesianParameter(line_position_parameter, one_attitude_parameter)
cubic_velocity_parameter = CubicVelocityParameter(1)

trajectory_parameter = TrajectoryParameter(cartesian_parameter, cubic_velocity_parameter)
planner = TrajectoryPlanner(trajectory_parameter)


class TestTrajectoryPlanner(TestCase):
    def test_interpolate(self):
        t = planner.interpolate(0.8)
        print(t)
