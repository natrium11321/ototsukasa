from database import Database
from drowner import Drowner
from unlocker import Unlocker

database = Database("157.82.7.193")
# drowner = Drowner(database)
# drowner.drown()
unlocker = Unlocker(database)
unlocker.is_locked()