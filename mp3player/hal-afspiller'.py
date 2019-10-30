##Music player on Raspberry

import vlc
import time
p=vlc.MediaPlayer("file:///home/pi/Music/c64/03Commando.mp3")
p.play()

time.sleep(5)
p.stop()
