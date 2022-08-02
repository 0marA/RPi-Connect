import tinytuya
from secrets import CHARGING_STATION_DEVICE_ID, CHARGING_STATION_IP, CHARGING_STATION_KEY, CELLO_LAMP_DEVICE_ID, CELLO_LAMP_IP, CELLO_LAMP_KEY, BEDSIDE_LAMPS_DEVICE_ID, BEDSIDE_LAMPS_IP, BEDSIDE_LAMPS_KEY

celloLamp = tinytuya.OutletDevice(CELLO_LAMP_DEVICE_ID, CELLO_LAMP_IP, CELLO_LAMP_KEY)
chargingStationLamp = tinytuya.OutletDevice(CHARGING_STATION_DEVICE_ID, CHARGING_STATION_IP, CHARGING_STATION_KEY)
bedsideLamp = tinytuya.OutletDevice(BEDSIDE_LAMPS_DEVICE_ID, BEDSIDE_LAMPS_IP, BEDSIDE_LAMPS_KEY)

celloLamp.set_version(3.3)
chargingStationLamp.set_version(3.1)
bedsideLamp.set_version(3.1)

celloLamp.turn_on()
chargingStationLamp.turn_on()
bedsideLamp.turn_on()