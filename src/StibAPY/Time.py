class Time():
	def __init__(self, timeStamp):
		self.timeStamp = timeStamp

	def getTime(self):
		return self.timeStamp

	def __str__(self):
		return str(self.timeStamp)

	def __repr__(self):
		return str(self)

