from machine import Pin
import utime
import _thread

led1 = Pin(16, machine.Pin.OUT)
led2 = Pin(15, machine.Pin.OUT)


sLock = _thread.allocate_lock()

def CoreTask():
    while True:
        sLock.acquire()
        print("Entered into the second Thred")
        utime.sleep(1)
        led2.high()
        print("Led 2 turned on")
        utime.sleep(2)
        led2.low()
        print("Led 2 turned off")
        utime.sleep(1)
        print("Exiting from the 2nd Thread")
        utime.sleep(1)
        sLock.release()

_thread.start_new_thread(CoreTask, ())

while True:
    # We acquire the semaphore lock
    sLock.acquire()
    print("Entered into the main Thred")
    led1.toggle()
    utime.sleep(0.15)
    print("Led 1 started to toggle.")
    utime.sleep(1)
    print("Exiting from the main Thread")
    utime.sleep(1)
    # We release the semaphore lock
    sLock.release()