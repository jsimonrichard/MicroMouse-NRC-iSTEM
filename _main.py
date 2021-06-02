"""
Entrypoint for the project
"""
# Imports

from machine import Pin
import utime
import dht

from config import AXIL_LENGTH, MIN_SENSOR_WIDTH
from config.pins import BUTTON_PIN, BUZZER_PIN, MOTOR_PINS, PING_PINS
from config.maze import UNIT_SIZE, MAZE_SIZE, SOLUTIONS
from drivers import button, buzzer, motor, ping
from maze import Maze
from robot import Robot

def init_robot():
    print("Imported Libraries")

    print("Initializing...")
    # Turn on Light
    led = Pin(25, Pin.OUT)
    led.high()

    # DRIVER INITIALIZATION
    btn = button.Button(BUTTON_PIN)
    bzz = buzzer.Buzzer(BUZZER_PIN)

    motors = motor.TwoWheel(MOTOR_PINS, AXIL_LENGTH)

    threshold = max(UNIT_SIZE) - MIN_SENSOR_WIDTH
    ping_sensors = list(map(lambda pins: ping.PingProximitySensor(pins, threshold), PING_PINS))
    ping_collection = ping.PingProxCollection(ping_sensors)

    dht_sensor = dht.DHT11(Pin(20))

    # MAZE INITIALIZATION
    maze = Maze(MAZE_SIZE)


    # ROBOT INITIALIZATION
    robot = Robot(
        btn,
        bzz,
        motors,
        ping_collection,
        dht_sensor,
        maze,
        UNIT_SIZE,
        SOLUTIONS,
        threshold
    )

    utime.sleep_ms(100)
    led.low()
    print("Pico Initialized")

    robot.Start()

def test_motors():
    import motor_test
    motor_test.main()

def test_path_correction():
    import path_correction_test
    path_correction_test.main()

test_path_correction()
