import logging
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER
from secrets import CELLO_LAMP_ID, CS_LAMP_ID, BEDSIDE_LAMP_ID, ACCESS_ID, ACCESS_KEY, API_ENDPOINT

toggle = True

# Enable debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

# Init OpenAPI and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()





# Get the instruction set of the device
CL_response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(BEDSIDE_LAMP_ID))
CSL_response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(CELLO_LAMP_ID))
BSL_response = openapi.get("/v1.0/iot-03/devices/{}/functions".format(CS_LAMP_ID))


# Send commands
CL_commands = {'commands': [{'code': 'switch_1', 'value': toggle}]}
CSL_commands = {'commands': [{'code': 'switch_1', 'value': toggle}]}
BSL_commands = {'commands': [{'code': 'switch_1', 'value': toggle}]}

openapi.post('/v1.0/iot-03/devices/{}/commands'.format(CELLO_LAMP_ID), CL_commands)
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(CS_LAMP_ID), CSL_commands)
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(BEDSIDE_LAMP_ID), BSL_commands)


