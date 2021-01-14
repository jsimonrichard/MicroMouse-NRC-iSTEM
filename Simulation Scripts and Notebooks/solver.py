class Solver:
    loop = {'E':'N', 'N':'W', 'W':'S', 'S':'E'}
    move = {'E': (1,0), 'N': (0,-1), 'W': (-1,0), 'S': (0,1)}

    def __init__(self, maze, target):
        self.maze = maze
        self.start = (maze.ix, maze.iy)
        self.target = target
    
    def solve(self):
        steps = []
        
        i = self.start[0]
        j = self.start[1]
        cell = self.maze.maze_map[i][j]
        steps.append(cell)
        
        orientation = 'E'
        while (cell.x, cell.y) != self.target:
            while cell.walls[orientation]:
                orientation = self.loop[orientation]
            move = self.move[orientation]
            i += move[0]
            j += move[1]

            cell = self.maze.maze_map[i][j]

            steps.append(move)
        
        return steps