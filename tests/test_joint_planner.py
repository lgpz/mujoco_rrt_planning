import unittest

import numpy as np

from arm.motion_planning.trajectory_planning.path_planning.joint_planning import JointParameter, JointPlanner

q0 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
q1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])


class MyTestCase(unittest.TestCase):

    def test_joint_planner(self):
        joint_parameter = JointParameter(q0, q1)
        joint_planner = JointPlanner(joint_parameter)
        t = joint_planner.interpolate(0.2)
        print(t)


if __name__ == '__main__':
    unittest.main()
