from datetime import datetime
from zoneinfo import ZoneInfo
from .Duration import Duration

class Time:
	@classmethod
	def now(cls):
		return cls(datetime.now(ZoneInfo("Europe/Brussels")).isoformat())

	def __init__(self, timeStamp):
		self.timeStamp = datetime.fromisoformat(timeStamp)

	def __str__(self):
		return str(self.timeStamp)

	def __repr__(self):
		return str(self)

	def __sub__(self, other):
		return Duration(self.timeStamp - other.timeStamp)

