import utime
from config import songs

class Direction:
    UP = 1
    DOWN = 3
    LEFT = 0
    RIGHT = 2

class State:
    CRAWL = 0
    HOMING = 1
    DASH = 2
    DASH_BACK = 3


class Robot:
    def __init__(self, btn, bzz, motors, ping_collection, maze):
        self._btn = btn
        self._bzz = bzz
        self._motors = motors
        self._ping_collection = ping_collection
        self._maze = maze

        self.step_up_factor = 5

        self.pos = (0,0)
        self.orientation = Direction.UP

        self.no_peripherals = False

        self.state = None

        self._ping = []
        self._del_ping = []

    def Start(self, no_peripherals=False):
        self.no_peripherals = no_peripherals

        # Play on sound
        self._bzz.play(songs.ON)

        # Wait to start until button is pressed
        while self._btn.low():
            ...

        self._start_crawl()

        self._loop()

    def _loop(self):
        while True:
            # Update ping values
            self._update_ping()
            print(self._ping)
            utime.sleep_ms(1000)

            # Run logic for the current state
            if self.state == State.CRAWL:
                self._crawl()
            elif self.state == State.HOMING:
                self._homing()
            elif self.state == State.DASH:
                self._dash()
            elif self.state == State.DASH_BACK:
                self._homing(step_up=self.step_up_factor)

    def _start_crawl(self):
        self.state = State.CRAWL
        self._bzz.play(songs.CRAWL)

    def _crawl(self):
        ...

    def _start_homing(self):
        self.state = State.HOMING
        self._bzz.play(songs.HOMING)

    def _start_dash_back(self):
        self.state = State.DASH_BACK

    def _homing(self, step_up=0):
        ...

    def _start_dash(self):
        self.state = State.DASH
        self._bzz.play(songs.DASH)

    def _dash(self):
        ...

    def _execute_path(self, path):
        ...

    def _update_ping(self):
        ping = [] if self.no_peripherals else self._ping_collection.ping()
        self._del_ping = [b - a for a,b in zip(self._ping, ping)]
        self._ping = ping
