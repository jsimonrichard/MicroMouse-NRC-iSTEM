#include <Arduino.h>
#include "drivers/motor.h"

namespace drivers {
  Motor::Motor(int motor_pin) {
    pin = motor_pin;
    pinMode(pin, OUTPUT);
  }

  void Motor::set(int motor_speed) {
    speed = motor_speed;
    // Set motor speed
  }
}
