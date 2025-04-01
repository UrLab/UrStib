class StopService():
	def __init__(self, stopRepository):
		self.stopRepository = stopRepository

	def searchStopsByName(self, search):
		return self.stopRepository.searchByName(search)

