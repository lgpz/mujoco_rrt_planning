import os
import numpy as np
from spatialmath import SO3

os.add_dll_directory("C://Users//Cybaster//.mujoco//mjpro150//bin")

from mujoco_py import load_model_from_path, MjSim, MjViewer
from mujoco_py.generated import const

from src.motion_planning.trajectory_planning import *

from src.robot import Robot

if __name__ == '__main__':

    model = load_model_from_path("../../assets/universal_robots_ur5e/scene.xml")
    sim = MjSim(model)
    viewer = MjViewer(sim)

    robot = Robot()
    dof = 6
    q0 = [0.0, 0.0, np.pi / 2, 0.0, -np.pi / 2, 0.0]
    robot.set_joint(q0)

    obstacles = [
        (0.3, 0.1, 0.05),
        (0.4, -0.1, 0.05),
        (0.5, 0.1, 0.05),
        (0.6, -0.1, 0.05),
        (0.7, 0.1, 0.05)
    ]
    rrt_map = RRTMap(area=[(0.15, -0.35), (0.85, 0.35)], obstacles=obstacles)

    start = [0.3, -0.3]
    goal = [0.7, 0.3]
    rrt_parameter = RRTParameter(start=[0.3, -0.3], goal=[0.7, 0.3], expand_dis=0.1, animation=True)
    rrt_planner = RRTPlanner(rrt_map=rrt_map, rrt_parameter=rrt_parameter)

    R0 = SO3.RPY(-np.pi, 0.0, -np.pi / 2)

    num = 201
    ss = np.linspace(0.0, 1.0, num)
    joints = np.zeros((num, dof))

    for i, si in enumerate(ss):
        Ti = rrt_planner.interpolate(si, R0)
        robot.move_cartesian(Ti)
        joints[i, :] = robot.get_joint()

    s_step = 0
    forward = True
    j = 0

    coms = [(*start, 0.0), (*goal, 0.0)]
    while True:
        for i in range(dof):
            sim.data.qpos[i] = joints[s_step, i]
            sim.data.qvel[i] = 0.0

        sim.step()
        viewer.render()

        for com in coms:
            viewer.add_marker(pos=com, size=np.array([0.01, 0.01, 0.01]), rgba=np.array([1., 0, 0, 1]),
                              type=const.GEOM_SPHERE)

        j += 1
        if j == 10:
            j = 0
            if forward:
                s_step += 1
                if s_step == num - 1:
                    forward = False
            else:
                s_step -= 1
                if s_step == 0:
                    forward = True
