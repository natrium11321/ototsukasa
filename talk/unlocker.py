from database import Database

class Unlocker:
	
	def __init__(self, db):
		self.db = db
		return
	
	def is_locked(self):
		row = self.db.fetch_reservation()
		time = row["updatetime"]
		password = row["password"]
		print type(time)
		print type(password)
		return
	
	def unlock(self):
		
		return
