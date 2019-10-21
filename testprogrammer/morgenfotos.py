import subprocess
import time
import datetime
import ftplib
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN, GPIO.PUD_UP)

print (GPIO.input(4))


minutter=0
sekunder=0
billeder=0
timerne=0
polls = 0
filename="a"
cmd = "raspistill  -w 1296 -h 972 -md 2 -q 75 -t 2500 -p 100,100,400,300 -ex night -ae 10,0xff,0x808000 -a 8 -ts -e jpg -o /home/pi/Pictures/cam/{0}%d.jpg".format(filename)


def pollFormat():
    global filename
    global minutter
    global sekunder
    global timerne
    t= time.time()
   
    now =  datetime.datetime.now()
    tid = datetime.time(now.hour, now.minute, now.second)
    timerne = int(time.strftime("%H"))
    minutter = int(time.strftime("%M"))
    sekunder = int(time.strftime("%S"))
    dagen = time.strftime("%A")
    
    filename = "%s%i%i%i"  %(dagen, timerne, minutter, sekunder)
    print (filename)
    return minutter

while True:
    
    pollFormat()
    polls+=1
    
    if  GPIO.input(4)==0:                         #timerne>=15 and timerne<=17:
        cmd = "raspistill  -w 1296 -h 972 -md 2 -q 75 -t 2500 -p 100,100,400,300 -ex night -ae 10,0xff,0x808000 -a 8 -ts -e jpg -o /home/pi/Pictures/cam/{0}.jpg".format(filename)
        subprocess.call(cmd, shell=True)
        session = ftplib.FTP('ftp.kongesquash.dk','kongesquash.dk','Raekon75')
        file= open('/home/pi/Pictures/cam/{0}.jpg'.format(filename),'rb')
        session.storbinary('STOR skole/{0}.jpg'.format(filename), file)
        file.close
        session.quit()
        time.sleep(60)
    else:
        print("det er ikke tid endnu")
        time.sleep(1)
    
