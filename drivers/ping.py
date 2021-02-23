class PingSensor:
    def __init__(self, echo_pin):
        self.echo_pin = echo_pin

class PingCollection:
    def __init__(self, trig_pin, sensors):
        self.trig_pin = trig_pin
        self.sensors = sensors
    
    def ping(self):
        ...