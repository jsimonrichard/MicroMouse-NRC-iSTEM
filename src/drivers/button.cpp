#include <Arduino.h>
#include "drivers/button.h"

namespace drivers {
  namespace button {
    void setup() {
        pinMode(BUTTON_PIN, INPUT);
    }

    bool isPressed() {
        bool state = digitalRead(BUTTON_PIN);
        if(state == HIGH) {
            return true;
        } else {
            return false;
        }
    }
  }
}
