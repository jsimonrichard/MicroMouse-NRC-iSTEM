#define BUZZER_PIN 0

#ifndef HEADER_BUZZER
  #define HEADER_BUZZER
    namespace drivers {
      namespace buzzer {
        void setup( void );

        void playStandBySound( void );
        void playStartUpSound( void );
        void playBuildMapSound( void );
        void playHomeSound( void );
        void playDashSound( void );
      }
    }
#endif
