# coding: UTF-8
import RPi.GPIO as GPIO
import speaker
import time
basepin = 23
interval = 10

class Diffuser:
	
	def __init__(self, speaker):
		self.speaker = speaker
	
	def diffuse(self):
		"""
		call aroma diffuser
		"""
		print("start")
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(basepin, GPIO.OUT)
		GPIO.output(basepin, GPIO.HIGH)
		time.sleep(3)
		speaker.speak("5")
		time.sleep(1)
		speaker.speak("4")
		time.sleep(1)
		speaker.speak("3")
		time.sleep(1)
		speaker.speak("2")
		time.sleep(1)
		speaker.speak("1")
		time.sleep(3)
		GPIO.output(basepin, GPIO.LOW)
		GPIO.cleanup()
		print("end")
