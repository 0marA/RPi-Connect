import logging
from tuya_connector import TuyaOpenAPI
from keys import CELLO_LAMP_ID, CS_LAMP_ID, BEDSIDE_LAMP_ID, ACCESS_ID, ACCESS_KEY, API_ENDPOINT
import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess

RST = None
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0

font = ImageFont.load_default()

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
    
def getStringValue(value):
    if value:
        return "On"
    else:
        return "Off"


while True:
    if GPIO.input(18) == True:
       
        if openapi.get("/v1.0/iot-03/devices/{}/status".format(CS_LAMP_ID))["result"][0]["value"] == True:
            setLamps = False
        else:
            setLamps = True
            
        setValue(setLamps)
            
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x+10, top + 16),       "Successfully Turned",  font=font, fill=255)
        draw.text((x+8, top+24),     getStringValue(setLamps) + " Omar's Room Lamps :)", font=font, fill=255)

        disp.image(image)
        disp.display()
        time.sleep(3)
        disp.begin()
        disp.clear()
        disp.display()
           

       