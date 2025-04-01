from HttpResponse import HttpResponse
from requests import get

class HttpGetter():
	def __init__(self):
		pass

	def get(self, url):
		response = HttpResponse(get(url))
		if response.isOk():
			return response
		raise HttpError(response.status_code, response)

