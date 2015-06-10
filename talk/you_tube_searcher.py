import json
import urllib

class YouTubeSearcher:
	
	def __init__(self):
		return
	
	def search(self, keyword):
		url = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyB8dADJ83IRXa3XMEGie06g3FDxM91enr0&part=id&type=video&q='
		f = urllib.urlopen(url + urllib.quote_plus(keyword))
		data = json.loads(f.read())
		if data["pageInfo"]["totalResults"] > 0:
			return data["items"][0]["id"]["videoId"]
		else:
			return None
