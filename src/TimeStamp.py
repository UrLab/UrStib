from time import time as now
from Duration import Duration

class TimeStamp():
	def __init__(self, time):
		self.__time = time
	
	def getTime(self):
		return self.__time

	def getRemainingTime(self):
		return Duration(self.getTime() - now())

