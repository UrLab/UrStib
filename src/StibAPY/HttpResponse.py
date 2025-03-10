class HttpResponse():
	def __init__(self, response):
		self.response = response

	def getStatusCode(self):
		return self.response.status_code

	def getJSON(self):
		return self.response.json()

