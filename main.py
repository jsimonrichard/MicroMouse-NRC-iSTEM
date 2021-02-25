"""
Entrypoint for the project
"""

# Light
from machine import Pin, Timer
led = Pin(25, Pin.OUT)
led.high()

# DRIVER INITIALIZATION

from config.pins import BUTTON_PIN, BUZZER_PIN, MOTOR_PINS, PING_PINS
from drivers import button, buzzer, motor, ping

btn = button.Button(BUTTON_PIN)
bzz = buzzer.Buzzer(BUZZER_PIN)

# Update this
motors = motor.Motor(MOTOR_PINS)

ping_sensors = {
    "front": ping.PingSensor( PING_PINS["ECHO"]["FRONT"] ),
    "back": ping.PingSensor( PING_PINS["ECHO"]["BACK"] ),
    "right": ping.PingSensor( PING_PINS["ECHO"]["RIGHT"] ),
    "left": ping.PingSensor( PING_PINS["ECHO"]["LEFT"] )
}
ping_collection = ping.PingCollection(PING_PINS["trig"], ping_sensors)


# MAZE INITIALIZATION

from config.maze import UNIT_SIZE, MAZE_SIZE, SOLUTIONS
from maze import Maze

maze = Maze(UNIT_SIZE, MAZE_SIZE, SOLUTIONS)


# ROBOT INITIALIZATION
from robot import Robot
robot = Robot(
    btn,
    bzz,
    motors,
    ping_collection,
    maze
)

robot.Start()