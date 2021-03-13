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
    def __init__(self, btn, bzz, motors, ping_collection, dht_sensor, maze, UNIT_SIZE):
        self._btn = btn
        self._bzz = bzz
        self._motors = motors
        self._ping_collection = ping_collection
        self._dht_sensor = dht_sensor
        self._maze = maze
        self.UNIT_SIZE = UNIT_SIZE

        self.step_up_factor = 5

        self.pos = (0,0)
        self.orientation = Direction.UP

        self.state = None

        self._ping = []
        self._del_ping = []
        self._last_unit_ping = []

    def Start(self):

        # Play on sound
        self._bzz.play(songs.ON)

        # Wait to start until button is pressed
        while not self._btn.isPressed:
            ...

        self._start_crawl()

        self._loop()

    def _loop(self):
        while True:
            # Update ping values
            self._update_ping()
            self._update_pos()
            print(self.pos)
            #print(self._dht_sensor.temperature)
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
        ping = self._ping_collection.ping()
        self._del_ping = [b - a for a,b in zip(self._ping, ping)]
        self._ping = ping

        if self._last_unit_ping == []:
            self._last_unit_ping = ping

    def _update_pos(self):
        delta = [b - a for a,b in zip(self._ping, self._last_unit_ping)]
        dx = (delta[ self.orientation ]-delta[ (self.orientation+2)%4 ])/2
        dy = (delta[ (self.orientation+1)%4 ]-delta[ (self.orientation+3)%4 ])/2
        di = int( dx/self.UNIT_SIZE[0] )
        dj = int( dy/self.UNIT_SIZE[1] )
        if di or dj:
            self.pos = (self.pos[0]+di, self.pos[1]+dj)
            self._last_unit_ping = self._ping

    def _rot_orientation_cw(self):
        self.orientation = (self.orientation-1) % 4

    def _rot_orientation_ccw(self):
        self.orientation = (self.orientation+1) % 4
