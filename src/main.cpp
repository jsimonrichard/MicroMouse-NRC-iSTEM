#include <Arduino.h>

// Drivers
#include "drivers/motor.h"
#include "drivers/ping.h"
#include "drivers/button.h"
#include "drivers/buzzer.h"

// States
#include "states/standby.h"
#include "states/startup.h"
#include "states/buildmap.h"
#include "states/home.h"
#include "states/dash.h"

using namespace drivers;
using namespace states;

State state;

void setup() {
  // Setup Serial
  Serial.begin(9600);

  // Setup Drivers
  motor::setup();
  ping::setup();
  button::setup();
  buzzer::setup();

  buzzer::playStandBySound();
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
