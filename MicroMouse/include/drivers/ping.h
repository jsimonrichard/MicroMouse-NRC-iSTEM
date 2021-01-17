#ifndef HEADER_PING
#define HEADER_PING

namespace drivers {
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
        int trig_pin,
        PingSensor front_sensor,
        PingSensor back_sensor,
        PingSensor left_sensor,
        PingSensor right_sensor);
      
      PingData ping();
    
    private:
      int trig_pin;

      PingSensor front_sensor;
      PingSensor back_sensor;
      PingSensor left_sensor;
      PingSensor right_sensor;
  };
}

#endif
