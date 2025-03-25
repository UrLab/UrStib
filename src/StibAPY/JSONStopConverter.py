from json import loads

class JSONStopConverter:
	def __init__(self):
		pass

	def convertStops(self, stops):
		return [self.convertStop(stop) for stop in stops["results"]]

	def convertStop(self, stop):
		gpsCoords = loads(stop["gpscoordinates"])
		gpsCoords = GPSCoords(gpsCoords["latitude"], gpsCoords["longitude"])
		name = Name(stop["name"]["fr"], stop["name"]["nl"])
		id_ = Id(stop["id"])
		return Stop(id_, name, gpsCoords)

