from ulab import numpy as np # pylint: disable=import-error

class Maze:
    def __init__(self, unit_size, maze_size, solution_units):
        self._unit_size = unit_size
        self._maze_size = maze_size
        self.targets = solution_units

        self._h_walls = np.ones((self._maze_size[0], self._maze_size[1]-1), dtype=bool)
        self._v_walls = np.ones((self._maze_size[0]-1, self._maze_size[1]), dtype=bool)
        self._visited = np.zeros(self._maze_size, dtype=bool)

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
            if self._v_walls[i, pos[1]]:
                ni = pos[0] - i
                break

        pi = self._maze_size[0] - pos[0]
        for i in range(pos[0], self._maze_size[0]-1):
            if self._v_walls[i, pos[1]]:
                pi = i - pos[0]
                break

        nj = pos[1]
        for j in reversed(range(pos[1]-1)):
            if self._h_walls[pos[0], j]:
                nj = pos[1] - j
                break

        pj = self._maze_size[1] - pos[1]
        for j in range(pos[1], self._maze_size[1]-1):
            if self._h_walls[pos[0], j]:
                pj = j - pos[1]
                break

        return (pi, nj, ni, pj)

    def path(self, start_pos, targets):
        def _solve(pos, targets):
            if pos in targets:
                yield [pos]
            else:
                i,j = pos

                if i > 0 and not self._v_walls[i-1,j]:
                    yield [pos]+next(_solve((i-1, j), targets))

                if i < self._maze_size[0]-1 and not self._v_walls[i,j]:
                    yield [pos]+next(_solve((i+1,j), targets))

                if j > 0 and not self._h_walls[i,j-1]:
                    yield [pos]+next(_solve((i,j-1), targets))

                if j < self._maze_size[1]-1 and not self._h_walls[i,j]:
                    yield [pos]+next(_solve((i,j+1), targets))

        return next(_solve(start_pos, targets))

    def solve_maze(self, pos):
        return self.path(pos, self.targets)
