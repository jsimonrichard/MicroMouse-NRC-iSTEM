from machine import Pin, PWM
from utime import sleep_ms

from config import L_MOTOR_DRIFT, R_MOTOR_DRIFT

class Motor:
    def __init__(self, pins):
        self.forward = PWM(Pin(pins["forward"]))
        self.backward = PWM(Pin(pins["backward"]))

    def set(self, pwm):
        if pwm >= 0:
            self.forward.duty_u16(pwm)
            self.backward.duty_u16(0)
        else:
            self.backward.duty_u16(-pwm)
            self.forward.duty_u16(0)

class TwoWheel:
    def __init__(self, pins, axil_length):
        self.l_motor = Motor(pins["left"])
        self.r_motor = Motor(pins["right"])
        self.width = axil_length

    def rot(self, pwm, r):
        if r == 0:
            lpwm = pwm
            rpwm = pwm
        elif r > 0:
            lpwm = pwm
            rpwm = -( r-self.width/2 )/( r+self.width/2 ) * pwm
        elif r < 0:
            lpwm = -( r+self.width/2)/( r-self.width/2 ) * pwm
            rpwm = pwm

        self.l_motor.set(int(L_MOTOR_DRIFT*lpwm))
        self.r_motor.set(int(R_MOTOR_DRIFT*rpwm))

    def straight(self, pwm):
        self.l_motor.set(int(L_MOTOR_DRIFT*pwm))
        self.r_motor.set(-int(R_MOTOR_DRIFT*pwm))

    def stop(self, jerk=0):
        if jerk:
            self.l_motor.set(int(jerk*20000))
            self.r_motor.set(int(-jerk*20000))
            sleep_ms(20)

        self.l_motor.set(0)
        self.r_motor.set(0)
