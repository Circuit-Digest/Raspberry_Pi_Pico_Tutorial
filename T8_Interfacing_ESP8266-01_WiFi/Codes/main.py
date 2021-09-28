'''
    File name: main.py
    Author: Noyel Seth
    Email: noyelseth@gmail.com
    MicroPython Version: 3.4
'''

from machine import UART, Pin
import time
from esp8266 import ESP8266

esp01 = ESP8266()
esp8266_at_ver = None

led=Pin(25,Pin.OUT)

print("StartUP",esp01.startUP())
#print("ReStart",esp01.reStart())
print("StartUP",esp01.startUP())
print("Echo-Off",esp01.echoING())
print("\r\n\r\n")

'''
Print ESP8266 AT comand version and SDK details
'''
esp8266_at_var = esp01.getVersion()
if(esp8266_at_var != None):
    print(esp8266_at_var)

'''
set the current WiFi in SoftAP+STA
'''
esp01.setCurrentWiFiMode()

#apList = esp01.getAvailableAPs()
#for items in apList:
#    print(items)
    #for item in tuple(items):
    #    print(item)
  
print("\r\n\r\n")

'''
Connect with the WiFi
'''
print("Try to connect with the WiFi..")
while (1):
    if "WIFI CONNECTED" in esp01.connectWiFi("ssid","pwd"):
        print("ESP8266 connect with the WiFi..")
        break;
    else:
        print(".")
        time.sleep(2)


print("\r\n\r\n")
print("Now it's time to start HTTP Get/Post Operation.......\r\n")

while(1):    
    led.toggle()
    time.sleep(1)
    
    '''
    Going to do HTTP Get Operation with www.httpbin.org/ip, It return the IP address of the connected device
    '''
    httpCode, httpRes = esp01.doHttpGet("www.httpbin.org","/ip","RaspberryPi-Pico", port=80)
    print("------------- www.httpbin.org/ip Get Operation Result -----------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("-----------------------------------------------------------------------------\r\n\r\n")
    
    
    '''
    Going to do HTTP Post Operation with www.httpbin.org/post
    '''
    post_json="abcdefghijklmnopqrstuvwxyz"  #"{\"name\":\"Noyel\"}"
    httpCode, httpRes = esp01.doHttpPost("www.httpbin.org","/post","RPi-Pico", "application/json",post_json,port=80)
    print("------------- www.httpbin.org/post Post Operation Result -----------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("--------------------------------------------------------------------------------\r\n\r\n")
    #break
    

