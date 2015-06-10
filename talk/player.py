import subprocess

class Player:
	
	def __init__(self):
		return
	
	def play(self, id):
		url = subprocess.check_output(["youtube-dl", "-g", '"'+id+'"'])
		subprocess.call(["omxplayer", "-o", "local", url])
