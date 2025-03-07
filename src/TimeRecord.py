class TimeRecord():
	def __init__(self, line, timeStamp, stop):
		self.line = line
		self.timeStamp = timeStamp
		self.stop = stop
	
	def getName(self):
		return self.line.getName()
	
	def getAbsoluteTime(self):
		return self.timeStamp

	def getStop(self):
		return self.stop

	def getRemainingTime(self):
		return self.timeStamp.getRemainingTime()

