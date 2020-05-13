# File: rotary_encoder_reading-1.py
# Date: 2020-05-12

import utime as time
from machine import Pin
import pyb
from micropython import const

POS_MAX = const(100)
POS_MIN = const(0)

# global variables 
cnt = 0
pos = 0

def ext_a_cb(irq_line):
    global cnt, pos
    a, b = a_pin.value(), b_pin.value()
    step = 1 if a^b else -1
    new_cnt = cnt+step
    new_cnt = max(4*POS_MIN,new_cnt)
    new_cnt = min(4*POS_MAX,new_cnt)
    cnt = new_cnt
    pos = cnt//4

def ext_b_cb(irq_line):
    global cnt, pos
    a, b = a_pin.value(), b_pin.value()
    step = -1 if a^b else +1
    new_cnt = cnt+step
    new_cnt = max(4*POS_MIN,new_cnt)
    new_cnt = min(4*POS_MAX,new_cnt)
    cnt = new_cnt
    pos = cnt//4

a_pin = Pin('PB4', mode=Pin.IN)
b_pin = Pin('PB5', mode=Pin.IN)

ext_a = pyb.ExtInt( a_pin,
            pyb.ExtInt.IRQ_RISING_FALLING,
            pyb.Pin.PULL_UP, ext_a_cb )
ext_b = pyb.ExtInt( b_pin,
            pyb.ExtInt.IRQ_RISING_FALLING,
            pyb.Pin.PULL_UP, ext_b_cb )

try:
    last_pos = pos
    while True:
        if last_pos != pos:
            print('Position: {}'.format(pos))
            last_pos = pos
        time.sleep_ms(20)
except KeyboardInterrupt:
    pass
finally:
    # disable external interrupts 
    pyb.ExtInt( a_pin,
            pyb.ExtInt.IRQ_RISING_FALLING,
            pull=pyb.Pin.PULL_NONE, callback=None)
    pyb.ExtInt( b_pin,
            pyb.ExtInt.IRQ_RISING_FALLING,
            pull=pyb.Pin.PULL_NONE, callback=None)
    print('Done')

