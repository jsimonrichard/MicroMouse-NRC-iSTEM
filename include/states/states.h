#ifndef HEADER_STATES
#define HEADER_STATES
  namespace states {
    enum State {
      StandBy,
      StartUp,
      BuildMap,
      Home,
      Dash
    };
  }
#endif

#include "standby.h"
#include "startup.h"
#include "buildmap.h"
#include "home.h"
#include "dash.h"
