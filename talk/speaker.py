import subprocess

class Speaker:
	
	def __init__(self):
		pass
		
	def speak(self, name):
		subprocess.call(["aplay", name])
