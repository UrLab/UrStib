class PassingTimesService():
	def __init__(self, passingTimesRepository):
		self.passingTimesRepository = passingTimesRepository

	def getPassingTimesByStop(self, stop):
		return self.passingTimesRepository.getPassingTimesByStop(stop)

