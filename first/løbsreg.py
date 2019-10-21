
#coding=UTF-8
from guizero import App, Text, TextBox, error, yesno
import sqlite3
import time

rundeNavne=['runde1','runde2','runde3','runde4','runde5']  #VARIABLE til indskrivning af rundetider
rundetidNavne=['runde1tid','runde2tid','runde3tid','runde4tid','runde5tid'] #variable til indskrivning af absolut rundetidspunkt

loeberbasen= sqlite3.connect('løbetider.db')  #SQL forbindelsen til basen
c=loeberbasen.cursor()  #cursoren er en slags genvej til mysql_query statements
#c.execute('''CREATE TABLE tider (nummer integer PRIMARY KEY AUTOINCREMENT, navn text, runder int, starttid int NULL, runde1tid int NULL, runde1 int NULL, runde2tid int NULL, runde2 int NULL)''')





niveau=0

def nummertjek():
    
    loeberNummer =  input("Scan naeste nummer")
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
         
        
indskriv(nummertjek())     
  
    

# her skal vaere en funktion der tjekker loeberens tid op imod hall of fame.



#compare input to loebetider



#input new lap into loebetider




#output new lap to console