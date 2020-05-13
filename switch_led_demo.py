# File: switch_led_demo.py
# Date: 2020-05-12
# Micropython-STM31F411CE Black Pill

import pyb
import utime as time

sw  = pyb.Switch() # user push button
led = pyb.LED(1  ) # on-board LED (blue), PC13 pin

# toggle the LED if the button switch is pressed.
sw.callback( lambda: led.toggle() )

try:
    last_time = time.ticks_ms()
    while True:
        now = time.ticks_ms()
        if sw.value(): # button hold pressed
            if time.ticks_diff( now, last_time ) >= 2000:
                print( 'button long pressed' )
                break
        else:
            last_time = now
			
except KeyboardInterrupt:
    pass
finally:
    sw.callback(None) 
    led.off()
    print('Done')

