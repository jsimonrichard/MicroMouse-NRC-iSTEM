"""
Entrypoint for the project
"""
# Imports

from machine import Pin
import utime

from config.pins import BUTTON_PIN, BUZZER_PIN, MOTOR_PINS, PING_PINS
from config.maze import UNIT_SIZE, MAZE_SIZE, SOLUTIONS
from drivers import button, buzzer, motor, ping
from maze import Maze
from robot import Robot

print("[PICO] Imported Libraries")

print("Initializing...")
# Turn on Light
led = Pin(25, Pin.OUT)
led.high()

# DRIVER INITIALIZATION
btn = button.Button(BUTTON_PIN)
bzz = buzzer.Buzzer(BUZZER_PIN, 1)

# Update this
motors = motor.TwoWheel(MOTOR_PINS)

ping_sensors = map(ping.PingSensor, PING_PINS)
ping_collection = ping.PingCollection(ping_sensors)

# MAZE INITIALIZATION
maze = Maze(MAZE_SIZE)


# ROBOT INITIALIZATION
robot = Robot(
    btn,
    bzz,
    motors,
    ping_collection,
    maze
)

utime.sleep_ms(100)
led.low()
print("[PICO] Initialized")

robot.Start(no_peripherals=True)

