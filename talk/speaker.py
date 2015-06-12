import subprocess

class Speaker:
	
	def __init__(self):
		pass
	
	def speak(self, text):
		speach = subprocess.check_output(["/home/pi/aquestalkpi/AquesTalkPi", text])
		subprocess.call(["aplay", speach])

if __name__ == "__main__":
	speaker = Speaker()
	speaker.speak("test")
