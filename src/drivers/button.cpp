#include "Arduino.h"

namespace drivers {
  namespace button {
    void setup() {
        pinMode(pin, INPUT);
    }

    bool isPressed() {
        bool state = digitalRead(BUTTON_PIN);
        if(state == HIGH) {
            return true;
        } else if (state == LOW) {
            return false;
        }
    }
  }
}
