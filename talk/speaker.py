import subprocess

class Speaker:
	
	def __init__(self):
		pass
	
	def speak(self, text, speed = 1):
		subprocess.call("/home/pi/aquestalkpi/AquesTalkPi -s " + str(speed) + " " + text + " | aplay", shell = True)

if __name__ == "__main__":
	speaker = Speaker()
	speaker.speak(raw_input().rstrip(), 10)
