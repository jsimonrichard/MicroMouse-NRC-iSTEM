#include "states/standby.h"

// Drivers
#include "drivers/motor.h"
#include "drivers/ping.h"
#include "drivers/button.h"
#include "drivers/buzzer.h"

namespace states {
  void standBy(State *state) {
    if(drivers::button::isPressed()) {
      // Switch state
      drivers::buzzer::playStartSound();
      *state = StartUp;
    }
  }
}
