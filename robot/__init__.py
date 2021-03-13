import utime
from config import songs

from .movement import enrout

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
    def __init__(self, btn, bzz, motors, ping_collection, dht_sensor, maze, UNIT_SIZE, SOLUTIONS):
        self._btn = btn
        self._bzz = bzz
        self._motors = motors
        self._ping_collection = ping_collection
        self._dht_sensor = dht_sensor
        self._maze = maze
        self.UNIT_SIZE = UNIT_SIZE
        self.SOLUTIONS = SOLUTIONS

        self.step_up_factor = 5

        self.pos = (0,0)
        self.orientation = Direction.UP

        self.state = None
        self.enroute = False
        self.enroute_path = []

        self.speed = 5

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
            if self.enroute:
                enroute(self)
            else:
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
        self._maze.setVisited(self.pos)

        went = False
        for k in range(4):
            if self._ping[k] > self.UNIT_SIZE[(self.orientation+k)%2]:
                self._motors.go(k)
                went = True

        if not went:
            targets = self._maze.getUnvisited()

            if not targets:
                self._start_homing()
                targets = [(0,0)]

            self.enroute = True
            self.enroute_path = self._maze.solvePath(self.pos, targets)

    def _start_homing(self):
        self.state = State.HOMING
        self._bzz.play(songs.HOMING)

    def _start_dash_back(self):
        self.state = State.DASH_BACK

    def _homing(self, step_up=0):
        self._start_dash()

    def _start_dash(self):
        self.state = State.DASH
        self._bzz.play(songs.DASH)

    def _dash(self):
        self.speed += self.step_up_factor
        self.enroute_path = self._maze.solvePath(self.pos, self.SOLUTIONS)
        self.enroute = True

    def _update_ping(self):
        ping = self._ping_collection.ping()
        self._del_ping = [b - a for a,b in zip(self._ping, ping)]
        self._ping = ping

        if self._last_unit_ping == []:
            self._last_unit_ping = ping

    def _update_pos(self):
        # Get change in position
        delta = [b - a for a,b in zip(self._ping, self._last_unit_ping)]

        dx = 0
        dy = 0
        # Only consider changes in direction of movement
        if self.orientation%2 == 0:
            c = 1 if self.orientation==0 else -1
            dx = c * (delta[2]-delta[0])/2
        else:
            c = 1 if self.orientation==3 else -1
            dy = c * (delta[2]-delta[0])/2

        # Get di, dj
        di = int( dx/self.UNIT_SIZE[0] )
        dj = int( dy/self.UNIT_SIZE[1] )
        if di or dj:
            self.pos = (self.pos[0]+di, self.pos[1]+dj)
            self._last_unit_ping = self._ping

    def _rot_orientation_cw(self):
        self.orientation = (self.orientation-1) % 4

    def _rot_orientation_ccw(self):
        self.orientation = (self.orientation+1) % 4
