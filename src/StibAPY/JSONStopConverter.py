from json import loads
from Stop import Stop
from Id import Id
from Name import Name
from GPSCoords import GPSCoords

class JSONStopConverter:
	def __init__(self):
		pass

	def convertStops(self, stops):
		return [self.convertStop(stop) for stop in stops["results"]]

	def convertStop(self, stop):
		print(stop)
		gpsCoords = loads(stop["gpscoordinates"])
		gpsCoords = GPSCoords(gpsCoords["latitude"], gpsCoords["longitude"])
		name = Name(dict(stop["name"])["fr"], dict(stop["name"])["nl"])
		id_ = Id(stop["id"])
		return Stop(id_, name, gpsCoords)

