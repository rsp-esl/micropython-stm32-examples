# File: dht22_demo.py
# Date: 2020-05-12
# Micropython, STM31F411CE Black Pill board 

from machine import Pin
import utime as time
import dht

sensor = dht.DHT22( Pin('B5') )

try:
    while True:
        try:
            # start measurement
            sensor.measure()
            # read measurement results
            t,h = sensor.temperature(), sensor.humidity()
            print( 'T={:.1f} deg.C, H={:.1f} %'.format(t,h) )
            time.sleep_ms(2000)
        except OSError:
            break
except KeyboardInterrupt:
    pass
finally:
    print('Done')

