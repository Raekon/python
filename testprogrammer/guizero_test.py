from guizero import *
import time

class print_up(object):
    def __init__(self):
        self.app = App()
        self.media=0   #is it photo or video
        self.box0=Box(self.app, layout="grid")  #set the initial box with coices
        self.button_photo=PushButton(self.box0, grid=[0,0], text="Photo", command=self.photo)   #photobutton
        self.button_video=PushButton(self.box0, grid=[3,0], text="Video", command=self.video)   #videobutton
        self.box1 = Box(self.app, layout="grid")   #second windows box
        self.box1.hide()  #Don't show the box yet, until user chooses btw phot and vid
        self.minute_text=Text(self.box1, text="Hvor mange minutter skal der filmes? ", grid=[0, 0,3,1])  
        self.minutes = TextBox(self.box1, text="", grid=[3, 0]) #total time
        self.minutes.focus()  #focus the first textbox
        self.timelapse_text=Text(self.box1, text="hvor mange sekunder mellem hvert billede? ", grid=[0, 1,3,1])
        self.timelapse = TextBox(self.box1, text="", grid=[3, 1])  #Whats the timelapse - this is changed in self.video
        self.filename_text=Text(self.box1, text="filnavn ? ", grid=[0, 2,3,1])
        self.filename = TextBox(self.box1, text="", grid=[3, 2])  #the base filename
        self.size_text=Text(self.box1, text=("størrelse: "), grid=[0, 3,2,1])
        self.picsize = Slider(self.box1, start=640, end=3280, grid=[3, 3], command=self.update_size)  #slider for the picture size
        self.picsize.text_size=1    #hide the native text on the slider
        self.slider_text = Text(self.box1, text="640 x 480",grid=[3, 4])    #display the slider values calculated in self.update_size
        self.color_choice=ButtonGroup(self.box1, options=["Farve", "Sort/hvid"], selected="Sort/hvid", grid=[0,5])   #choose color
        self.namestamp_choice= ButtonGroup(self.box1, options=["Timestamp", "numre"], selected="Timestamp", grid=[1,5])   #chose number scheme for filenames
        self.preview_choice= ButtonGroup(self.box1, options=["200", "400", "800","fullsize","ingen preview"], selected="ingen preview", grid=[2,5])  #chose preview size
        self.submitbutton=PushButton(self.box1, command=self.printit, text="Submit", grid=[3,6])
        self.resetbutton=PushButton(self.box1, command=self.reset, text="Reset", grid=[0,6])
        
        
    def photo(self):
        self.box0.hide()  #hide the inital box
        self.box1.show()    #show tha main choices box
        self.media=0        #set the media variable to 0
        
    def video(self):
        self.box0.hide()  #hide the initial box
        self.timelapse_text.value="hvor mange billeder i sekundet?"   #framerate instead of timelapse
        self.videoslider=Slider(self.box1, start=640, end=1080, grid=[3, 3], command=self.update_videosize)  #new size-slider for video
        self.picsize.hide()  #hide the timeslider for photos
        self.media=1    
        self.box1.show()  
        
    def reset(self):
        self.box1.hide()  #hide the inital box
        self.box0.show()    #show tha main choices box
        self.media=0        #set the media variable to 0

    def printit(self):
        print("virker knappen? {0},{1},{2},{3},{4},{5},{6}".format(self.minutes.get(), self.timelapse.get(), self.filename.get(),self.picsize.value,self.color_choice.value,self.namestamp_choice.value,self.preview_choice.value))

    def update_videosize(self):     #this function calculates the height from the chosen width-input
        self.slider_text.value=self.videoslider.value
        picture_width=int(float(self.videoslider.value))
        picture_height=int(picture_width//1.33)
        width_text="{0} x {1}".format(picture_width,picture_height)
        self.slider_text.value=width_text    #set the text under the slider to the result
        
    def update_size(self):     #this function calculates the height from the chosen width-input
        self.slider_text.value=self.picsize.value
        picture_width=int(float(self.picsize.value))
        picture_height=int(picture_width//1.33)
        width_text="{0} x {1}".format(picture_width,picture_height)
        self.slider_text.value=width_text   #set the text under the slider to the result



printer=print_up()
#printer.app.display()
