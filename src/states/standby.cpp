#include "states/standby.h"
#include "states/startup.h"

// Drivers
#include "drivers/motor.h"
#include "drivers/ping.h"
#include "drivers/button.h"
#include "drivers/buzzer.h"

using namespace drivers;

namespace states {
  namespace standBy {
    void start(State *state) {
      buzzer::playStandBySound();
      *state = StandBy;
    }

    void loop(State *state) {
      if(drivers::button::isPressed()) {
        startUp::start(state);
      }
    }
  }
}
