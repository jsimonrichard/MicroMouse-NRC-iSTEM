#include <Arduino.h>
#include "drivers/button.h"

namespace drivers {
  Button::Button(int button_pin) {
    pin = button_pin;
    pinMode(pin, INPUT);
  }

  bool Button::isPressed() {
      return digitalRead(pin) == HIGH;
  }
}
