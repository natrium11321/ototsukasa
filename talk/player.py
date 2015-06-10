import subprocess
import threading
import time

class Player:
	
	def __init__(self):
		self.thread = threading.Thread(target = self.target)
	
	def play(self, id):
		url = subprocess.check_output(["youtube-dl", "-g", "https://www.youtube.com/watch?v=" + id]).rstrip()
		self.thread.start()
		self.process = subprocess.Popen(["omxplayer", "-o", "local", url], stdin = PIPE)
	
	def target(self):
		time.sleep(5)
		self.process.communicate("q")
