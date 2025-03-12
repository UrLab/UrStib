from HttpGetter import HttpGetter

class EndPoint():
	def __init__(self, baseUrl, dataset, endPointFormat, httpGetter):
		self.url = url + endPointFormat.format(dataset.getName())
		self.dataset = dataset
		self.baseUrl = baseUrl
		self.endPointFormat = endPointFormat
		self.httpGetter = HttpGetter

	def get(self, query):
		return self.httpGetter.get(self.url + query.getUrlFormat())

