import subprocess

class Player:
	def __init__(self):
		return
	def play(self, id):
		cmd = "vlc.exe --run-time=5 http://youtube.com/embed/" + id + " vlc://quit"
		subprocess.call(cmd.strip().split(" "))