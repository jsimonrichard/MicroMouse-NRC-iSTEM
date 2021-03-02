from machine import Pin, PWM

class Motor:
    def __init__(self, pins):
        self.forward = PWM(Pin(pins["forward"]))
        self.backward = PWM(Pin(pins["backward"]))

    def set(self, pwm):
        if pwm >= 0:
            self.forward.duty_u16(pwm)
            self.backward.duty_u16(0)
        else:
            self.backward.duty_u16(pwm)
            self.forward.duty_u16(0)

class TwoWheel:
    def __init__(self, pins):
        self.l_motor = Motor(pins["left"])
        self.r_motor = Motor(pins["right"])
