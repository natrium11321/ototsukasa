from database import Database
from datetime import datetime, timedelta

class Unlocker:
	
	def __init__(self, db):
		self.db = db
		return
	
	def is_locked(self):
		now_time = datetime.utcnow()
		status = self.db.fetch_status()
		status_time = status["updatetime"]
		yoyaku = self.db.fetch_reservation()
		yoyaku_time = yoyaku["updatetime"]
		if status_time < yoyaku_time && now_time - yoyaku_time < timedelta(minutes = 10):
			self.password = row["password"]
			return True
		else:
			return False
	
	def try_to_unlock(self, password):
		if password == self.password:
			self.db.update_status(True)
			return True
		else:
			return False
