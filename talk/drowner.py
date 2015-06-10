from database import Database
from player import Player
from you_tube_searcher import YouTubeSearcher

class Drowner:
	
	def __init__(self, db):
		self.db = db
		self.searcher = YouTubeSearcher()
		self.player = Player()
		return
	
	def drown(self, keyword = None):
		if keyword:
			id = self.searcher.search(keyword)
			if id:
				self.db.register_music(keyword, id)
				self.player.play(id)
		else:
			id = self.db.fetch_music_randomly()
			self.player.play(id)
		return
