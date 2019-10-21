from PIL import Image, ImageFilter
import threading
import subprocess
import ftplib
import os
import time
import datetime
from PIL import Image,ImageDraw


print (os.getcwd())
os.chdir("/home/pi/Pictures/cam")
print (os.getcwd())
dir_cont=os.listdir()
dir_cont.sort()
print (dir_cont)
length=len(dir_cont)
print (length)
for i in range(length):
    im1=Image.open(dir_cont[i])
    im2=Image.open(dir_cont[0])
    im3 = Image.new('RGB',(im1.size),color=200)
    image1 = im1.load()
    image2 = im2.load()
    image3 = ImageDraw.Draw(im3,'RGB')
    #im3.save('/home/pi/pythonfiles/billedbehandling/blank/blank_image.jpg')
    #im3.show()
    #time.sleep(3)
    print("shown")
    print(im1.size)
    print(dir_cont[i])
    print(dir_cont[i+1])
    for y in range(1,pix1[1],1):
        print(y)
        for x in range(1,pix1[0],1):
            pix1=image1[x,y]
            pix2=image2[x,y]
            av1=(sum(pix1)/len(pix1))
            av2=(sum(pix2)/len(pix2))
            
            if (av1-av2)/10>=1:
                #print ("hov, her er en fejl mellem billede {0} og billede {1}. pix 1 er {2} og pix 2 er {3}".format(dir_cont[i],dir_cont[i+1],av1, av2))
                #print ("x er {0} og y er {1}".format(x,y))
                image3.point([(x,y)],1)
            elif (av1-av2)/10<=-1:
                #print ("hov, her er en fejl mellem billede {0} og billede {1}. pix 1 er {2} og pix 2 er {3}".format(dir_cont[i],dir_cont[i+1],av1, av2))
                #print ("x er {0} og y er {1}".format(x,y))
                image3.point([(x,y)],"white")
                #time.sleep(0.2)
    im3.save('/home/pi/Pictures/blank/blank_image{0}.jpg'.format(i+100,quality=95))
    print("så er den gemt")
    time.sleep(2)
print("færdig")                
    

