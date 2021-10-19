from machine import Pin,UART

uart = UART(0,9600)

LedGPIO = 16

led = Pin(LedGPIO, Pin.OUT)

while True:
    if uart.any():
        command = uart.readline()
        # print(command)   # uncomment this line to see the recieved data
        if command==b'\xd0':
            led.high()
            print("ON")
        elif command==b'\xd5':
            led.low()
            print("OFF")
            