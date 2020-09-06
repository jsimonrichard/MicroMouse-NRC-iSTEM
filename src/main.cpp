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

  standBy::start(&state);
}

void loop() {
  // Check State
  switch (state) {
    case StandBy:
      standBy::loop(&state);
      break;
    case StartUp:
      startUp::loop(&state);
      break;
    case BuildMap:
      buildMap::loop(&state);
      break;
    case Home:
      home::loop(&state);
      break;
    case Dash:
      dash::loop(&state);
      break;
  }
  
  delay(10);
}
