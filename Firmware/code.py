import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


def init_button(btn):
    new_btn = digitalio.DigitalInOut(btn)
    new_btn.direction = digitalio.Direction.INPUT
    new_btn.pull = digitalio.Pull.DOWN
    return new_btn


def press_button(btn, release=True):
    keyboard.press(btn)
    if release:
        time.sleep(0.1)
        keyboard.release(btn)


#Setting pin varables
Screen_1_Btn_Pin = board.GP1
Screen_2_Btn_Pin = board.GP2
Screen_3_Btn_Pin = board.GP3
Screen_4_Btn_Pin = board.GP4
Censor_Btn_Pin = board.GP15

#..
keyboard = Keyboard(usb_hid.devices)

#Screen Button 1
Screen_1_Btn = init_button(Screen_1_Btn_Pin)

#Screen Button 2
Screen_2_Btn = init_button(Screen_2_Btn_Pin)

#Screen Button 3
Screen_3_Btn = init_button(Screen_3_Btn_Pin)

#Screen Button 4
Screen_4_Btn = init_button(Screen_4_Btn_Pin)

#Censor Button
Censor_Btn = init_button(Censor_Btn_Pin)


while True:
    if Censor_Btn.value:
        print("Censor Buttion pressed")
        press_button(Keycode.SPACEBAR, release=False)
    else:
        keyboard.release(Keycode.SPACEBAR)
        
    if Screen_1_Btn.value:
        print("Buttion 1 pressed")
        press_button(Keycode.ONE)
        
    if Screen_2_Btn.value:
        print("Buttion 2 pressed")
        press_button(Keycode.TWO)
    
    if Screen_3_Btn.value:
        print("Buttion 3 pressed")
        press_button(Keycode.THREE)
        
    if Screen_4_Btn.value:
        print("Buttion 4 pressed")
        press_button(Keycode.FOUR)
        
    time.sleep(0.1)
