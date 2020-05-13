# File: sw_timer_demo-2.py
# Date: 2020-05-12
# Micropython-STM31F411CE Black Pill

import pyb
from machine import Timer
import utime as time

done = False

def start_time():
    sw.callback( None ) 
    tim.init( mode=Timer.ONE_SHOT,
          period=3000, # in msec
          callback=led_pulses )

def led_pulses(t):
    global done
    led = pyb.LED(1) # on-board LED (blue)
    # blink the LED for 10 times 
    for i in range(20):
        led.toggle()
        time.sleep_ms(100)
    t.deinit() # disable timer 
    done = True

tim = Timer(-1)
sw  = pyb.Switch()
sw.callback( start_time ) 

try:
    while not done:
        pass
except KeyboardInterrupt:
    pass
finally:
    print('Done')

