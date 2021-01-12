#include "states.h"

#ifndef HEADER_STANDBY
#define HEADER_STANDBY
  namespace states {
    namespace standBy {
      void start( State *state );
      void loop( State *state );
    }
  }
#endif
