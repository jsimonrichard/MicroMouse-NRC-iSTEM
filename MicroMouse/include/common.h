// Drivers
#include "drivers/motor.h"
#include "drivers/ping.h"
#include "drivers/button.h"
#include "drivers/buzzer.h"

// Actors
#include "actors/robot.h"
#include "actors/maze.h"

/* Drivers */
extern Motor left_motor;
extern Motor right_motor;

PingCollection ping_collection;

Button button;
Buzzer buzzer;

/* Actors */
Robot robot;
Maze maze;