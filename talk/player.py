import subprocess

class Player:
	
	def __init__(self):
		return
	
	def play(self, id):
		cmd = "/usr/bin/vlc --run-time=5 http://youtube.com/embed/" + id + " vlc://quit"
		print cmd
		subprocess.call(cmd.strip().split(" "))
