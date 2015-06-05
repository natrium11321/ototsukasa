import subprocess

class Player:
	def __init__(self):
		return
	def play(self, id):
		cmd = "vlc.exe http://youtube.com/embed/" + id
		subprocess.call(cmd.strip().split(" "))