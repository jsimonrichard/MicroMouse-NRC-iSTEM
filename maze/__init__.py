def array2d(size, init_value=0):
    return [[init_value for j in range(size[1])] for i in range(size[0])]

class Maze:
    def __init__(self, maze_size):
        self._maze_size = maze_size

        self._h_walls = array2d((self._maze_size[0], self._maze_size[1]-1), init_value=True)
        self._v_walls = array2d((self._maze_size[0]-1, self._maze_size[1]), init_value=True)
        self._visited = array2d(self._maze_size, init_value=False)

    def makeRandom(self):
        from random import choice

        for i in range(self._maze_size[0]):
            for j in range(self._maze_size[1]-1):
                self._h_walls[i][j] = choice([True,False])

        for i in range(self._maze_size[0]-1):
            for j in range(self._maze_size[1]):
                self._v_walls[i][j] = choice([True,False])

    def __str__(self):
        out = "*" + "--*"*self._maze_size[0] + "\n"
        for j in range(self._maze_size[1]-1):
            out += "|  " + "  ".join([ "|" if self._v_walls[i][j] else " " for i in range(self._maze_size[0]-1) ]) + "  |\n"
            out += "*" + "*".join([ "--" if self._h_walls[i][j] else "  " for i in range(self._maze_size[0]) ]) + "*\n"

        out += "|  " + "  ".join([ "|" if self._v_walls[i][ self._maze_size[1]-1 ] else " " for i in range(self._maze_size[0]-1) ]) + "  |\n"
        out += "*" + "--*"*self._maze_size[0] + "\n"
        return out

    def _parse_ping(self, distances, orientation):
        ...

    def getExpected(self, pos):
        """
        Returns the expected number units to the first walls in all directions
        """

        ni = pos[0]
        for i in reversed(range(pos[0])):
            if self._v_walls[i][pos[1]]:
                ni = pos[0] - i - 1
                break

        pi = self._maze_size[0]-1 - pos[0]
        for i in range(pos[0], self._maze_size[0]-1):
            if self._v_walls[i][pos[1]]:
                pi = i - pos[0]
                break

        nj = pos[1]
        for j in reversed(range(pos[1])):
            if self._h_walls[pos[0]][j]:
                nj = pos[1] - j - 1
                break

        pj = self._maze_size[1]-1 - pos[1]
        for j in range(pos[1], self._maze_size[1]-1):
            if self._h_walls[pos[0]][j]:
                pj = j - pos[1]
                break

        return (pi, nj, ni, pj)

    def _solve(self, start_pos, targets=[]):
        parents = {start_pos: None}
        queue = [start_pos]

        # Loop until the queue is empty or the target is found
        solved = False
        end = ()
        while queue:
            i,j = queue.pop(0)

            if (i,j) in targets:
                end = (i,j)
                solved = True
                break

            # Check cardinal directions
            if i > 0 and not self._v_walls[i-1][j] and (i-1,j) not in parents:
                queue.append((i-1,j))
                parents[(i-1,j)] = (i,j)

            if i < self._maze_size[0]-1 and not self._v_walls[i][j] and (i+1,j) not in parents:
                queue.append((i+1,j))
                parents[(i+1,j)] = (i,j)

            if j > 0 and not self._h_walls[i][j-1] and (i,j-1) not in parents:
                queue.append((i,j-1))
                parents[(i,j-1)] = (i,j)

            if j < self._maze_size[1]-1 and not self._h_walls[i][j] and (i,j+1) not in parents:
                queue.append((i,j+1))
                parents[(i,j+1)] = (i,j)

        if targets:
            if not solved:
                raise Exception("Path could not be solved")
            else:
                return (parents, end)
        else:
            return parents

    def solvePath(self, start_pos, targets):
        parents, end = self._solve(start_pos, targets=targets)

        path = []
        pos = end
        while pos:
            path.append(pos)
            pos = parents[pos]

        return path
