"""
This is the file for GPIO pin configuration.
"""

BUTTON_PIN = 22
BUZZER_PIN = 21

DHT_PIN = 20

MOTOR_PINS = {
    "right": {
        "forward": 6,
        "backward": 7
    },
    "left": {
        "forward": 8,
        "backward": 9
    }
}

PING_PINS = [
    { # Front
        "trig": 12,
        "echo": 13
    },
    
    { # Rigth
        "trig": 14,
        "echo": 15
    },

    { # Back
        "trig": 16,
        "echo": 17
    },
    
    { # Left
        "trig": 18,
        "echo": 19
    }
]
