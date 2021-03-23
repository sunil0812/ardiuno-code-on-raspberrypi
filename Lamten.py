from machine import Pin , ADC 
from utime import sleep

#digital write 25 onboard LED
def digitalwrite(pin,high_low):
    Pin(pin,Pin.OUT).value(high_low)

#digital read  25
def digitalread (pin):
    Pin(pin,Pin.IN,Pin.PULL_DOWN)

#analog write PWM
def analogwrite (pin,voltout):
    f   =60
    t   =1/f
    dc  =(voltout/5)
    ton = dc*t
    toff= t-ton
    write =Pin(pin,Pin.OUT)
    write.value(1)# 1 is high 5 volt
    sleep(ton)#half second
    write.value(0)# 0 is low 0 volt
    sleep(toff)#half second
    
    
#analog read 16 bit 
def analogread(pin):
    ADC(pin).read_u16()
#delay(time in seconds)    
def delay(time):
    sleep(time)

#blink
def blink(pin,time):
    Pin(pin,Pin.OUT).value(1)
    sleep(time)
    Pin(pin,Pin.OUT).value(0)
    sleep(time)

