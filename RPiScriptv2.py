import logging
from tuya_connector import TuyaOpenAPI
from keys import CELLO_LAMP_ID, CS_LAMP_ID, BEDSIDE_LAMP_ID, ACCESS_ID, ACCESS_KEY, API_ENDPOINT
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.OUT)

openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

setLamps = False

CSL_STATUS = openapi.get("/v1.0/iot-03/devices/{}/status".format(CS_LAMP_ID))["result"][0]["value"]
  
def setValue(value):
    CL_commands = {'commands': [{'code': 'switch_1', 'value': value}]}
    CSL_commands = {'commands': [{'code': 'switch_1', 'value': value}]}
    BSL_commands = {'commands': [{'code': 'switch_1', 'value': value}]}

    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(CELLO_LAMP_ID), CL_commands)
    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(CS_LAMP_ID), CSL_commands)
    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(BEDSIDE_LAMP_ID), BSL_commands)


while True:
    if GPIO.input(18) == True:
       
        if openapi.get("/v1.0/iot-03/devices/{}/status".format(CS_LAMP_ID))["result"][0]["value"] == True:
            setLamps = False
        else:
            setLamps = True
           
        setValue(setLamps)
       