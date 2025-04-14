class StopRepository():
	def __init__(self, stops, stopConverter, apiClient):
		self.stops = set(stops)
		self.stopConverter = stopConverter
		self.apiClient = apiClient

	def searchByName(self, searchName):
		stops = self.apiClient.searchStopsByName(searchName)
		stops = self.stopConverter.convertStops(stops)
		for stop in stops:
			self.stops.add(stop)
		return stops

	def getStopsByName(self, name):
		stops = []
		for stop in self.stops:
			if stop.getName() == name:
				stops.append(stop)
		return stops

	def getStopsById(self, id_):
		stops = []
		for stop in self.stops:
			if stop.getId() == id_:
				stops.append(stop)
		return stops

