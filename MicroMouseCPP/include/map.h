#include <vector>

#ifndef HEADER_MAP
#define HEADER_MAP
  namespace map {
    class Node {
      public:
        int pos[2];
        bool open[4];
        int connected[4] = {0,0,0,0};

        Node(int x, int y);
        void setOpen(int dirIndex);
        void connect(int nodeIndex);
    };

    class Map {
      public:
        void visit(int pos[2]);
        int node(int pos[2]); // Returns index of a node

      private:
        std::vector<Node> nodes;
    };
  }
#endif