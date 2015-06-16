import subprocess
import time

class Player:
	
	def __init__(self):
		pass
	
	def play(self, id):
		url = subprocess.check_output(["youtube-dl", "-g", "https://www.youtube.com/watch?v=" + id]).rstrip()
		self.process = subprocess.Popen(["omxplayer", "-o", "local", "--vol", "-100", url], stdin = subprocess.PIPE)
		time.sleep(20)
		self.process.communicate("q")
