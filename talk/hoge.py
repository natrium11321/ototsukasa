from database import Database
from drowner import Drowner

database = Database("157.82.7.193")
drowner = Drowner(database)
drowner.drown(raw_input())
print "unko"