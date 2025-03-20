class Query:
	def __init__(self, urlFormat):
		self.__url = urlFormat
		self.select = ""
		self.where = ""
		self.groupBy = ""
		seff.orderBy = ""
		self.limit = ""
		self.offset = ""
		self.refine = ""
		self.exclude = ""
		self.lang = ""
		self.timezone = ""
		self.includeLinks = ""
		self.includeAppMetas = ""

	def __str__(self):
		return self.__url.format(self.datasetId, self.select, self.where, self.groupBy, self.orderBy, self.limit, self.offset, self.refine, self.exclude, self.lang, self.timezone, self.includeLinks, self.includeAppMetas)

