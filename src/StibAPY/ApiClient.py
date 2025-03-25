class ApiClient():
	def __init__(self, baseUrl, endpointUrlRepository, endPointFactory, queryDirector):
		self.baseUrl = baseUrl
		self.endpointUrlRepository = endpointUrlRepository
		self.endPointFactory = endPointFactory
		self.queryDirector = queryDirector

	def getStopsByName(self, stopName):
		endPoint = self.endPointFactory.createEndPoint(self.baseUrl + self.endpointUrlRepository.getStopsUrl())
		response = endPoint.get(self.queryDirector.constructStopQuery(stopName))
		return response.getJSON()

