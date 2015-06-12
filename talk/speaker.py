import subprocess

class Speaker:

	def __init__(self):
		pass
<<<<<<< HEAD
		
	def speak(self, s):
		subprocess.call(["~/aquestalkpi/AquesTalkPi", s, "|", "aplay"])
=======

	def speak(self, name):
		subprocess.call(["aplay", name])

def main():
	speaker = Speaker()
	speaker.speak(raw_input().rstrip())

if __name__ == '__main__':
	main()
>>>>>>> 2e4f980a0e5a307025ad717376d98a4303aa7ef2
