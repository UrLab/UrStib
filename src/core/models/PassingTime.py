from .Time import Time

class PassingTime():
	def __init__(self, destination, arrivalTime, lineId, message):
		self.destination = destination
		self.arrivalTime = arrivalTime
		self.lineId = lineId
		self.message = message

	def getDestination(self):
		return self.destination

	def getArrivalTime(self):
		return self.arrivalTime

	def getLineId(self):
		return self.lineId

	def getMessage(self):
		return self.message

	def getRemainingTime(self):
		return self.arrivalTime - Time.now()

	def __str__(self):
		return f"{self.lineId} {self.destination} {self.arrivalTime} {self.message}"

	def __repr__(self):
		return str(self)

