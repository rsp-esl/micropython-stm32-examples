# File: hw_timer_demo.py
# Date: 2020-05-12
# Micropython-STM31F411CE Black Pill

import utime as time
from machine import Pin
import pyb

led = pyb.LED(1)    # on-board LED (blue)

# create Timer (select TIM1..TIM11)
tim = pyb.Timer( 1, freq=10 ) # 10 Hz (fast LED blink)
tim.callback( lambda t: led.toggle() )

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    tim.callback(None)
    tim.deinit()
    print('Done')

