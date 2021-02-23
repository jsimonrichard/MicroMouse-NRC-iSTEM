#include "drivers/ping.h"

using namespace drivers;

#ifndef HEADER_ROBOT
#define HEADER_ROBOT

struct Movement {
    int i;
    int j;
};

struct Position {
    int i;
    int j;
    Position operator+(Movement a); // Position + Movement = Position
    Movement operator-(Position a); // Posiiton - Position = Movement
};


enum State {
    StandBy,
    Crawl,
    Homing,
    Dash
};

class Robot {
    public:
        void loop();

        State get_state() { return state; };
        void set_state(State new_state) { state = new_state; };

        void set_walls(PingData ping_data);

    private:
        State state;
        Position pos;
        Movement orientation; 
};

#endif