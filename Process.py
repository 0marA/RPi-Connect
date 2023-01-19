from tuya_connector import TuyaOpenAPI
from keys import CELLO_LAMP_ID, CS_LAMP_ID, BEDSIDE_LAMP_ID, ACCESS_ID, ACCESS_KEY, API_ENDPOINT
import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from rpi_ws281x import *

LED_COUNT      = 30     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 65      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

pixels = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
pixels.begin()

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
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.OUT)

openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

setLamps = False
pixelStatus = True

CSL_STATUS = openapi.get("/v1.0/iot-03/devices/{}/status".format(CS_LAMP_ID))["result"][0]["value"]
  
def setValue(value):
    CL_commands = {'commands': [{'code': 'switch_1', 'value': value}]}
    CSL_commands = {'commands': [{'code': 'switch_1', 'value': value}]}
    BSL_commands = {'commands': [{'code': 'switch_1', 'value': value}]}

    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(CELLO_LAMP_ID), CL_commands)
    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(CS_LAMP_ID), CSL_commands)
    openapi.post('/v1.0/iot-03/devices/{}/commands'.format(BEDSIDE_LAMP_ID), BSL_commands)
    
def getStringValue(value):
    return "On" if value else "Off"

def setPixels(pixelStatus):
    if pixelStatus:
        colorWipe(pixels, Color(255, 255, 255))  # Red wipe
    else:
        colorWipe(pixels, Color(0, 0, 0))  # Red wipe
        
    
    

def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

while True:
    if GPIO.input(12) == True:
        time.sleep(0.5)
        
        if GPIO.input(12) == True:
            pixelStatus = not pixelStatus
            setPixels(pixelStatus)
            
            
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x+10, top + 16),       "Successfully Turned",  font=font, fill=255)
            draw.text((x+20, top+24),     getStringValue(pixelStatus) + " Watch Light", font=font, fill=255)
            
            disp.image(image)
            disp.display()
            time.sleep(3)
            disp.clear()
            disp.display()
            
        else:
            openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
            openapi.connect()
            
            if openapi.get("/v1.0/iot-03/devices/{}/status".format(CS_LAMP_ID))["result"][0]["value"] == True:
                setLamps = False
            else:
                setLamps = True
                
            draw.rectangle((0,0,width,height), outline=0, fill=0)
            draw.text((x+10, top + 16),       "Successfully Turned",  font=font, fill=255)
            draw.text((x+8, top+24),     getStringValue(setLamps) + " Omar's Room Lamps", font=font, fill=255)
            
            setValue(setLamps)

            disp.image(image)
            disp.display()
            time.sleep(3)
            disp.clear()
            disp.display()
           

       