class StopDetailsRecord():
	def __init__(self, stopGPSCoords, stopID, stopName):
		self.gpsCoords = stopGPSCoords
		self.id = stopID 
		self.name = stopName

	def getCoords(self):
		return self.gpsCoord

	def getID(self):
		return self.id

	def getName(self):
		return self.name

	def __eq__(self, other):
		return self.gpsCoords == other.getCoords()

	def __hash__(self):
		return hash(self.gpsCoords)

