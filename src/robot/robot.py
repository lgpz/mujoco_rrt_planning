import copy

import numpy as np
import roboticstoolbox as rtb
from spatialmath import SE3


class Robot:
    def __init__(self):
        d1 = 0.163
        d4 = 0.134
        d5 = 0.1
        d6 = 0.1 + 0.2

        a3 = 0.425
        a4 = 0.392

        self.dof = 6
        self.q0 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        alpha_array = [0.0, -np.pi / 2, 0.0, 0.0, np.pi / 2, -np.pi / 2]
        a_array = [0.0, 0.0, a3, a4, 0.0, 0.0]
        d_array = [d1, 0.0, 0.0, d4, d5, d6]
        theta_array = [0.0, -np.pi / 2, 0.0, np.pi / 2, 0.0, 0.0]

        links = []
        for i in range(6):
            links.append(rtb.DHLink(d=d_array[i], alpha=alpha_array[i], a=a_array[i], offset=theta_array[i], mdh=True))
        self.robot = rtb.DHRobot(links)

    def fkine(self, q) -> SE3:
        return self.robot.fkine(q)

    def ikine(self, Tep):
        result = self.robot.ikine_NR(Tep, q0=self.q0)
        if result.success:
            return result.q
        return []

    def move_cartesian(self, T: SE3):
        q = self.ikine(T)

        assert len(q)  # inverse kinematics failure
        self.set_joint(q)

    def set_joint(self, q):
        self.q0 = q[:]

    def get_joint(self):
        return copy.deepcopy(self.q0)

    def get_cartesian(self):
        return self.fkine(self.q0)


if __name__ == '__main__':
    ur_robot = Robot()
    q0 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    T1 = ur_robot.fkine(q0)
    print(T1)
    ur_robot.move_cartesian(T1)
    q_new = ur_robot.get_joint()
    print(q_new)
