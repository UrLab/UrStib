class EndPoint():
	def __init__(self, url, httpGetter):
		self.url = url
		self.httpGetter = httpGetter

	def get(self, query):
		return self.httpGetter.get(self.url + str(query))

