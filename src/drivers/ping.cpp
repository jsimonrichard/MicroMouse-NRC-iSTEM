#include <Arduino.h>
#include "drivers/ping.h"

namespace drivers {
  namespace ping {
    void setup(void) {
      pinMode(TRIG_PIN, OUTPUT);

      pinMode(ECHO_PINF, INPUT);
      pinMode(ECHO_PINB, INPUT);
      pinMode(ECHO_PINL, INPUT);
      pinMode(ECHO_PINR, INPUT);
    }

    PingData ping() { // returns inches
      digitalWrite(TRIG_PIN, LOW); //turn off the Trig pin in case it was on before
      delayMicroseconds(2); //a very short break

      digitalWrite(TRIG_PIN, HIGH); //turn on the Trig pin to send a sound wave
      delayMicroseconds(10); //a short break to let the operation happen
      digitalWrite(TRIG_PIN, LOW); //turn off the Trig pin to end the sound wave output

      PingData output;
      output.time = millis();

      output.front = pulseIn(ECHO_PINF, HIGH) * 0.01348833 / 2;
      output.back = pulseIn(ECHO_PINB, HIGH) * 0.01348833 / 2;
      output.left = pulseIn(ECHO_PINL, HIGH) * 0.01348833 / 2;
      output.right = pulseIn(ECHO_PINR, HIGH) * 0.01348833 / 2;

      return output;
    }
  }
}
