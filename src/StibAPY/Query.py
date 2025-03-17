class Query:
	def __init__(self, urlFormat):
		self.__url = urlFormat
		self.__valid = False
		self.datasetId = None
		self.select = None
		self.where = None
		self.groupBy = None
		seff.orderBy = None
		self.limit = None
		self.offset = None
		self.refine = None
		self.exclude = None
		self.lang = None
		self.timezone = None
		self.includeLinks = None
		self.includeAppMetas = None

	def isValid(self):
		return self.__valid

	def verify(self):
		if self.datasetId is None:
			self.__valid = False
		else:
			self.__valid = True

	def getUrlFormat(self):
		if not self.__valid:
			raise ValueError("Query is not valid")
		return self.__url.format(self.datasetId, self.select, self.where, self.groupBy, self.orderBy, self.limit, self.offset, self.refine, self.exclude, self.lang, self.timezone, self.includeLinks, self.includeAppMetas)

