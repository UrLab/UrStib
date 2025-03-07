class GPSCoords():
	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	def getLatitude(self):
		return self.latitude

	def getLongitude(self):
		return self.longitude

	def __eq__(self, other):
		return self.latitude == other.getLatitude() and self.longitude == other.getLongitude()

	def __hash__(self):
		return hash((self.latitude, self.longitude))

