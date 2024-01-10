import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

class BtnControl:
    def __init__(self, name, pin, key):
        self.name=name
        self.btn=digitalio.DigitalInOut(pin)
        self.btn.direction=digitalio.Direction.INPUT
        self.btn.pull=digitalio.Pull.DOWN
        self.key=key
        self.last_value=False

    def update(self):
        global keyboard
        if not self.last_value and self.btn.value:
            print(self.name+" pressed")
            keyboard.press(self.key)
        if self.last_value and not self.btn.value:
            print(self.name+" released")
            keyboard.release(self.key)
        self.last_value=self.btn.value

list_btns=[
    BtnControl("Censor button", board.GP15, Keycode.SPACEBAR),
    BtnControl("Button 1", board.GP1, Keycode.ONE),
    BtnControl("Button 2", board.GP2, Keycode.TWO),
    BtnControl("Button 3", board.GP3, Keycode.THREE),
    BtnControl("Button 4", board.GP4, Keycode.FOUR),
]

while True:
    for button in list_btns:
        button.update()

    time.sleep(0.1)

