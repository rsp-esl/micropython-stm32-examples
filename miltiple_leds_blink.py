# File: miltiple_leds_blink.py
# Date: 2020-05-12

import utime as time
from machine import Pin, Timer
from micropython import const
import pyb

LED_ON  = const(0)
LED_OFF = const(1)

pin_names = ['PB7', 'PB8', 'PB9']
leds   = []
timers = []

def timer_cb(t):
    for i in range(len(leds)):
        if t is timers[i]:
             # toggle: read-modify-write
             x = leds[i].value()
             leds[i].value( not x )
             break

for pin in pin_names:
    leds.append( Pin(pin,mode=Pin.OUT_PP,value=LED_OFF) )

for i in range(len(leds)): 
    timers.append( Timer(-1, freq=(1<<i), callback=timer_cb) )

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    for led in leds:
        led.value(LED_OFF)
    for tim in timers:
        tim.deinit()
    print('Done')

