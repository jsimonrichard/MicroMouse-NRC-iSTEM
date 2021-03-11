import utime

class Direction:
    UP = 1
    DOWN = 3
    LEFT = 0
    RIGHT = 2

class Robot:
    def __init__(self, btn, bzz, motors, ping_collection, maze):
        self._btn = btn
        self._bzz = bzz
        self._motors = motors
        self._ping_collection = ping_collection
        self._maze = maze

        self.pos = (0,0)
        self.orientation = Direction.UP

        self.no_peripherals = False

        self._ping = []
        self._del_ping = []

    def Start(self, no_peripherals=False):
        self.no_peripherals = no_peripherals
        self._loop()

    def _loop(self):
        while True:
            self._update_ping()
            print(self._ping)
            utime.sleep_ms(1000)

    def _update_ping(self):
        ping = [] if self.no_peripherals else self._ping_collection.ping()
        self._del_ping = [b - a for a,b in zip(self._ping, ping)]
        self._ping = ping
