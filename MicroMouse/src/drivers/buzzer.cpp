#include <Arduino.h>
#include "drivers/buzzer.h"

namespace drivers {
  Buzzer::Buzzer(int buzzer_pin) {
    pin = buzzer_pin;
    pinMode(pin, OUTPUT);
  }

  void Buzzer::play(vector<array<int,2>> song) {
      for (array<int,2> note : song) {
        if(note[0] == 0) {
          delay(note[1]);
        } else {
        tone(pin, note[0], note[1]); 
        }
      } 
  }
}
