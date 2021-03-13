def forward(speed, orientation, ping, del_ping, motors):
    if abs(del_ping[0]) > 0.2 and abs(del_ping[0]) < 5:
        ...

    l_speed = 1
    r_speed = 1
    motors.forward(l_speed, r_speed)
