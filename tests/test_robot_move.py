import numpy as np
from spatialmath import SO3, SE3

from arm.motion_planning.trajectory_planning import *

from arm.robot import Robot

if __name__ == '__main__':
    ur_robot = Robot()
    q0 = [0.0, 0.0, np.pi / 2, 0.0, -np.pi / 2, 0.0]
    ur_robot.set_joint(q0)
    T0 = ur_robot.get_cartesian()
    T1 = SE3(x=0.2, y=0.0, z=0.0) * T0

    t0 = T0.t
    R0 = SO3(T0.R)
    t1 = T1.t
    R1 = SO3(T1.R)

    line_position_parameter = LinePositionParameter(t0, t1)
    one_attitude_parameter = OneAttitudeParameter(R0, R1)
    cartesian_parameter = CartesianParameter(line_position_parameter, one_attitude_parameter)
    cubic_velocity_parameter = CubicVelocityParameter(1.0)

    trajectory_parameter = TrajectoryParameter(cartesian_parameter, cubic_velocity_parameter)
    trajectory_planner = TrajectoryPlanner(trajectory_parameter)

    t = np.linspace(0, 1.0, 101)
    for ti in t:
        Ti = trajectory_planner.interpolate(ti)
        ur_robot.move_cartesian(Ti)
        print(ur_robot.get_joint())
