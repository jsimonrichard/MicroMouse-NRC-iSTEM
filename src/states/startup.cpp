#include "states/startup.h"

// Drivers
#include "drivers/motor.h"
#include "drivers/ping.h"
#include "drivers/button.h"
#include "drivers/buzzer.h"

using namespace drivers;

namespace states {
  namespace startUp {

    ping::PingResponse lastResponse;

    void start(State *state) {
      buzzer::playStartUpSound();
      *state = StartUp;

      lastResponse = ping::ping();
    }

    void loop(State *state) {
      // Get square with the course
      ping::PingResponse response = ping::ping();

      lastResponse = response;
    }
  }
}
