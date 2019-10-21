
#coding=UTF-8
#from guizero import App, Text, TextBox, error, yesno
import sqlite3
import time
from tkinter import *
from tkinter import ttk





rundeNavne=['runde1','runde2','runde3','runde4','runde5']  #VARIABLE til indskrivning af rundetider
rundetidNavne=['starttid','runde1tid','runde2tid','runde3tid','runde4tid','runde5tid'] #variable til indskrivning af absolut rundetidspunkt

loeberbasen= sqlite3.connect('løbetider.db')  #SQL forbindelsen til basen
c=loeberbasen.cursor()  #cursoren er en slags genvej til mysql_query statements
#c.execute('''CREATE TABLE tider (nummer integer PRIMARY KEY AUTOINCREMENT, navn text, runder int, starttid int NULL, runde1tid int NULL, runde1 int NULL, runde2tid int NULL, runde2 int NULL)''')


def nummer_længde_tjek(*args):
    tjeknummer=feet.get()
    
    if (len(tjeknummer)>=4):
        løberinfo()

def løberinfo(*args):
    try:
        #det første finder alle løberens data
        tid_nu=time.time()
        løbernummer=int(feet.get())
        c.execute("SELECT * FROM tider WHERE nummer=?", (løbernummer,))
        løberdata=c.fetchone()
        løber_navn=løberdata[1]
        løbet_runder=int(løberdata[2])
        løbet_tid=løberdata[(løbet_runder*2+3)]
        #forrige_tid=løberdata[
        
        
        #denne linje sætter texten til siden
        meters.set(løber_navn)
        l_runder.set(løbet_runder)
        l_tid.set(løbet_tid)
        warning_frame.grid_remove()       
        feet_entry.delete(0, END)
        
        #dette skriver de relevante data tilbage til databasen.
        
        
    except TypeError:
        meters.set("der er ikke nogen løberinfo, så du må lige vente lidt")
        warning_frame.grid()
        feet_entry.delete(0, END)
    except ValueError:
        #meters.set("der er ikke noget gyldigt løbernummer")
        warning_frame.grid(column=3, row=5, columnspan=2,rowspan=5)
        feet_entry.delete(0, END)
        
    
app1 = Tk()
app1.resizable(width=False, height=False)
app1.geometry('{}x{}'.format(800, 600))
app1.title("tidregistrering")

imgobj = PhotoImage(file='c64.gif')
warn_img=PhotoImage(file='Warning.gif')


mainframe = ttk.Frame(app1, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

imageframe =  ttk.Label(mainframe, image=imgobj)
imageframe.grid(column=1, row=1, columnspan=5, rowspan=10)  #grid bør ikke laves i samme linje som selve framen, for så henviser variablen til grid'et og ikke til label-objectet
warning_frame=ttk.Label(mainframe, image=warn_img)
warning_frame.grid(column=3, row=5, columnspan=3,rowspan=5)



feet = StringVar()  #StringVar sætter en variabel som TK systemet holder øje med om den ændrer sig
meters = StringVar()
l_runder=StringVar()
l_tid=StringVar()

feet_entry = ttk.Entry(mainframe, width=17, textvariable=feet)
feet_entry.grid(column=2, row=5)


ttk.Label(mainframe, textvariable=meters).grid(column=2, row=6)  #denne label er ikke navngivet og skal ikke manupulerets senere. Derfor må den godt stå  ién linje.
ttk.Label(mainframe, textvariable=l_runder).grid(column=2, row=7)
ttk.Label(mainframe, textvariable=l_tid).grid(column=2, row=8)

ttk.Label(mainframe, text="løbernummer").grid(column=1, row=5)
ttk.Label(mainframe, text="Løberens navn").grid(column=1, row=6)
ttk.Label(mainframe, text="antal runder løbet:").grid(column=1, row=7)
ttk.Label(mainframe, text="sidste rundes tid:").grid(column=1, row=8)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
warning_frame.grid_remove()   #SKAL stå efter den der child.grid_config-ting
feet_entry.focus()
app1.bind('<Return>', løberinfo)
app1.bind('<KeyRelease>', nummer_længde_tjek)

app1.mainloop()