import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    if GPIO.input(15) == True:
        print("Button 20 Pressed")