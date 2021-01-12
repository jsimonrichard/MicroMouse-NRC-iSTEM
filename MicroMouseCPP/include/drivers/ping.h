#define TRIG_PIN 9

#define ECHO_PINF 1
#define ECHO_PINB 2
#define ECHO_PINL 3
#define ECHO_PINR 4

#ifndef HEADER_PING
  #define HEADER_PING
    namespace drivers {
      namespace ping {
        struct PingData {
          unsigned long time; // in milliseconds

          double front;
          double back;
          double left;
          double right;

          PingData operator+(PingData a) {
            return {time-a.time, front+a.front, back+a.back, left+a.left, right+a.right};
          }

          PingData operator-(PingData a) {
            return {time-a.time, front-a.front, back-a.back, left-a.left, right-a.right};
          }

          double avg() {
            return (front+back+left+right) / 4;
          }
        };
        
        void setup( void );
        PingData ping( void );
      }
    }
#endif
