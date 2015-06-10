import subprocess

class Player:
	
	def __init__(self):
		return
	
	def play(self, id):
		url = subprocess.check_output(["youtube-dl", "-g", "https://www.youtube.com/watch?v=" + id]).rstrip()
		subprocess.call(["omxplayer", "-o", "local", url])
