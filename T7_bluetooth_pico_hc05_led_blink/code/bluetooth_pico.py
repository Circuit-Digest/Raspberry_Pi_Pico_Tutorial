from machine import Pin,UART

uart = UART(0, baudrate=38400, tx=Pin(0), rx=Pin(1))

Led = 15

led = Pin(Led, Pin.OUT)

while True:
    if uart.any():
        command = uart.readline()
        if command==b'\x01':
            led.high()
            print("ON")
        else:
            led.low()
            print("OFF")