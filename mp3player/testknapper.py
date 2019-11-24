import gpiozero
import vlc
import time
import os
import gpiozero
import random

button2=gpiozero.Button(3)
print("testknapper")

while True:
    if button2.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
    time.sleep(.5)
