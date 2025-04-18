class QueryDirector():
	def __init__(self, queryBuilder):
		self.queryBuilder = queryBuilder

	def constructStopQuery(self, stopName):
		self.queryBuilder.reset()
		self.queryBuilder.setWhere(f"name like \"{stopName}\"")
		self.queryBuilder.setLimit("100")
		return self.queryBuilder.getQuery()

	def constructPassingTimesQuery(self, stopId):
		self.queryBuilder.reset()
		self.queryBuilder.setWhere(f"pointid=\"{stopId}\"")
		self.queryBuilder.setLimit("100")
		return self.queryBuilder.getQuery()

