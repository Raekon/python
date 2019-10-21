
#coding=UTF-8
#from guizero import App, Text, TextBox, error, yesno
import sqlite3
import time
from tkinter import *
from tkinter import ttk

rundeNavne=['runde1','runde2','runde3','runde4','runde5']  #VARIABLE til indskrivning af rundetider
rundetidNavne=['runde1tid','runde2tid','runde3tid','runde4tid','runde5tid'] #variable til indskrivning af absolut rundetidspunkt

loeberbasen= sqlite3.connect('løbetider.db')  #SQL forbindelsen til basen
c=loeberbasen.cursor()  #cursoren er en slags genvej til mysql_query statements
#c.execute('''CREATE TABLE tider (nummer integer PRIMARY KEY AUTOINCREMENT, navn text, runder int, starttid int NULL, runde1tid int NULL, runde1 int NULL, runde2tid int NULL, runde2 int NULL)''')

def slet(*args):
    loebernummer_entry.clear()
    print("så er der slettet")

app1=Tk()
app1.title="Tidsregistrering"
mainframe = ttk.Frame(app1, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
loebernummer = StringVar()
loebernummer_entry = ttk.Entry(mainframe, width=7, textvariable=loebernummer)
loebernummer_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Button(mainframe, text="slet", command=slet).grid(column=3, row=3, sticky=W)
loebernummer_entry.focus()
app1.bind('<Return>', slet)
#scannerbox.focus()
#loeberNummer =  scannerbox.get()

#scannerbox.bind('<Return>', slet())

#app1.display()
print (loebernummer)



niveau=0

def nummertjek(loebernummer):
    
    
    if loeberNummer!="":
        tid=int(time.time())
        #her skal der vaere en funktion der tjekker rundens nummer.
        c.execute("SELECT * FROM tider WHERE nummer=?", (loeberNummer,))  # henter loeberens data
        loeberdata=c.fetchone()    #henter den runde loeberen er i gang med (-1)
        if loeberdata!=None:
            print("Scannent ok")
            return(loeberdata)
        else:
            print("Der er sket en fejl i scanningen. Scan igen")
            nummertjek()
        return(loeberdata)
            
#print (nummertjek())

def indskriv(loeberdata):
    global runeNavne
    global rundetidNavne
    loebernummer=loeberdata[0]
    rundenummer=loeberdata[2]
    forrigerunde=rundenummer-1
    naesterunde=rundenummer+1
    starttid=loeberdata[3]
    nutid=int(time.time())
    dennerundestid=rundetidNavne[rundenummer]
    dennerundesnavn=rundeNavne[rundenummer]
    if (rundenummer==0):
        rundetid=nutid-starttid
        
    else:
        print("forrige runde er ",forrigerunde)
        
        forrigerundesnavn=rundetidNavne[forrigerunde]
        c.execute("select {} from tider WHERE nummer=1234 " .format(forrigerundesnavn))
        data= (c.fetchone())
        forrigerundestid=(data[0])
        rundetid=nutid-forrigerundestid
        
    

    #tjekker om tiden er hurtigere en rekorden
    c.execute("SELECT * from halloffame where plads=1")
    rekord=c.fetchone()
    if (rundetid<=rekord[3]):
        svar=input("denne tid er hurtigere end rekorden. skal den godtages? j/n")
        if svar=='j':
            c.execute("UPDATE tider set runder=?, {}=?, {}=? WHERE nummer=?".format(dennerundestid, dennerundesnavn),(naesterunde,  nutid,  rundetid, loebernummer))
        else:
            print("tiden er ikke blevet godkendt. Scan evt igen")
    else:
        c.execute("UPDATE tider set runder=?, {}=?, {}=? WHERE nummer=?".format(dennerundestid, dennerundesnavn),(naesterunde,  nutid,  rundetid, loebernummer))
    loeberbasen.commit()
         
        
indskriv(nummertjek(loebernummer))     
  
    

# her skal vaere en funktion der tjekker loeberens tid op imod hall of fame.



#compare input to loebetider



#input new lap into loebetider




#output new lap to console