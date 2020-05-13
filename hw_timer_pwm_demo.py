# File: hw_timer_pwm_demo.py
# Date: 2020-05-12
# Micropython-STM31F411CE Black Pill 

import utime as time
from machine import Pin
import pyb

# print system frequencies
freq = pyb.freq() 
print( 'CPU  frequecy [Hz]:', freq[0] )  # 96MHz
print( 'AHB  frequecy [Hz]:', freq[1] )  # 96MHz
print( 'APB1 frequecy [Hz]:', freq[2] )  # 24MHz
print( 'APB2 frequecy [Hz]:', freq[3] )  # 48MHz

# create Timer (use TIM4)
tim = pyb.Timer( 4, freq=5 ) # 5 Hz (for LED blink)

# Choose PB8 pin for TIM4_CH3 or PB9 pin for TIM4_CH4
pwm = tim.channel( 3, pyb.Timer.PWM,
         pin=pyb.Pin.board.PB8, pulse_width=0 )
pwm.pulse_width( tim.period()//2 ) # 50% duty cycle

print( 'prescaler   : {:>5}'.format( tim.prescaler()) )
print( 'frequency   : {:>5} [Hz]'.format( tim.freq())  )
print( 'period      : {:>5} [us]'.format( tim.period()) )
print( 'pulse width : {:>5} [us]'.format( pwm.pulse_width()) )

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
finally:
    tim.deinit()
    print('Done')

