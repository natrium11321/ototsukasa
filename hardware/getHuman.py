#code : UTF-8

# --- setup --- #
inputpin = 26

import RPi.GPIO as GPIO

def getHuman():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(inputpin, GPIO.IN)
    tmp = GPIO.input(inputpin)
    GPIO.cleanup()
    return tmp
