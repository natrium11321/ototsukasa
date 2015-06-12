# coding: UTF-8
import RPi.GPIO as GPIO
import time
basepin = 23
interval = 10

def diffuse():
    """
    call aroma diffuser
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(basepin, GPIO.OUT)
    GPIO.output(basepin, GPIO.HIGH)
    time.sleep(interval)
    GPIO.output(basepin, GPIO.LOW)
    GPIO.cleanup()
