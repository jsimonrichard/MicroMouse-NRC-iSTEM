#define TRIG_PIN 9;
#define ECHO_PINS {1, 2, 3, 4}

#ifndef HEADER_PING
  #define HEADER_PING
    namespace drivers {
      namespace ping {
        void setup( void );
        void ping( int index );

        struct PingResponse {
          unsigned long time;
          int values[4];
        };
      }
    }
#endif
