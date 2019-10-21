from guizero import *

class game (object):
    def __init__(self):
        self.app=App()
        self.box1=Box(self.app, layout='grid')
        for x in range(3):  #distributing background fields making 3x3 grid
            for y in range(3):
                Picture(self.box1,image='bg150.png',grid=[x,y])
                
        self.man_left=Picture(self.box1,image='man_left.png',grid=[1,1])
        self.man_right=Picture(self.box1,image='man_right.png',grid=[1,1],visible=False)
        self.butt=PushButton(self.box1, text="text", grid=[0,1])
        
        def clicked(event_data):
            print("The man was clicked")
            self.man_left.visible=False
            self.man_right.visible=True
            
        
        
        self.man_left.when_clicked=clicked

        
game1=game()


            
        