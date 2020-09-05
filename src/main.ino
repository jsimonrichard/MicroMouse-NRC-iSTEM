// Drivers
#include "drivers/drivers.h"
#include "states/states.h"

State state;

void setup() {
  // Setup
  Serial.begin(9600);
  drivers::setup();

  drivers::buzzer::playStandBySound();
  state = states::StandBy;
}

void loop() {
  // Check State
  switch (state) {
    case states::StandBy:
      states::standBy(&state);
      break;
    case states::StartUp:
      states::startUp(&state);
      break;
    case states::BuildMap:
      states::buildMap(&state);
      break;
    case states::Home:
      states::home(&state);
      break;
    case states::Dash:
      states::dash(&state);
      break;
  }

  delay(10);
}
