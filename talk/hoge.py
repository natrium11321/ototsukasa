from database import Database
from drowner import Drowner

database = Database("157.82.6.126")
drowner = Drowner(database)
drowner.drown(raw_input())
print "unko"