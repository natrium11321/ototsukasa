from datetime import datetime, timedelta
import json
import urllib

nowtime = datetime.utcnow()
print nowtime
updatetime = datetime.utcnow()
print updatetime
print updatetime - nowtime < timedelta(minutes = 10)

keyword = raw_input().decode('utf-8')
url = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyB8dADJ83IRXa3XMEGie06g3FDxM91enr0&part=id&type=video&q='
f = urllib.urlopen(url + urllib.quote_plus(keyword.encode('utf-8')))
data = json.loads(f.read())
print data