#include "../drivers/drivers.h"

namespace states {
  void startUp(State *state) {
    // Get square with the course

    // Switch state
    drivers::buzzer::playBuildMapSound();
    state = BuildMap;
  }
}
