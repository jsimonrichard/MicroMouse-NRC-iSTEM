#define BUTTON_PIN 0

#ifndef HEADER_BUTTON
  #define HEADER_BUTTON
    namespace drivers {
      namespace button {
      public:
        void setup( void );
        bool isPressed( void );
      }
    }
#endif
