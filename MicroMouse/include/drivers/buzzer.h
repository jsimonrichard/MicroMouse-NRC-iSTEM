#include <vector>

using namespace std;

#ifndef HEADER_BUZZER
#define HEADER_BUZZER

namespace drivers {
  class Buzzer {
    public:
      Buzzer(int pin);
      void play(vector<int[2]> sound);
    
    private:
      int pin;
  };
}

#endif
