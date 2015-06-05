from database import Database
from player import Player
from you_tube_searcher import YouTubeSearcher

class Drowner:
	
	def __init__(self):
		searcher = YouTubeSearcher()
		player = Player()
		return
	
	def drown(self):
		id = db.fetch_music_randomly()
		player.play(id)
		return
	
	def drown(self, keyword):
		id = searcher.search(keyword)
		if id:
			db.register_music(keyword, id)
			player.play(id)
		return
