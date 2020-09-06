#define TRIG_PIN 9

#define ECHO_PINF 1
#define ECHO_PINB 2
#define ECHO_PINL 3
#define ECHO_PINR 4

#ifndef HEADER_PING
  #define HEADER_PING
    namespace drivers {
      namespace ping {
        struct PingResponse {
          unsigned long time;

          double front;
          double back;
          double left;
          double right;
        };
        
        void setup( void );
        PingResponse ping( void );
      }
    }
#endif
