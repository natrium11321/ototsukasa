import subprocess

class Speaker:
	
	def __init__(self):
		pass
	
	# speed : 50-300
	def speak(self, text, speed = 100):
		subprocess.call("/home/pi/aquestalkpi/AquesTalkPi -s " + str(speed) + " " + text + " | aplay", shell = True)
