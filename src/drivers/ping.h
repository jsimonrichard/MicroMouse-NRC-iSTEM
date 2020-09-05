#define TRIG_PIN 9;
#define ECHO_PINS {1, 2, 3, 4};

#ifndef HEADER_PING
  #define HEADER_PING
    namespace drivers {
      namespace ping {
      public:
        void setup( void );
        void ping( int index );

        struct PingResponse {
          unsigned long time;
          int values[ sizeof(ECHO_PINS)/sizeof(ECHO_PINS[0]) ];
        }
      }
    }
#endif
