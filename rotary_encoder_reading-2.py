# File: rotary_encoder_reading-2.py
# Date: 2020-05-12

import utime as time
from machine import Pin
import pyb
from micropython import const

args = {'pull': pyb.Pin.PULL_NONE, 'af': pyb.Pin.AF2_TIM3}
a_pin = Pin('PB4', mode=pyb.Pin.AF_PP, **args)
b_pin = Pin('PB5', mode=pyb.Pin.AF_PP, **args)

NUM_STEPS = const(100)
timer = pyb.Timer(3, prescaler=1, period=(4*NUM_STEPS-1))
channel = timer.channel(1, pyb.Timer.ENC_AB)

timer.counter(0) # reset counter

try:
    saved_cnt = timer.counter()//4
    while True:
        cnt = timer.counter()//4
        if saved_cnt != cnt:
            saved_cnt = cnt
            print( 'Position: {}'.format(cnt) )
        time.sleep_ms(10)
except KeyboardInterrupt:
    pass
finally:
    timer.deinit()
    print('Done')

