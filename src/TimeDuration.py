from DurationException import DurationException

class TimeDuration():
	def __init__(self, value):
		if value <= 0:
			raise DurationException("TimeDuration must be positive")
		self.value = value

