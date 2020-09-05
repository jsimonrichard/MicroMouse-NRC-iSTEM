#include "Arduino.h"

namespace driver {
  namespace motor {

    void setup() {
        //Set pins as outputs
        pinMode(MOTOR_L_PIN, OUTPUT);
        pinMode(MOTOR_R_PIN, OUTPUT);
    }

    void setMotorL(int speed) { // Speed: pwm forward if > 0, -pwm backwards if < 0
        if (speed > 0)
        {
            // speed = pwm forward
            analogWrite(MOTOR_L_PIN, speed/2+1000);
        } else if (speed < 0) {
            // -speed = pwm backward
            analogWrite(MOTOR_L_PIN, 1000+speed);
        }
    }

    void setMotorR(int speed) { // Speed: pwm forward if > 0, -pwm backwards if < 0
        if (speed > 0)
        {
            // speed = pwm forward
            analogWrite(MOTOR_R_PIN, speed/2+1000);
        } else if (speed < 0) {
            // -speed = pwm backward
            analogWrite(MOTOR_R_PIN, 1000+speed);
        }
    }

    void stopMotorL() {
        analogWrite(MOTOR_L_PIN, 0);
    }

    void stopMotorR() {
        analogWrite(MOTOR_R_PIN, 0);
    }
  }
}
