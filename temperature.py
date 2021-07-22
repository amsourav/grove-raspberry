#!/usr/bin/env python

from seeed_dht import DHT 
import time
from grove.display.jhd1802 import JHD1802

READ_TIMEOUT = 5
SLOT = 16 # digital

def main():
    # use i2c port on board 
    lcd = JHD1802()
 
    # Temperature Sensor
    # 11 is the non pro sensor, 16 is pin slot
    sensor = DHT('11', SLOT)
    i = 0
    while True:
        humi, temp = sensor.read()
        lcd.setCursor(0, 0)
        lcd.write('temp #{0:2}: {1:2}C'.format(i, temp))
        lcd.setCursor(1,0)
        lcd.write('humi #{0:2}: {1:2}%'.format(i, humi))
        print('computing...\n')
        i+=1
        time.sleep(READ_TIMEOUT)
 
if __name__ == '__main__':
    main()