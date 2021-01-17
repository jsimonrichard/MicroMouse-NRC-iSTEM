#ifndef HEADER_MAZE
#define HEADER_MAZE

class Maze {
  public:
    bool visited[10][10] = { false };
    bool wall_open[10][10][2] = { false }; // [Right, Bottom] for each cell (some values for edge/corner cells are invalid)
};

#endif