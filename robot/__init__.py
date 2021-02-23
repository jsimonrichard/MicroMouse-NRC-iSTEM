class Robot:
    def __init__(self, btn, bzz, motors, ping_collection, maze):
        self.btn = btn
        self.bzz = bzz
        self.motors = motors
        self.ping_collection = ping_collection
        self.maze = maze

    def Start(self):
        ...