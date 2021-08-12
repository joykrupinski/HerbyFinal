import time
from mraa import getGpioLookup
from upm import pyupm_buzzer as upmBuzzer
import pandas as pd
from datetime import date

#Moisture import
from grove.grove_moisture_sensor import GroveMoistureSensor

#display import
from grove.display.jhd1802 import JHD1802

#TDS import
from TDS import GroveTDS

#Light import
from grove.grove_light_sensor_v1_2 import GroveLightSensor

#humidity and temperature import
from seeed_dht import DHT

#import for csv file
import csv

#seperate sensor functions to read and process values, to be called in main
  
#tds and moisture       
def moisture_tds_main():    
        #read sensor values
        sensor = GroveMoistureSensor(4)
        sensor_tds = GroveTDS(0)
        
        #print sensor values
        print('TDS Value: {0}'.format(sensor_tds.TDS))
        
        mois = sensor.moisture
        if 0 <= mois and mois < 300:
            level = 'dry'
        elif 300 <= mois and mois < 600:
            level = 'moist'
        else:
            level = 'wet'
        
        #print values in terminal (level printed in terminal)      
        print('moisture: {}, {}'.format(mois, level)) 
        return mois,sensor_tds.TDS
        
#light       
def Light_main():      
        #read sensor values
        sensor = GroveLightSensor(2)
        #print values in terminal
        print('light value {}'.format(sensor.light))
        
        return sensor.light
        
#temperature and humidity
def temp_hum_main():
        #display
        lcd = JHD1802()
        #find correct port in base hat
        sensor = DHT('11', 5)
        
        #read sensor values
        humi, temp = sensor.read()
        #print values in terminal
        print('temperature {}C, humidity {}%'.format(temp,humi))
            
        #print values on display
        lcd.setCursor(0,0)
        lcd.write('temperature: {0:2}C'.format(temp))
        #lcd.setCursor(1,0)
        #lcd.write('humidity: {0:5}%'.format(humi))
        
        return humi,temp
        
#main functions calls all sensor functions and writes values in csv file 
def main():
    
    while True:
        
        #call all sensors
        mois,tds = moisture_tds_main()
        light = Light_main()
        hum,temp = temp_hum_main()
        
        #get current date in correct format and write all sensor values in file with according date
        currentDate = date.today()
        today = currentDate.strftime('%m/%d/%y')
        toWrite = [tds, mois, light, temp, hum]
        #create data frame 
        df = pd.read_csv('test.csv')
        df[today] = toWrite
        df.to_csv('test.csv', index=False)
        #sleep for 24h, programm runs once a day
        time.sleep(86400)
        

if __name__ == '__main__':
    main()
