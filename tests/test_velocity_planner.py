import unittest

from arm.motion_planning.trajectory_planning.velocity_planning import CubicVelocityParameter, \
    QuinticVelocityParameter, VelocityPlanner


class MyTestCase(unittest.TestCase):

    def test_cubic_velocity_planner(self):
        cubic_velocity_parameter = CubicVelocityParameter(1.0)
        velocity_planner = VelocityPlanner(cubic_velocity_parameter)
        t = velocity_planner.interpolate(0.4)
        print(t)

    def test_quintic_velocity_planner(self):
        velocity_parameter = QuinticVelocityParameter(1.0)
        velocity_planner = VelocityPlanner(velocity_parameter)
        t = velocity_planner.interpolate(0.4)
        print(t)


if __name__ == '__main__':
    unittest.main()
