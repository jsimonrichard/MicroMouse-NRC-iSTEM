#include <Arduino.h>

#include "common.h"

// Drivers
#include "drivers/motor.h"
#include "drivers/ping.h"
#include "drivers/button.h"
#include "drivers/buzzer.h"

// Actors
#include "actors/maze.h"
#include "actors/robot.h"

using namespace drivers;

void setup() {
  // Setup Serial
  Serial.begin(9600);

  // Play Sound
  buzzer->play(SOUND_ON);
}

void loop() {
  robot->loop();
  delay(10);
}
