class PassingTimeCollection():
	def __init__(self, passingTimes):
		self.passingTimes = passingTimes

	def __iter__(self):
		return iter(self.passingTimes)

	def __next__(self):
		return next(self.passingTimes)

