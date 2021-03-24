from machine import Pin
from utime import ticks_us, sleep_us

class PingProximitySensor:
    def __init__(self, pins, threshold):
        self.echo = Pin(pins["echo"], Pin.IN)
        self.trig = Pin(pins["trig"], Pin.OUT)
        self.threshold = threshold

        self.ping_value = 0

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

        self.ping_value = dur/58 # in cm

    def getProx(self):
        return self.ping_value <= self.threshold

class PingProxCollection:
    def __init__(self, sensors):
        self.sensors = sensors

    def ping(self):
        out = []
        for sensor in self.sensors:
            sensor.ping()
            out.append( sensor.ping_value )
        return out

    def getProx(self):
        out = []
        for sensor in self.sensors:
            out.append( sensor.getProx() )
        return out
