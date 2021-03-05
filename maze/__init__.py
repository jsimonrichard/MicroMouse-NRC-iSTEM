from ulab import numpy as np # pylint: disable=import-error

class Maze:
    def __init__(self, unit_size, maze_size, solutions):
        self.unit_size = unit_size
        self.maze_size = maze_size
        self.solutions = solutions

        self._h_walls = np.ones((maze_size[0], maze_size[1]-1))
        self._v_walls = np.ones((maze_size[0]-1, maze_size[1]))
        self._visited = np.zeros(maze_size)

    def _parse_ping(self, distances, orientation):
        ...

    def _get_expected(self, pos):
        """
        Returns the expected number units to the first walls in all directions
        """
        if not self._visited[pos]:
            return False

        ni = pos[0]
        for i in reversed(range(pos[0]-1)):
            if self._v_walls[i][ pos[1] ]:
                ni = pos[0] - i
                break

        pi = self.maze_size[0] - pos[0]
        for i in range(pos[0], self.maze_size[0]-1):
            if self._v_walls[i][ pos[1] ]:
                pi = i - pos[0]
                break

        nj = pos[1]
        for j in reversed(range(pos[1]-1)):
            if self._h_walls[ pos[0] ][j]:
                nj = pos[1] - j
                break

        pj = self.maze_size[1] - pos[1]
        for j in range(pos[1], self.maze_size[1]-1):
            if self._h_walls[ pos[0] ][j]:
                pj = j - pos[1]
                break

        return (pi, nj, ni, pj)


    def _gen_graph(self):
        ...
