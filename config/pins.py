"""
This is the file for GPIO pin configuration.
"""

BUTTON_PIN = 22
BUZZER_PIN = 21

DHT_PIN = 20

MOTOR_PINS = {
    "left": {
        "forward": 6,
        "backward": 7
    },
    "right": {
        "forward": 8,
        "backward": 9
    }
}

PING_PINS = [
    { # Left
        "trig": 14,
        "echo": 15
    },

    { # Front
        "trig": 12,
        "echo": 13
    },

    { # Right
        "trig": 18,
        "echo": 19
    },

    { # Back
        "trig": 16,
        "echo": 17
    }
]
