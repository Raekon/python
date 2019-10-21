#coding=UTF-8
#from guizero import App, Text, TextBox, error, yesno
import sqlite3
import time
from tkinter import *
from tkinter import ttk

global knapCheck

try:
    knapCheck
except NameError:
    knapCheck=0
    print("knapCheck blev sat til 0")

def knapTryk():
    global knapCheck
    print("knappen blev trykket ",knapCheck," gange")
    if (knapCheck==1):
        text.grid_remove()
        knapCheck+=1
    
    else:
        knapCheck+=1


    if (knapCheck==3):
        button.grid_remove()
        text.grid(row=2, column=2)
        
mainWindow=Tk()
mainWindow.title("testfunktion")
mainWindow.geometry('400x250+800+400')

bgImage=PhotoImage(file='400x250.png')



topFrame=Label(mainWindow, image=bgImage)
topFrame.grid(row=0, column=0, columnspan=5, rowspan=5)
bottomFrame=Frame(mainWindow, bg="yellow")
bottomFrame.grid(row=2, column=1)
text=Button(mainWindow, text="knap2")
text.grid(row=1, column=1)

button=Button(mainWindow, text="knap", command=knapTryk)
button.grid(row=1, column=2)

