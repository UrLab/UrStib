class StopService():
	def __init__(self, stopRepository, apiClient):
		self.stopRepository = stopRepository
		self.apiClient = apiClient

	def searchStopsByName(self, name):
		stops = self.apiClient.getStopByName(name)
		self.stopRepository.updateStops(stops)

