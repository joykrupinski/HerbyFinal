import time
from mraa import getGpioLookup
from upm import pyupm_buzzer as upmBuzzer

from grove.grove_temperature_humidity_aht20 import GroveTemperatureHumidityAHT20
from grove.display.jhd1802 import JHD1802

def main():
    
        lcd = JHD1802()
        
        sensor = GroveTemperatureHumidityAHT20(2)
        
        while True:
                humi, temp = sensor.read()
                print('temperature {}C, humidity {}%'.format(temp,humi))
                
                lcd.setCursor(0,0)
                lcd.write('temperature: {0:2}C'.format(temp))

                lcd.setCursor(0,1)
                lcd.write('humidity: {0:5}%'.format(humi))

                time.sleep(10)

if __name__ == '__main__':
    main()