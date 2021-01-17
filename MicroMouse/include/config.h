#ifndef HEADER_CONFIG
#define HEADER_CONFIG

/* GPIO Pin Configuration */

#define BUTTON_PIN 0

#define BUZZER_PIN 0

#define MOTOR_L_PIN 15
#define MOTOR_R_PIN 16

#define PING_TRIG_PIN 9
#define PING_ECHO_PIN_F 1
#define PING_ECHO_PIN_B 2
#define PING_ECHO_PIN_L 3
#define PING_ECHO_PIN_R 4

/* Speed Configuration 
Nothing here yet... */


/* Sound Configuration */

/*
Stand By Sound
E4 for 0.25 seconds
B4 for 0.25 seconds
E5 for 0.25 seconds
G#5 for 0.25 seconds
B5 for 0.25 seconds
*/
#define SOUND_STAND_BY { \
    [330,250], \
    [494,250], \
    [659,250], \
    [831,250], \
    [988,250] \
}

/*
Start Up Sound
A4 for 0.5 seconds
E5 for 0.5 seconds
*/
#define SOUND_START_UP { \
    [440,500], \
    [659,500] \
}

/*
Build Map Sound
B5 for 0.25 seconds
*/
#define SOUND_BUILD_MAP { \
    [988,250] \
}

/*
Homing Sound
B5 for 0.25 seconds
E5 for 0.25 seconds
B4 for 0.25 seconds
*/
#define SOUND_HOMING { \
    [988,250], \
    [659,250], \
    [494,250] \
}

/*
Dash Sound
B4 for 0.25 seconds
Break
B4 for 0.25 seconds
Break
E5 for 0.5 seconds
*/
#define SOUND_DASH { \
    [494,250], \
    [0,2], \
    [494,250], \
    [0,2], \
    [659,500] \
}

#endif /* HEADER_CONFIG */