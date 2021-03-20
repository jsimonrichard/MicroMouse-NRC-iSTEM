from utime import sleep_ms

directions = [(1,0), (0,-1), (-1,0), (0,1)]

def _is_square(ping):
    for v in ping:
        if v > 300: # Ping sensor timed out
            return False
    return True

def move(robot, direction):
    # Orient the robot
    if direction+robot.orientation%2:
        robot.motors.rot( robot.speed, 0 )
        sleep_ms(200)
        while True:
            robot.update_ping()
            if _is_square(robot.ping):
                break
            sleep_ms(10)

    # Move
    start_pos = robot.pos
    target = [ a+b for a, b in zip(start_pos, directions[direction]) ]

    while robot.pos != target:
        if robot.orientation == direction:
            robot.motors.straight(robot.speed)
        else:
            robot.motors.straight(-robot.speed)
        robot.update_ping()
        robot.update_pos()

def forward(speed, orientation, ping, del_ping, motors):
    if abs(del_ping[0]) > 0.2 and abs(del_ping[0]) < 5:
        ...

    l_speed = 1
    r_speed = 1
    motors.forward(l_speed, r_speed)

def enroute(robot):
    ...
