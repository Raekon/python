import subprocess
import time
import datetime
import ftplib
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN, GPIO.PUD_DOWN)
while GPIO.input(4)==0:
    p=0
starttid=time.time()
print ("færdig")
sluttid=time.time()
tid=sluttid-starttid
print(tid)


    
    
    
