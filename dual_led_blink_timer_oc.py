# File: dual_led_blink_timer_oc.py
# Date: 2020-05-12

import pyb

# T3_CH1 -> PB4 pin, T3_CH2 -> PB5 pin
timer = pyb.Timer(3, freq=2) # use TIM3, freq. 2 Hz

half_period = (timer.period()+1)//2

ch1 = timer.channel(1, mode=pyb.Timer.OC_TOGGLE,
            pin=pyb.Pin.board.PB4, compare=0)
ch2 = timer.channel(2, mode=pyb.Timer.OC_TOGGLE,
            pin=pyb.Pin.board.PB5, compare=half_period)
try:
    while True: 
        pass # do nothing in main loop
except KeyboardInterrupt:
    pass
finally:
    timer.deinit() # turn off timer
    print('Done')
	
