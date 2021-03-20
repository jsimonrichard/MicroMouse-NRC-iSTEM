"""
Test for the motors
"""

from machine import Pin
from utime import sleep_ms

from config import AXIL_LENGTH
from config.pins import MOTOR_PINS, BUTTON_PIN

from drivers.motor import TwoWheel
from drivers.button import Button

led = Pin(25, Pin.OUT)
led.high()

btn = Button(BUTTON_PIN)
while not btn.isPressed:
    ...
led.low()
sleep_ms(1000)

speed = 30000
motors = TwoWheel(MOTOR_PINS, AXIL_LENGTH)

print("Let's goooooooo")

motors.straight(speed)
sleep_ms(3000)
motors.straight(-speed)
sleep_ms(3000)
motors.stop()

print("Yeah!!!!!")
