from PIL import Image, ImageFilter
import time

im=Image.open('Wednesday.png')
px=im.load()
print(im.format,im.size,im.mode)

def rainbow_specific():
    for y in range(10,255):
        for x in range (1,640):
            #print("%s på pixel %i,%i" %(px[x,y],x,y))
            if px[x,y]!=(57,49,165):
                px[x,y]=(x%255,x%255+y,255-y%255)
                print ("her er en anden farve")
                #time.sleep(1)

def rainbow_all():
    for y in range (1,400):
        for x in range (1,640):
            px[x,y]=(x%255,(x+y)%255,y%255)
            
def readPix(x,y):
    r,g,b=px[x,y]
    print ("red: %i  green:%i   blue:%i" %(r,g,b))
    r+=30
    g+=30
    b+=30
    px[x,y]=(r,b,g)
    
def compare():
    im1=Image.open('Wednesday.png')
    im2=Image.open('Wednesday.jpg')
    image1=im1.load()
    image2=im2.load()
    
    for y in range(1,972):
        for x in range(1,1296):
            pix1=image1[x,y]
            pix2=image2[x,y]
            
            if pix1!=pix2:
                print ("hov, her er en fejl. pix 1 er %s og pix 2 er %s" %(pix1, pix2))
                print ("x er %i og y er %i" %(x,y))
                time.sleep(3)
                

print (px[200,200])

#blurred = im.filter(ImageFilter.BLUR)
#readPix(200,200)
#print (px[200,200])
compare()
    # Display both images
#im.save ("Wednesday.png")    
#im.show()
#blurred.show()