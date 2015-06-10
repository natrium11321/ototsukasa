from datetime import datetime, timedelta

nowtime = datetime.utcnow()
print nowtime
updatetime = datetime.utcnow()
print updatetime
print updatetime - nowtime < timedelta(minutes = 10)

a = "?&="
a = a.replace("?", "\\?")
print a