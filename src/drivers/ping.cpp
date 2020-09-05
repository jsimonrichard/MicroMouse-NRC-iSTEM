#include "Arduino.h"

namespace drivers {
  namespace ping {
    void setup(void) {
        pinMode(TRIG_PIN, OUTPUT);

        for (int i = 0; i < sizeof(ECHO_PINS)/sizeof(ECHO_PINS[0]); i++) {
            pinMode(ECHO_PINS[i], INPUT);
        }
    }

    unsigned long ping(int index) { // returns inches
        digitalWrite(TRIG_PIN, LOW); //turn off the Trig pin incase it was on before
        delayMicroseconds(2); //a very short break

        digitalWrite(TRIG_PIN, HIGH); //turn on the Trig pin to send a sound wave
        delayMicroseconds(10); //a short break to let the operation happen
        digitalWrite(TRIG_PIN, LOW); //turn off the Trig pin to end the sound wave output

        long dur = pulseIn(ECHO_PINS[index], HIGH); //sensor the sound wave reflection time
        unsigned long dis = dur * 0.01348833 / 2;

        return dis;
    }
  }
}
