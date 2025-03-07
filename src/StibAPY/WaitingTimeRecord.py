class WaitingTimeRecord():
	def __init__(self, pointId, lineId, passingTimeCollection):
		self.pointId = pointId
		self.lineId = lineId
		self.passingTimeCollection = passingTimeCollection

	def getPointId(self):
		return self.pointId

	def getLineId(self):
		return self.lineId

	def getPassingTimeCollection(self):
		return self.passingTimeCollection

