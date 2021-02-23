#include <Arduino.h>
#include "drivers/ping.h"

namespace drivers {

  PingData PingData::operator+(PingData a) {
    return {time-a.time, front+a.front, back+a.back, left+a.left, right+a.right};
  }

  PingData PingData::operator-(PingData a) {
    return {time-a.time, front-a.front, back-a.back, left-a.left, right-a.right};
  }

  /* PingSensor Class */
  PingSensor::PingSensor(int e_pin) {
    echo_pin = e_pin;
    pinMode(echo_pin, INPUT);
  }

  double PingSensor::read() {
    return pulseIn(echo_pin, HIGH) * 0.01348833 / 2;
  }

  /* PingCollection Class */
  PingCollection::PingCollection(
    int t_pin,
    PingSensor *f_sensor, PingSensor *b_sensor, PingSensor *l_sensor, PingSensor *r_sensor):
    front_sensor(f_sensor), back_sensor(b_sensor), left_sensor(l_sensor), right_sensor(r_sensor) {
      trig_pin = t_pin;
      pinMode(trig_pin, OUTPUT);
  }

  PingData PingCollection::ping() {
      digitalWrite(trig_pin, LOW); //turn off the Trig pin in case it was on before
      delayMicroseconds(2); //a very short break

      digitalWrite(trig_pin, HIGH); //turn on the Trig pin to send a sound wave
      delayMicroseconds(10); //a short break to let the operation happen
      digitalWrite(trig_pin, LOW); //turn off the Trig pin to end the sound wave output

      PingData output;
      output.time = millis();

      output.front = front_sensor->read();
      output.back = back_sensor->read();
      output.left = left_sensor->read();
      output.right = right_sensor->read();

      return output;
  }
}
