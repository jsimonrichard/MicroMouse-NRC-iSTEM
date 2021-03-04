from machine import Pin
from utime import ticks_us, sleep_us

class PingSensor:
    def __init__(self, pins):
        self.echo = Pin(pins["echo"], Pin.IN)
        self.trig = Pin(pins["trig"], Pin.OUT)

    async def ping(self):
        """
        Make the sensor ping and get a distance (in cm) asyncronously
        TODO: Check this
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
            ...
        end_time = ticks_us() # End time

        distance = (end_time - start_time)/58 # in cm
        return distance

class PingCollection:
    def __init__(self, sensors):
        self.sensors = sensors

    async def ping(self):
        out = []
        for sensor in self.sensors:
            out.append( await sensor.ping() )
        return out
