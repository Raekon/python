import subprocess
import time
import datetime
import ftplib
import RPi.GPIO as GPIO
p=0
o=1
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN, GPIO.PUD_DOWN)
while True:
    while GPIO.input(4)==1:
        p+=1
        o=0
    while o==0:
        print(p)
        o=1
        p=0
