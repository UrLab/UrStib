class PassingTimesRepository():
	def __init__(self, passingTimes, passingTimeConverter, apiClient):
		self.passingTimes = passingTimes
		self.passingTimeConverter = passingTimeConverter
		self.apiClient = apiClient

	def getPassingTimesByStop(self, stop):
		passingTimes = self.apiClient.getPassingTimesByStopId(stop.getId())
		passingTimes = self.passingTimeConverter.convertPassingTimes(passingTimes)
		for passingTime in passingTimes:
			self.passingTimes.add(passingTime)
		return passingTimes

