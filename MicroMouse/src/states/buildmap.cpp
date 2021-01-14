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

      // Create start node
    }

    void loop(State *state) {
      // If at intersection
          // create node
          // connect it with previous
          // pick new direction
      // Else If at deadend
          // go back to last node
          // (do not create node)

      // If moved another unit
          // log in squares visited
    }
  }
}
