# Display Image & text on I2C driven ssd1306 OLED display 
from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C

import utime


analog_value = machine.ADC(28)
conversion_factor = 3.3 / (65535)



WIDTH  = 128                                            # oled display width
HEIGHT = 64                                            # oled display height

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=200000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)


oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display


 # Clear the oled display in case it has junk on it.
oled.fill(0)

# Add some text
oled.text("CIRCUIT",5,8)
oled.text("DIGEST",45,18)
oled.text("ADC",28,40)

# Finally update the oled display so the image & text is displayed
oled.show()
utime.sleep(1)

while True:
   
    oled.fill(0)
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    utime.sleep(0.2)
    voltageValue = reading* conversion_factor

  
    oled.text("Voltage:",5,8)
    oled.text(str(voltageValue)+"V",15,25)
    oled.show()
    utime.sleep(1)
    