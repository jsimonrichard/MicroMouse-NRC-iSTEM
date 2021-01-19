#include <vector>

#include "config.h"
#include "robot.h"
#include "drivers/ping.h"

using namespace std;

#ifndef HEADER_MAZE
#define HEADER_MAZE

typedef vector<int[2]> path;

class Maze {
  public:
    void set_walls(Position pos, PingData sensor_data);
    path solve();

  private:
    void trim();
    path solve_recursive();

    bool visited[MAZE_WIDTH][MAZE_HEIGHT] = { false };
    bool wall_open[MAZE_WIDTH][MAZE_HEIGHT][2] = { false }; // [Right, Bottom] for each cell (some values for edge/corner cells are invalid)
};

#endif