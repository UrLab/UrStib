class StibAPIEndPoint():
	def __init__(self, url, getter):
		self.url = url
		self.recordFactory = recordFactory

	def getURL(self):
		return self.url

	def get(self, query):
		return getter.get(self.url + query.getRequest())

