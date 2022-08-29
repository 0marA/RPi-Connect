import RPi.GPIO as GPIO
import tinytuya
import time
from secrets import CHARGING_STATION_DEVICE_ID, CHARGING_STATION_IP, CHARGING_STATION_KEY, CELLO_LAMP_DEVICE_ID, CELLO_LAMP_IP, CELLO_LAMP_KEY, BEDSIDE_LAMPS_DEVICE_ID, BEDSIDE_LAMPS_IP, BEDSIDE_LAMPS_KEY

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.OUT)

celloLamp = tinytuya.OutletDevice(CELLO_LAMP_DEVICE_ID, CELLO_LAMP_IP, CELLO_LAMP_KEY)
chargingStationLamp = tinytuya.OutletDevice(CHARGING_STATION_DEVICE_ID, CHARGING_STATION_IP, CHARGING_STATION_KEY)
bedsideLamp = tinytuya.OutletDevice(BEDSIDE_LAMPS_DEVICE_ID, BEDSIDE_LAMPS_IP, BEDSIDE_LAMPS_KEY)

celloLamp.set_version(3.3)
chargingStationLamp.set_version(3.1)
bedsideLamp.set_version(3.1)

lampsOn = False
while True:
    if GPIO.input(18) == True:
        if (lampsOn):
            celloLamp.turn_on()
            chargingStationLamp.turn_on()
            bedsideLamp.turn_on()
            print("Turned on")
            GPIO.output(23, GPIO.HIGH)
            time.sleep(.5)
            GPIO.output(23, GPIO.LOW)
        else:
            celloLamp.turn_off()
            chargingStationLamp.turn_off()
            bedsideLamp.turn_off()
            print("Turned off")
            GPIO.output(23, GPIO.HIGH)
            time.sleep(.5)
            GPIO.output(23, GPIO.LOW)
