import numpy as np
from spatialmath import SO3

from arm.motion_planning.trajectory_planning.path_planning.cartesian_planning import AttitudePlanner
from arm.motion_planning.trajectory_planning.path_planning.cartesian_planning import OneAttitudeParameter
from arm.motion_planning.trajectory_planning.path_planning.cartesian_planning import TwoAttitudeParameter
from arm.motion_planning.trajectory_planning.path_planning.cartesian_planning import ThreeAttitudeParameter


R0 = SO3()
R1 = SO3.RPY([np.pi / 3, np.pi / 4, np.pi / 6])


def test_attitude_one_planner():
    one_attitude_parameter = OneAttitudeParameter(R0, R1)
    planner = AttitudePlanner(one_attitude_parameter)
    t = planner.interpolate(0.4)
    print(t)


def test_attitude_two_planner():
    two_attitude_parameter = TwoAttitudeParameter(R0, R1)
    planner = AttitudePlanner(two_attitude_parameter)
    t = planner.interpolate(0.4)
    print(t)


def test_attitude_three_planner():
    R0 = SO3.Rx(np.pi / 6)
    vec_n = np.array([0, 0, 1])
    three_attitude_parameter = ThreeAttitudeParameter(R0, R1, vec_n)
    planner = AttitudePlanner(three_attitude_parameter)
    t = planner.interpolate(0.75)
    print(t)


if __name__ == '__main__':
    test_attitude_one_planner()

    test_attitude_two_planner()

    test_attitude_three_planner()
