#include "motor.h"
#include "ping.h"
#include "button.h"
#include "buzzer.h"

#ifndef HEADER_DRIVERS
  #define HEADER_DRIVERS
    namespace drivers {
      void setup( void ) {
        motor::setup();
        ping::setup();
        button::setup();
        buzzer::setup();
      }
    }
#endif
