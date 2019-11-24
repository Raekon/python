##Music player on Raspberry
import glob
import vlc
import time
import os
import gpiozero
import random

dir_cont=sorted(os.listdir("/home/pi/Music/c64"))
print (dir_cont)
playing = False
button1=gpiozero.Button(2, pull_up=True, bounce_time=0.1)
button2=gpiozero.Button(3, pull_up=True, bounce_time=0.1)
button3=gpiozero.Button(4, pull_up=True, bounce_time=0.1)
button4=gpiozero.Button(17, pull_up=True, bounce_time=0.1)
button5=gpiozero.Button(27, pull_up=True, bounce_time=0.1)
row1=gpiozero.LED(26,initial_value=True)
row2=gpiozero.LED(19,initial_value=True)
row3=gpiozero.LED(13,initial_value=True)
row4=gpiozero.LED(6,initial_value=True)
row5=gpiozero.LED(5,initial_value=True)

stopbutton=gpiozero.Button(9,pull_up=True, bounce_time=0.1)

initial_volume=60 

buttons=[button1,button2,button3,button4,button5]
rows=[row1,row2,row3,row4,row5]
counter=0
print("row1 er {0}".format(row1.value))
print("buttton 2 er {0}".format(button2.value))

while (True):
    if(counter%100000==0):
        print("row1 er {0} Button 2 er{1}".format(row1.value,button2.value))
        if playing:
            print(p.get_position())
    for row in range(5):
        rows[row].off()
        for button in range(5):
            if (buttons[button].value):
                if playing==True:
                    p.stop()
                playing=True
                playfile=(glob.glob("/home/pi/Music/c64/{0}-{1}*".format(row,button)))
                print(playfile)
                p=vlc.MediaPlayer("{0}".format(playfile[0]))
                print(p.audio_set_volume(initial_volume))
                p.play()
                p.set_position(0.31)
                buttons[button].wait_for_release(2)
                print("button is releaed")
        rows[row].on()
    counter+=1
    if(stopbutton.value and playing==True):
        print("Der blev trykket stop")
        for x in range(initial_volume,0, -1):
            p.audio_set_volume(x)
            time.sleep(.02)
        p.stop()
    
        

while(True):
    if button2.is_pressed:
        if playing==True:
            p.stop()
        playing=True
        print(dir_cont[2])
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
        i = random.choice(dir_cont)
        p=vlc.MediaPlayer("file:///home/pi/Music/c64/{0}".format(i))
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

