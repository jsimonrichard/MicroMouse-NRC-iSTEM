#include "../drivers/drivers.h"

namespace states {
  void standBy(State *state) {
    if(drivers::button::isPressed()) {
      // Switch state
      drivers::buzzer::playStartSound();
      state = StartUp;
    }
  }
}
