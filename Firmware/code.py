import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Setting pin varables
Screen_1_Btn_Pin = board.GP1
Screen_2_Btn_Pin = board.GP2
Screen_3_Btn_Pin = board.GP3
Screen_4_Btn_Pin = board.GP4
Censor_Btn_Pin = board.GP15


# ..
keyboard = Keyboard(usb_hid.devices)

# Screen Button 1
Screen_1_Btn = digitalio.DigitalInOut(Screen_1_Btn_Pin)
Screen_1_Btn.direction = digitalio.Direction.INPUT
Screen_1_Btn.pull = digitalio.Pull.DOWN

# Screen Button 2
Screen_2_Btn = digitalio.DigitalInOut(Screen_2_Btn_Pin)
Screen_2_Btn.direction = digitalio.Direction.INPUT
Screen_2_Btn.pull = digitalio.Pull.DOWN

# Screen Button 3
Screen_3_Btn = digitalio.DigitalInOut(Screen_3_Btn_Pin)
Screen_3_Btn.direction = digitalio.Direction.INPUT
Screen_3_Btn.pull = digitalio.Pull.DOWN

# Screen Button 4
Screen_4_Btn = digitalio.DigitalInOut(Screen_4_Btn_Pin)
Screen_4_Btn.direction = digitalio.Direction.INPUT
Screen_4_Btn.pull = digitalio.Pull.DOWN

# Censor Button
Censor_Btn = digitalio.DigitalInOut(Censor_Btn_Pin)
Censor_Btn.direction = digitalio.Direction.INPUT
Censor_Btn.pull = digitalio.Pull.DOWN


while True:
    if Censor_Btn.value:
        print("Censor Buttion pressed")
        keyboard.press(Keycode.SPACEBAR)
        time.sleep(0.1)
        keyboard.release(Keycode.SPACEBAR)

    if Screen_1_Btn.value:
        print("Buttion 1 pressed")
        keyboard.press(Keycode.ONE)
        time.sleep(0.1)
        keyboard.release(Keycode.ONE)

    if Screen_2_Btn.value:
        print("Buttion 2 pressed")
        keyboard.press(Keycode.TWO)
        time.sleep(0.1)
        keyboard.release(Keycode.TWO)

    if Screen_3_Btn.value:
        print("Buttion 3 pressed")
        keyboard.press(Keycode.THREE)
        time.sleep(0.1)
        keyboard.release(Keycode.THREE)

    if Screen_4_Btn.value:
        print("Buttion 3 pressed")
        keyboard.press(Keycode.FOUR)
        time.sleep(0.1)
        keyboard.release(Keycode.FOUR)

    time.sleep(0.1)
