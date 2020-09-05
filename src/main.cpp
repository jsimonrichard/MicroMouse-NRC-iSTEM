#include <Arduino.h>

// Drivers
#include "drivers/drivers.h"
#include "states/states.h"

using namespace states;

State state;

void setup() {
  // Setup
  Serial.begin(9600);
  drivers::setup();

  drivers::buzzer::playStandBySound();
  state = StandBy;
}

void loop() {
  // Check State
  switch (state) {
    case StandBy:
      standBy(&state);
      break;
    case StartUp:
      startUp(&state);
      break;
    case BuildMap:
      buildMap(&state);
      break;
    case Home:
      home(&state);
      break;
    case Dash:
      dash(&state);
      break;
  }
  
  delay(10);
}
