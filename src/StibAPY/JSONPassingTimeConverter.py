from json import loads

class JSONPassingTimeConverter:
	def __init__(self):
		pass

	def convertTimes(self, passingTimes):
		return [self.convertPassingTime(passingTime) for passingTime in passingTimes]

	def convertPassingTime(self, passingTime):
		gpsCoords = loads(stop["gpscoordinates"])
		gpsCoords = GPSCoords(gpsCoords["latitude"], gpsCoords["longitude"])
		name = loads(stop["name"])
		name = Name(name["fr"], name["nl"])
		id_ = Id(stop["id"])
		return Stop(id_, name, gpsCoords)

