#ifndef HEADER_BUTTON
#define HEADER_BUTTON

namespace drivers {
  class Button {
    public:
      Button(int button_pin);
      bool isPressed( void );
    
    private:
      int pin;
  };
}

#endif