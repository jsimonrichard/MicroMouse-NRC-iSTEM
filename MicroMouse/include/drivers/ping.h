#ifndef HEADER_PING
#define HEADER_PING

namespace drivers {
  struct PingData {
    unsigned long time; // in milliseconds

    double front;
    double back;
    double left;
    double right;

    PingData operator+(PingData a);
    PingData operator-(PingData a); 
  };

  class PingSensor {
    public:
      PingSensor(int echo_pin);
      double read();
    
    private:
      int echo_pin;
  };

  class PingCollection {
    public:
      PingCollection(
        int t_pin,
        PingSensor *f_sensor,
        PingSensor *b_sensor,
        PingSensor *l_sensor,
        PingSensor *r_sensor);
      
      PingData ping();
    
    private:
      int trig_pin;

      PingSensor *front_sensor;
      PingSensor *back_sensor;
      PingSensor *left_sensor;
      PingSensor *right_sensor;
  };
}

#endif
