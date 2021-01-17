#include <Arduino.h>
#include "drivers/buzzer.h"

namespace drivers {
  Buzzer::Buzzer(int buzzer_pin) {
    pin = buzzer_pin;
    pinMode(pin, OUTPUT);
  }

  void Buzzer::play(vector<int[2]> sound) {
      vector<int[2]>::iterator ptr;
      for (ptr = sound.begin(); ptr < sound.end(); ptr++) 
        tone(pin, *ptr[0], *ptr[1]); 
  }
}
