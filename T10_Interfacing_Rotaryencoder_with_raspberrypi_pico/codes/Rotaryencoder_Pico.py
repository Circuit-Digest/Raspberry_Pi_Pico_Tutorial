import time  
from rotary_irq_rp2 import RotaryIRQ  
from machine import Pin  
SW=Pin(20,Pin.IN,Pin.PULL_UP)  
r = RotaryIRQ(pin_num_clk=18,   
        pin_num_dt=19,   
        min_val=0,   
        reverse=False,   
        range_mode=RotaryIRQ.RANGE_UNBOUNDED)  
val_old = r.value()  
while True:  
   try:  
     val_new = r.value()
     if SW.value()==0:  
       print("Button Pressed")  
       print("Selected Number is : ",val_new)    
       while SW.value()==0:  
         continue    
     if val_old != val_new:  
       val_old = val_new  
       print('result =', val_new)  
     time.sleep_ms(50)  
   except     KeyboardInterrupt:  
     break

