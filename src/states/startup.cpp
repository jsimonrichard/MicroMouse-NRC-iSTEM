#include "states/startup.h"

// Drivers
#include "drivers/motor.h"
#include "drivers/ping.h"
#include "drivers/button.h"
#include "drivers/buzzer.h"

namespace states {
  void startUp(State *state) {
    // Get square with the course

    // Switch state
    drivers::buzzer::playBuildMapSound();
    *state = BuildMap;
  }
}
