#!usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys
import subprocess
from pygame.locals import *
import RPi.GPIO as GPIO
import threading
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(14,GPIO.IN, GPIO.PUD_DOWN)

print (GPIO.input(4))

pygame.init()

#cmd = "raspistill  -w 1296 -h 972 -md 2 -q 75 -t 1000  -ts -e jpg -o /home/pi/Pictures/cam/$filnavn%d.jpg"
#subprocess.call(cmd, shell=True)

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

#variables
MenuLevel=1   #set initial menulevel controls which part of the menu you are in

#colours
black=(0,0,0,0)
white=(255,255,255)

running=1
count =1
pygame.display.set_caption("mortens retro-launcher")  

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      tråd(self.name, 5)
      print ("Exiting " + self.name)



#Images are objects with a filename, possible folder name, pointer to executable (to be implemented)
class Images():
    def __init__ (self, filename, x,y):   #her kunne der godt være en henvisning til den exe.fil der aabner programmet.
        self.load=pygame.image.load(filename)    ##load the image into a pygame object
        self.x=x  #the pictures x coordinate
        self.y=y   #the pictures y-coordinate

#images
c64 = Images('c64small.jpg',150,20)
mame = Images('mame_small.jpg', 150, 300)

#global function to check whether to return to the main menu
def TjekHjem():
    global MenuLevel
    global running
    Keypress=pygame.event.wait()
    if Keypress.type==KEYDOWN:
        if Keypress.key==pygame.K_h:  #checks for the key "h" for "Home"
            print("du har trykket på h")
            MenuLevel=1     #set otoplevel menu
        elif Keypress.key==pygame.K_q:
            print("Quitter")
            running = 0
            MenuLevel=0
            return
        
def tråd(threadName,delay):
    global count
    while count<10:
        print ("thread running %i" %(count,))
        time.sleep(count)
        count+=1
    

Window = pygame.display.set_mode((800,600),0 ,32)  

thread1=myThread(1,"tråden",5)
thread1.start()

while running==1:
    Window = pygame.display.set_mode((800,600),0 ,32)
            
    
    while MenuLevel==1:

        Window = pygame.display.set_mode((800,600),0 ,32)
        
        Window.blit(c64.load,(c64.x,c64.y))
        Window.blit(mame.load,(mame.x,mame.y))
        pygame.display.flip()
        venter=pygame.event.wait()
        if venter.type==KEYDOWN:
            if venter.key==pygame.K_1:
                print("du har valgt Commodore 64")
                MenuLevel=2
            elif venter.key==pygame.K_2:
                print ("du har valgt MAME")
                MenuLevel=3
            elif venter.key==pygame.K_q:
                print ("du har valgt at sige farvel")
                MenuLevel=0
                running=0
    while MenuLevel==2:
                
        #Window =pygame.display.set_mode((800,600),0 ,32)
        Window.blit(c64.load,(150, 50))
        pygame.display.flip()
        TjekHjem()
        
    while MenuLevel==3:
           
        #Window =pygame.display.set_mode((800,600),0 ,32)
        Window.fill(black)
        Window.blit(mame.load,(150, 50))
        pygame.display.flip()
        TjekHjem()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=0
            

print("Elvis has left the building")

pygame.display.quit()        
pygame.quit()
pygame.quit()
sys.exit()