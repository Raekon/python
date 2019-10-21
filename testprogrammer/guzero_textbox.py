from guizero import *

def typeme(wef):
    print("typeme kører")
    print(wef)
    textbox.destroy()
    textbox=TextBox(app, command=typeme, grid=[0,0])
        
def mouseme(event_data):
    print(event_data.widget)
    print(event_data.x)
    
   

app=App(layout="grid")
textbox=TextBox(app, command=typeme, grid=[0,0])
text=Text(app, text="text", grid=[0,1])
text.when_key_pressed = typeme
text.when_clicked = mouseme

