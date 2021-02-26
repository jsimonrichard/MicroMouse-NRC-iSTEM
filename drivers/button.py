from machine import Pin

class Button:
    def __init__(self, pin):
        self._pin = Pin(pin, Pin.IN)

    @property
    def isPressed(self):
        return self._pin.value()
