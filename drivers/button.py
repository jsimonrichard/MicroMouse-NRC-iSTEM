from machine import Pin

class Button:
    def __init__(self, pin):
        self._pin = Pin(pin, Pin.IN, Pin.PULL_DOWN)

    @property
    def isPressed(self):
        return self._pin.value()
