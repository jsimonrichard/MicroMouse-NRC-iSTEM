#include "common.h"

// Actors
#include "actors/robot.h"
#include "actors/maze.h"

/* Driver Initiation*/
void init() { 
    left_motor = new Motor(MOTOR_L_PIN);
    right_motor = new Motor(MOTOR_R_PIN);

    front_ping_sensor = new PingSensor(PING_ECHO_PIN_F);
    back_ping_sensor = new PingSensor(PING_ECHO_PIN_B);
    left_ping_sensor = new PingSensor(PING_ECHO_PIN_L);
    right_ping_sensor = new PingSensor(PING_ECHO_PIN_R);

    ping_collection = new PingCollection(PING_TRIG_PIN,
        front_ping_sensor,
        back_ping_sensor,
        left_ping_sensor,
        right_ping_sensor);

    button = new Button(BUTTON_PIN);
    buzzer = new Buzzer(BUZZER_PIN);
}