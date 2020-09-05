#define BUZZER_PIN 0

#ifndef HEADER_BUZZER
  #define HEADER_BUZZER
    namespace drivers {
      namespace buzzer {
      public:
        void setup( void );

        void playStartSound( void );
        void playMapCompleteSound( void );
        void playSprintSound( void );
        void playFinishSound( void );
      }
    }
#endif
