# File: timer_input_capture.py 
# Date: 2020-05-12
# Micropython-STM31F411CE Black Pill board

import pyb
import utime as time

# Use TIM3_CH1 / PB4 to create PWM output
# Frequency = 50 Hz, period=20000 usec, pulse width 1500 usec
servo_pin = pyb.Pin.board.PB4 # PWM output pin
timer3 = pyb.Timer(3, mode=pyb.Timer.UP, prescaler=83, period=19999)
servo  = timer3.channel(1, mode=pyb.Timer.PWM, pin=servo_pin)
servo.pulse_width(0)

saved_capture = 0
t_pulse = 0

def ic_cb(timer):
    global saved_capture, t_pulse
    if ic_pin.value(): # rising edge
        saved_capture = ic.capture()
    else: # falling edge
        t_pulse = (ic.capture() - saved_capture)
        t_pulse &= 0x0fffffff

# Use TIM2_CH2/ PB3 for input capture
# Frequency = 1MHz (1 usec resolution)
ic_pin = pyb.Pin.board.PB3 # Input capture pin
timer2 = pyb.Timer(2, prescaler=83, period=0x0fffffff)
print( hex(timer2.period()), timer2.prescaler() )
ic = timer2.channel(2, mode=pyb.Timer.IC,
    pin=ic_pin, polarity=pyb.Timer.BOTH, callback=ic_cb)
try:
    values = [1000, 1250, 1500, 1750, 2000]
    while True:
        for pw in values:
            servo.pulse_width( pw )
            time.sleep_ms(100)
            print( 'Pulse width {} usec'.format(t_pulse) )
            t_pulse = 0 # clear measurement value
        time.sleep_ms(500)
except KeyboardInterrupt:
    pass
finally:
    # turn on timers
    timer2.deinit() 
    timer3.deinit() 
    print('Done')

