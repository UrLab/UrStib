from HttpResponse import HttpResponse
from requests import get

class HttpGetter():
	def __init__(self):
		pass

	def get(self, url):
		return HttpResponse(get(url))

