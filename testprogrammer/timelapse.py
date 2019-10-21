import subprocess
import time
import datetime

minutter=0
sekunder=0
billeder=0
polls = 0
cmd = "raspistill  -w 1296 -h 972 -md 2 -q 75 -t 500  -ts -e jpg -o /home/pi/Pictures/cam/$filnavn%d.jpg"

print ("hvad er det, der tager så lang tid?")
def pollFormat():
    global minutter
    global sekunder
    t= time.time()
    print("1")
    now =  datetime.datetime.now()
    tid = datetime.time(now.hour, now.minute, now.second)
    print("2")
    minutter = int(time.strftime("%-M"))
    sekunder = int(time.strftime("%-S"))
    print("3")
    return minutter

while True:
    print ("4")
    pollFormat()
    polls+=1
    print("5")
    if minutter>=59 or minutter<=30:
        if sekunder%30==0:
            subprocess.call(cmd, shell=True)
            billeder+=1
            print("antal billeder taget: ",billeder)
            print ("antal polls: ", polls)
            polls=0
            time.sleep(28)
    else:
        print("det er ikke tid endnu")
        time.sleep(30)
    