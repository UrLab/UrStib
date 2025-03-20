class QueryDirector():
	def __init__(self, queryBuilder):
		self.queryBuilder = queryBuilder

	def constructStopQuery(self, stopName):
		self.queryBuilder.reset()
		self.queryBuilder.setWhere(f"name like \"{stopName}\"")
		return self.queryBuilder.getQuery()

