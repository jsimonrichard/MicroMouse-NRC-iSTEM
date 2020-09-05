#define MOTOR_L_PIN 15
#define MOTOR_R_PIN 16

#ifndef HEADER_MOTOR
  #define HEADER_MOTOR
  namespace drivers {
    namespace motor {
      void setup( void );

      void setMotorL( int speed );
      void setMotorR( int speed );

      void stopMotorL( void );
      void stopMotorR( void );
    }
  }

#endif
