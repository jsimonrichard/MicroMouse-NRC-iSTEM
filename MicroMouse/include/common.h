#include "config.h"

// Drivers
#include "drivers/motor.h"
#include "drivers/ping.h"
#include "drivers/button.h"
#include "drivers/buzzer.h"

// Actors
#include "actors/robot.h"
#include "actors/maze.h"

/* Driver Initiation*/
Motor left_motor(MOTOR_L_PIN);
Motor right_motor(MOTOR_R_PIN);

PingSensor front_ping_sensor(PING_ECHO_PIN_F);
PingSensor back_ping_sensor(PING_ECHO_PIN_B);
PingSensor left_ping_sensor(PING_ECHO_PIN_L);
PingSensor right_ping_sensor(PING_ECHO_PIN_R);

PingCollection ping_collection(PING_TRIG_PIN,
  front_ping_sensor,
  back_ping_sensor,
  left_ping_sensor,
  right_ping_sensor);

Button button(BUTTON_PIN);
Buzzer buzzer(BUZZER_PIN);

/* Actors */
Robot robot;
Maze maze;