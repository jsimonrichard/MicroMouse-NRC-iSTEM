#include <vector>

#ifndef HEADER_MAP
#define HEADER_MAP
  namespace maze {
    class Maze {
      public:
        bool visited[10][10] = { false };
        bool open[10][10][2] = { false }; // [Right, Bottom] for each cell (some values for edge/corner cells are invalid)

    };
  }
#endif