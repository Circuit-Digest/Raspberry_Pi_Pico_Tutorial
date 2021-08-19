from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
import framebuf,sys

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                            # oled display height

image_byte_arr = b'BM\xbe\x00\x00\x00\x00\x00\x00\x00>\x00\x00\x00(\x00\x00\x00 \x00\x00\x00 \x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc4\x0e\x00\x00\xc4\x0e\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xfc?\xff\xff\xfb\xcf\xff\xff\xe7\xf7\xff\xff\xc7\xf1\xff\xffs\xc6\x7f\xfe\xf1\xcf\xbf\xfd\xf7\xef\xbf\xfd\xf7\xf7\xdf\xff\xff\xf7\xdf\xfb\xef\xf3\xdf\xf9\xc7\xf1\x8f\xf6\x13\xeco\xf7|>w\xf7~\x7fw\xf7\xfe\x7fw\xf7\xff\x7fo\xfb\x7f\x7fo\xfc~~\x1f\xfd\xbc=\xff\xff\xe3\xe3\xbf\xfe\xf7\xf7\xbf\xff\x7f\xff\x7f\xff3\xe4\xff\xffx\x1f\x7f\xfe\xfc?\xbf\xfd\xfe?\xff\xfb\xff\x7f\xdf\xfb\xff\x7f\xdf\xfb\xfe\x7f\xef\xfb\xff\xbf\xef\xf9\xfb\xdf\x9f\xff\x0f\xf0\xff'
image_width = 32
image_height = 32

#OLED I2C Configuration
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000) #Init I2C using pinsGP17&GP16 (defaultI2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c) # Init oled display



#OLED Text display Function
def displayText(text, position=(0,0),clear_oled=True,show_text=True):
    if clear_oled:
        oled.fill(0) # Clear the oled display in case it has junk on it.
    oled.text(text,position[0],position[1]) # dispaying text
    if show_text:
        oled.show()  # Updating the display
        
        
#OLED Image display function
        
def displayImage(image_byte_array, image_resolution,position=(0,0),clear_oled=False,show_img=True):
    img = bytearray(image_byte_array)
    img = bytearray([img[i] for i in range(len(img)-1,-1,-1)])
    
    frame = framebuf.FrameBuffer(img, image_resolution[0], image_resolution[1], framebuf.MONO_HMSB) # MONO_HLSB, MONO_VLSB, MONO_HMSB
    
    if clear_oled:
        oled.fill(0) # clear the OLED
        print("clear")
    if show_img:
        oled.blit(frame, position[0],position[1]) # show the image at location (x=0,y=0)
        oled.show()
        
        print("display")


#Scrolling Text on OLED
text1 = "Welcome to"
text2 = "CircuitDigest"

for x in range(0, WIDTH):
    displayText(text1,(x,0),clear_oled=False,show_text=True)
    displayText(text2,(WIDTH-x,20),clear_oled=True,show_text=True)
    if x == WIDTH:
        break
    else:
        x+=5
        
        



while True:
    y=0
    text = "Interfacing OLED"
    oled.fill(0)
    
    #Scrolling Text And Image Horizontaly
    for x in range(0,WIDTH-image_width):
        displayImage(image_byte_arr,(image_width,image_height),(x,y),clear_oled=False)
        displayText(text,(x,y+40),clear_oled=False,show_text=True)
        
        if x == (WIDTH-image_width)-1:
            break
        else:
            x+=2
            oled.fill(0)
            
    #Reverse Scrolling Text And Image Horizontaly
    for x in range(WIDTH-image_width,-1,-1):
        displayImage(image_byte_arr,(image_width,image_height),(x,y),clear_oled=True)
        displayText(text,(x,y+40),clear_oled=False,show_text=True)
        if x == 0:
            break
        else:
            x-=2
    
