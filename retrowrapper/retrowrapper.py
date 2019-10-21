#!usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame, sys
import subprocess
from pygame.locals import *
import RPi.GPIO as GPIO

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
    Keypress=pygame.key.get_pressed()
    if Keypress[pygame.K_h]:  #checks for the key "h" for "Home"
        print("du har trykket på h")
        MenuLevel=1     #set otoplevel menu
    elif Keypress[pygame.K_q]:
        print("Quitter")
        running = 0
        MenuLevel=0
        return
pygame.display.set_caption("mortens retro-launcher")    

while running==1:
    Window = pygame.display.set_mode((800,600),0 ,32)
            
    
    while MenuLevel==1:

        Window = pygame.display.set_mode((800,600),0 ,32)
        
        Window.blit(c64.load,(c64.x,c64.y))
        Window.blit(mame.load,(mame.x,mame.y))
        pygame.display.update()
        Keypress = pygame.key.get_pressed()
        if Keypress[pygame.K_1]:
            print("du har valgt Commodore 64")
            MenuLevel=2
        elif Keypress[pygame.K_2]:
            print ("du har valgt MAME")
            MenuLevel=3
    
    while MenuLevel==2:
        
        TjekHjem()
        Window =pygame.display.set_mode((800,600),0 ,32)
        Window.blit(c64.load,(150, 200))
        pygame.display.update()
        
    while MenuLevel==3:
        
        TjekHjem()
        Window =pygame.display.set_mode((800,600),0 ,32)
        Window.blit(mame.load,(150, 200))
        pygame.display.update()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=0
            

print("Elvis has left the building")

pygame.display.quit()        
pygame.quit()
pygame.quit()
sys.exit()