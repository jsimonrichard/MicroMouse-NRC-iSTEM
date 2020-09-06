#define MOTOR_L_PIN 15
#define MOTOR_R_PIN 16

#ifndef HEADER_MOTOR
  #define HEADER_MOTOR
    namespace drivers {
      namespace motor {
        void setup( void );

        void setMotors( int lspeed, int rspeed );
      }
    }
#endif
