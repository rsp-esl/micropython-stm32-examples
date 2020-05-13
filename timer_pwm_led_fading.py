# File: timer_pwm_led_fading.py
# Date: 2020-05-12
# Micropython-STM31F411CE Black Pill board

import utime as time
from machine import Pin
import pyb
import math

# create a hardware Timer (use TIM4)
tim = pyb.Timer(4, prescaler=47, period=999) # TIM4

# frequency (Hz) = APB2 frequency (Hz)/(prescaler+1)/(period+1)
#                = 48 MHz / 48 / 1000 = 1kHz or 1000 Hz
# You can choose PB8 pin for TIM4_CH3, or PB9 pin for TIM4_CH4

pwm = tim.channel(4, pyb.Timer.PWM,
         pin=pyb.Pin.board.PB9, pulse_width=0)

print( 'PWM period    [us]:', tim.period() )
print( 'PWM frequency [Hz]:', tim.freq()   )

try:
    P = tim.period() # get PWM period in usec
    N = 16
    steps = [int(P*math.sin(math.pi*i/N)) for i in range(N)]
    while True:
        for pw in steps:
           pwm.pulse_width( pw )
           time.sleep_ms( 100 )
except KeyboardInterrupt:
    pass
finally:
    tim.deinit()
    print('Done')

