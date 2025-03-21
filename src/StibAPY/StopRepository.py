class StopRepository():
	def __init__(self, stops, jsonConverter):
		self.stops = stops
		self.jsonConverter = jsonConverter

	def getStopsByName(self, name):
		stops = []
		for stop in self.stops:
			if stop.getName() == name:
				stops.append(stop)
		return stops

	def updateStops(self, newStops):
		
		flag = True
		for newStop in newStops:
			for stop in self.stops:
				if stop.getId() == newStop.getId():
					flag = False
					break
			if flag:
				self.stops.append(newStop)

