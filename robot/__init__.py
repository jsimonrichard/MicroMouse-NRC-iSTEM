import utime
from config import songs, ROT_PWM, ROT_TIME, CRAWL_PWM, CRAWL_VEL

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

directions = [(1,0), (0,-1), (-1,0), (0,1)]

class Robot:
    def __init__(self, btn, bzz, motors, ping_collection, dht_sensor, maze, UNIT_SIZE, SOLUTIONS, ping_threshold):
        self._btn = btn
        self._bzz = bzz
        self._motors = motors
        self._ping_collection = ping_collection
        self._dht_sensor = dht_sensor
        self._maze = maze
        self.UNIT_SIZE = UNIT_SIZE
        self.SOLUTIONS = SOLUTIONS

        self.bounce_threshold = ping_threshold*0.8

        self.pos = (0,0)
        self.orientation = Direction.LEFT

        self.state = None
        self.enroute_state = False
        self.enroute_path = []

        self.prox = []
        self.ping = []

        self.anchor_pos = self.pos

    def Start(self):

        # Play on sound
        self._bzz.play(songs.ON)

        # Wait to start until button is pressed
        while not self._btn.isPressed:
            ...
        utime.sleep(1)

        self._start_crawl()

        self._loop()

    def _loop(self):
        while True:
            # Update ping values
            self._update_ping()
            print("Ping:", self.ping)
            print("Prox:", self.prox)
            print("Pos:", self.pos)
            #print(self._dht_sensor.temperature)
            utime.sleep_ms(1000)

            if self._btn.isPressed:
                self._bzz.play(songs.CRAWL)
                utime.sleep(1)
                self._rot_ccw(phantom=True)

            # Run logic for the current state
            if self.enroute_state:
                self._enroute()
            else:
                if self.state == State.CRAWL:
                    self._crawl()
                elif self.state == State.HOMING:
                    self._homing()
                elif self.state == State.DASH:
                    self._dash()
                elif self.state == State.DASH_BACK:
                    self._homing()

            print()

    def _start_crawl(self):
        self.state = State.CRAWL
        self._bzz.play(songs.CRAWL)

    def _crawl(self):
        self._maze.setVisited(self.pos)

        went = False
        for k in range(4):
            if not self.prox[k]: # TODO: Check if not visited
                self._move((self.orientation+k)%4)
                went = True

        if not went:
            targets = self._maze.getUnvisited()

            if not targets:
                self._start_homing()
                targets = [(0,0)]

            self.enroute_state = True
            self.enroute_path = self._maze.solvePath(self.pos, targets)

    def _start_homing(self):
        self.state = State.HOMING
        self._bzz.play(songs.HOMING)

    def _start_dash_back(self):
        self.state = State.DASH_BACK

    def _homing(self):
        self._start_dash()

    def _start_dash(self):
        self.state = State.DASH
        self._bzz.play(songs.DASH)

    def _dash(self):
        self.enroute_path = self._maze.solvePath(self.pos, self.SOLUTIONS)
        self.enroute_state = True

    def _update_ping(self):
        self.ping = self._ping_collection.ping()
        self.prox = self._ping_collection.getProx()

    def _reset_anchor(self):
        self.anchor_pos = self.pos
        self.anchor_time = utime.ticks_ms()

    def _move(self, direction):
        # Orient the robot
        print("direction:", direction)
        if (direction+self.orientation)%2:
            self._rot_ccw()

        # Move
        start_time = utime.ticks_ms()
        dur = self.UNIT_SIZE[direction%2]*1000/CRAWL_VEL
        print("Duration:", dur)

        while utime.ticks_ms()-start_time <= dur:
            if self.orientation == direction:
                if self.ping[(self.orientation+1)%4] < self.bounce_threshold:
                    print("asdfasf1")
                    self._motors.rot(CRAWL_PWM, 40)
                elif self.ping[(self.orientation-1)%4] < self.bounce_threshold:
                    print("asdfasf2")
                    self._motors.rot(CRAWL_PWM, -40)
                else:
                    self._motors.straight(CRAWL_PWM)
            else:
                if self.ping[(self.orientation-1)%4] < self.bounce_threshold:
                    print("asdfasf3")
                    self._motors.rot(-CRAWL_PWM, 40)
                elif self.ping[(self.orientation+1)%4] < self.bounce_threshold:
                    print("asdfas4")
                    self._motors.rot(-CRAWL_PWM, -40)
                else:
                    self._motors.straight(-CRAWL_PWM)
            self._update_ping()

        self._motors.stop()

        delta = directions[direction]
        self.pos = (self.pos[0]+delta[0], self.pos[1]+delta[1])

        self._reset_anchor()

    def _rot_ccw(self, phantom=False):
        if not phantom:
            self._motors.rot(-ROT_PWM, 0)
            utime.sleep_ms(ROT_TIME)
            self._motors.stop()

        self.orientation = (self.orientation+1) % 4

        self._reset_anchor()

    def _enroute(self):
        if self.pos in self.enroute_path:
            delta = (self.enroute_path[self.pos][0]-self.pos[0], self.enroute_path[self.pos][1]-self.pos[1])
            direction = directions.index(delta)
            self._move(direction)
        else:
            raise Exception("The robutt is off track")
