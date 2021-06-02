"""
Test for the motors
motor_test.py
"""

from machine import Pin
from utime import sleep_ms

from config import AXIL_LENGTH
from config.pins import MOTOR_PINS, BUTTON_PIN

from drivers.motor import TwoWheel
from drivers.button import Button

led = Pin(25, Pin.OUT)
btn = Button(BUTTON_PIN)

speed = 30000
motors = TwoWheel(MOTOR_PINS, AXIL_LENGTH)

def main():
    led.high()

    while not btn.isPressed:
        ...
    led.low()
    sleep_ms(500)

    print("Let's goooooooo")

    motors.straight(speed)
    sleep_ms(1000)
    motors.stop()

    print("Yeah!!!!!")

def _main():
    led.high()
    while not btn.isPressed:
        ...
    led.low()

    sleep_ms(500)

    while True:
        motors.straight(speed)
        sleep_ms(100)
        motors.stop(jerk=-1)
        sleep_ms(100)
