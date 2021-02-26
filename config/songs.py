"""
Sounds for the buzzer
"""

ON = [
    (330,250), # E4 for 0.25 seconds
    (494,250), # B4 for 0.25 seconds
    (659,250), # E5 for 0.25 seconds
    (831,250), # G#5 for 0.25 seconds
    (988,250)  # B5 for 0.25 seconds
]

START_CRAWL = [
    (988,250) # B5 for 0.25 seconds
]

START_HOMING = [
    (988,250), # B5 for 0.25 seconds
    (659,250), # E5 for 0.25 seconds
    (494,250)  # B4 for 0.25 seconds
]

START_DASH = [
    (494,250), # B4 for 0.25 seconds
    (0,2),     # Break
    (494,250), # B4 for 0.25 seconds
    (0,2),     # Break
    (659,500)  # E5 for 0.5 seconds
]