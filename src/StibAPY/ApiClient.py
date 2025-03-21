class ApiClient():
	def __init__(self, baseUrl, endpointUrlRepository, endPointFactory, queryDirector):
		self.baseUrl = baseUrl
		self.endpointUrlRepository = endpointUrlRepository
		self.endPointFactory = endPointFactory
		self.queryDirector = queryDirector

	def getStopByName(self, stopName):
		endPoint = self.endPointFactory.createEndPoint(self.baseUrl + self.endpointUrlRepository.getStopsUrl())
		return endPoint.get(self.queryDirector.constructStopQuery(stopName))

