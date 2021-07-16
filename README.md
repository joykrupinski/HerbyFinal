# HerbyFinal
Welcome to HERBY! If you would like to build your own hydroponic system and surveil it with a raspberry pi you've come to the right place. 
We have worked on our own system and have uploaded all necessary code and code documentation in this repo. 

You will find relevant python code to use with a TDS, Temperature and Humidity, Light, Moisture sensor. The sensors as well as the relevant code files were purchased from SEEED Studio together with a Grove Base Hat (https://github.com/Seeed-Studio/grove.py). These are the hardware components we used and the code files you will need to start the sensors. All files are included in this git repo.

∙Raspberry Pi 3B with Raspbian OS
∙Grove Hat Base Kit (with Display, code for display all in display folder)
∙TDS Sensor - TDS.py
∙Moisture Sensor - grove_moisture_sensor.py
∙Light Sensor - grove_light_sensor_v1_2.py
∙Temperature and Humidity - no seperate file, installation of CircuitPython-DHT Library necessary, import used in herby.py

∙files for signal processing to be used as imports: adc.py (processing from analog ports - Analog Digital Converter), i2c.py (processing from digital ports)
∙Code to run all sensors simultaneously - herby.py

∙Written file for automated git push - test.csv
∙Website (with python dash) - app.py
∙Website was deployed with Heroku:
   requirements for cloud deployment - requirements.txt (includes necessary python libraries), Procfile (source file, required python version)


For more detailed information and further set-up/ hardware components read the step by step guide also provided in this repository

Website: https://herbyproject.herokuapp.com/

