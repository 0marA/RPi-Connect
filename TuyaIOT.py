import logging
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

ACCESS_ID = "5aejhctqdjm747t9ps9j"
ACCESS_KEY = "169213aeb5da4d79a47c7114a8a73c7d"
API_ENDPOINT = "https://openapi.tuyaus.com"

CELLO_LAMP_ID = "eb578c7cb30fd0513cmxyq"
CS_LAMP_ID = "75070011840d8e52a412"
BEDSIDE_LAMP_ID = "75070011840d8e52a4e7"


# Enable debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

# Init OpenAPI and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()


# Call APIs from Tuya
# Get the device information
CL_response = openapi.get("/v1.0/iot-03/devices/{}".format(BEDSIDE_LAMP_ID))
CSL_response = openapi.get("/v1.0/iot-03/devices/{}".format(CELLO_LAMP_ID))
BSL_response = openapi.get("/v1.0/iot-03/devices/{}".format(CS_LAMP_ID))


# Get the instruction set of the device
CL_response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(BEDSIDE_LAMP_ID))
CSL_response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(CELLO_LAMP_ID))
BSL_response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(CS_LAMP_ID))


# Send commands
CL_commands = {'commands': [{'code': 'switch_1', 'value': True}]}
CSL_commands = {'commands': [{'code': 'switch_1', 'value': True}]}
BSL_commands = {'commands': [{'code': 'switch_1', 'value': True}]}

openapi.post('/v1.0/iot-03/devices/{}/commands'.format(CELLO_LAMP_ID), CL_commands)
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(CS_LAMP_ID), CSL_commands)
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(BEDSIDE_LAMP_ID), BSL_commands)


# Get the status of a single device
CL_response = openapi.get("/v1.0/iot-03/devices/{}/status".format(BEDSIDE_LAMP_ID))
CSL_commands = openapi.get("/v1.0/iot-03/devices/{}/status".format(CELLO_LAMP_ID))
BSL_commands = openapi.get("/v1.0/iot-03/devices/{}/status".format(CS_LAMP_ID))