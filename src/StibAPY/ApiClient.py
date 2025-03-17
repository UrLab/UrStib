class ApiClient():
	def __init__(self, baseUrl, endpointUrlRepository, endPointFactory, queryDirector):
		self.baseUrl = baseUrl
		self.endpointUrlRepository = endpointUrlRepository
		self.endPointFactory = endPointFactory
		self.queryDirector = queryDirector

	def getStopIds(self, stopName):
		endPoint = self.endPointFactory.createEndPoint(self.baseUrl + self.endpointUrlRepository.getStopsUrl())
		endPoint.get(self.queryDirector.makeStopsQuery(stopName))
		# TODO

