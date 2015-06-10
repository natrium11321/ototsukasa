import subprocess

class Speaker:

	def __init__(self):
		pass

	def speak(self, name):
		subprocess.call(["aplay", name])

def main():
	speaker = Speaker()
	speaker.speak(raw_input().rstrip())

if __name__ == '__main__':
	main()
