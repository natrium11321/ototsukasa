from database import Database
from drowner import Drowner
from unlocker import Unlocker
#import time
#from datetime import datetime

#nowtime = datetime.utcnow()
#print nowtime
#time.sleep(3)
#updatetime = datetime.utcnow()
#print updatetime
#print updatetime - nowtime

database = Database("157.82.7.193")
drowner = Drowner(database)
drowner.drown(raw_input())
#unlocker = Unlocker(database)
#unlocker.is_locked()