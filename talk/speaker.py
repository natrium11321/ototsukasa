import subprocess

class Speaker:
	
	def __init__(self):
		pass
	
	def speak(self, s):
		subprocess.call(["~/aquestalkpi/AquesTalkPi", s, "|", "aplay"])

if __name__ == "__main__":
	speaker = Speaker()
	speaker.speak("test")
