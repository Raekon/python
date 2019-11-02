##Music player on Raspberry

import vlc
import time
import os
import gpiozero
import random

time.sleep(2)
dir_cont=os.listdir("/home/pi/Music/c64")
print (dir_cont)
playing = False
button2=gpiozero.Button(2, bounce_time=0.01)
button3=gpiozero.Button(3, bounce_time=0.01)
button4=gpiozero.Button(17, bounce_time=0.01)

while(True):
    if button2.is_pressed:
        if playing==True:
            p.stop()
        playing=True
        p=vlc.MediaPlayer("file:///home/pi/Music/c64/{0}".format(dir_cont[2]))
        p.play()
        button2.wait_for_release(10)
    if button3.is_pressed:
        if playing ==True:
            p.stop()
        playing=True
        p=vlc.MediaPlayer("file:///home/pi/Music/c64/{0}".format(dir_cont[3]))
        p.play()
        button3.wait_for_release(10)
    if button4.is_pressed:
        if playing ==True:
            p.stop()
        playing=True
        p=vlc.MediaPlayer("file:///home/pi/Music/c64/{0}".format(dir_cont[4]))
        p.play()
        button4.wait_for_release(10)

while(True):
    
    if button2.is_pressed and playing==False:
        playing=True
        i = random.choice(dir_cont)
        p=vlc.MediaPlayer("file:///home/pi/Music/c64/{0}".format(i))
        p.play()
        button2.wait_for_release()
    if button3.is_pressed and playing==True:
        p.stop()
        playing=False
        button3.wait_for_release()

