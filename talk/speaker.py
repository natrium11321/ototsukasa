import subprocess

class Speaker:
	
	def __init__(self):
		pass
	
	def speak(self, text):
		speech = subprocess.check_output(["/home/pi/aquestalkpi/AquesTalkPi", text])
		print speech
		subprocess.call(["aplay", speech])

if __name__ == "__main__":
	speaker = Speaker()
	speaker.speak("test")
