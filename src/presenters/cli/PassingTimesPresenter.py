class PassingTimesPresenter():
	def __init__(self):
		pass

	def getMaximums(self, passingTimes):
		highestLineNumber = 0
		longestStringSize = 0
		biggestTime = 0
		for passingTime in passingTimes:
			lineId = passingTime.getLineId()
			destination = passingTime.getDestination()
			time = passingTime.getRemainingTime()
			if len(lineId) > highestLineNumber:
				highestLineNumber = len(str(lineId))
			if len(destination) > longestStringSize:
				longestStringSize = len(str(destination))
			if time > biggestTime:
				biggestTime = time
		biggestTime = len(str(biggestTime))
		return highestLineNumber, longestStringSize, biggestTime

	def present(self, passingTimes):
		highestLineNumber, longestStringSize, biggestTime = self.getMaximums(passingTimes)

