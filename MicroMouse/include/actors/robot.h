#include "drivers/ping.h"

using namespace drivers;

#ifndef HEADER_ROBOT
#define HEADER_ROBOT

struct Movement {
    int i;
    int j;
};

struct Position: Movement {
    struct Position& operator+=(const Movement& rhs) { i += rhs.i; j += rhs.j; return *this; }
    struct Movement& operator-=(const Position& rhs) { i -= rhs.i; j -= rhs.j; return *this; }
};

Position operator+(Position a, Movement b) { return a+=b; }; // Position + Movement = Position
Movement operator-(Position a, Position b) { return a-=b; }; // Posiiton - Position = Movement

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