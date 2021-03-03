import numpy as np

class Maze:
    def __init__(self, unit_size, maze_size, solutions):
        self.unit_size = unit_size
        self.maze_size = maze_size
        self.solutions = solutions

        self._h_walls = np.ones((maze_size[0]-1, maze_size[1]))
        self._v_walls = np.ones((maze_size[0], maze_size[1]-1))

    def _parse_ping(self, distances, orientation):
        ...

    def _gen_graph(self):
        ...
