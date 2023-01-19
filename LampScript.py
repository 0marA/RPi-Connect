import logging
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER
from keys import CELLO_LAMP_ID, CS_LAMP_ID, BEDSIDE_LAMP_ID, ACCESS_ID, ACCESS_KEY, API_ENDPOINT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.OUT)

lampsOn = False

# Enable debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

# Init OpenAPI and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Get the instruction set of the device
CL_response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(BEDSIDE_LAMP_ID))
CSL_response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(CELLO_LAMP_ID))
BSL_response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(CS_LAMP_ID))


def setValue(value):
    # Send commands
    CL_commands = {'commands': [{'code': 'switch_1', 'value': value}]}
    CSL_commands = {'commands': [{'code': 'switch_1', 'value': value}]}
    BSL_commands = {'commands': [{'code': 'switch_1', 'value': value}]}

    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(CELLO_LAMP_ID), CL_commands)
    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(CS_LAMP_ID), CSL_commands)
    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(BEDSIDE_LAMP_ID), BSL_commands)


while True:
    if GPIO.input(18) == True:
        setValue(lampsOn)
        lampsOn = not lampsOn