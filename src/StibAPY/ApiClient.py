class ApiClient():
	def __init__(self, endpointRepository, queryDirector):
		self.endpointRepository = endpointRepository
		self.queryDirector = queryDirector

	def searchStopsByName(self, stopName):
		endPoint = self.endpointRepository.getStopsDetailsEndPoint()
		response = endPoint.get(self.queryDirector.constructStopQuery(stopName))
		return response.getJSON()

