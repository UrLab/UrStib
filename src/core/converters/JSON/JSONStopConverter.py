from json import loads
from core.models import Stop, Id, Name, GPSCoords

class JSONStopConverter:
	def __init__(self):
		pass

	def convertStops(self, stops):
		return [self.convertStop(stop) for stop in stops["results"]]

	def convertStop(self, stop):
		gpsCoords = loads(stop["gpscoordinates"])
		gpsCoords = GPSCoords(gpsCoords["latitude"], gpsCoords["longitude"])
		name = loads(stop["name"])
		name = Name(name["fr"], name["nl"])
		id_ = Id(stop["id"])
		return Stop(id_, name, gpsCoords)

