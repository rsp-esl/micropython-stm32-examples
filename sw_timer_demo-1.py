# File: sw_timer_demo-1.py
# Date: 2020-05-12
# Micropython-STM31F411CE Black Pill

import pyb
from machine import Timer
import utime as time

sw  = pyb.Switch()  # user push button
led = pyb.LED(1)    # on-board LED (blue)

# create a software timer in periodic mode 
tim = Timer(-1)
tim.init( mode=Timer.PERIODIC,
          period=500, # period in msec
          callback=lambda t: led.toggle() )
try:
    last_time = time.ticks_ms()
    while True:
        if sw.value(): # button  pressed
            break
except KeyboardInterrupt:
    pass
finally:
    sw.callback(None)
    led.off()
    tim.deinit()
    print('Done')

