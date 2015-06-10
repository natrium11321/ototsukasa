import subprocess

class Speaker:
	
	def __init__(self):
	
	def speak(self, name):
		subprocess.call(["aplay", name])
