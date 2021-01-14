#include <Arduino.h>
#include "drivers/motor.h"

namespace drivers {
  namespace motor {
    void setup() {
        //Set pins as outputs
        pinMode(MOTOR_L_PIN, OUTPUT);
        pinMode(MOTOR_R_PIN, OUTPUT);
    }

    void setMotors(int lspeed, int rspeed) {
        
    }
  }
}
