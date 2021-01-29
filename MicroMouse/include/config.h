#include <vector>
#include <array>
using namespace std;

#ifndef HEADER_CONFIG
#define HEADER_CONFIG

/* GPIO Pin Configuration */

#define BUTTON_PIN 0

#define BUZZER_PIN 0

#define MOTOR_L_PIN 15
#define MOTOR_R_PIN 16

#define PING_TRIG_PIN 9
#define PING_ECHO_PIN_F 1
#define PING_ECHO_PIN_B 2
#define PING_ECHO_PIN_L 3
#define PING_ECHO_PIN_R 4

/* Maze Configuration */

#define MAZE_HEIGHT 10
#define MAZE_WIDTH 10

const int MAZE_START[2] = {0,0};
const vector<array<int,2>> MAZE_SOLUTION {
    {4,4},
    {4,5},
    {5,4},
    {5,5}
};

/* Speed Configuration 
Nothing here yet... */


/* Sound Configuration */
typedef vector<array<int,2>> path;

/*
On Sound
E4 for 0.25 seconds
B4 for 0.25 seconds
E5 for 0.25 seconds
G#5 for 0.25 seconds
B5 for 0.25 seconds
*/
const path SOUND_ON {
    {330,250},
    {494,250},
    {659,250},
    {831,250},
    {988,250}
};

/*
Crawl Sound
B5 for 0.25 seconds
*/
const path SOUND_CRAWL {
    {988,250}
};

/*
Homing Sound
B5 for 0.25 seconds
E5 for 0.25 seconds
B4 for 0.25 seconds
*/
const path SOUND_HOMING {
    {988,250},
    {659,250},
    {494,250} 
};

/*
Dash Sound
B4 for 0.25 seconds
Break
B4 for 0.25 seconds
Break
E5 for 0.5 seconds
*/
const path SOUND_DASH {
    {494,250},
    {0,2},
    {494,250},
    {0,2},
    {659,500}
};

#endif /* HEADER_CONFIG */