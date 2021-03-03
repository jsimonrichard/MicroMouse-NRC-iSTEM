from enum import Enum
import uasyncio

class Direction(Enum):
    UP = (1,0)
    DOWN = (-1,0)
    LEFT = (0,-1)
    RIGHT = (0,1)

class Robot:
    def __init__(self, btn, bzz, motors, ping_collection, maze):
        self._btn = btn
        self._bzz = bzz
        self._motors = motors
        self._ping_collection = ping_collection
        self._maze = maze

        self.pos = (0,0)
        self.orientation = Direction.UP

        self._ping = {}
        self._del_ping = {}

    def Start(self):
        uasyncio.create_task(self._update_ping())

    async def _update_ping(self):
        ping = await self._ping_collection.ping()
        self._del_ping = ping - self._ping
        self._ping = ping
