from Player import Player
from YouTubeSearcher import YouTubeSearcher

class Drowner:
	def __init__(self):
		searcher = YouTubeSearcher()
		player = Player()
		return
	def drown(self):
		return
	def drown(self, keyword):
		id = searcher.search(keyword)
		player.play(id)
		return