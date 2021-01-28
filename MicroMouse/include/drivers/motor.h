

#ifndef HEADER_MOTOR
#define HEADER_MOTOR

namespace drivers {
  class Motor {
    public:
      Motor(int pin);

      void set(int speed);
      int get() { return speed; };

    private:
      int pin;
      int speed;
  };
}

#endif
