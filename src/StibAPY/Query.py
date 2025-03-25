class Query:
	# limit, offset, lang and timezone must be set
	def __init__(self, urlFormat):
		self.__url = urlFormat
		self.select = ""
		self.where = ""
		self.groupBy = ""
		self.orderBy = ""
		self.limit = 100
		self.offset = 0
		self.refine = ""
		self.exclude = ""
		self.lang = "fr"
		self.timezone = "Europe/Brussels"
		self.includeLinks = ""
		self.includeAppMetas = ""

	def __str__(self):
		return self.__url.format(self.select, self.where, self.groupBy, self.orderBy, self.limit, self.offset, self.refine, self.exclude, self.lang, self.timezone, self.includeLinks, self.includeAppMetas)

