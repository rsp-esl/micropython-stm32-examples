# File: button_click_count.py
# Date: 2020-05-12

import utime as time
from machine import Pin, Timer
import pyb

clicked = False

def ext_int_cb(irq_line):
    global ext_irq, clicked
    ext_irq.disable()
    clicked = True

btn_pin = Pin('PA0', mode=Pin.IN)
ext_irq = pyb.ExtInt( btn_pin,
            pyb.ExtInt.IRQ_FALLING,
            pyb.Pin.PULL_UP, ext_int_cb )
try:
    cnt = 0
    while True:
        if clicked:
            cnt += 1
            print('Button clicked', cnt)
            clicked = False
            ext_irq.enable()
        time.sleep_ms(200)
except KeyboardInterrupt:
    pass
finally:
    ext_irq.disable()
    print('Done')

