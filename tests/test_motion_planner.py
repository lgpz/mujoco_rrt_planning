import numpy as np
from spatialmath import SO3

from arm.motion_planning import PositionPlanningModeEnum
from arm.motion_planning import AttitudePlannerModeEnum
from arm.motion_planning import MotionParameter
from arm.motion_planning import MotionPlanner

p0 = np.array([0, 1, 0])
p1 = np.array([1, 0, 0])
pc = np.array([0, 0, 0])

R0 = SO3.Rx(np.pi / 6)
R1 = SO3.RPY([np.pi / 3, np.pi / 4, np.pi / 6])
vec_n = np.array([0, 0, 1])


def test_line_one_planner():
    line_one_parameter = MotionParameter(
        p0, R0, p1, R1, 1.0, PositionPlanningModeEnum.LINE, AttitudePlannerModeEnum.ONE)
    planner = MotionPlanner(line_one_parameter)
    t = planner.get_motion(0.4)
    print(t)


def test_arc_center_one_planner():
    arc_center_one_parameter = MotionParameter(
        p0, R0, p1, R1, 1.0, PositionPlanningModeEnum.ARC_CENTER, AttitudePlannerModeEnum.ONE, pc=pc)
    planner = MotionPlanner(arc_center_one_parameter)
    t = planner.get_motion(0.4)
    print(t)


def test_line_two_planner():
    line_two_parameter = MotionParameter(
        p0, R0, p1, R1, 1.0, PositionPlanningModeEnum.LINE, AttitudePlannerModeEnum.TWO)
    planner = MotionPlanner(line_two_parameter)
    t = planner.get_motion(0.4)
    print(t)


def test_arc_center_two_planner():
    arc_center_two_parameter = MotionParameter(
        p0, R0, p1, R1, 1.0, PositionPlanningModeEnum.ARC_CENTER, AttitudePlannerModeEnum.TWO, pc=pc)
    planner = MotionPlanner(arc_center_two_parameter)
    t = planner.get_motion(0.4)
    print(t)


def test_line_three_planner():
    line_three_parameter = MotionParameter(
        p0, R0, p1, R1, 1.0, PositionPlanningModeEnum.LINE, AttitudePlannerModeEnum.THREE, vec_n=vec_n)
    planner = MotionPlanner(line_three_parameter)
    t = planner.get_motion(0.4)
    print(t)


def test_arc_center_three_planner():
    arc_center_three_parameter = MotionParameter(
        p0, R0, p1, R1, 1.0, PositionPlanningModeEnum.ARC_CENTER, AttitudePlannerModeEnum.THREE, pc=pc, vec_n=vec_n)
    planner = MotionPlanner(arc_center_three_parameter)
    t = planner.get_motion(0.4)
    print(t)


if __name__ == '__main__':
    test_line_one_planner()

    test_arc_center_one_planner()

    test_line_two_planner()

    test_arc_center_two_planner()

    test_line_three_planner()

    test_arc_center_three_planner()
