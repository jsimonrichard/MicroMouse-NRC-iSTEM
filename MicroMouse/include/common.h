#include "config.h"

// Drivers
#include "drivers/motor.h"
#include "drivers/ping.h"
#include "drivers/button.h"
#include "drivers/buzzer.h"

// Actors
#include "actors/robot.h"
#include "actors/maze.h"

#ifndef HEADER_COMMON
#define HEADER_COMMON

/* Driver Initiation*/
Motor *left_motor, *right_motor;
extern Motor *left_motor, *right_motor;

PingSensor *front_ping_sensor, *back_ping_sensor, *left_ping_sensor, *right_ping_sensor;
extern PingSensor *front_ping_sensor, *back_ping_sensor, *left_ping_sensor, *right_ping_sensor;
PingCollection *ping_collection;
extern PingCollection *ping_collection;

Button* button;
extern Button* button;
Buzzer* buzzer;
extern Buzzer* buzzer;

/* Actors */
Robot* robot;
extern Robot* robot;
Maze* maze;
extern Maze* maze;

#endif