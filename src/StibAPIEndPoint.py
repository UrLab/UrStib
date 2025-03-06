from requests import get

class StibAPIEndPoint():
	def __init__(self, url, recordFactory):
		self.url = url

	def getURL(self):
		return self.url

	def get(self, query):
		return recordFactory.createCollection(get(self.url + query))

