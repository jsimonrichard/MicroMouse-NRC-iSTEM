from machine import Pin, PWM
from utime import sleep_ms

class Buzzer:
    def __init__(self, pin):
        self._buzzer = PWM(Pin(pin))
        self._duty_level = 64000

    def _play_sound(self, freq, ms):
        if freq:
            self._buzzer.freq(freq)
            self._buzzer.duty_u16(self._duty_level)
        sleep_ms(ms)
        self._buzzer.duty_u16(0)

    def play(self, song):
        for freq, ms in song:
            self._play_sound(freq, ms)
