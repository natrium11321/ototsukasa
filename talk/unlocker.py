from database import Database
from datetime import datetime, timedelta

class Unlocker:
	
	def __init__(self, db):
		self.db = db
		return
	
	def is_locked(self):
		row = self.db.fetch_reservation()
		updatetime = row["updatetime"]
		nowtime = datetime.utcnow()
		if nowtime - updatetime > timedelta(minutes = 10):
			return False
		self.password = row["password"]
		return True
	
	def unlock(self, password):
		
		return
