#indskrivning til databsaen

import sqlite3
løberbasen= sqlite3.connect('løbetider.db')
c=løberbasen.cursor()

c.execute('''SELECT * FROM tider''')
print (c.fetchone())

niveau=0

while niveau==0:
    løberNavn =  input("indtast et navn: ")
    print ("løbernavn er "+løberNavn)
    if løberNavn!="":
        c.execute('''insert into tider (navn) values (?)''',(løberNavn,))
        løberbasen.commit()
        løberbasen.close()