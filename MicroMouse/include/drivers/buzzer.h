#include <vector>
#include <array>

using namespace std;

#ifndef HEADER_BUZZER
#define HEADER_BUZZER

namespace drivers {
  class Buzzer {
    public:
      Buzzer(int pin);
      void play(vector<array<int,2>> sound);
    
    private:
      int pin;
  };
}

#endif
