from database import Database
from player import Player
from speaker import Speaker
from you_tube_searcher import YouTubeSearcher

class Drowner:
	
	def __init__(self, db):
		self.db = db
		self.searcher = YouTubeSearcher()
		self.player = Player()
		self.speaker = Speaker()
		return
	
	def drown(self, keyword = None):
		if keyword:
			id = self.searcher.search(keyword)
			if id:
				print id
				self.db.register_music(keyword, id)
				self.player.play(id)
		else:
			row = self.db.fetch_music_randomly()
			id = row["url"]
			address = row["address"]
			self.speaker.speak(address + "‚ÌƒgƒCƒŒ‚©‚ç")
			self.player.play(id)
		return
