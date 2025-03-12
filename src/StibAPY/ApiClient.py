class ApiClient():
	def __init__(self, baseUrl, endpointUrlRepository, endPointFactory):
		self.baseUrl = baseUrl
		self.endpointUrlRepository = endpointUrlRepository
		self.endPointFactory = endPointFactory

	def getStopIds(self, stopName):
		endPoint = self.endPointFactory.createEndPoint(self.baseUrl + self.endpointUrlRepository.getStopsUrl())
		return endPoint.get(

