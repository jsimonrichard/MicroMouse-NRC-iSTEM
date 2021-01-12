#include "states/startup.h"
#include "states/buildmap.h"

#include <cmath>

// Drivers
#include "drivers/motor.h"
#include "drivers/ping.h"
#include "drivers/button.h"
#include "drivers/buzzer.h"

using namespace drivers;

namespace states {
  namespace startUp {

    ping::PingData lastResponse;
    int squareSpeed = 1; // > 0 starts clockwise, < 0 starts counter-clockwise

    void start(State *state) {
      buzzer::playStartUpSound();
      *state = StartUp;

      // Get first ping
      lastResponse = ping::ping();

      // Start moving
      motor::setMotors(squareSpeed, -squareSpeed);
    }

    void loop(State *state) {
      // Get square with the course
      ping::PingData response = ping::ping();
      ping::PingData diff = response - lastResponse;
      double avg = diff.avg();

      if(std::abs(avg) > 0.1) {
        // Not square enough

        // Check if it overshot
        if(avg > 0) {
          squareSpeed *= -1;
        }

        // Move at speed proportional to diff
        motor::setMotors(-avg*squareSpeed, avg*squareSpeed);

        lastResponse = response;

      } else {
        // It's square
        motor::setMotors(0, 0);
        buildMap::start(state);
      }
    }
  }
}
