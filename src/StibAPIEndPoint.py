from requests import get

class StibAPIEndPoint():
	def __init__(self, url, recordFactory):
		self.url = url
		self.recordFactory = recordFactory

	def getURL(self):
		return self.url

	def get(self, query):
		return self.recordFactory.createCollection(get(self.url + query).json()["results"])

