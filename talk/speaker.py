import subprocess

class Speaker:
	
	def __init__(self):
		pass
	
	def speak(self, text):
		subprocess.call("/home/pi/aquestalkpi/AquesTalkPi " + text + " | aplay", shell = True)

if __name__ == "__main__":
	speaker = Speaker()
	speaker.speak(raw_input().rstrip())
