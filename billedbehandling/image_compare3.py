from PIL import Image, ImageFilter
import threading
import subprocess
import ftplib
import os
import time
import datetime
from PIL import Image,ImageDraw, ImageChops


print (os.getcwd())
os.chdir("/home/pi/Pictures/cam")
print (os.getcwd())
dir_cont=sorted(os.listdir())
print (dir_cont)
length=len(dir_cont)
print (length)
for i in range(length):
    if i<10:
        j="00"+str(i)
    elif i>9 and i<100:
        j="0"+str(i)
    else:
        j=str(i)
    im1=Image.open(dir_cont[0],mode='r')
    im2=Image.open(dir_cont[i],mode='r')
    im3=ImageChops.subtract(im1,im2)
    im3.save('/home/pi/Pictures/blank/blank_image{0}.jpg'.format(j),quality=95)
    #image1 = im1.load()
    #image2 = im2.load()
    #image3 = ImageDraw.Draw(im3,'RGB')
    #im3.save('/home/pi/pythonfiles/billedbehandling/blank/blank_image.jpg')
    #im3.show()
    #time.sleep(3)
    #im3=Image.alpha_composite(im1,im2)
   
    print("så er den gemt")
    time.sleep(2)
print("færdig")                
    

