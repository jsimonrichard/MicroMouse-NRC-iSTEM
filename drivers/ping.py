from machine import Pin
from utime import ticks_us, sleep_us

class PingSensor:
    def __init__(self, pins):
        self.echo = Pin(pins["echo"], Pin.IN)
        self.trig = Pin(pins["trig"], Pin.OUT)

    def ping(self):
        """
        Make the sensor ping and get a distance (in cm) asyncronously
        """
        # Send a pulse
        self.trig.off() # Make sure it's off
        sleep_us(2)

        self.trig.on()
        sleep_us(10) # Pulse length
        self.trig.off()

        # Wait for beginning of ping
        while self.echo.value() == 0:
            ...
        start_time = ticks_us() # Start time

        # Wait for end of ping
        while self.echo.value() == 1:
            dur = ticks_us() - start_time
            if dur > 20000:
                break

        distance = dur/58 # in cm
        return distance

class PingCollection:
    def __init__(self, sensors):
        self.sensors = sensors

    def ping(self):
        out = []
        for sensor in self.sensors:
            out.append( sensor.ping() )
        return out
