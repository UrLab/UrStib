class ApiClient():
	def __init__(self, endpointRepository, queryDirector):
		self.endpointRepository = endpointRepository
		self.queryDirector = queryDirector

	def searchStopsByName(self, stopName):
		endPoint = self.endpointRepository.getStopsDetailsEndPoint()
		query = self.queryDirector.constructStopQuery(stopName)
		response = endPoint.get(query)
		return response.getJSON()

