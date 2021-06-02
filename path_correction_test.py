from utime import sleep_ms

from drivers import motor, button, ping, buzzer

from config import AXIL_LENGTH, MIN_SENSOR_WIDTH, CRAWL_PWM
from config.pins import BUTTON_PIN, BUZZER_PIN, MOTOR_PINS, PING_PINS
from config.maze import UNIT_SIZE, MAZE_SIZE, SOLUTIONS

btn = button.Button(BUTTON_PIN)
bzz = buzzer.Buzzer(BUZZER_PIN)

motors = motor.TwoWheel(MOTOR_PINS, AXIL_LENGTH)

threshold = max(UNIT_SIZE) - MIN_SENSOR_WIDTH
ping_sensors = list(map(lambda pins: ping.PingProximitySensor(pins, threshold), PING_PINS))
ping_collection = ping.PingProxCollection(ping_sensors)

def update_ping():
    ping = ping_collection.ping()
    prox = ping_collection.getProx()
    return (ping, prox)

CORRECTION_RADIUS = 120

def left():
    motors.rot(-CRAWL_PWM, -CORRECTION_RADIUS)
    sleep_ms(300)
    motors.stop()

def right():
    motors.rot(CRAWL_PWM, CORRECTION_RADIUS)
    sleep_ms(300)
    motors.stop()

def straight():
    motors.straight(CRAWL_PWM)
    sleep_ms(300)
    motors.stop()

def main():
    ping = []
    prox = []

    orientation = 0
    direction = 0

    while not btn.isPressed:
        ...

    while True:
        ping, prox = update_ping()
        print(ping)
        if orientation == direction:
            if ping[(orientation+1)%4] < threshold:
                print("left")
                motors.rot(-CRAWL_PWM, -CORRECTION_RADIUS)
            elif ping[(orientation-1)%4] < threshold:
                print("right")
                motors.rot(CRAWL_PWM, CORRECTION_RADIUS)
            else:
                print("Straight")
                motors.straight(CRAWL_PWM)
        else:
            if ping[(orientation-1)%4] < threshold:
                print("left")
                motors.rot(-CRAWL_PWM, CORRECTION_RADIUS)
            elif ping[(orientation+1)%4] < threshold:
                print("right")
                motors.rot(-CRAWL_PWM, -CORRECTION_RADIUS)
            else:
                motors.straight(-CRAWL_PWM)
