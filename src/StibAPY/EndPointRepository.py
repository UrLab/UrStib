from HttpGetter import HttpGetter
from EndPoint import EndPoint
from json import loads


class EndPointRepository:
	def __init__(self, baseUrl, filePath):
		self.baseUrl = baseUrl
		with open(filePath, "r") as f:
			self.resourcePaths = loads(f.read())

	def getStopsDetailsEndPoint(self):
		return EndPoint(self.baseUrl + self.resourcePaths["stop-details"], HttpGetter())

	def getWaitingTimeEndPoint(self):
		return EndPoint(self.baseUrl + self.resourcePaths["waiting-time-rt"], HttpGetter())

