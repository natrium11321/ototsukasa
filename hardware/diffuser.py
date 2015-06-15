# coding: UTF-8
import RPi.GPIO as GPIO
import threading
import time
basepin = 23
interval = 10

class Diffuser:
	
	def __init__(self):
		pass
	
	def run(self):
		"""
		call aroma diffuser
		"""
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(basepin, GPIO.OUT)
		GPIO.output(basepin, GPIO.HIGH)
		time.sleep(interval)
		GPIO.output(basepin, GPIO.LOW)
		GPIO.cleanup()
	
	def diffuse(self):
		threading.Thread(target = self.run).start()
