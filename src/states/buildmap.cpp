#include "states/buildmap.h"

// Drivers
#include "drivers/motor.h"
#include "drivers/ping.h"
#include "drivers/button.h"
#include "drivers/buzzer.h"

//Actions
#include "actions/actions.h"

using namespace drivers;

namespace states {
  namespace buildMap {
    actions::Action action;

    void start(State *state) {
      buzzer::playBuildMapSound();
      *state = BuildMap;
    }

    void loop(State *state) {
      
    }
  }
}
