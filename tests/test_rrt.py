from src.motion_planning import RRTPlanner, RRTParameter, RRTMap

if __name__ == '__main__':
    animation = True

    obstacles = [
        (4, 10, 3.0),
        (8.0, 5.0, 2.0),
        (12.0, 11.0, 2.0),
        (17, 13, 2.0),
    ]

    rrt_map = RRTMap(area=[(-2.0, -2.0), (20.0, 20.0)], obstacles=obstacles)
    rrt_parameter = RRTParameter(start=[0.0, 0.0], goal=[18.0, 18.0], expand_dis=2.0, max_iter=200,
                                 animation=animation)
    rrt_planner = RRTPlanner(rrt_map, rrt_parameter)
